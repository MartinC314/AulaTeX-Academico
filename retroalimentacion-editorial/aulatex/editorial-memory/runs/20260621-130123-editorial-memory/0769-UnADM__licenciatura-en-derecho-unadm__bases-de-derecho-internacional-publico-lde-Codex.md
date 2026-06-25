{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas institucionales, de estructura, calidad y trazabilidad ya validas en el destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se transfieren solo abstracciones editoriales estables; no se traslada contenido tematico de Filosofia del Derecho.",
    "Se detectan pendientes locales verificables: tokens sin expandir en README/programa y corte de entorno tabular en reporte .tex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia: Bases de derecho internacional publico.",
    "Usar contexto curricular local verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local LDE-S4B1 en metadatos de entregables.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Tratar Codex/GPT-Pro como procedencia provisional, no como identidad del entregable.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada propia; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio personal.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes.",
    "Aplicar los ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna de actividad y producto final.",
    "Mantener auditoria de parseo JSON en cada ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper, oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Reparar cierre de entornos tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Conservar nombres de archivo locales salvo normalizacion acordada."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Validar que toda clave citada exista en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas y deduplicadas.",
    "Aplicar compresion lossless por union-dedupe sin recorte semantico.",
    "No propagar supuestos como reglas definitivas.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual en saltos transversales.",
    "Si falta contexto local, conservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico vs publico con acento en nombres visibles. [supuesto]",
    "Confirmar si se normalizaran nombres con caracteres anómalos en README.",
    "Confirmar si la materia requiere plantillas adicionales por tipo de actividad.",
    "Confirmar politica local para renombre de archivos cuando se corrijan tokens Slug.",
    "Confirmar si hay rubrica transversal obligatoria para conclusion juridica."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Bases de derecho internacional publico.",
        "No mezclar metadatos curriculares con materias origen."
      ]
    },
    "essence": [
      "Consigna primero, estructura despues, evidencia siempre.",
      "Problema juridico y conclusion transferible como eje funcional.",
      "Trazabilidad y parseabilidad como condicion de memoria util."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Mantener coherencia institucional, metodologica y tecnica en LaTeX.",
      "Permitir propagacion segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
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
          "justification": "El producto y su forma dependen de la instruccion semanal."
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
          "kind": "develops",
          "justification": "La estructura valida facilita controles automaticos de calidad."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El marco institucional define tono, formato y rigor."
        }
      ],
      "evidence": [
        "README destino: ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Archivo .bib destino: claves institucionales existentes.",
        "Historial: incidencias de salida no parseable y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicacion completa de reglas repetidas y variantes equivalentes.",
      "Ciclo 17: se preservan reglas utiles previas sin eliminacion regresiva.",
      "Ciclo 17: se agregan mejoras verificables locales (tokens Slug y tabular truncado).",
      "Ciclo 17: transferencia transversal limitada a abstracciones estables."
    ]
  }
}