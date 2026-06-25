{
  "summary": [
    "Se sincroniza memoria transversal hacia Derecho administrativo y control sin regresion.",
    "Se preservan reglas institucionales validas y se deduplican en modo lossless.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene prioridad de normalizacion estructurada antes de propagar.",
    "Se crea consolidacion minima verificable para destino con contexto local parcial."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Alinear ubicacion curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Declarar fuente provisional cuando aplique: Codex o GPT-Pro."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Incluir evidencia y fuentes en la seccion de desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el producto al tipo solicitado por planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Corregir placeholders y tokens sin expandir en README y programa."
  ],
  "activity_rules": [
    "Explicitar tipo de producto antes de desarrollar: reporte, presentacion o visual.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar traslape de contenido doctrinal de otras materias sin validacion local.",
    "Vincular el analisis con control administrativo y aplicacion profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que reglas heredadas no contradigan el programa analitico local.",
    "Detener propagacion si existen campos criticos vacios."
  ],
  "latex_rules": [
    "Mantener espanol y codificacion correcta en .tex y .bib.",
    "Mantener formato letterpaper segun plantilla local.",
    "Completar metadatos institucionales y academicos antes de compilar.",
    "Sustituir 'Actividad X' por numero y nombre real.",
    "Sustituir 'Nombre por definir' de figura docente antes de entregar.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas o nombres con caracteres espurios antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) por slug literal en archivos de control. [supuesto]"
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias.",
    "Usar solo obras consultables o provistas en consigna.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad entre afirmacion, cita y entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir a nodos laterales solo abstracciones editoriales estables.",
    "No propagar redaccion literal ni contenido doctrinal no verificado.",
    "Aplicar estrategia union-dedupe lossless en cada ciclo.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Si hay fuente provisional, exigir normalizacion manual antes de fusion final."
  ],
  "open_questions": [
    "Confirmar formato de citacion obligatorio de la carrera. [supuesto]",
    "Confirmar nombre oficial de figura docente en plantilla.",
    "Confirmar si el ano de consulta 2026 del sitio UnADM se mantiene.",
    "Confirmar convencion final para carpeta de referencias local.",
    "Confirmar si todos los tokens Slug sin expandir son artefactos a corregir. [supuesto]"
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
        "No invencion de fuentes.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Marco local regido por README y programa analitico."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con rigor juridico y utilidad profesional.",
      "Asegurar coherencia institucional entre contenido, forma y fuentes."
    ],
    "style_markers": [
      "Secciones funcionales y trazables.",
      "Supuestos etiquetados de forma visible.",
      "Cierre practico obligatorio.",
      "Consistencia README-programa-tex-bib."
    ],
    "argumentative_patterns": [
      "Problema y objetivo.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia y evidencia.",
      "Conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Control administrativo"
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
          "justification": "La identidad institucional exige rigor y trazabilidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion aplicable requiere fundamento verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura valida evita perdida y errores de propagacion."
        },
        {
          "source": "Control administrativo",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La materia orienta a aplicacion profesional en gestion y control."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo derecho-administrativo-y-control.bib.",
        "Regla institucional: bloquear salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion completa sin eliminar reglas utiles previas.",
      "Ciclo 20: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 20: reforzados gates de JSON, trazabilidad y supuestos.",
      "Ciclo 20: excluido contenido doctrinal especifico de Filosofia del Derecho por no equivalencia de nodo."
    ]
  }
}