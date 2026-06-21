{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas y se elimina duplicidad por union-dedupe lossless.",
    "Se refuerza ADN editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseables.",
    "Se agregan mejoras verificables de normalizacion en README y programa analitico del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Tratar Codex y GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Conservar al alumno registrado en plantilla si no hay instruccion local que lo sustituya."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
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
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar.",
    "Verificar correspondencia del producto con la consigna de la actividad."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivo del README.",
    "Revisar y cerrar correctamente entornos tabular antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Validar que las claves citadas existan en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas, generales y no duplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recortar reglas utiles previas.",
    "No transferir contenido tematico especifico de Filosofia del Derecho a materia no equivalente.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener incidencias historicas de parseo como trazabilidad activa.",
    "No propagar supuestos como reglas definitivas."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre uso de publico con o sin acento en nombres visibles.",
    "Confirmar correccion de tokens $(@{...}.Slug) en README y programa analitico del destino.",
    "Confirmar reparacion del corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Supuesto: no hay consigna de actividad especifica en este salto transversal.",
    "Confirmar formato minimo de conclusion juridica por tipo de evidencia en esta materia."
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
      "Conceptos y marco normativo-doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos y verificables.",
      "Preservar coherencia institucional y calidad argumentativa en toda la materia.",
      "Permitir propagacion segura entre nodos sin perder reglas utiles."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable.",
      "Trazabilidad de fuentes y decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Analisis propio",
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
          "justification": "La forma del entregable depende del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo comprobable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin fuente y referencias rotas."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La postura del estudiante convierte datos en criterio juridico aplicable."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "bases-de-derecho-internacional-publico.bib.",
        "Reglas heredadas de calidad institucional UnADM."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion completa de reglas repetidas en summary, identidad y calidad.",
      "Ciclo 10: transferencia transversal limitada a abstracciones estables; sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 10: se mantiene regla historica de bloqueo por JSON no parseable.",
      "Ciclo 10: se refuerza correccion de tokens Slug sin expandir y caracteres anomalos en README/programa.",
      "Ciclo 10: se preserva compatibilidad LaTeX y control de integridad cita-bibliografia."
    ]
  }
}