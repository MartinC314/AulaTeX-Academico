from __future__ import annotations

import os
import queue
import re
import subprocess
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from .agent import AgentRequest, AulaTeXAgent
from .agentic_patterns import pattern_catalog_markdown
from .chat_sessions import AulaTeXChatStore, MULTIMOTOR_SEVERITY_LABELS, multimotor_severity_label
from .config import credential_status
from .editorial_memory import (
    EDITORIAL_LEVELS,
    ENGINE_PRIORITY,
    MEMORY_SECTIONS,
    EditorialMemoryBuilder,
    EditorialMemoryEvent,
    EditorialMemoryRequest,
    EditorialMemoryStore,
)
from .llm_bridge import LLM_ENGINES, AulaTeXLLMClient
from .workspace import AulaTeXWorkspace, EditorialScope


UNSELECTED_OPTION = "Sin seleccionar"
PROPAGATION_LABELS = {
    "local": "Solo origen",
    "ascendente": "Ascendente",
    "ascendente-exhaustivo": "Ascendente exhaustivo",
}
PROPAGATION_VALUES = tuple(PROPAGATION_LABELS)


class ToolTip:
    def __init__(self, widget, text: str, *, wraplength: int = 340) -> None:
        self.widget = widget
        self.text = text
        self.wraplength = wraplength
        self.tip_window: tk.Toplevel | None = None
        self.widget.bind("<Enter>", self._show, add="+")
        self.widget.bind("<Leave>", self._hide, add="+")
        self.widget.bind("<ButtonPress>", self._hide, add="+")

    def _show(self, _event=None) -> None:
        if self.tip_window is not None or not self.text.strip():
            return
        x = self.widget.winfo_rootx() + 18
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 10
        self.tip_window = tk.Toplevel(self.widget)
        self.tip_window.wm_overrideredirect(True)
        self.tip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            self.tip_window,
            text=self.text,
            justify="left",
            background="#fffde7",
            relief="solid",
            borderwidth=1,
            wraplength=self.wraplength,
            padx=8,
            pady=6,
        )
        label.pack()

    def _hide(self, _event=None) -> None:
        if self.tip_window is not None:
            self.tip_window.destroy()
            self.tip_window = None


class AulaTeXApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("AulaTeX - suite editorial e investigacion")
        self.geometry("1180x760")
        self.minsize(980, 640)

        self.workspace = AulaTeXWorkspace()
        self.llm = AulaTeXLLMClient()
        self.chat_store = AulaTeXChatStore(self.workspace, self.llm)
        self.agent = AulaTeXAgent(self.workspace, self.llm)
        self.editorial_store = EditorialMemoryStore(self.workspace)
        self.editorial_builder = EditorialMemoryBuilder(self.workspace, self.llm, self.editorial_store)
        self.editorial_scopes, self.editorial_children = self.workspace.editorial_scope_index()
        self.events: queue.Queue[tuple[str, object]] = queue.Queue()
        self._tooltips: list[ToolTip] = []
        self._busy_groups: dict[str, list[tuple[object, str]]] = {}
        self.llm_session_nodes: dict[str, str] = {}
        self.llm_multi_severity = tk.StringVar(value="normal")
        self.feedback_cancel_event = threading.Event()

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
        self.builder_tab = ttk.Frame(notebook, padding=12)
        self.compile_tab = ttk.Frame(notebook, padding=12)
        self.extractor_tab = ttk.Frame(notebook, padding=12)
        self.feedback_tab = ttk.Frame(notebook, padding=12)

        notebook.add(self.panel_tab, text="Panel")
        notebook.add(self.llm_tab, text="LLM")
        notebook.add(self.agent_tab, text="Agente")
        notebook.add(self.arch_tab, text="Arquitectura")
        notebook.add(self.builder_tab, text="Construccion")
        notebook.add(self.compile_tab, text="Compilar")
        notebook.add(self.extractor_tab, text="Extractor")
        notebook.add(self.feedback_tab, text="Retroalimentacion")

        self._build_panel_tab()
        self._build_llm_tab()
        self._build_agent_tab()
        self._build_arch_tab()
        self._build_builder_tab()
        self._build_compile_tab()
        self._build_extractor_tab()
        self._build_feedback_tab()

    def _build_panel_tab(self) -> None:
        self.panel_tab.columnconfigure(1, weight=1)
        self.panel_tab.rowconfigure(3, weight=1)
        ttk.Label(self.panel_tab, text="Repositorio").grid(row=0, column=0, sticky="w")
        ttk.Label(self.panel_tab, text=str(self.workspace.repo_root)).grid(row=0, column=1, sticky="w")
        ttk.Label(self.panel_tab, text="Credenciales").grid(row=1, column=0, sticky="w", pady=(8, 0))
        ttk.Label(self.panel_tab, text=str(self.llm.env_path)).grid(row=1, column=1, sticky="w", pady=(8, 0))
        ttk.Button(self.panel_tab, text="Verificar LLMs", command=self._check_llms).grid(row=2, column=0, sticky="w", pady=12)
        ttk.Button(self.panel_tab, text="Refrescar arbol", command=self._refresh_tree).grid(row=2, column=1, sticky="w", pady=12)

        columns = ("bib", "pres", "rep")
        self.template_tree = ttk.Treeview(self.panel_tab, columns=columns, show="tree headings")
        self.template_tree.heading("#0", text="Plantillas")
        self.template_tree.heading("bib", text="Bibliografia")
        self.template_tree.heading("pres", text="Presentacion")
        self.template_tree.heading("rep", text="Reporte")
        self.template_tree.column("#0", width=480)
        self.template_tree.column("bib", width=100, anchor="center")
        self.template_tree.column("pres", width=100, anchor="center")
        self.template_tree.column("rep", width=100, anchor="center")
        self.template_tree.grid(row=3, column=0, columnspan=2, sticky="nsew")

        self.template_details = tk.Text(self.panel_tab, height=8)
        self.template_details.grid(row=4, column=0, columnspan=2, sticky="ew")
        self.template_tree.bind("<<TreeviewSelect>>", self._on_template_selected)
        self._refresh_tree()

    def _build_llm_tab(self) -> None:
        self.llm_tab.columnconfigure(0, weight=1)
        self.llm_tab.rowconfigure(1, weight=1)

        header = ttk.Frame(self.llm_tab)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        header.columnconfigure(0, weight=1)
        ttk.Label(
            header,
            text="Chat AulaTeX con sesiones persistentes, compactacion y modo multimotor.",
        ).grid(row=0, column=0, sticky="w")
        help_button = ttk.Button(header, text="Como usar", command=self._show_llm_help)
        help_button.grid(row=0, column=1, sticky="e")

        paned = ttk.Panedwindow(self.llm_tab, orient="horizontal")
        paned.grid(row=1, column=0, sticky="nsew")

        sidebar = ttk.LabelFrame(paned, text="Sesiones tematicas", padding=10)
        content = ttk.Frame(paned, padding=(12, 0, 0, 0))
        paned.add(sidebar, weight=1)
        paned.add(content, weight=4)

        sidebar.columnconfigure(0, weight=1)
        sidebar.rowconfigure(1, weight=1)
        ttk.Label(
            sidebar,
            text="Cinco espacios fijos: cada uno conserva historial y memoria compactada.",
            wraplength=250,
        ).grid(row=0, column=0, sticky="ew")

        self.llm_session_tree = ttk.Treeview(sidebar, columns=("motor", "ctx", "estado"), show="tree headings", height=12)
        self.llm_session_tree.heading("#0", text="Tema")
        self.llm_session_tree.heading("motor", text="Motor")
        self.llm_session_tree.heading("ctx", text="Contexto")
        self.llm_session_tree.heading("estado", text="Activos")
        self.llm_session_tree.column("#0", width=130)
        self.llm_session_tree.column("motor", width=120, anchor="center")
        self.llm_session_tree.column("ctx", width=92, anchor="center")
        self.llm_session_tree.column("estado", width=70, anchor="center")
        self.llm_session_tree.grid(row=1, column=0, sticky="nsew", pady=(8, 0))
        self.llm_session_tree.bind("<<TreeviewSelect>>", self._on_llm_session_selected)

        session_actions = ttk.Frame(sidebar)
        session_actions.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        compact_button = ttk.Button(session_actions, text="Compactar", command=self._compact_selected_llm_session)
        compact_button.grid(row=0, column=0, sticky="w")
        export_button = ttk.Button(session_actions, text="Exportar", command=self._export_selected_llm_session)
        export_button.grid(row=0, column=1, sticky="w", padx=(8, 0))
        clear_button = ttk.Button(session_actions, text="Limpiar", command=self._clear_selected_llm_session)
        clear_button.grid(row=0, column=2, sticky="w", padx=(8, 0))

        content.columnconfigure(0, weight=1)
        content.rowconfigure(2, weight=1)
        content.rowconfigure(4, weight=1)

        self.llm_session_title = tk.StringVar(value="Editorial")
        self.llm_session_meta = tk.StringVar(value="Selecciona una sesion para comenzar.")
        ttk.Label(content, textvariable=self.llm_session_title, font=("TkDefaultFont", 11, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Label(content, textvariable=self.llm_session_meta, wraplength=760).grid(row=1, column=0, sticky="ew", pady=(4, 10))

        transcript_frame = ttk.LabelFrame(content, text="Conversacion", padding=8)
        transcript_frame.grid(row=2, column=0, sticky="nsew")
        transcript_frame.columnconfigure(0, weight=1)
        transcript_frame.rowconfigure(0, weight=1)
        self.llm_output = tk.Text(transcript_frame, height=18, wrap="word")
        self.llm_output.grid(row=0, column=0, sticky="nsew")

        prompt_frame = ttk.LabelFrame(content, text="Nuevo mensaje", padding=8)
        prompt_frame.grid(row=3, column=0, sticky="ew", pady=(10, 0))
        prompt_frame.columnconfigure(0, weight=1)
        self.prompt_text = tk.Text(prompt_frame, height=7, wrap="word")
        self.prompt_text.grid(row=0, column=0, sticky="ew")
        prompt_actions = ttk.Frame(prompt_frame)
        prompt_actions.grid(row=1, column=0, sticky="ew", pady=(8, 0))
        prompt_actions.columnconfigure(1, weight=1)
        self.llm_send_button = ttk.Button(prompt_actions, text="Enviar al chat", command=self._run_llm_prompt)
        self.llm_send_button.grid(row=0, column=0, sticky="w")
        ttk.Label(prompt_actions, text="Severidad MultiMotor").grid(row=0, column=1, sticky="e", padx=(12, 6))
        self.llm_multi_severity_combo = ttk.Combobox(
            prompt_actions,
            textvariable=self.llm_multi_severity,
            values=tuple(MULTIMOTOR_SEVERITY_LABELS),
            state="readonly",
            width=12,
        )
        self.llm_multi_severity_combo.grid(row=0, column=2, sticky="e")
        self.llm_status = tk.StringVar(value="Listo")
        ttk.Label(prompt_actions, textvariable=self.llm_status).grid(row=0, column=3, sticky="e", padx=(12, 0))

        memory_frame = ttk.LabelFrame(content, text="Memoria compactada y diagnostico", padding=8)
        memory_frame.grid(row=4, column=0, sticky="nsew", pady=(10, 0))
        memory_frame.columnconfigure(0, weight=1)
        memory_frame.rowconfigure(0, weight=1)
        self.llm_system = tk.Text(memory_frame, height=10, wrap="word")
        self.llm_system.grid(row=0, column=0, sticky="nsew")

        self._attach_tooltip(
            help_button,
            "Abre una guia corta de uso del chat: cuando usar cada sesion, como se guarda el historial y como funciona la compactacion.",
        )
        self._attach_tooltip(
            self.llm_session_tree,
            "Cada fila es una sesion fija por tema. Se muestra motor, contexto estimado y numero de mensajes activos frente al total historico.",
        )
        self._attach_tooltip(
            compact_button,
            "Fuerza la compactacion del historial seleccionado para convertir mensajes antiguos en memoria breve reutilizable.",
        )
        self._attach_tooltip(
            export_button,
            "Exporta la sesion completa a Markdown dentro de retroalimentacion-editorial/aulatex/llm-chat/exports.",
        )
        self._attach_tooltip(
            clear_button,
            "Borra los mensajes y la memoria compactada de la sesion actual. Util cuando quieras reiniciar solo ese tema.",
        )
        self._attach_tooltip(
            self.prompt_text,
            "Escribe aqui la instruccion. El sistema agrega memoria compactada e historial reciente automaticamente antes de consultar el motor asignado.",
        )
        self._attach_tooltip(
            self.llm_send_button,
            "Envia el mensaje a la sesion activa. En MultiMotor se consultan todos los motores en paralelo y se sintetiza consenso.",
        )
        self._attach_tooltip(
            self.llm_multi_severity_combo,
            "Controla la profundidad de MultiMotor: rapido prioriza velocidad, normal equilibra y profundo solicita analisis y validaciones extra.",
        )
        self._attach_tooltip(
            self.llm_system,
            "Muestra ayuda del tema, resumen compacto persistente y, si aplica, el detalle del ultimo consenso multimotor.",
        )
        self._register_busy_widgets("llm-chat", self.llm_send_button, self.llm_multi_severity_combo)

        self._refresh_llm_sessions()
        self._refresh_llm_view("editorial")

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
        self.agent_browse_button = ttk.Button(self.agent_tab, text="Buscar", command=self._browse_agent_target)
        self.agent_browse_button.grid(row=0, column=2, padx=(8, 0))
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
        self.agent_run_button = ttk.Button(self.agent_tab, text="Ejecutar ciclo investigar-compilar-evaluar", command=self._run_agent)
        self.agent_run_button.grid(row=8, column=1, sticky="w", pady=10)
        self.agent_output = tk.Text(self.agent_tab, height=18)
        self.agent_output.grid(row=9, column=0, columnspan=3, sticky="nsew")
        self.agent_tab.rowconfigure(9, weight=1)
        self._attach_tooltip(self.agent_browse_button, "Selecciona la carpeta objetivo desde donde el agente leerá contexto y aplicará la memoria editorial heredada.")
        self._attach_tooltip(self.agent_run_button, "Ejecuta el ciclo agentico usando la memoria editorial persistente del scope resuelto y sus ancestros.")
        self._register_busy_widgets("agent", self.agent_run_button, self.agent_browse_button)

    def _build_arch_tab(self) -> None:
        self.arch_tab.columnconfigure(0, weight=1)
        self.arch_tab.rowconfigure(0, weight=1)
        self.arch_text = tk.Text(self.arch_tab, height=32, wrap="word")
        self.arch_text.grid(row=0, column=0, sticky="nsew")
        self.arch_text.insert("end", pattern_catalog_markdown())

    def _build_builder_tab(self) -> None:
        self.builder_tab.columnconfigure(0, weight=1)
        self.builder_tab.rowconfigure(1, weight=1)

        summary = tk.Text(self.builder_tab, height=12, wrap="word")
        summary.grid(row=0, column=0, sticky="ew")
        summary.insert(
            "end",
            "CONSTRUCCION DESCENDENTE DE NODOS\n\n"
            "Este flujo es distinto de Retroalimentacion y distinto del Agente actual.\n\n"
            "Objetivo:\n"
            "- Crear instituciones, carreras, materias o actividades nuevas.\n"
            "- Generar memoria fundacional.\n"
            "- Generar plan editorial.\n"
            "- Generar maqueta TEX.\n\n"
            "Memoria utilizada:\n"
            "Ancestros + Padre + Hermanos existentes.\n\n"
            "Formula:\n"
            "NodoNuevo = Ancestros + Padre + Hermanos + ReglasInterinstitucionales\n\n"
            "Posteriormente la maqueta pasa al flujo de investigacion, redaccion y evaluacion.\n"
        )
        summary.configure(state="disabled")

        planner = tk.Text(self.builder_tab, wrap="word")
        planner.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        planner.insert(
            "end",
            "Pendiente de implementacion operativa:\n\n"
            "1. Seleccionar padre editorial.\n"
            "2. Detectar hermanos existentes.\n"
            "3. Construir memoria fundacional.\n"
            "4. Generar plan.md.\n"
            "5. Generar maqueta.tex.\n"
            "6. Transferir al flujo de investigacion/redaccion.\n"
        )
        planner.configure(state="disabled")

    def _build_compile_tab(self) -> None:
        self.compile_tab.columnconfigure(1, weight=1)
        self.compile_target = tk.StringVar(value="")
        ttk.Label(self.compile_tab, text="Archivo .tex").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.compile_tab, textvariable=self.compile_target).grid(row=0, column=1, sticky="ew")
        self.compile_browse_button = ttk.Button(self.compile_tab, text="Buscar", command=self._browse_tex)
        self.compile_browse_button.grid(row=0, column=2, padx=(8, 0))
        self.compile_run_button = ttk.Button(self.compile_tab, text="Compilar", command=self._compile_selected)
        self.compile_run_button.grid(row=1, column=1, sticky="w", pady=10)
        self.compile_output = tk.Text(self.compile_tab, height=28)
        self.compile_output.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.compile_tab.rowconfigure(2, weight=1)
        self._attach_tooltip(self.compile_browse_button, "Busca un archivo TeX concreto para compilar con el wrapper compartido latexmk-build.ps1.")
        self._attach_tooltip(self.compile_run_button, "Lanza la compilación del TeX seleccionado y muestra el tail de stdout/stderr.")
        self._register_busy_widgets("compile", self.compile_run_button, self.compile_browse_button)

    def _build_extractor_tab(self) -> None:
        self.extractor_open_button = ttk.Button(self.extractor_tab, text="Abrir extractor GUI", command=self._open_extractor_gui)
        self.extractor_open_button.grid(row=0, column=0, sticky="w")
        self.extractor_probe_button = ttk.Button(self.extractor_tab, text="Probar configuracion", command=self._probe_extractor)
        self.extractor_probe_button.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.extractor_output = tk.Text(self.extractor_tab, height=30)
        self.extractor_output.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(10, 0))
        self.extractor_tab.rowconfigure(1, weight=1)
        self.extractor_tab.columnconfigure(1, weight=1)
        self._attach_tooltip(self.extractor_open_button, "Abre la interfaz específica del extractor de conceptos e ideas en una ventana separada.")
        self._attach_tooltip(self.extractor_probe_button, "Ejecuta la comprobación de configuración del extractor y reporta el resultado en esta pestaña.")
        self._register_busy_widgets("extractor", self.extractor_probe_button)

    def _build_feedback_tab(self) -> None:
        self.feedback_tab.columnconfigure(0, weight=1)
        self.feedback_tab.rowconfigure(5, weight=1)
        self.feedback_tab.rowconfigure(6, weight=1)

        self.feedback_institution = tk.StringVar(value=UNSELECTED_OPTION)
        self.feedback_career = tk.StringVar(value=UNSELECTED_OPTION)
        self.feedback_subject = tk.StringVar(value=UNSELECTED_OPTION)
        self.feedback_activity = tk.StringVar(value=UNSELECTED_OPTION)
        self.feedback_build_level = tk.StringVar(value="materia")
        self.feedback_propagation = tk.StringVar(value="ascendente")
        self.feedback_iterations = tk.IntVar(value=2)
        self.feedback_max_tokens = tk.IntVar(value=1400)
        self.feedback_engines = tk.StringVar(value=", ".join(self._ordered_feedback_engines()))
        self.feedback_scope_status = tk.StringVar(value="Origen resuelto: pendiente")
        self.feedback_progress_status = tk.StringVar(value="Listo para construir memoria editorial.")
        self.feedback_progress = tk.DoubleVar(value=0.0)

        source_frame = ttk.LabelFrame(self.feedback_tab, text="Origen editorial", padding=10)
        source_frame.grid(row=0, column=0, sticky="ew")
        for index in range(8):
            source_frame.columnconfigure(index, weight=1 if index % 2 else 0)

        ttk.Label(source_frame, text="Institucion").grid(row=0, column=0, sticky="w")
        self.feedback_institution_combo = ttk.Combobox(source_frame, textvariable=self.feedback_institution, state="readonly")
        self.feedback_institution_combo.grid(row=0, column=1, sticky="ew", padx=(6, 12))
        self.feedback_institution_combo.bind("<<ComboboxSelected>>", self._on_feedback_source_changed)

        ttk.Label(source_frame, text="Carrera").grid(row=0, column=2, sticky="w")
        self.feedback_career_combo = ttk.Combobox(source_frame, textvariable=self.feedback_career, state="readonly")
        self.feedback_career_combo.grid(row=0, column=3, sticky="ew", padx=(6, 12))
        self.feedback_career_combo.bind("<<ComboboxSelected>>", self._on_feedback_source_changed)

        ttk.Label(source_frame, text="Materia").grid(row=0, column=4, sticky="w")
        self.feedback_subject_combo = ttk.Combobox(source_frame, textvariable=self.feedback_subject, state="readonly")
        self.feedback_subject_combo.grid(row=0, column=5, sticky="ew", padx=(6, 12))
        self.feedback_subject_combo.bind("<<ComboboxSelected>>", self._on_feedback_source_changed)

        ttk.Label(source_frame, text="Actividad").grid(row=0, column=6, sticky="w")
        self.feedback_activity_combo = ttk.Combobox(source_frame, textvariable=self.feedback_activity, state="readonly")
        self.feedback_activity_combo.grid(row=0, column=7, sticky="ew", padx=(6, 0))
        self.feedback_activity_combo.bind("<<ComboboxSelected>>", self._on_feedback_source_changed)

        ttk.Label(source_frame, textvariable=self.feedback_scope_status).grid(row=1, column=0, columnspan=8, sticky="w", pady=(10, 0))

        control_frame = ttk.LabelFrame(self.feedback_tab, text="Construccion de memoria", padding=10)
        control_frame.grid(row=1, column=0, sticky="ew", pady=(10, 0))
        for index in range(6):
            control_frame.columnconfigure(index, weight=1 if index in {1, 3, 5} else 0)

        ttk.Label(control_frame, text="Nivel destino").grid(row=0, column=0, sticky="w")
        self.feedback_build_combo = ttk.Combobox(control_frame, textvariable=self.feedback_build_level, state="readonly")
        self.feedback_build_combo.grid(row=0, column=1, sticky="ew", padx=(6, 12))
        self.feedback_build_combo.bind("<<ComboboxSelected>>", self._on_feedback_plan_changed)

        ttk.Label(control_frame, text="Propagacion").grid(row=0, column=2, sticky="w")
        self.feedback_propagation_combo = ttk.Combobox(
            control_frame,
            textvariable=self.feedback_propagation,
            values=PROPAGATION_VALUES,
            state="readonly",
        )
        self.feedback_propagation_combo.grid(row=0, column=3, sticky="ew", padx=(6, 12))
        self.feedback_propagation_combo.bind("<<ComboboxSelected>>", self._on_feedback_plan_changed)

        ttk.Label(control_frame, text="Iteraciones").grid(row=0, column=4, sticky="w")
        self.feedback_iterations_spin = ttk.Spinbox(control_frame, from_=1, to=12, textvariable=self.feedback_iterations, width=8)
        self.feedback_iterations_spin.grid(row=0, column=5, sticky="w", padx=(6, 0))

        ttk.Label(control_frame, text="Motores en orden").grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.feedback_engines_entry = ttk.Entry(control_frame, textvariable=self.feedback_engines)
        self.feedback_engines_entry.grid(row=1, column=1, columnspan=3, sticky="ew", padx=(6, 12), pady=(10, 0))
        ttk.Label(control_frame, text="Max tokens").grid(row=1, column=4, sticky="w", pady=(10, 0))
        self.feedback_tokens_spin = ttk.Spinbox(control_frame, from_=128, to=16000, increment=128, textvariable=self.feedback_max_tokens, width=10)
        self.feedback_tokens_spin.grid(row=1, column=5, sticky="w", padx=(6, 0), pady=(10, 0))

        action_frame = ttk.Frame(self.feedback_tab)
        action_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        action_frame.columnconfigure(6, weight=1)
        self.feedback_run_button = ttk.Button(action_frame, text="Construir memoria editorial", command=self._run_feedback_memory)
        self.feedback_run_button.grid(row=0, column=0, sticky="w")
        self.feedback_cancel_button = ttk.Button(action_frame, text="Cancelar", command=self._cancel_feedback_memory, state="disabled")
        self.feedback_cancel_button.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.feedback_lock_button = ttk.Button(action_frame, text="Fijar reglas actuales", command=self._lock_feedback_scope)
        self.feedback_lock_button.grid(row=0, column=2, sticky="w", padx=(8, 0))
        self.feedback_unlock_button = ttk.Button(action_frame, text="Liberar fijacion", command=self._unlock_feedback_scope)
        self.feedback_unlock_button.grid(row=0, column=3, sticky="w", padx=(8, 0))
        self.feedback_refresh_button = ttk.Button(action_frame, text="Refrescar vista", command=self._refresh_feedback)
        self.feedback_refresh_button.grid(row=0, column=4, sticky="w", padx=(8, 0))
        self.feedback_help_button = ttk.Button(action_frame, text="Ayuda", command=self._show_feedback_help)
        self.feedback_help_button.grid(row=0, column=5, sticky="w", padx=(8, 0))
        ttk.Progressbar(action_frame, variable=self.feedback_progress, maximum=100).grid(row=0, column=6, sticky="ew", padx=(12, 0))
        ttk.Label(action_frame, textvariable=self.feedback_progress_status).grid(row=1, column=0, columnspan=7, sticky="w", pady=(8, 0))

        plan_frame = ttk.LabelFrame(self.feedback_tab, text="Plan de propagacion", padding=10)
        plan_frame.grid(row=3, column=0, sticky="nsew", pady=(10, 0))
        plan_frame.columnconfigure(0, weight=1)
        plan_frame.rowconfigure(0, weight=1)
        self.feedback_plan_text = tk.Text(plan_frame, height=8, wrap="word")
        self.feedback_plan_text.grid(row=0, column=0, sticky="nsew")

        metrics_frame = ttk.LabelFrame(self.feedback_tab, text="Metricas por motor y ciclo", padding=10)
        metrics_frame.grid(row=4, column=0, sticky="nsew", pady=(10, 0))
        metrics_frame.columnconfigure(0, weight=1)
        metrics_frame.rowconfigure(0, weight=1)
        self.feedback_metrics_text = tk.Text(metrics_frame, height=7, wrap="word")
        self.feedback_metrics_text.grid(row=0, column=0, sticky="nsew")

        memory_frame = ttk.LabelFrame(self.feedback_tab, text="Memoria editorial actual", padding=10)
        memory_frame.grid(row=5, column=0, sticky="nsew", pady=(10, 0))
        memory_frame.columnconfigure(0, weight=1)
        memory_frame.rowconfigure(0, weight=1)
        self.feedback_memory_text = tk.Text(memory_frame, height=14, wrap="word")
        self.feedback_memory_text.grid(row=0, column=0, sticky="nsew")

        output_frame = ttk.LabelFrame(self.feedback_tab, text="Salida del orquestador", padding=10)
        output_frame.grid(row=6, column=0, sticky="nsew", pady=(10, 0))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        self.feedback_output = tk.Text(output_frame, height=12, wrap="word")
        self.feedback_output.grid(row=0, column=0, sticky="nsew")

        self._attach_tooltip(self.feedback_institution_combo, "Selecciona la institución base. Al cambiarla se filtran carreras, materias y actividades disponibles para construir memoria editorial.")
        self._attach_tooltip(self.feedback_career_combo, "Selecciona el programa educativo. Si dejas materia vacía, la propagación lateral puede abarcar otros programas de la institución.")
        self._attach_tooltip(self.feedback_subject_combo, "Selecciona la materia si quieres precisión local; desde aquí también se habilita la selección de actividades detectadas.")
        self._attach_tooltip(self.feedback_activity_combo, "La actividad afina el punto de arranque. La memoria puede propagarse desde ella hacia materia, carrera, institución e interinstitucional.")
        self._attach_tooltip(self.feedback_build_combo, "Define hasta qué nivel debe llegar la construcción en esta corrida: desde el origen actual hacia materia, carrera, institución o interinstitucional.")
        self._attach_tooltip(self.feedback_propagation_combo, "Ascendente: sube hasta el nivel destino. Ascendente exhaustivo: antes de consolidar cada nivel incorpora todos los elementos del nivel inferior.")
        self._attach_tooltip(self.feedback_iterations_spin, "Número de pasadas completas del orquestador. Cada ciclo vuelve a consultar los motores en el orden configurado.")
        self._attach_tooltip(self.feedback_engines_entry, "Lista separada por comas. Se ejecutan del más rápido al más profundo; el orden por defecto ya sigue esa estrategia.")
        self._attach_tooltip(self.feedback_tokens_spin, "Límite de salida por llamada LLM. Útil para controlar profundidad y costo por ciclo.")
        self._attach_tooltip(self.feedback_run_button, "Inicia la construcción de memoria editorial del scope seleccionado siguiendo el plan visible arriba.")
        self._attach_tooltip(self.feedback_cancel_button, "Solicita cancelación cooperativa. La corrida termina al cerrar la llamada LLM en curso y conserva lo ya consolidado.")
        self._attach_tooltip(self.feedback_lock_button, "Fija las secciones actuales del scope para que siguientes corridas no las modifiquen. Se mantiene el principio de no regresión.")
        self._attach_tooltip(self.feedback_unlock_button, "Libera las fijaciones manuales del scope actual para permitir nuevas fusiones en próximas corridas.")
        self._attach_tooltip(self.feedback_refresh_button, "Relee catálogo, plan, métricas y memoria persistida desde la base SQLite y los snapshots del scope actual.")
        self._attach_tooltip(self.feedback_help_button, "Abre una guía corta para operar la construcción de memoria editorial y entender las opciones de propagación.")
        self._attach_tooltip(self.feedback_plan_text, "Vista previa del recorrido ascendente que seguirá el orquestador hasta el nivel destino seleccionado.")
        self._attach_tooltip(self.feedback_metrics_text, "Resumen histórico por motor y por ciclo para los scopes actualmente incluidos en el plan visible.")
        self._attach_tooltip(self.feedback_memory_text, "Memoria editorial persistida del scope actual, incluyendo herencia útil y secciones fijadas manualmente.")
        self._attach_tooltip(self.feedback_output, "Bitácora en vivo del orquestador: inicio, progreso por motor, resultados, cancelación o cierre de corrida.")
        self._register_busy_widgets(
            "feedback",
            self.feedback_run_button,
            self.feedback_lock_button,
            self.feedback_unlock_button,
            self.feedback_refresh_button,
            self.feedback_institution_combo,
            self.feedback_career_combo,
            self.feedback_subject_combo,
            self.feedback_activity_combo,
            self.feedback_build_combo,
            self.feedback_propagation_combo,
            self.feedback_iterations_spin,
            self.feedback_engines_entry,
            self.feedback_tokens_spin,
        )

        self._refresh_feedback_catalog()
        self._refresh_feedback()

    def _thread(self, fn) -> None:
        threading.Thread(target=fn, daemon=True).start()

    def _log(self, widget: tk.Text, text: str) -> None:
        previous_state = str(widget.cget("state"))
        widget.configure(state="normal")
        widget.insert("end", text + "\n")
        widget.see("end")
        if previous_state == "disabled":
            widget.configure(state="disabled")

    def _set_text(self, widget: tk.Text, text: str, *, readonly: bool = False) -> None:
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("end", text)
        widget.see("end")
        if readonly:
            widget.configure(state="disabled")

    def _attach_tooltip(self, widget, text: str) -> None:
        self._tooltips.append(ToolTip(widget, text))

    def _register_busy_widgets(self, group: str, *widgets) -> None:
        self._busy_groups[group] = [(widget, str(widget.cget("state"))) for widget in widgets]

    def _set_busy(self, group: str, busy: bool) -> None:
        for widget, initial_state in self._busy_groups.get(group, []):
            widget.configure(state="disabled" if busy else initial_state)
        if group == "feedback":
            self.feedback_cancel_button.configure(state="normal" if busy else "disabled")

    def _show_llm_help(self) -> None:
        messagebox.showinfo(
            "AulaTeX - Chat LLM",
            "1. Elige una sesion fija segun el tipo de trabajo.\n"
            "2. Escribe el mensaje en 'Nuevo mensaje'.\n"
            "3. AulaTeX guarda el historial automaticamente.\n"
            "4. Cuando el contexto crece, se compacta a una memoria breve reutilizable.\n"
            "5. Usa MultiMotor para consultas importantes: lanza todos los motores en paralelo y devuelve consenso.\n"
            "6. Ajusta la severidad de MultiMotor: rapido / normal / profundo.\n\n"
            "Sesiones sugeridas:\n"
            "- Editorial: tono, estilo y lineamientos.\n"
            "- Proyecto: estructura, alcance y entregables.\n"
            "- Investigacion: conceptos, autores y sintesis.\n"
            "- Operativo: LaTeX, scripts y compilacion.\n"
            "- MultiMotor: contraste entre todos los motores.",
        )

    def _show_feedback_help(self) -> None:
        messagebox.showinfo(
            "AulaTeX - Memoria editorial",
            "1. Selecciona institución, carrera, materia y, si aplica, actividad.\n"
            "2. Elige el nivel destino y el modo de propagación.\n"
            "3. Ajusta iteraciones, motores y max tokens.\n"
            "4. Revisa el plan de propagación antes de ejecutar.\n"
            "5. Construye la memoria: el progreso avanza por scope, ciclo y motor.\n"
            "6. Usa 'Fijar reglas actuales' para congelar secciones validadas y evitar que futuras corridas las alteren.\n"
            "7. Consulta métricas por motor y ciclo para comparar profundidad, estabilidad y volumen de salida.\n"
            "8. Si cancelas, se conserva lo ya consolidado y el manifiesto queda marcado como cancelado.",
        )

    def _selected_llm_session(self) -> str:
        selected = self.llm_session_tree.selection() if hasattr(self, "llm_session_tree") else ()
        if selected:
            return self.llm_session_nodes.get(selected[0], "editorial")
        states = self.chat_store.list_sessions()
        return states[0].definition.key if states else "editorial"

    def _refresh_llm_sessions(self) -> None:
        if not hasattr(self, "llm_session_tree"):
            return
        selected_key = self._selected_llm_session()
        for item in self.llm_session_tree.get_children():
            self.llm_session_tree.delete(item)
        self.llm_session_nodes = {}
        for state in self.chat_store.list_sessions():
            mode_label = "Todos" if state.definition.mode == "multi" else state.definition.assigned_engine
            node = self.llm_session_tree.insert(
                "",
                "end",
                text=state.definition.label,
                values=(mode_label, state.context_label, f"{state.active_messages}/{state.message_count}"),
                open=True,
            )
            self.llm_session_nodes[node] = state.definition.key
            if state.definition.key == selected_key:
                self.llm_session_tree.selection_set(node)
                self.llm_session_tree.focus(node)
        if not self.llm_session_tree.selection() and self.llm_session_tree.get_children():
            first = self.llm_session_tree.get_children()[0]
            self.llm_session_tree.selection_set(first)
            self.llm_session_tree.focus(first)

    def _on_llm_session_selected(self, _event=None) -> None:
        self._refresh_llm_view(self._selected_llm_session())

    def _refresh_llm_view(self, session_key: str | None = None, *, status: str | None = None) -> None:
        key = session_key or self._selected_llm_session()
        state = self.chat_store.get_session_state(key)
        messages = self.chat_store.get_messages(key, include_compacted=False, limit=80)
        timeline = self.chat_store.get_visible_history(key, message_limit=80, compaction_limit=20)
        if state.definition.mode == "multi":
            self.llm_multi_severity_combo.configure(state="readonly")
        else:
            self.llm_multi_severity_combo.configure(state="disabled")
        self.llm_session_title.set(state.definition.label)
        self.llm_session_meta.set(
            f"{state.definition.description} | Modo: {'multimotor' if state.definition.mode == 'multi' else 'especializado'} | "
            f"Motores: {', '.join(state.definition.engine_list)} | Contexto estimado: ~{state.context_label} | "
            f"Compactaciones: {state.compaction_count}"
        )
        transcript = self._format_llm_transcript(timeline)
        diagnostics = self._format_llm_diagnostics(state, messages)
        self._set_text(self.llm_output, transcript, readonly=True)
        self._set_text(self.llm_system, diagnostics, readonly=True)
        self.llm_status.set(status or f"Sesion activa: {state.definition.label}")

    def _format_llm_transcript(self, timeline) -> str:
        if not timeline:
            return (
                "Sin mensajes aun.\n\n"
                "Sugerencia: usa una sesion tematica distinta para cada tipo de trabajo y deja que AulaTeX compacte el contexto automaticamente."
            )
        chunks: list[str] = []
        for item in timeline:
            if item.kind == "compaction" and item.compaction is not None:
                summary = item.compaction
                chunks.extend(
                    [
                        f"Resumen compactado #{summary.id}",
                        f"Mensajes resumidos: {summary.compacted_messages} | Caracteres: {summary.compacted_chars}",
                        summary.summary_text,
                        "",
                        "═" * 72,
                        "",
                    ]
                )
                continue
            if item.message is None:
                continue
            role = "Usuario" if item.message.role == "user" else "Asistente"
            engine = f" [{item.message.engine}]" if item.message.engine else ""
            chunks.extend([f"{role}{engine}", item.message.content, "", "─" * 72, ""])
        return "\n".join(chunks).strip()

    def _format_llm_diagnostics(self, state, messages) -> str:
        lines = [
            self.chat_store.session_help(state.definition.key),
            "",
            f"Contexto estimado actual: ~{state.context_label}",
            f"Mensajes activos: {state.active_messages} de {state.message_count}",
            f"Compactaciones registradas: {state.compaction_count}",
            "",
            "Memoria compactada vigente:",
            state.summary_text or "Sin memoria compactada aun.",
        ]
        if state.definition.mode == "multi":
            lines.extend(["", f"Severidad MultiMotor seleccionada: {multimotor_severity_label(self.llm_multi_severity.get())}"])
        last_multi = None
        for message in reversed(messages):
            if isinstance(message.metadata, dict) and message.metadata.get("engine_results"):
                last_multi = message.metadata["engine_results"]
                break
        if last_multi:
            lines.extend(["", "Ultimo consenso multimotor:"])
            for item in last_multi:
                engine = item.get("engine", "Motor")
                ok = "OK" if item.get("ok") else "ERROR"
                body = item.get("text") or item.get("error") or "Sin contenido."
                lines.append(f"- {engine}: {ok} | {body[:220].replace(chr(10), ' ')}")
        return "\n".join(lines).strip()

    def _compact_selected_llm_session(self) -> None:
        session_key = self._selected_llm_session()

        def work() -> None:
            compacted = self.chat_store.compact_session(session_key, force=True)
            status = "Sesion compactada." if compacted else "No habia suficiente historial para compactar."
            self.events.put(("llm-refresh", {"session_key": session_key, "status": status}))

        self._thread(work)

    def _export_selected_llm_session(self) -> None:
        session_key = self._selected_llm_session()

        def work() -> None:
            path = self.chat_store.export_session_markdown(session_key)
            self.events.put(("llm-refresh", {"session_key": session_key, "status": f"Sesion exportada en {path}"}))

        self._thread(work)

    def _clear_selected_llm_session(self) -> None:
        session_key = self._selected_llm_session()
        state = self.chat_store.get_session_state(session_key)
        confirmed = messagebox.askyesno(
            "AulaTeX",
            f"¿Reiniciar la sesion '{state.definition.label}'? Se borrara historial y memoria compactada de ese tema.",
        )
        if not confirmed:
            return
        self.chat_store.clear_session(session_key)
        self._refresh_llm_sessions()
        self._refresh_llm_view(session_key, status=f"Sesion {state.definition.label} reiniciada.")

    def _check_llms(self) -> None:
        def work() -> None:
            for engine in self.llm.engines():
                result = self.llm.check(engine)
                self.events.put(("llm", f"[LLM] {engine}: {'OK' if result.ok else 'ERROR'} {result.text or result.error}"))

        self._thread(work)

    def _refresh_tree(self) -> None:
        for item in self.template_tree.get_children():
            self.template_tree.delete(item)

        self.template_details.delete("1.0", "end")
        self.template_details.insert("end", "Seleccione un nodo para ver detalles.\n")

        self.template_nodes = {}
        for node in self.workspace.scan_template_inventory():
            self._insert_template_node("", node)

    def _insert_template_node(self, parent: str, node) -> None:
        values = (
            "[x]" if node.has_bibliography else "[ ]",
            "[x]" if node.has_presentation else "[ ]",
            "[x]" if node.has_report else "[ ]",
        )
        item = self.template_tree.insert(parent, "end", text=f"{node.level}: {node.name}", values=values, open=node.level != "materia")
        self.template_nodes[item] = node
        for child in node.children:
            self._insert_template_node(item, child)

    def _on_template_selected(self, _event=None) -> None:
        selected = self.template_tree.selection()
        if not selected:
            return
        node = self.template_nodes.get(selected[0])
        if node is None:
            return
        self.template_details.delete("1.0", "end")
        self.template_details.insert(
            "end",
            f"Nivel: {node.level}\nRuta: {node.relative_path}\nBibliografia: {', '.join(node.bibliography_files) or 'FALTA'}\nPresentacion: {', '.join(node.presentation_files) or 'FALTA'}\nReporte: {', '.join(node.report_files) or 'FALTA'}\nEstado: {'COMPLETO' if node.is_complete else 'INCOMPLETO'}",
        )

    def _run_llm_prompt(self) -> None:
        session_key = self._selected_llm_session()
        prompt = self.prompt_text.get("1.0", "end").strip()
        if not prompt:
            messagebox.showwarning("AulaTeX", "Escribe un prompt.")
            return
        self.prompt_text.delete("1.0", "end")
        severity = self.llm_multi_severity.get()
        self._set_busy("llm-chat", True)

        def work() -> None:
            try:
                self.events.put(("llm-system", f"Procesando en {self.chat_store.get_definition(session_key).label}..."))
                tool_result = self._handle_local_tool_prompt(prompt)
                if tool_result is not None:
                    result = self.chat_store.record_local_exchange(session_key, prompt, tool_result)
                else:
                    result = self.chat_store.send_prompt(session_key, prompt, severity=severity)
                self.events.put(("llm-refresh", {"session_key": session_key, "status": result.status_message}))
            except Exception as exc:
                self.events.put(("llm-error", f"{type(exc).__name__}: {exc}"))

        self._thread(work)

    def _handle_local_tool_prompt(self, prompt: str) -> str | None:
        text = prompt.lower()

        if "lista" in text and ".tex" in text:
            files = self.workspace.find_tex_files(limit=200)
            return "[HERRAMIENTA] Archivos TEX encontrados\n\n" + "\n".join(self.workspace.relative(f) for f in files[:200])

        if "compila" in text or "compilar" in text:
            match = re.search(r"(?:en|dentro de)\s+([\w\-/]+)", text)
            target = match.group(1) if match else "."
            tex_files = self.workspace.find_tex_files(target, limit=20)
            if not tex_files:
                return f"[HERRAMIENTA] No se encontraron TEX en {target}"

            outputs = []
            for tex in tex_files[:5]:
                result = self.workspace.compile_tex(tex)
                outputs.append(f"{'OK' if result.ok else 'ERROR'} {self.workspace.relative(tex)}")
            return "[HERRAMIENTA] Compilacion ejecutada\n\n" + "\n".join(outputs)

        if "explora" in text or "analiza carpeta" in text:
            return self.workspace.context_summary(".", max_chars=4000)

        return None

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
        self._set_busy("agent", True)

        def work() -> None:
            try:
                result = self.agent.run(request)
                self.events.put(("agent", f"[AGENTE] {'OK' if result.ok else 'CON OBSERVACIONES'}\nReporte: {result.report_path}"))
            except Exception as exc:
                self.events.put(("agent-error", f"[AGENTE] ERROR {type(exc).__name__}: {exc}"))

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
        self._set_busy("compile", True)

        def work() -> None:
            try:
                result = self.workspace.compile_tex(target)
                self.events.put(("compile", f"[COMPILAR] {'OK' if result.ok else 'ERROR'} {target}\n{result.stdout[-4000:]}\n{result.stderr[-2000:]}"))
            except Exception as exc:
                self.events.put(("compile-error", f"[COMPILAR] ERROR {type(exc).__name__}: {exc}"))

        self._thread(work)

    def _open_extractor_gui(self) -> None:
        script = self.workspace.scripts_dir / "extractor.ps1"
        subprocess.Popen(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)], cwd=str(self.workspace.repo_root))

    def _probe_extractor(self) -> None:
        script = self.workspace.scripts_dir / "extractor-conceptos-ideas" / "runners" / "probar_configuracion.ps1"
        self._set_busy("extractor", True)

        def work() -> None:
            try:
                proc = subprocess.run(
                    ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)],
                    cwd=str(script.parent),
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                )
                self.events.put(("extractor", f"[EXTRACTOR] {proc.returncode}\n{proc.stdout}\n{proc.stderr}"))
            except Exception as exc:
                self.events.put(("extractor-error", f"[EXTRACTOR] ERROR {type(exc).__name__}: {exc}"))

        self._thread(work)

    def _refresh_feedback(self) -> None:
        self._refresh_feedback_catalog()
        self._refresh_feedback_plan_and_memory()

    def _refresh_feedback_catalog(self) -> None:
        self.editorial_scopes, self.editorial_children = self.workspace.editorial_scope_index()
        institutions = sorted(scope.label for scope in self.editorial_scopes.values() if scope.level == "institucion")
        self.feedback_institution_combo.configure(values=self._with_unselected(institutions))
        if self.feedback_institution.get() not in self.feedback_institution_combo.cget("values"):
            self.feedback_institution.set(UNSELECTED_OPTION)
        self._sync_feedback_source_filters()

    def _sync_feedback_source_filters(self) -> None:
        institution = self._selected_feedback_value(self.feedback_institution)
        selected_career = self._selected_feedback_value(self.feedback_career)
        selected_subject = self._selected_feedback_value(self.feedback_subject)
        selected_activity = self._selected_feedback_value(self.feedback_activity)

        careers = sorted(
            scope.label
            for scope in self.editorial_scopes.values()
            if scope.level == "carrera" and scope.institution == institution
        )
        career_values = self._with_unselected(careers)
        self.feedback_career_combo.configure(values=career_values)
        if selected_career not in careers:
            self.feedback_career.set(UNSELECTED_OPTION)
            selected_career = ""

        subjects = sorted(
            scope.label
            for scope in self.editorial_scopes.values()
            if scope.level == "materia"
            and scope.institution == institution
            and scope.career == selected_career
        )
        subject_values = self._with_unselected(subjects)
        self.feedback_subject_combo.configure(values=subject_values)
        if selected_subject not in subjects:
            self.feedback_subject.set(UNSELECTED_OPTION)
            selected_subject = ""

        activities = sorted(
            scope.label
            for scope in self.editorial_scopes.values()
            if scope.level == "actividad"
            and scope.institution == institution
            and scope.career == selected_career
            and scope.subject == selected_subject
        )
        activity_values = self._with_unselected(activities)
        self.feedback_activity_combo.configure(values=activity_values)
        if selected_activity not in activities:
            self.feedback_activity.set(UNSELECTED_OPTION)

    def _on_feedback_source_changed(self, _event=None) -> None:
        self._sync_feedback_source_filters()
        self._refresh_feedback_plan_and_memory()

    def _on_feedback_plan_changed(self, _event=None) -> None:
        self._refresh_feedback_plan_and_memory()

    def _resolve_feedback_scope(self) -> EditorialScope | None:
        institution = self._selected_feedback_value(self.feedback_institution)
        career = self._selected_feedback_value(self.feedback_career)
        subject = self._selected_feedback_value(self.feedback_subject)
        activity = self._selected_feedback_value(self.feedback_activity)

        if activity and subject:
            key = self.workspace._scope_key("actividad", institution=institution, career=career, subject=subject, activity=activity)
        elif subject:
            key = self.workspace._scope_key("materia", institution=institution, career=career, subject=subject)
        elif career:
            key = self.workspace._scope_key("carrera", institution=institution, career=career)
        elif institution:
            key = self.workspace._scope_key("institucion", institution=institution)
        else:
            key = "interinstitucional"
        return self.editorial_scopes.get(key)

    def _refresh_feedback_plan_and_memory(self) -> None:
        scope = self._resolve_feedback_scope()
        self._refresh_feedback_build_levels(scope)

        self.feedback_plan_text.delete("1.0", "end")
        self.feedback_metrics_text.delete("1.0", "end")
        self.feedback_memory_text.delete("1.0", "end")

        if scope is None:
            self.feedback_scope_status.set("Origen resuelto: no encontrado")
            self.feedback_plan_text.insert("end", "Selecciona una institucion, carrera, materia o actividad valida.\n")
            self.feedback_metrics_text.insert("end", "# Metricas\n\n- Sin plan activo.\n")
            self.feedback_memory_text.insert("end", self._feedback_schema_preview())
            return

        self.feedback_scope_status.set(
            f"Origen resuelto: {scope.level} | {scope.key} | ruta {scope.relative_path or '.'}"
        )
        build_level = self.feedback_build_level.get() or scope.level
        try:
            plan = self.editorial_builder.plan_scopes(scope.key, build_level, self.feedback_propagation.get())
        except ValueError as exc:
            plan = []
            self.feedback_plan_text.insert("end", f"Plan invalido: {exc}\n")

        self.feedback_plan_text.insert("end", f"Propagacion: {PROPAGATION_LABELS.get(self.feedback_propagation.get(), self.feedback_propagation.get())}\n")
        self.feedback_plan_text.insert("end", f"Nivel destino: {build_level}\n\n")
        if plan:
            for index, item in enumerate(plan, start=1):
                self.feedback_plan_text.insert("end", f"{index}. {item.level} | {item.label} | {item.key}\n")
        else:
            self.feedback_plan_text.insert("end", "No hay scopes programados para esta combinacion.\n")
        self.feedback_metrics_text.insert("end", self.editorial_store.render_metrics_markdown([item.key for item in plan] or [scope.key]))

        memory = self.editorial_store.get_memory(scope.key)
        if any(memory.get(section) for section in MEMORY_SECTIONS):
            self.feedback_memory_text.insert("end", self.editorial_store.render_memory_markdown(scope, memory))
            inherited = self.editorial_store.summarize_for_scope(scope.key, include_ancestors=True, max_chars=7000)
            if inherited.strip():
                self.feedback_memory_text.insert("end", "\n\n## Herencia util\n\n")
                self.feedback_memory_text.insert("end", inherited)
        else:
            self.feedback_memory_text.insert("end", self._feedback_schema_preview(scope))

    def _refresh_feedback_build_levels(self, scope: EditorialScope | None) -> None:
        if scope is None:
            options = ["interinstitucional"]
            default_level = "interinstitucional"
        else:
            start_index = EDITORIAL_LEVELS.index(scope.level)
            options = list(EDITORIAL_LEVELS[start_index:])
            default_level = "materia" if scope.level == "actividad" else scope.level
            if default_level not in options:
                default_level = options[0]
        self.feedback_build_combo.configure(values=options)
        if self.feedback_build_level.get() not in options:
            self.feedback_build_level.set(default_level)

    def _feedback_schema_preview(self, scope: EditorialScope | None = None) -> str:
        lines = ["# Estructura de memoria editorial", ""]
        if scope is not None:
            lines.extend(
                [
                    f"- Alcance actual: {scope.level}",
                    f"- Scope: {scope.key}",
                    "",
                ]
            )
        lines.append("## Secciones persistentes")
        lines.append("")
        for section in MEMORY_SECTIONS:
            lines.append(f"- {section}: lista de reglas o hallazgos compactados sin perdida")
        lines.extend(
            [
                "",
                "## Principios",
                "",
                "- No regresion: solo union y deduplicacion, nunca borrado destructivo.",
                "- Propagacion: del origen hacia niveles superiores mediante consolidacion editorial.",
                "- Reutilizacion: el Agente consume esta memoria para plantillas y actividades aguas abajo.",
            ]
        )
        return "\n".join(lines)

    def _ordered_feedback_engines(self) -> list[str]:
        return sorted(self.llm.engines(), key=lambda engine: (ENGINE_PRIORITY.get(engine, 999), engine))

    def _parse_feedback_engines(self) -> list[str]:
        selected = [item.strip() for item in self.feedback_engines.get().split(",") if item.strip()]
        valid = [engine for engine in selected if engine in self.llm.engines()]
        return valid or self._ordered_feedback_engines()

    def _selected_feedback_value(self, variable: tk.StringVar) -> str:
        value = variable.get().strip()
        if not value or value == UNSELECTED_OPTION:
            return ""
        return value

    def _with_unselected(self, values: list[str]) -> tuple[str, ...]:
        return tuple([UNSELECTED_OPTION, *values])

    def _run_feedback_memory(self) -> None:
        scope = self._resolve_feedback_scope()
        if scope is None:
            messagebox.showwarning("AulaTeX", "Selecciona un scope editorial valido.")
            return

        engines = self._parse_feedback_engines()
        request = EditorialMemoryRequest(
            source_scope_key=scope.key,
            build_level=self.feedback_build_level.get(),
            propagation_mode=self.feedback_propagation.get(),
            iterations=max(1, int(self.feedback_iterations.get())),
            engines=engines,
            max_tokens=max(128, int(self.feedback_max_tokens.get())),
        )

        self.feedback_cancel_event = threading.Event()
        self.feedback_progress.set(0.0)
        self.feedback_progress_status.set("Construyendo memoria editorial...")
        self._log(self.feedback_output, f"[MEMORIA] Inicio en {scope.key} con motores: {', '.join(engines)}")
        self._set_busy("feedback", True)

        def on_progress(event: EditorialMemoryEvent) -> None:
            self.events.put(("feedback-progress", event))

        def work() -> None:
            try:
                result = self.editorial_builder.build(request, progress=on_progress, cancel_event=self.feedback_cancel_event)
                self.events.put(("feedback-result", result))
            except Exception as exc:
                self.events.put(("feedback-error", f"[MEMORIA] ERROR {type(exc).__name__}: {exc}"))

        self._thread(work)

    def _cancel_feedback_memory(self) -> None:
        if self.feedback_cancel_button.cget("state") == "disabled":
            return
        self.feedback_cancel_event.set()
        self.feedback_progress_status.set("Cancelación solicitada. Se cerrará al terminar la llamada en curso.")
        self._log(self.feedback_output, "[MEMORIA] Cancelación solicitada por el usuario.")

    def _lock_feedback_scope(self) -> None:
        scope = self._resolve_feedback_scope()
        if scope is None:
            messagebox.showwarning("AulaTeX", "Selecciona un scope editorial antes de fijar reglas.")
            return
        payload = self.editorial_store.lock_scope_sections(scope.key)
        locked = payload.get("locked_sections", [])
        self._log(self.feedback_output, f"[MEMORIA] Scope fijado: {scope.key} | secciones={', '.join(locked) or 'ninguna'}")
        self._refresh_feedback_plan_and_memory()

    def _unlock_feedback_scope(self) -> None:
        scope = self._resolve_feedback_scope()
        if scope is None:
            messagebox.showwarning("AulaTeX", "Selecciona un scope editorial antes de liberar fijación.")
            return
        self.editorial_store.unlock_scope_sections(scope.key)
        self._log(self.feedback_output, f"[MEMORIA] Fijación liberada para {scope.key}")
        self._refresh_feedback_plan_and_memory()

    def _drain_events(self) -> None:
        while True:
            try:
                category, event = self.events.get_nowait()
            except queue.Empty:
                break
            if category == "agent":
                self._set_busy("agent", False)
                self._log(self.agent_output, event)
            elif category == "agent-error":
                self._set_busy("agent", False)
                self._log(self.agent_output, str(event))
            elif category == "llm":
                self._log(self.llm_output, event)
            elif category == "llm-system":
                self.llm_status.set(event)
            elif category == "llm-refresh":
                self._set_busy("llm-chat", False)
                payload = event if isinstance(event, dict) else {}
                self._refresh_llm_sessions()
                self._refresh_llm_view(payload.get("session_key"), status=payload.get("status"))
            elif category == "llm-error":
                self._set_busy("llm-chat", False)
                self.llm_status.set("Error en el chat LLM")
                self._refresh_llm_sessions()
                self._refresh_llm_view(self._selected_llm_session(), status=str(event))
            elif category == "compile":
                self._set_busy("compile", False)
                self._log(self.compile_output, event)
            elif category == "compile-error":
                self._set_busy("compile", False)
                self._log(self.compile_output, str(event))
            elif category == "extractor":
                self._set_busy("extractor", False)
                self._log(self.extractor_output, event)
            elif category == "extractor-error":
                self._set_busy("extractor", False)
                self._log(self.extractor_output, str(event))
            elif category == "feedback-progress":
                self._handle_feedback_progress(event)
            elif category == "feedback-result":
                self._set_busy("feedback", False)
                self.feedback_progress.set(100.0)
                if event.cancelled:
                    self.feedback_progress_status.set("Memoria editorial cancelada.")
                    self._log(self.feedback_output, f"[MEMORIA] CANCELADA\nManifest: {event.manifest_path}")
                else:
                    self.feedback_progress_status.set(f"Memoria editorial cerrada: {'OK' if event.ok else 'CON OBSERVACIONES'}")
                    self._log(self.feedback_output, f"[MEMORIA] {'OK' if event.ok else 'CON OBSERVACIONES'}\nManifest: {event.manifest_path}")
                self._refresh_feedback()
            elif category == "feedback-error":
                self._set_busy("feedback", False)
                self.feedback_progress_status.set("Fallo en la construccion de memoria editorial.")
                self._log(self.feedback_output, str(event))
        self.after(250, self._drain_events)

    def _handle_feedback_progress(self, event: EditorialMemoryEvent) -> None:
        percent = 0.0
        if event.total > 0:
            percent = (float(event.current) / float(event.total)) * 100.0
        self.feedback_progress.set(percent)
        self.feedback_progress_status.set(event.message)
        prefix = f"[{event.kind.upper()}]"
        if event.engine:
            prefix += f" {event.engine}"
        if event.cycle:
            prefix += f" ciclo={event.cycle}"
        if event.scope_key:
            prefix += f" scope={event.scope_key}"
        self._log(self.feedback_output, f"{prefix} {event.message}")
        if event.kind in {"result", "done"}:
            self._refresh_feedback_plan_and_memory()


def main() -> None:
    app = AulaTeXApp()
    app.mainloop()
