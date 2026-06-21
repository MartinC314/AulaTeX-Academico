{
  "summary": [
    "Se consolida sincronización transversal entre actividad origen y materia destino con estrategia conservadora.",
    "Se preservan reglas útiles previas y se deduplican sin pérdida.",
    "Se transfieren solo abstracciones editoriales estables: identidad, estructura, calidad y trazabilidad.",
    "Se evita transferir contenido temático específico de Filosofía del Derecho al nodo de Derecho Internacional Público.",
    "Se refuerza normalización obligatoria de salidas estructuradas antes de propagación recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad del entregable.",
    "Conservar alumno de plantilla si no existe instruccion local de reemplazo."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la consigna.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, argumentos, normas y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad.",
    "Mantener auditoria de parseo JSON por ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Completar metadatos de portada de forma coherente con actividad en curso.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir nombres de archivo con caracteres anómalos detectados en README.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Revisar y cerrar entornos tabular incompletos antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Conservar entradas institucionales base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar lateralmente solo reglas generales y estables entre nodos no equivalentes.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "Conservar incidencias historicas de salidas no parseables para control de calidad."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico sin acento frente a público con acento. [supuesto]",
    "Confirmar reparacion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre correcto del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si existe rubrica local por actividad para afinar profundidad argumentativa. [supuesto]",
    "Confirmar si se requiere regla local adicional para fuentes de derecho internacional publico por unidad. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Garantizar coherencia entre consigna, desarrollo y cierre.",
      "Asegurar trazabilidad editorial y tecnica para propagacion recursiva segura."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados de forma visible.",
      "Cierre con criterio juridico aplicable.",
      "Consistencia cita-bibliografia obligatoria."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia",
        "Propagacion recursiva segura"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "El producto y la forma del entregable dependen de la consigna."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo comprobable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La trazabilidad de fuentes fortalece la validez argumentativa."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad institucional define tono, rigor y formato."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "bases-de-derecho-internacional-publico.bib.",
        "Plantillas .tex locales de reporte y presentacion.",
        "Memoria consolidada previa con incidencias de parseo JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 17: se transfiere patron transversal problema-conceptos-evidencia-analisis-conclusion.",
      "Ciclo 17: se mantiene estrategia conservadora sin traslado tematico de Filosofia del Derecho.",
      "Ciclo 17: se consolidan reglas tecnicas de LaTeX para tokens sin expandir y entornos incompletos.",
      "Ciclo 17: se preserva trazabilidad de fuentes provisionales como procedencia, no identidad."
    ]
  }
}