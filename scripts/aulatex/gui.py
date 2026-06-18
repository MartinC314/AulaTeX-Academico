from __future__ import annotations

import os
import queue
import subprocess
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from .agent import AgentRequest, AulaTeXAgent
from .agentic_patterns import pattern_catalog_markdown
from .config import credential_status
from .llm_bridge import LLM_ENGINES, AulaTeXLLMClient
from .workspace import AulaTeXWorkspace


class AulaTeXApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("AulaTeX - suite editorial e investigacion")
        self.geometry("1180x760")
        self.minsize(980, 640)

        self.workspace = AulaTeXWorkspace()
        self.llm = AulaTeXLLMClient()
        self.agent = AulaTeXAgent(self.workspace, self.llm)
        self.events: queue.Queue[tuple[str, str]] = queue.Queue()

        self._build_ui()
        self.after(250, self._drain_events)

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky="nsew")

        self.panel_tab = ttk.Frame(notebook, padding=12)
        self.llm_tab = ttk.Frame(notebook, padding=12)
        self.agent_tab = ttk.Frame(notebook, padding=12)
        self.arch_tab = ttk.Frame(notebook, padding=12)
        self.compile_tab = ttk.Frame(notebook, padding=12)
        self.extractor_tab = ttk.Frame(notebook, padding=12)
        self.feedback_tab = ttk.Frame(notebook, padding=12)

        notebook.add(self.panel_tab, text="Panel")
        notebook.add(self.llm_tab, text="LLM")
        notebook.add(self.agent_tab, text="Agente")
        notebook.add(self.arch_tab, text="Arquitectura")
        notebook.add(self.compile_tab, text="Compilar")
        notebook.add(self.extractor_tab, text="Extractor")
        notebook.add(self.feedback_tab, text="Retroalimentacion")

        self._build_panel_tab()
        self._build_llm_tab()
        self._build_agent_tab()
        self._build_arch_tab()
        self._build_compile_tab()
        self._build_extractor_tab()
        self._build_feedback_tab()

    def _build_panel_tab(self) -> None:
        self.panel_tab.columnconfigure(1, weight=1)
        ttk.Label(self.panel_tab, text="Repositorio").grid(row=0, column=0, sticky="w")
        ttk.Label(self.panel_tab, text=str(self.workspace.repo_root)).grid(row=0, column=1, sticky="w")
        ttk.Label(self.panel_tab, text="Credenciales").grid(row=1, column=0, sticky="w", pady=(8, 0))
        ttk.Label(self.panel_tab, text=str(self.llm.env_path)).grid(row=1, column=1, sticky="w", pady=(8, 0))
        ttk.Button(self.panel_tab, text="Verificar LLMs", command=self._check_llms).grid(row=2, column=0, sticky="w", pady=12)
        ttk.Button(self.panel_tab, text="Refrescar arbol", command=self._refresh_tree).grid(row=2, column=1, sticky="w", pady=12)
        self.tree_text = tk.Text(self.panel_tab, height=24, wrap="none")
        self.tree_text.grid(row=3, column=0, columnspan=2, sticky="nsew")
        self.panel_tab.rowconfigure(3, weight=1)
        self._refresh_tree()

    def _build_llm_tab(self) -> None:
        self.llm_tab.columnconfigure(1, weight=1)
        ttk.Label(self.llm_tab, text="Motor").grid(row=0, column=0, sticky="w")
        self.llm_engine = tk.StringVar(value="Codex")
        ttk.Combobox(self.llm_tab, textvariable=self.llm_engine, values=LLM_ENGINES, state="readonly").grid(row=0, column=1, sticky="ew")
        ttk.Label(self.llm_tab, text="Prompt").grid(row=1, column=0, sticky="nw", pady=(10, 0))
        self.prompt_text = tk.Text(self.llm_tab, height=10)
        self.prompt_text.grid(row=1, column=1, sticky="nsew", pady=(10, 0))
        ttk.Button(self.llm_tab, text="Ejecutar prompt", command=self._run_llm_prompt).grid(row=2, column=1, sticky="w", pady=8)
        self.llm_output = tk.Text(self.llm_tab, height=18)
        self.llm_output.grid(row=3, column=0, columnspan=2, sticky="nsew")
        self.llm_tab.rowconfigure(3, weight=1)

    def _build_agent_tab(self) -> None:
        self.agent_tab.columnconfigure(1, weight=1)
        self.agent_target = tk.StringVar(value="UnADM/licenciatura-en-derecho-unadm/historia-del-derecho-en-mexico-lde")
        self.agent_level = tk.StringVar(value="materia")
        self.agent_action = tk.StringVar(value="generar-actividad")
        self.agent_activity = tk.IntVar(value=1)
        self.agent_iterations = tk.IntVar(value=5)
        self.agent_engines = tk.StringVar(value="Codex, Claude Foundry, GPT-Pro, Auto (model-router)")
        self.agent_compile = tk.BooleanVar(value=True)
        self.agent_apply = tk.BooleanVar(value=False)

        ttk.Label(self.agent_tab, text="Objetivo").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.agent_tab, textvariable=self.agent_target).grid(row=0, column=1, sticky="ew")
        ttk.Button(self.agent_tab, text="Buscar", command=self._browse_agent_target).grid(row=0, column=2, padx=(8, 0))
        ttk.Label(self.agent_tab, text="Nivel").grid(row=1, column=0, sticky="w", pady=(8, 0))
        ttk.Combobox(self.agent_tab, textvariable=self.agent_level, values=("institucion", "carrera", "materia"), state="readonly").grid(row=1, column=1, sticky="ew", pady=(8, 0))
        ttk.Label(self.agent_tab, text="Accion").grid(row=2, column=0, sticky="w", pady=(8, 0))
        ttk.Combobox(
            self.agent_tab,
            textvariable=self.agent_action,
            values=("generar-plantilla", "generar-actividad", "realizar-actividad", "evaluar"),
            state="readonly",
        ).grid(row=2, column=1, sticky="ew", pady=(8, 0))
        ttk.Label(self.agent_tab, text="Actividad").grid(row=3, column=0, sticky="w", pady=(8, 0))
        ttk.Spinbox(self.agent_tab, from_=1, to=99, textvariable=self.agent_activity, width=8).grid(row=3, column=1, sticky="w", pady=(8, 0))
        ttk.Label(self.agent_tab, text="Motores").grid(row=4, column=0, sticky="w", pady=(8, 0))
        ttk.Entry(self.agent_tab, textvariable=self.agent_engines).grid(row=4, column=1, sticky="ew", pady=(8, 0))
        ttk.Label(self.agent_tab, text="Iteraciones").grid(row=5, column=0, sticky="w", pady=(8, 0))
        ttk.Spinbox(self.agent_tab, from_=1, to=5, textvariable=self.agent_iterations, width=8).grid(row=5, column=1, sticky="w", pady=(8, 0))
        ttk.Checkbutton(self.agent_tab, text="Compilar objetivo", variable=self.agent_compile).grid(row=6, column=1, sticky="w", pady=(8, 0))
        ttk.Checkbutton(self.agent_tab, text="Copiar reporte al objetivo", variable=self.agent_apply).grid(row=7, column=1, sticky="w")
        ttk.Button(self.agent_tab, text="Ejecutar ciclo investigar-compilar-evaluar", command=self._run_agent).grid(row=8, column=1, sticky="w", pady=10)
        self.agent_output = tk.Text(self.agent_tab, height=18)
        self.agent_output.grid(row=9, column=0, columnspan=3, sticky="nsew")
        self.agent_tab.rowconfigure(9, weight=1)

    def _build_arch_tab(self) -> None:
        self.arch_tab.columnconfigure(0, weight=1)
        self.arch_tab.rowconfigure(0, weight=1)
        self.arch_text = tk.Text(self.arch_tab, height=32, wrap="word")
        self.arch_text.grid(row=0, column=0, sticky="nsew")
        self.arch_text.insert("end", pattern_catalog_markdown())

    def _build_compile_tab(self) -> None:
        self.compile_tab.columnconfigure(1, weight=1)
        self.compile_target = tk.StringVar(value="")
        ttk.Label(self.compile_tab, text="Archivo .tex").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.compile_tab, textvariable=self.compile_target).grid(row=0, column=1, sticky="ew")
        ttk.Button(self.compile_tab, text="Buscar", command=self._browse_tex).grid(row=0, column=2, padx=(8, 0))
        ttk.Button(self.compile_tab, text="Compilar", command=self._compile_selected).grid(row=1, column=1, sticky="w", pady=10)
        self.compile_output = tk.Text(self.compile_tab, height=28)
        self.compile_output.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.compile_tab.rowconfigure(2, weight=1)

    def _build_extractor_tab(self) -> None:
        ttk.Button(self.extractor_tab, text="Abrir extractor GUI", command=self._open_extractor_gui).grid(row=0, column=0, sticky="w")
        ttk.Button(self.extractor_tab, text="Probar configuracion", command=self._probe_extractor).grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.extractor_output = tk.Text(self.extractor_tab, height=30)
        self.extractor_output.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(10, 0))
        self.extractor_tab.rowconfigure(1, weight=1)
        self.extractor_tab.columnconfigure(1, weight=1)

    def _build_feedback_tab(self) -> None:
        self.feedback_tab.columnconfigure(0, weight=1)
        ttk.Button(self.feedback_tab, text="Refrescar retroalimentacion", command=self._refresh_feedback).grid(row=0, column=0, sticky="w")
        self.feedback_text = tk.Text(self.feedback_tab, height=32)
        self.feedback_text.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        self.feedback_tab.rowconfigure(1, weight=1)
        self._refresh_feedback()

    def _thread(self, fn) -> None:
        threading.Thread(target=fn, daemon=True).start()

    def _log(self, widget: tk.Text, text: str) -> None:
        widget.insert("end", text + "\n")
        widget.see("end")

    def _check_llms(self) -> None:
        def work() -> None:
            for engine in self.llm.engines():
                result = self.llm.check(engine)
                self.events.put(("llm", f"[LLM] {engine}: {'OK' if result.ok else 'ERROR'} {result.text or result.error}"))

        self._thread(work)

    def _refresh_tree(self) -> None:
        self.tree_text.delete("1.0", "end")
        tree = self.workspace.scan_tree()
        self.tree_text.insert("end", "LLM credentials\n")
        for status in credential_status():
            label = "OK" if status.ok else "FALTAN"
            missing = ", ".join(status.missing) if status.missing else "-"
            self.tree_text.insert("end", f"  {status.engine}: {label} missing={missing}\n")
        self.tree_text.insert("end", "\n")
        for institution, careers in tree.items():
            self.tree_text.insert("end", f"{institution}\n")
            for career, subjects in careers.items():
                self.tree_text.insert("end", f"  {career} ({len(subjects)})\n")
            self.tree_text.insert("end", "\n")

    def _run_llm_prompt(self) -> None:
        prompt = self.prompt_text.get("1.0", "end").strip()
        if not prompt:
            messagebox.showwarning("AulaTeX", "Escribe un prompt.")
            return

        def work() -> None:
            result = self.llm.call(self.llm_engine.get(), prompt)
            self.events.put(("llm", f"[PROMPT {result.engine}] {'OK' if result.ok else 'ERROR'}\n{result.text or result.error}"))

        self._thread(work)

    def _browse_agent_target(self) -> None:
        path = filedialog.askdirectory(initialdir=str(self.workspace.repo_root))
        if path:
            self.agent_target.set(self.workspace.relative(path))

    def _run_agent(self) -> None:
        engines = [item.strip() for item in self.agent_engines.get().split(",") if item.strip()]
        request = AgentRequest(
            target=self.agent_target.get(),
            level=self.agent_level.get(),
            action=self.agent_action.get(),
            activity_number=int(self.agent_activity.get()),
            engines=engines,
            iterations=int(self.agent_iterations.get()),
            compile_tex=bool(self.agent_compile.get()),
            apply_feedback=bool(self.agent_apply.get()),
        )

        def work() -> None:
            result = self.agent.run(request)
            self.events.put(("agent", f"[AGENTE] {'OK' if result.ok else 'CON OBSERVACIONES'}\nReporte: {result.report_path}"))

        self._thread(work)

    def _browse_tex(self) -> None:
        path = filedialog.askopenfilename(initialdir=str(self.workspace.repo_root), filetypes=[("TeX", "*.tex")])
        if path:
            self.compile_target.set(self.workspace.relative(path))

    def _compile_selected(self) -> None:
        target = self.compile_target.get().strip()
        if not target:
            messagebox.showwarning("AulaTeX", "Selecciona un archivo .tex.")
            return

        def work() -> None:
            result = self.workspace.compile_tex(target)
            self.events.put(("compile", f"[COMPILAR] {'OK' if result.ok else 'ERROR'} {target}\n{result.stdout[-4000:]}\n{result.stderr[-2000:]}"))

        self._thread(work)

    def _open_extractor_gui(self) -> None:
        script = self.workspace.scripts_dir / "extractor.ps1"
        subprocess.Popen(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)], cwd=str(self.workspace.repo_root))

    def _probe_extractor(self) -> None:
        script = self.workspace.scripts_dir / "extractor-conceptos-ideas" / "runners" / "probar_configuracion.ps1"

        def work() -> None:
            proc = subprocess.run(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)],
                cwd=str(script.parent),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            self.events.put(("extractor", f"[EXTRACTOR] {proc.returncode}\n{proc.stdout}\n{proc.stderr}"))

        self._thread(work)

    def _refresh_feedback(self) -> None:
        self.feedback_text.delete("1.0", "end")
        bitacora = self.workspace.feedback_root / "bitacora.md"
        if bitacora.exists():
            self.feedback_text.insert("end", bitacora.read_text(encoding="utf-8", errors="replace")[-30000:])
        else:
            self.feedback_text.insert("end", "Todavia no hay bitacora AulaTeX.\n")

    def _drain_events(self) -> None:
        while True:
            try:
                category, event = self.events.get_nowait()
            except queue.Empty:
                break
            if category == "agent":
                self._log(self.agent_output, event)
            elif category == "llm":
                self._log(self.llm_output, event)
            elif category == "compile":
                self._log(self.compile_output, event)
            elif category == "extractor":
                self._log(self.extractor_output, event)
            self._refresh_feedback()
        self.after(250, self._drain_events)


def main() -> None:
    app = AulaTeXApp()
    app.mainloop()
