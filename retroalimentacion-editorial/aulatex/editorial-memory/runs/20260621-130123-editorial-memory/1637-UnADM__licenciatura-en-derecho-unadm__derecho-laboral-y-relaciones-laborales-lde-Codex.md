{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM y ejes editoriales reutilizables.",
    "Se transfiere solo abstraccion estable desde Filosofia del Derecho hacia Derecho laboral.",
    "Se mantiene normalizacion obligatoria de salidas no parseables antes de propagar.",
    "Se refuerza estructura canonica: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia destino.",
    "Usar contexto curricular verificado de la materia destino.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar traslado literal de contenido de otras materias sin pertinencia laboral.",
    "Contextualizar cada actividad en un conflicto o situacion laboral verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver marcadores de plantilla sin expandir en nombres de archivo.",
    "Supuesto: el entorno authortable de la plantilla requiere cierre antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Centralizar bibliografia local en el .bib canonico de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Si un nodo vecino esta vacio, inyectar cerebro editorial minimo y dejar vacios abiertos."
  ],
  "open_questions": [
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar formato de cita juridica exigido por docente.",
    "Confirmar politica de autoria en plantilla: fija institucional o variable por alumno.",
    "Supuesto: la consigna de cada actividad puede requerir formato distinto a reporte.",
    "Confirmar convencion final de nombres canonicos para artefactos por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion obligatoria de salidas no estructuradas.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Asegurar coherencia entre consigna, estructura argumentativa y evidencia.",
      "Sostener identidad institucional y utilidad profesional del cierre juridico."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin redaccion literal heredada entre nodos no equivalentes.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar evidencia y doctrina.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion de salidas no parseables",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad de citas y rigor formal."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento normativo."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita contaminar memoria con estructuras defectuosas."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva de razonamiento y evidencia."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "Archivo .bib local con claves institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se consolida transferencia transversal conservadora sin recorte.",
      "Se deduplican reglas repetidas y se mantienen todas las utiles.",
      "Se refuerza gate de JSON parseable como condicion de propagacion.",
      "Se preservan ejes editoriales estables y se adaptan al contexto laboral."
    ]
  }
}