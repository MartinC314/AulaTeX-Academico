{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles previas y se deduplican sin perdida.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "No mezclar metadatos curriculares entre materias."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separados README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "No asumir formato final sin confirmacion de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con consigna local vigente.",
    "Mantener auditoria de parseo JSON por ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener clase article con spanish, letterpaper y oneside.",
    "No cambiar estructura base de portada sin instruccion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Reparar entornos LaTeX incompletos antes de nuevas entregas."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Validar que toda clave citada exista en el .bib local.",
    "Mantener claves BibTeX estables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y verificadas.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "No propagar supuestos como reglas definitivas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar traslado literal de redaccion entre nodos no equivalentes.",
    "Conservar incidencias historicas de salida no estructurada para control de riesgo."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico/publico con acento en nombres visibles. [supuesto]",
    "Confirmar si el curso requiere seccion fija de marco normativo internacional por actividad. [supuesto]",
    "Confirmar si se normalizaran todos los tokens $(@{...}.Slug) en repositorio destino. [supuesto]",
    "Confirmar rubrica local de evaluacion para ajustar profundidad argumentativa. [supuesto]"
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "No mezclar contexto curricular del origen con el destino."
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
      "Transformar planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Asegurar trazabilidad editorial y calidad tecnica en flujos LaTeX y BibTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales no redundantes.",
      "Supuestos etiquetados.",
      "Cierre aplicable a practica juridica."
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
        "Consistencia cita-bibliografia"
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
          "justification": "El formato y profundidad del entregable dependen de la consigna."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "supports",
          "justification": "La estructura valida facilita controles de integridad editorial."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad define tono, orden y criterios de entrega."
        }
      ],
      "evidence": [
        "README destino: identidad, estructura y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bib local destino: claves institucionales verificables.",
        "Memoria origen: regla transversal de normalizacion y gates de parseo JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 49: deduplicacion completa de reglas repetidas sin recorte semantico.",
      "Ciclo 49: refuerzo de gates JSON y consistencia cita-bibliografia.",
      "Ciclo 49: transferencia transversal limitada a abstracciones editoriales estables.",
      "Ciclo 49: se mantiene estrategia conservadora y sin regresion."
    ]
  }
}