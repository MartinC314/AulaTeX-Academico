from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from threading import Event
from typing import Callable

from .llm_bridge import LLM_ENGINES, AulaTeXLLMClient
from .workspace import AulaTeXWorkspace, EditorialScope


EDITORIAL_LEVELS = (
    "actividad",
    "materia",
    "carrera",
    "institucion",
    "interinstitucional",
)

ENGINE_PRIORITY = {
    "Codex": 10,
    "Auto (model-router)": 20,
    "Claude Foundry": 30,
    "GPT-Pro": 40,
}

MEMORY_SECTIONS = (
    "summary",
    "identity_rules",
    "structure_rules",
    "activity_rules",
    "quality_gates",
    "latex_rules",
    "bibliography_rules",
    "propagation_hints",
    "open_questions",
)

MEMORY_STRING_FIELDS = (
    "artifact_name",
)

MEMORY_LIST_FIELDS = (
    "sources",
    "artifact_types",
    "supported_artifact_types",
    "source_documents",
    "source_fragments",
    "concepts",
    "section_titles",
    "citations",
    "bibliography_index",
)

MEMORY_DICT_FIELDS = (
    "node_metadata",
    "curricular_context",
    "artifact_templates",
    "tex_blueprint",
)


@dataclass(frozen=True)
class EditorialMemoryRequest:
    source_scope_key: str
    build_level: str = "materia"
    propagation_mode: str = "ascendente"
    iterations: int = 2
    engines: list[str] | tuple[str, ...] = ("Codex", "Claude Foundry", "GPT-Pro")
    max_tokens: int = 1400


@dataclass(frozen=True)
class EditorialMemoryEvent:
    kind: str
    message: str
    current: int = 0
    total: int = 0
    scope_key: str = ""
    engine: str = ""
    cycle: int = 0


@dataclass(frozen=True)
class EditorialMemoryBuildResult:
    run_id: str
    run_dir: Path
    manifest_path: Path
    built_scopes: tuple[str, ...]
    ok: bool
    cancelled: bool = False


class EditorialMemoryStore:
    def __init__(self, workspace: AulaTeXWorkspace | None = None) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.root = self.workspace.feedback_root / "editorial-memory"
        self.root.mkdir(parents=True, exist_ok=True)
        self.db_path = self.root / "editorial-memory.db"
        self.scopes_dir = self.root / "scopes"
        self.scopes_dir.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        with self._connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS scopes (
                    scope_key TEXT PRIMARY KEY,
                    level TEXT NOT NULL,
                    label TEXT NOT NULL,
                    relative_path TEXT NOT NULL,
                    institution TEXT NOT NULL,
                    career TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    activity TEXT NOT NULL,
                    parent_key TEXT NOT NULL,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS memories (
                    scope_key TEXT PRIMARY KEY,
                    level TEXT NOT NULL,
                    memory_json TEXT NOT NULL,
                    source_scope_key TEXT NOT NULL,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS runs (
                    run_id TEXT PRIMARY KEY,
                    source_scope_key TEXT NOT NULL,
                    build_level TEXT NOT NULL,
                    propagation_mode TEXT NOT NULL,
                    iterations INTEGER NOT NULL,
                    engines_json TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    completed_at TEXT,
                    ok INTEGER NOT NULL DEFAULT 0
                );

                CREATE TABLE IF NOT EXISTS cycles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    run_id TEXT NOT NULL,
                    scope_key TEXT NOT NULL,
                    cycle_index INTEGER NOT NULL,
                    engine TEXT NOT NULL,
                    ok INTEGER NOT NULL,
                    response_chars INTEGER NOT NULL,
                    response_text TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

    def upsert_scope(self, scope: EditorialScope) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO scopes (
                    scope_key, level, label, relative_path, institution, career, subject, activity, parent_key
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(scope_key) DO UPDATE SET
                    level=excluded.level,
                    label=excluded.label,
                    relative_path=excluded.relative_path,
                    institution=excluded.institution,
                    career=excluded.career,
                    subject=excluded.subject,
                    activity=excluded.activity,
                    parent_key=excluded.parent_key,
                    updated_at=CURRENT_TIMESTAMP
                """,
                (
                    scope.key,
                    scope.level,
                    scope.label,
                    scope.relative_path,
                    scope.institution,
                    scope.career,
                    scope.subject,
                    scope.activity,
                    scope.parent_key,
                ),
            )

    def start_run(self, request: EditorialMemoryRequest, engines: list[str], run_id: str) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO runs (run_id, source_scope_key, build_level, propagation_mode, iterations, engines_json, ok)
                VALUES (?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    run_id,
                    request.source_scope_key,
                    request.build_level,
                    request.propagation_mode,
                    int(request.iterations),
                    json.dumps(engines, ensure_ascii=False),
                ),
            )

    def finish_run(self, run_id: str, ok: bool) -> None:
        with self._connect() as conn:
            conn.execute(
                "UPDATE runs SET completed_at=CURRENT_TIMESTAMP, ok=? WHERE run_id=?",
                (1 if ok else 0, run_id),
            )

    def record_cycle(
        self,
        *,
        run_id: str,
        scope_key: str,
        cycle_index: int,
        engine: str,
        ok: bool,
        response_text: str,
    ) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO cycles (run_id, scope_key, cycle_index, engine, ok, response_chars, response_text)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (run_id, scope_key, cycle_index, engine, 1 if ok else 0, len(response_text), response_text),
            )

    def get_memory(self, scope_key: str) -> dict:
        with self._connect() as conn:
            row = conn.execute("SELECT memory_json FROM memories WHERE scope_key=?", (scope_key,)).fetchone()
        if row is None:
            return self._empty_memory()
        payload = json.loads(row["memory_json"])
        return self._normalize_memory(payload)

    def save_memory(self, scope: EditorialScope, payload: dict, source_scope_key: str) -> None:
        normalized = self._normalize_memory(payload)
        normalized = self._enrich_memory(scope, normalized)
        self.upsert_scope(scope)
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO memories (scope_key, level, memory_json, source_scope_key)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(scope_key) DO UPDATE SET
                    level=excluded.level,
                    memory_json=excluded.memory_json,
                    source_scope_key=excluded.source_scope_key,
                    updated_at=CURRENT_TIMESTAMP
                """,
                (scope.key, scope.level, json.dumps(normalized, ensure_ascii=False, indent=2), source_scope_key),
            )
        json_path = self.scopes_dir / f"{scope.key.replace('/', '__')}.json"
        json_path.write_text(json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8")
        markdown_path = self.scopes_dir / f"{scope.key.replace('/', '__')}.md"
        markdown_path.write_text(self.render_memory_markdown(scope, normalized), encoding="utf-8")
        self._write_local_scope_memory(scope, normalized)

    def _write_local_scope_memory(self, scope: EditorialScope, payload: dict) -> None:
        from pathlib import Path

        rel = Path(scope.relative_path)
        if scope.level == "actividad":
            subject_dir = self.workspace.repo_root / rel
            memory_dir = subject_dir / f".memoria-{scope.subject}"
            filename = f"memoria-{scope.subject}-{scope.activity.lower().replace(' ', '-')}.json"
        elif scope.level == "materia":
            career_dir = (self.workspace.repo_root / rel).parent
            memory_dir = career_dir / f".memoria-{scope.career or career_dir.name}"
            filename = f"memoria-{scope.subject}.json"
        elif scope.level == "carrera":
            institution_dir = (self.workspace.repo_root / rel).parent
            memory_dir = institution_dir / f".memoria-{scope.institution}"
            filename = f"memoria-{scope.career}.json"
        elif scope.level == "institucion":
            memory_dir = self.workspace.repo_root / ".memoria-global"
            filename = f"memoria-{scope.institution}.json"
        else:
            return

        memory_dir.mkdir(parents=True, exist_ok=True)
        (memory_dir / filename).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def _enrich_memory(self, scope: EditorialScope, payload: dict) -> dict:
        enriched = self._normalize_memory(payload)
        metadata = {
            "scope_key": scope.key,
            "level": scope.level,
            "label": scope.label,
            "relative_path": scope.relative_path,
            "institution": scope.institution,
            "career": scope.career,
            "subject": scope.subject,
            "activity": scope.activity,
            "parent_key": scope.parent_key,
        }
        enriched["node_metadata"] = {**enriched.get("node_metadata", {}), **metadata}

        if scope.level not in {"actividad", "materia"}:
            enriched["schema_version"] = 2
            return enriched

        subject_dir = self.workspace.repo_root / scope.relative_path
        activity_number = "".join(ch for ch in scope.activity if ch.isdigit()) if scope.level == "actividad" else ""

        artifact_paths: dict[str, Path] = {}
        report_template = subject_dir / f"reporte-{scope.subject}.tex"
        presentation_template = subject_dir / f"presentacion-{scope.subject}.tex"
        if report_template.exists():
            artifact_paths["reporte_base"] = report_template
        if presentation_template.exists():
            artifact_paths["presentacion_base"] = presentation_template
        if scope.level == "actividad" and activity_number:
            report_activity = subject_dir / f"reporte-{scope.subject}-Actividad-{activity_number}.tex"
            presentation_activity = subject_dir / f"presentacion-{scope.subject}-Actividad-{activity_number}.tex"
            if report_activity.exists():
                artifact_paths["reporte"] = report_activity
            if presentation_activity.exists():
                artifact_paths["presentacion"] = presentation_activity

        artifact_types = [kind for kind in ("reporte", "presentacion") if kind in artifact_paths]
        supported_types = [kind for kind in ("reporte", "presentacion") if f"{kind}_base" in artifact_paths or kind in artifact_paths]
        if scope.level == "actividad":
            primary_type = artifact_types[0] if artifact_types else (supported_types[0] if supported_types else "reporte")
            if activity_number:
                enriched["artifact_name"] = f"{primary_type}-{scope.subject}-Actividad-{activity_number}"
            enriched["artifact_types"] = _dedupe_lines(enriched.get("artifact_types", []) + artifact_types)
        else:
            templates: dict[str, str] = dict(enriched.get("artifact_templates", {}))
            if "reporte_base" in artifact_paths:
                templates["reporte"] = f"reporte-{scope.subject}"
            if "presentacion_base" in artifact_paths:
                templates["presentacion"] = f"presentacion-{scope.subject}"
            enriched["artifact_templates"] = templates
            enriched["supported_artifact_types"] = _dedupe_lines(enriched.get("supported_artifact_types", []) + supported_types)

        source_documents = list(enriched.get("source_documents", []))
        source_fragments = list(enriched.get("source_fragments", []))
        concepts = list(enriched.get("concepts", []))
        section_titles = list(enriched.get("section_titles", []))
        citations = list(enriched.get("citations", []))
        bibliography_index = list(enriched.get("bibliography_index", []))
        tex_blueprint = dict(enriched.get("tex_blueprint", {}))

        readme_path = subject_dir / "README.md"
        if readme_path.exists():
            source_documents.append(self.workspace.relative(readme_path))
            source_fragments.extend(_extract_nonempty_lines(self._safe_read_text(readme_path), limit=6, max_len=220))

        program_path = next(iter(sorted(subject_dir.glob("programa-analitico*.md"))), None)
        curricular_context = dict(enriched.get("curricular_context", {}))
        if program_path is not None and program_path.exists():
            source_documents.append(self.workspace.relative(program_path))
            program_context = _extract_program_context(self._safe_read_text(program_path))
            curricular_context = {**program_context, **curricular_context}
            source_fragments.extend(program_context.get("source_fragments", []))
            concepts.extend(program_context.get("work_axes", []))

        bib_paths = [path for path in sorted(subject_dir.glob("*.bib")) if path.is_file()]
        for bib_path in bib_paths:
            source_documents.append(self.workspace.relative(bib_path))
            bib_index = _extract_bibliography_index(self._safe_read_text(bib_path))
            bibliography_index.extend(bib_index)
            concepts.extend(_extract_bibliography_titles(bib_index))

        artifact_blueprints: dict[str, dict] = {}
        for kind, tex_path in artifact_paths.items():
            source_documents.append(self.workspace.relative(tex_path))
            blueprint = _extract_tex_blueprint(self._safe_read_text(tex_path), self.workspace.relative(tex_path))
            artifact_blueprints[kind] = blueprint
            section_titles.extend(blueprint.get("section_titles", []))
            citations.extend(blueprint.get("cited_keys", []))
            concepts.extend(blueprint.get("concepts", []))
            source_fragments.extend(blueprint.get("source_fragments", []))
            for key in ("coursename", "coursecode", "documentsubject", "documenttitle", "documentsubtitle"):
                value = blueprint.get(key)
                if value and key not in curricular_context:
                    curricular_context[key] = value

        if artifact_blueprints:
            tex_blueprint["artifacts"] = artifact_blueprints
            preferred_key = "reporte" if "reporte" in artifact_blueprints else next(iter(artifact_blueprints.keys()))
            tex_blueprint["primary"] = artifact_blueprints.get(preferred_key, {})

        enriched["curricular_context"] = curricular_context
        enriched["tex_blueprint"] = tex_blueprint
        enriched["source_documents"] = _dedupe_lines(source_documents)
        enriched["source_fragments"] = _dedupe_lines(source_fragments)
        enriched["concepts"] = _dedupe_lines(concepts)
        enriched["section_titles"] = _dedupe_lines(section_titles)
        enriched["citations"] = _dedupe_lines(citations)
        enriched["bibliography_index"] = _dedupe_lines(bibliography_index)
        enriched["sources"] = _dedupe_lines(enriched.get("sources", []) + enriched["source_documents"])
        enriched["schema_version"] = 2
        return enriched

    def _safe_read_text(self, path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""

    def render_memory_markdown(self, scope: EditorialScope, payload: dict | None = None) -> str:
        data = self._normalize_memory(payload or self.get_memory(scope.key))
        lines = [
            "# Memoria editorial AulaTeX",
            "",
            f"- Alcance: {scope.level}",
            f"- Etiqueta: {scope.label}",
            f"- Ruta: {scope.relative_path}",
            f"- Compresion: {data['compression'].get('method', 'union-dedupe')}",
            f"- Sin regresion: {'si' if data['compression'].get('lossless', True) else 'no'}",
            f"- Secciones fijadas: {', '.join(data.get('locked_sections', [])) or 'ninguna'}",
            "",
        ]
        for section in MEMORY_SECTIONS:
            items = data.get(section, [])
            if not items:
                continue
            lines.append(f"## {section}")
            lines.append("")
            lines.extend(f"- {item}" for item in items)
            lines.append("")
        return "\n".join(lines)

    def summarize_for_scope(self, scope_key: str, include_ancestors: bool = True, max_chars: int = 6000) -> str:
        by_key, _children = self.workspace.editorial_scope_index()
        scope = by_key.get(scope_key)
        if scope is None:
            return ""
        scope_keys = [scope_key]
        if include_ancestors:
            scope_keys.extend(item.key for item in self.workspace.scope_chain(scope_key)[1:])

        chunks: list[str] = []
        for key in scope_keys:
            current = by_key.get(key)
            if current is None:
                continue
            memory = self.get_memory(key)
            if all(not memory.get(section) for section in MEMORY_SECTIONS):
                continue
            chunk = self.render_memory_markdown(current, memory)
            if sum(len(item) for item in chunks) + len(chunk) > max_chars:
                break
            chunks.append(chunk)
        return "\n\n".join(chunks)

    def lock_scope_sections(self, scope_key: str, sections: list[str] | None = None) -> dict:
        by_key, _children = self.workspace.editorial_scope_index()
        scope = by_key.get(scope_key)
        if scope is None:
            return self._empty_memory()
        payload = self.get_memory(scope_key)
        if sections is None:
            sections = [section for section in MEMORY_SECTIONS if payload.get(section)]
        locked = set(payload.get("locked_sections", []))
        locked.update(section for section in sections if section in MEMORY_SECTIONS)
        payload["locked_sections"] = sorted(locked)
        self.save_memory(scope, payload, scope_key)
        return payload

    def unlock_scope_sections(self, scope_key: str, sections: list[str] | None = None) -> dict:
        by_key, _children = self.workspace.editorial_scope_index()
        scope = by_key.get(scope_key)
        if scope is None:
            return self._empty_memory()
        payload = self.get_memory(scope_key)
        locked = set(payload.get("locked_sections", []))
        if sections is None:
            locked.clear()
        else:
            locked.difference_update(section for section in sections if section in MEMORY_SECTIONS)
        payload["locked_sections"] = sorted(locked)
        self.save_memory(scope, payload, scope_key)
        return payload

    def render_metrics_markdown(self, scope_keys: list[str] | tuple[str, ...]) -> str:
        keys = [key for key in scope_keys if key]
        if not keys:
            return "# Metricas\n\n- Sin scopes seleccionados.\n"
        placeholders = ", ".join("?" for _ in keys)
        with self._connect() as conn:
            by_engine = conn.execute(
                f"""
                SELECT engine, COUNT(*) AS calls, SUM(CASE WHEN ok = 1 THEN 1 ELSE 0 END) AS ok_calls,
                       AVG(response_chars) AS avg_chars, MAX(response_chars) AS max_chars
                FROM cycles
                WHERE scope_key IN ({placeholders})
                GROUP BY engine
                ORDER BY engine
                """,
                tuple(keys),
            ).fetchall()
            by_cycle = conn.execute(
                f"""
                SELECT cycle_index, COUNT(*) AS calls, SUM(CASE WHEN ok = 1 THEN 1 ELSE 0 END) AS ok_calls,
                       AVG(response_chars) AS avg_chars
                FROM cycles
                WHERE scope_key IN ({placeholders})
                GROUP BY cycle_index
                ORDER BY cycle_index
                """,
                tuple(keys),
            ).fetchall()
        lines = ["# Metricas del orquestador", ""]
        if by_engine:
            lines.extend(["## Por motor", ""])
            for row in by_engine:
                lines.append(
                    f"- {row['engine']}: llamadas={row['calls']}, ok={row['ok_calls']}, promedio_chars={int(row['avg_chars'] or 0)}, max_chars={int(row['max_chars'] or 0)}"
                )
            lines.append("")
        if by_cycle:
            lines.extend(["## Por ciclo", ""])
            for row in by_cycle:
                lines.append(
                    f"- Ciclo {row['cycle_index']}: llamadas={row['calls']}, ok={row['ok_calls']}, promedio_chars={int(row['avg_chars'] or 0)}"
                )
            lines.append("")
        if len(lines) == 2:
            lines.append("- Aun no hay ejecuciones registradas para este plan.")
        return "\n".join(lines)

    def _empty_memory(self) -> dict:
        payload = {section: [] for section in MEMORY_SECTIONS}
        for field in MEMORY_STRING_FIELDS:
            payload[field] = ""
        for field in MEMORY_LIST_FIELDS:
            payload[field] = []
        for field in MEMORY_DICT_FIELDS:
            payload[field] = {}
        payload["locked_sections"] = []
        payload["compression"] = {"method": "union-dedupe", "lossless": True}
        payload["schema_version"] = 2
        return payload

    def _normalize_memory(self, payload: dict) -> dict:
        normalized = self._empty_memory()
        if not isinstance(payload, dict):
            return normalized
        for field in MEMORY_STRING_FIELDS:
            value = payload.get(field, "")
            normalized[field] = value.strip() if isinstance(value, str) else ""
        for section in MEMORY_SECTIONS:
            items = payload.get(section, [])
            if isinstance(items, str):
                items = [items]
            if isinstance(items, list):
                normalized[section] = _dedupe_lines(items)
        for field in MEMORY_LIST_FIELDS:
            items = payload.get(field, [])
            if isinstance(items, str):
                items = [items]
            if isinstance(items, list):
                normalized[field] = _dedupe_lines(items)
        for field in MEMORY_DICT_FIELDS:
            value = payload.get(field, {})
            if isinstance(value, dict):
                normalized[field] = value
        locked_sections = payload.get("locked_sections", [])
        if isinstance(locked_sections, str):
            locked_sections = [locked_sections]
        if isinstance(locked_sections, list):
            normalized["locked_sections"] = sorted(
                section for section in _dedupe_lines(locked_sections) if section in MEMORY_SECTIONS
            )
        compression = payload.get("compression", {})
        if isinstance(compression, dict):
            normalized["compression"] = {
                "method": compression.get("method", "union-dedupe"),
                "lossless": bool(compression.get("lossless", True)),
            }
        try:
            normalized["schema_version"] = max(2, int(payload.get("schema_version", 2)))
        except (TypeError, ValueError):
            normalized["schema_version"] = 2
        return normalized


class EditorialMemoryBuilder:
    def __init__(
        self,
        workspace: AulaTeXWorkspace | None = None,
        llm_bridge: AulaTeXLLMClient | None = None,
        store: EditorialMemoryStore | None = None,
    ) -> None:
        self.workspace = workspace or AulaTeXWorkspace()
        self.llm = llm_bridge or AulaTeXLLMClient()
        self.store = store or EditorialMemoryStore(self.workspace)

    def build(
        self,
        request: EditorialMemoryRequest,
        progress: Callable[[EditorialMemoryEvent], None] | None = None,
        cancel_event: Event | None = None,
    ) -> EditorialMemoryBuildResult:
        run_id = self.workspace.timestamp()
        run_dir = self.store.root / "runs" / f"{run_id}-editorial-memory"
        run_dir.mkdir(parents=True, exist_ok=True)

        by_key, children = self.workspace.editorial_scope_index()
        source_scope = by_key.get(request.source_scope_key)
        if source_scope is None:
            raise ValueError(f"Scope no encontrado: {request.source_scope_key}")
        if request.build_level not in EDITORIAL_LEVELS:
            raise ValueError(f"Nivel editorial invalido: {request.build_level}")

        engines = self._normalize_engines(request.engines)
        self.store.start_run(request, engines, run_id)
        for scope in by_key.values():
            self.store.upsert_scope(scope)

        plan = self._plan_scopes(source_scope, request.build_level, request.propagation_mode, by_key, children)
        total = max(1, len(plan) * max(1, int(request.iterations)) * len(engines))
        current = 0
        cycle_logs: list[dict] = []
        overall_ok = True
        cancelled = False

        self._emit(progress, EditorialMemoryEvent("start", f"Plan editorial: {', '.join(scope.label for scope in plan)}", 0, total, source_scope.key))

        for scope in plan:
            if self._is_cancelled(cancel_event):
                cancelled = True
                break
            for cycle_index in range(1, max(1, int(request.iterations)) + 1):
                if self._is_cancelled(cancel_event):
                    cancelled = True
                    break
                for engine in engines:
                    if self._is_cancelled(cancel_event):
                        cancelled = True
                        break
                    current += 1
                    prompt = self._build_prompt(source_scope, scope, cycle_index, request, by_key)
                    self._emit(
                        progress,
                        EditorialMemoryEvent(
                            "progress",
                            f"{scope.label} | ciclo {cycle_index} | {engine}",
                            current,
                            total,
                            scope.key,
                            engine,
                            cycle_index,
                        ),
                    )
                    result = self.llm.call(engine, prompt, max_tokens=request.max_tokens)
                    response_text = result.text if result.ok else result.error
                    self.store.record_cycle(
                        run_id=run_id,
                        scope_key=scope.key,
                        cycle_index=cycle_index,
                        engine=result.engine,
                        ok=result.ok,
                        response_text=response_text,
                    )
                    current_memory = self.store.get_memory(scope.key)
                    candidate = self._parse_response(response_text, source_scope, scope, engine, cycle_index)
                    merged = self._merge_non_regressive(current_memory, candidate, source_scope, scope)
                    self.store.save_memory(scope, merged, request.source_scope_key)
                    cycle_logs.append(
                        {
                            "scope_key": scope.key,
                            "scope_level": scope.level,
                            "cycle": cycle_index,
                            "engine": result.engine,
                            "ok": result.ok,
                            "chars": len(response_text),
                        }
                    )
                    scope_file = run_dir / f"{current:04d}-{scope.key.replace('/', '__')}-{result.engine.replace(' ', '_')}.md"
                    scope_file.write_text(response_text, encoding="utf-8")
                    if not result.ok:
                        overall_ok = False
                    self._emit(
                        progress,
                        EditorialMemoryEvent(
                            "result",
                            f"{result.engine}: {'OK' if result.ok else 'ERROR'} ({len(response_text)} chars)",
                            current,
                            total,
                            scope.key,
                            result.engine,
                            cycle_index,
                        ),
                    )
                if cancelled:
                    break
            if cancelled:
                break

        manifest = {
            "run_id": run_id,
            "source_scope_key": request.source_scope_key,
            "build_level": request.build_level,
            "propagation_mode": request.propagation_mode,
            "iterations": int(request.iterations),
            "engines": engines,
            "built_scopes": [scope.key for scope in plan],
            "cycles": cycle_logs,
            "ok": overall_ok and not cancelled,
            "cancelled": cancelled,
        }
        manifest_path = run_dir / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        self.store.finish_run(run_id, overall_ok and not cancelled)
        self.workspace.append_bitacora(run_id, "memoria-editorial", manifest)
        if cancelled:
            self._emit(progress, EditorialMemoryEvent("cancelled", f"Memoria editorial cancelada en {run_dir}", current, total, source_scope.key))
        else:
            self._emit(progress, EditorialMemoryEvent("done", f"Memoria editorial cerrada en {run_dir}", total, total, source_scope.key))
        return EditorialMemoryBuildResult(run_id, run_dir, manifest_path, tuple(scope.key for scope in plan), overall_ok and not cancelled, cancelled)

    def plan_scopes(
        self,
        source_scope_key: str,
        build_level: str,
        propagation_mode: str,
    ) -> list[EditorialScope]:
        by_key, children = self.workspace.editorial_scope_index()
        source_scope = by_key.get(source_scope_key)
        if source_scope is None:
            return []
        return self._plan_scopes(source_scope, build_level, propagation_mode, by_key, children)

    def _normalize_engines(self, engines: list[str] | tuple[str, ...]) -> list[str]:
        selected = [engine for engine in engines if engine in self.llm.engines()]
        if not selected:
            selected = [engine for engine in LLM_ENGINES if engine in ENGINE_PRIORITY]
        return sorted(selected, key=lambda engine: (ENGINE_PRIORITY.get(engine, 999), engine))

    def _plan_scopes(
        self,
        source_scope: EditorialScope,
        build_level: str,
        propagation_mode: str,
        by_key: dict[str, EditorialScope],
        children: dict[str, list[EditorialScope]],
    ) -> list[EditorialScope]:
        allowed = {"local", "ascendente", "ascendente-exhaustivo", "recursivo"}
        mode = propagation_mode if propagation_mode in allowed else "ascendente"
        order = {level: index for index, level in enumerate(EDITORIAL_LEVELS)}
        if order[build_level] < order[source_scope.level]:
            raise ValueError("El nivel de construccion no puede ser mas profundo que el origen seleccionado")

        plan: list[EditorialScope] = []
        seen: set[str] = set()
        current = source_scope
        while current is not None:
            if mode == "recursivo":
                self._append_subtree_postorder(plan, seen, current, children)
            else:
                self._append_scope(plan, seen, current)

            if mode == "ascendente-exhaustivo":
                parent = by_key.get(current.parent_key)
                if parent is not None:
                    for sibling in children.get(parent.key, []):
                        self._append_scope(plan, seen, sibling)

            if current.level == build_level:
                break
            if mode == "local":
                break
            next_scope = by_key.get(current.parent_key)
            current = next_scope
        return plan

    def _append_scope(self, plan: list[EditorialScope], seen: set[str], scope: EditorialScope) -> None:
        if scope.key in seen:
            return
        plan.append(scope)
        seen.add(scope.key)

    def _append_subtree_postorder(
        self,
        plan: list[EditorialScope],
        seen: set[str],
        scope: EditorialScope,
        children: dict[str, list[EditorialScope]],
    ) -> None:
        for child in children.get(scope.key, []):
            self._append_subtree_postorder(plan, seen, child, children)
        self._append_scope(plan, seen, scope)

    def _build_prompt(
        self,
        source_scope: EditorialScope,
        target_scope: EditorialScope,
        cycle_index: int,
        request: EditorialMemoryRequest,
        by_key: dict[str, EditorialScope],
    ) -> str:
        current_memory = self.store.get_memory(target_scope.key)
        parent_memory = ""
        if target_scope.parent_key and target_scope.parent_key in by_key:
            parent_memory = self.store.summarize_for_scope(target_scope.parent_key, include_ancestors=True, max_chars=2500)
        local_context = self.workspace.context_summary(target_scope.relative_path, max_chars=4000)
        memory_json = json.dumps(current_memory, ensure_ascii=False, indent=2)
        return (
            "Eres AulaTeX y estas consolidando memoria editorial persistente para una suite academica en LaTeX. "
            "Debes preservar todo lo valido, agregar solo mejoras verificables y nunca eliminar reglas utiles previas. "
            "La compresion debe ser lossless por deduplicacion, no por recorte. Responde solo JSON valido.\n\n"
            f"Origen: {source_scope.level} | {source_scope.key}\n"
            f"Destino: {target_scope.level} | {target_scope.key}\n"
            f"Propagacion: {request.propagation_mode}\n"
            f"Ciclo: {cycle_index}\n\n"
            "Esquema requerido:\n"
            "{\n"
            '  "summary": ["..."],\n'
            '  "identity_rules": ["..."],\n'
            '  "structure_rules": ["..."],\n'
            '  "activity_rules": ["..."],\n'
            '  "quality_gates": ["..."],\n'
            '  "latex_rules": ["..."],\n'
            '  "bibliography_rules": ["..."],\n'
            '  "propagation_hints": ["..."],\n'
            '  "open_questions": ["..."]\n'
            "}\n\n"
            "Reglas: usa frases cortas, accionables y sin duplicados; marca supuestos; no inventes fuentes.\n\n"
            f"Memoria actual del destino:\n{memory_json}\n\n"
            f"Memoria heredada:\n{parent_memory or 'Sin memoria heredada aun.'}\n\n"
            f"Contexto local:\n{local_context}\n"
        )

    def _parse_response(
        self,
        response_text: str,
        source_scope: EditorialScope,
        target_scope: EditorialScope,
        engine: str,
        cycle_index: int,
    ) -> dict:
        payload = _extract_first_json(response_text)
        if payload is None:
            fallback_lines = _extract_bullets(response_text)
            return {
                "summary": fallback_lines[:8] or [f"Salida sin JSON parseable desde {engine} para {target_scope.label}"],
                "identity_rules": [f"Fuente provisional: {engine} desde {source_scope.label}"],
                "structure_rules": [],
                "activity_rules": [],
                "quality_gates": ["Revisar respuesta no estructurada antes de aplicar aguas abajo."],
                "latex_rules": [],
                "bibliography_rules": [],
                "propagation_hints": [f"Ciclo {cycle_index} necesita normalizacion manual si se reutiliza."],
                "open_questions": [],
            }
        return payload

    def _merge_non_regressive(
        self,
        current: dict,
        candidate: dict,
        source_scope: EditorialScope,
        target_scope: EditorialScope,
    ) -> dict:
        merged = self.store._normalize_memory(current)
        candidate_normalized = self.store._normalize_memory(candidate)
        locked_sections = set(merged.get("locked_sections", []))
        for section in MEMORY_SECTIONS:
            if section in locked_sections:
                merged[section] = _dedupe_lines(merged.get(section, []))
                continue
            merged[section] = _dedupe_lines(merged.get(section, []) + candidate_normalized.get(section, []))
        merged["sources"] = _dedupe_lines(
            merged.get("sources", [])
            + candidate_normalized.get("sources", [])
            + [source_scope.key, target_scope.key]
        )
        merged["locked_sections"] = sorted(locked_sections)
        merged["compression"] = {"method": "union-dedupe", "lossless": True}
        merged["schema_version"] = max(2, int(candidate_normalized.get("schema_version", 2) or 2))
        return merged

    def _emit(self, callback: Callable[[EditorialMemoryEvent], None] | None, event: EditorialMemoryEvent) -> None:
        if callback is not None:
            callback(event)

    def _is_cancelled(self, cancel_event: Event | None) -> bool:
        return bool(cancel_event is not None and cancel_event.is_set())


def _dedupe_lines(items: list[str]) -> list[str]:
    seen: set[str] = set()
    normalized: list[str] = []
    for item in items:
        if not isinstance(item, str):
            continue
        value = re.sub(r"\s+", " ", item).strip(" -\t\r\n")
        if not value:
            continue
        marker = value.lower()
        if marker in seen:
            continue
        seen.add(marker)
        normalized.append(value)
    return normalized


def _extract_first_json(text: str) -> dict | None:
    if not text.strip():
        return None
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL | re.IGNORECASE)
    if fenced:
        try:
            payload = json.loads(fenced.group(1))
            return payload if isinstance(payload, dict) else None
        except json.JSONDecodeError:
            pass

    start = text.find("{")
    while start >= 0:
        depth = 0
        for index in range(start, len(text)):
            char = text[index]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    candidate = text[start : index + 1]
                    try:
                        payload = json.loads(candidate)
                        return payload if isinstance(payload, dict) else None
                    except json.JSONDecodeError:
                        break
        start = text.find("{", start + 1)
    return None


def _extract_bullets(text: str) -> list[str]:
    bullets: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(("-", "*")):
            bullets.append(line[1:].strip())
            continue
        if re.match(r"^\d+[.)]\s+", line):
            bullets.append(re.sub(r"^\d+[.)]\s+", "", line))
    return _dedupe_lines(bullets)


def _latex_to_plain(text: str) -> str:
    value = text or ""
    value = re.sub(r"\\textbf\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\textit\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\emph\{([^{}]*)\}", r"\1", value)
    value = value.replace("\\\\", " ")
    value = value.replace("~", " ")
    value = re.sub(r"\\[a-zA-Z]+", " ", value)
    value = value.replace("{", " ").replace("}", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def _extract_nonempty_lines(text: str, *, limit: int = 8, max_len: int = 240) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        line = _latex_to_plain(raw)
        if not line:
            continue
        lines.append(line[:max_len])
        if len(lines) >= limit:
            break
    return _dedupe_lines(lines)


def _extract_program_context(text: str) -> dict:
    normalized = text or ""
    headings = list(re.finditer(r"^##\s+(.+)$", normalized, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(headings):
        start = match.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(normalized)
        sections[match.group(1).strip().lower()] = normalized[start:end].strip()

    work_axes: list[str] = []
    ejes = sections.get("ejes de trabajo", "")
    for line in ejes.splitlines():
        stripped = line.strip()
        if re.match(r"^\d+[.)]?\s+", stripped):
            work_axes.append(re.sub(r"^\d+[.)]?\s+", "", stripped))

    source_fragments = []
    for key in ("encuadre institucional", "proposito de realizacion"):
        if sections.get(key):
            source_fragments.extend(_extract_nonempty_lines(sections[key], limit=2, max_len=240))
    source_fragments.extend(work_axes[:5])
    return {
        "institutional_frame": _latex_to_plain(sections.get("encuadre institucional", "")),
        "purpose": _latex_to_plain(sections.get("proposito de realizacion", "")),
        "work_axes": _dedupe_lines(work_axes),
        "source_fragments": _dedupe_lines(source_fragments),
    }


def _extract_bibliography_index(text: str) -> list[str]:
    entries: list[str] = []
    entry_pattern = re.compile(r"@\w+\{\s*([^,]+),(.+?)(?=^@\w+\{|\Z)", re.DOTALL | re.MULTILINE)
    for match in entry_pattern.finditer(text or ""):
        key = match.group(1).strip()
        body = match.group(2)
        title_match = re.search(r"\btitle\s*=\s*[{"](.+?)[}"]\s*,?\n", body, re.DOTALL | re.IGNORECASE)
        title = _latex_to_plain(title_match.group(1)) if title_match else ""
        entries.append(f"{key} :: {title}" if title else key)
    return _dedupe_lines(entries)


def _extract_bibliography_titles(entries: list[str]) -> list[str]:
    titles: list[str] = []
    for item in entries:
        if " :: " in item:
            _key, title = item.split(" :: ", 1)
            if title:
                titles.append(title)
    return _dedupe_lines(titles)


def _extract_tex_blueprint(text: str, relative_path: str) -> dict:
    macros: dict[str, str] = {}
    for name in ("documenttitle", "documentsubtitle", "documentsubject", "coursename", "coursecode", "documentauthor"):
        match = re.search(rf"\\def\\{name}\s*\{{(.*?)\}}", text, re.DOTALL)
        if match:
            macros[name] = _latex_to_plain(match.group(1))

    abstract_match = re.search(r"\\begin\{abstractd\}(.*?)\\end\{abstractd\}", text, re.DOTALL)
    abstract_text = _latex_to_plain(abstract_match.group(1)) if abstract_match else ""
    section_titles = _dedupe_lines([_latex_to_plain(item) for item in re.findall(r"\\section\{([^}]*)\}", text)])
    subsection_titles = _dedupe_lines([_latex_to_plain(item) for item in re.findall(r"\\subsection\{([^}]*)\}", text)])
    cited_keys: list[str] = []
    for chunk in re.findall(r"\\cite\w*\{([^}]*)\}", text):
        cited_keys.extend(part.strip() for part in chunk.split(",") if part.strip())
    concept_nodes = _dedupe_lines(
        [_latex_to_plain(item) for item in re.findall(r"\\node\[[^\]]+\]\s*\([^)]+\)\s*at\s*\([^)]+\)\s*\{([^}]*)\};", text)]
    )
    intro_match = re.search(r"\\section\{Introducci[oó]n\}(.*?)(?=\\section\{|\\end\{document\})", text, re.DOTALL | re.IGNORECASE)
    intro_text = _latex_to_plain(intro_match.group(1)) if intro_match else ""
    source_fragments = []
    if abstract_text:
        source_fragments.extend(_extract_nonempty_lines(abstract_text, limit=3, max_len=260))
    if intro_text:
        source_fragments.extend(_extract_nonempty_lines(intro_text, limit=4, max_len=260))
    source_fragments.extend(concept_nodes[:8])

    return {
        "relative_path": relative_path,
        **macros,
        "abstract": abstract_text,
        "section_titles": section_titles,
        "subsection_titles": subsection_titles,
        "cited_keys": _dedupe_lines(cited_keys),
        "concepts": concept_nodes,
        "source_fragments": _dedupe_lines(source_fragments),
    }