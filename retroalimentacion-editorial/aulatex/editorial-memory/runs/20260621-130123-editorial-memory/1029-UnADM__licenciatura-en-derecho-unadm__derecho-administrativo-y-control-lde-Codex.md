{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas validas previas del destino sin regresion y con deduplicacion lossless.",
    "Se refuerzan ejes editoriales estables: problema, conceptos y fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene prioridad institucional de normalizacion estructurada y JSON parseable antes de propagar.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho por no equivalencia de nodo."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Mantener ubicacion curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en planeacion semanal.",
    "Explicitar tipo de producto antes de desarrollar: reporte, presentacion o visual.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, .tex y .bib.",
    "Corregir placeholders y tokens sin expandir en README y programa analitico. [supuesto]"
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular el tema con control administrativo y practica profesional.",
    "No asumir fuentes de semanas posteriores sin confirmacion local.",
    "Separar reglas editoriales generales de contenido sustantivo heredado de otras materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que reglas heredadas no contradigan el programa analitico local.",
    "Validar que README y programa analitico no conserven rutas corruptas o placeholders."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en español y letterpaper segun base local.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Asegurar coherencia entre documenttitle, documentsubtitle y actividad real.",
    "Reemplazar Actividad X por numero y nombre reales.",
    "Completar figura docente antes de entrega.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo espurios en README antes de referenciar en LaTeX. [supuesto]"
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener entradas base institucionales mientras no exista instruccion local en contrario."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No propagar redaccion literal ni doctrina especifica de Filosofia del Derecho.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresion.",
    "Preservar alertas institucionales historicas sobre salidas no estructuradas.",
    "Si hay conflicto entre regla heredada y contexto local, priorizar programa analitico local y marcar conflicto."
  ],
  "open_questions": [
    "Confirmar convencion final para carpeta de referencias en README (aparece nombre espurio). [supuesto]",
    "Confirmar correccion definitiva de tokens PowerShell sin expandir en README y programa. [supuesto]",
    "Confirmar nombre oficial de figura docente en plantilla.",
    "Confirmar formato institucional de citacion exigido por la materia.",
    "Confirmar si año de consulta 2026 del sitio UnADM debe actualizarse por ciclo."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion.",
        "No invencion de fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Coursecode local: LDE-S6B1."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo verificables.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Trazabilidad editorial entre consigna, desarrollo y evidencia."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para practica juridica.",
      "Asegurar consistencia institucional entre contenido, forma y fuentes."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones estables y reutilizables.",
      "Cierre practico obligatorio.",
      "Supuestos etiquetados de forma visible.",
      "Compatibilidad tecnica entre README, LaTeX y BibTeX."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Delimitar conceptos y marco normativo.",
      "Sustentar con evidencia verificable.",
      "Desarrollar analisis propio.",
      "Cerrar con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Control administrativo",
        "Normalizacion estructurada"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor de fuentes."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se construye sobre una delimitacion clara del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion practica requiere sustento juridico verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura valida evita perdida de contexto y errores de propagacion."
        },
        {
          "source": "Control administrativo",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La materia orienta el cierre hacia aplicacion profesional en administracion y control."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local de Derecho administrativo y control.",
        "Archivo derecho-administrativo-y-control.bib.",
        "Regla institucional heredada: no propagar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se transfieren solo abstracciones estables desde nodo no equivalente.",
      "Ciclo 16: se conserva regla critica de bloqueo por JSON no parseable.",
      "Ciclo 16: se refuerza patron argumentativo comun sin mover doctrina especifica de Filosofia del Derecho.",
      "Ciclo 16: se mantienen vacios locales abiertos con marca [supuesto] para verificacion posterior."
    ]
  }
}