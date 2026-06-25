{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de origen hacia materia destino con estrategia conservadora.",
    "Se preservan reglas utiles previas y se deduplican sin recorte semantico.",
    "Se refuerza el nucleo estable: identidad UnADM, estructura argumentativa, evidencia verificable y normalizacion JSON.",
    "No se transfiere contenido tematico especifico de Filosofia del Derecho al destino por no equivalencia disciplinar.",
    "Se incorpora incidencia local verificable: tokens sin expandir y cortes de texto en README/reporte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local LDE-S4B1 en metadatos.",
    "No mezclar metadatos curriculares entre materias origen y destino.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separados README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, argumentos y criterio propio.",
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
    "Validar sintaxis LaTeX y cierre de entornos antes de compilar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con clase article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres con caracteres anómalos o cortes de texto en rutas y listados.",
    "Supuesto: el .bib canonico local es bases-de-derecho-internacional-publico.bib segun archivo existente."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido doctrinal especifico del origen.",
    "No propagar supuestos como reglas definitivas.",
    "Conservar incidencias historicas de salida no estructurada para auditoria.",
    "Mantener compresion lossless por union-dedupe sin regresion."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre 'publico' vs 'público' en nombres visibles.",
    "Confirmar si se normalizan de inmediato tokens $(@{...}.Slug) en README/programa.",
    "Confirmar reparacion del corte de entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar formato minimo de conclusion juridica por tipo de actividad en esta materia."
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
        "Trazabilidad de fuentes provisionales sin convertirlas en autoridad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Bases de derecho internacional publico.",
        "Codigo local: LDE-S4B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion JSON para memoria reusable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos consistentes y verificables.",
      "Preservar identidad institucional y calidad academica en toda actividad.",
      "Habilitar propagacion transversal segura entre nodos."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable.",
      "Consistencia cita-bibliografia."
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
        "Consistencia cita-bibliografia",
        "Trazabilidad de fuentes provisionales"
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
          "justification": "El producto define forma y profundidad del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes provisionales",
          "kind": "supports",
          "justification": "La estructura parseable conserva procedencia y estado de verificacion."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La integridad academica es rasgo institucional."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El orden argumentativo conduce a cierre aplicable."
        }
      ],
      "evidence": [
        "README destino: define identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: define proposito y ejes de trabajo.",
        "Bib local destino: confirma claves institucionales base.",
        "Incidencia local verificable: tokens $(@{...}.Slug) sin expandir en README/programa.",
        "Incidencia local verificable: corte de entorno tabular en reporte .tex."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se transfieren solo abstracciones estables del origen no equivalente.",
      "Ciclo 19: se mantiene regla dura de bloqueo por JSON no parseable.",
      "Ciclo 19: se refuerza etiquetado de supuestos y no invencion de fuentes.",
      "Ciclo 19: se preserva contexto curricular exclusivo del destino.",
      "Ciclo 19: se agregan incidencias tecnicas locales a gates de compilacion y normalizacion."
    ]
  }
}