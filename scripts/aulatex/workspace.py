from __future__ import annotations

import json
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path


INSTITUTIONS = ("UnADM", "UCNL", "UANL", "ITESCA", "IIIEPE")
SKIP_DIR_NAMES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".build",
    "assets-itesca",
    "assets-ucnl",
    "assets-uanl",
    "assets-unadm",
    "logs-compilacion-tex",
}


@dataclass(frozen=True)
class CommandResult:
    ok: bool
    returncode: int
    stdout: str
    stderr: str


class AulaTeXWorkspace:
    def __init__(self, repo_root: str | Path | None = None) -> None:
        self.repo_root = Path(repo_root or Path(__file__).resolve().parents[2]).resolve()
        self.scripts_dir = self.repo_root / "scripts"
        self.feedback_root = self.repo_root / "retroalimentacion-editorial" / "aulatex"
        self.feedback_root.mkdir(parents=True, exist_ok=True)

    def timestamp(self) -> str:
        return time.strftime("%Y%m%d-%H%M%S")

    def relative(self, path: str | Path) -> str:
        p = Path(path).resolve()
        try:
            return p.relative_to(self.repo_root).as_posix()
        except ValueError:
            return str(p)

    def resolve_target(self, target: str | Path | None) -> Path:
        if not target:
            return self.repo_root
        p = Path(target)
        if not p.is_absolute():
            p = self.repo_root / p
        return p.resolve()

    def scan_tree(self) -> dict[str, dict[str, list[str]]]:
        tree: dict[str, dict[str, list[str]]] = {}
        for institution in INSTITUTIONS:
            root = self.repo_root / institution
            if not root.exists():
                continue
            careers: dict[str, list[str]] = {}
            for career in sorted([p for p in root.iterdir() if p.is_dir() and p.name not in SKIP_DIR_NAMES]):
                subjects = [
                    child.name
                    for child in sorted(career.iterdir())
                    if child.is_dir() and child.name not in SKIP_DIR_NAMES and not child.name.startswith("referencias-")
                ]
                careers[career.name] = subjects
            tree[institution] = careers
        return tree

    def find_tex_files(self, target: str | Path | None = None, limit: int = 200) -> list[Path]:
        root = self.resolve_target(target)
        if root.is_file() and root.suffix.lower() == ".tex":
            return [root]
        if not root.exists():
            return []
        files: list[Path] = []
        for path in sorted(root.rglob("*.tex")):
            if any(part in SKIP_DIR_NAMES for part in path.relative_to(root).parts):
                continue
            files.append(path)
            if len(files) >= limit:
                break
        return files

    def context_summary(self, target: str | Path | None, max_chars: int = 9000) -> str:
        root = self.resolve_target(target)
        chunks: list[str] = [f"Target: {self.relative(root)}"]
        if not root.exists():
            chunks.append("Target does not exist yet.")
            return "\n".join(chunks)

        if root.is_file():
            candidates = [root]
        else:
            names = ("README.md", "COMPILACION.md")
            candidates = [root / name for name in names if (root / name).exists()]
            candidates.extend(sorted(root.glob("programa-analitico*.md"))[:3])
            candidates.extend(sorted(root.glob("*.bib"))[:3])
            candidates.extend(sorted(root.glob("reporte-*.tex"))[:2])
            candidates.extend(sorted(root.glob("presentacion-*.tex"))[:2])

        for candidate in candidates:
            if not candidate.exists() or not candidate.is_file():
                continue
            if candidate.suffix.lower() not in {".md", ".txt", ".tex", ".bib"}:
                continue
            try:
                text = candidate.read_text(encoding="utf-8", errors="replace")
            except Exception as exc:
                chunks.append(f"## {self.relative(candidate)}\n[read error: {exc}]")
                continue
            remaining = max_chars - sum(len(c) for c in chunks)
            if remaining <= 0:
                break
            chunks.append(f"## {self.relative(candidate)}\n{text[:remaining]}")
        return "\n\n".join(chunks)

    def compile_tex(self, tex_file: str | Path, clean_mode: str = "none") -> CommandResult:
        tex = self.resolve_target(tex_file)
        script = self.scripts_dir / "latexmk-build.ps1"
        cmd = [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script),
            str(tex),
            "-CleanMode",
            clean_mode,
        ]
        proc = subprocess.run(
            cmd,
            cwd=str(self.repo_root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return CommandResult(proc.returncode == 0, proc.returncode, proc.stdout, proc.stderr)

    def append_bitacora(self, run_id: str, title: str, data: dict) -> None:
        path = self.feedback_root / "bitacora.md"
        payload = json.dumps(data, ensure_ascii=False, indent=2)
        prefix = ""
        if not path.exists() or not path.read_text(encoding="utf-8", errors="replace").strip():
            prefix = "# Bitacora AulaTeX\n\n"
        with path.open("a", encoding="utf-8") as fh:
            fh.write(f"{prefix}\n## {run_id} - {title}\n\n```json\n{payload}\n```\n")
