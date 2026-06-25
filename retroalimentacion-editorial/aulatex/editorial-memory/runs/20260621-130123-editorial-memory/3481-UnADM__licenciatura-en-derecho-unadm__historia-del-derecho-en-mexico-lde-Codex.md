{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora entre nodos no equivalentes.",
    "Se preservan reglas utiles previas del destino y se refuerzan con abstracciones estables del origen.",
    "Se mantiene el nucleo editorial de cinco ejes: problema, conceptos/fuentes, producto, analisis propio y conclusion juridica.",
    "Se consolida control de calidad: JSON parseable, normalizacion previa y trazabilidad de supuestos.",
    "Se evita transferencia de contenido tematico especifico de Filosofia del Derecho hacia Historia del Derecho en Mexico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de la materia: Historia del Derecho en Mexico.",
    "Conservar datos curriculares locales: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato de salida al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Corregir placeholders de Slug en README y programa antes de automatizar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores sin evidencia de consigna.",
    "Adaptar entrega a reporte, presentacion o producto visual segun consigna.",
    "Registrar fuentes especificas de cada actividad en el .bib local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion lossless por union y deduplicacion sin recorte.",
    "Evitar regresiones de reglas utiles previas."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentacion segun tipo de entrega.",
    "Conservar metadatos: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y creditos.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de compilar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Mantener trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No propagar bibliografia tematica de otras materias sin consulta efectiva local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No transferir redaccion literal ni contenido tematico no verificable.",
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Mantener alerta historica de salidas no parseables en niveles superiores.",
    "Si falta consigna local, conservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional: Mexico o Mexico con acento. [supuesto]",
    "Confirmar si LDE-S1B1 es codigo oficial o local de plantilla. [supuesto]",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar que el .bib canonico local es historia-del-derecho-en-mexico.bib tras resolver Slug.",
    "Verificar y corregir lineas con render anomalo en README (eporte, eferencias). [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante inferencias no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Resolver problemas juridicos con estructura academica verificable.",
      "Sostener analisis con conceptos, normas, doctrina y evidencia.",
      "Alinear cada producto a consigna real y cierre transferible.",
      "Preservar trazabilidad y control de calidad en memoria editorial."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para practica juridica.",
      "Mantener continuidad editorial entre actividades y materias sin perder contexto local."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explicito antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Citas explicitas en afirmaciones sustantivas.",
      "Cierre con implicacion juridica practica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> conceptos/marco -> analisis propio -> conclusion aplicada.",
      "Descripcion minima y argumentacion maxima con respaldo verificable.",
      "Consistencia entre consigna, desarrollo, citas y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia entre consigna y producto",
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
          "justification": "La identidad institucional exige verificabilidad y forma academica consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan contenido y evitan desviaciones de la consigna."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura entre nodos."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Metadatos y fuentes consultables sostienen la validez del argumento."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura razonada permite cerrar con aplicacion profesional."
        }
      ],
      "evidence": [
        "README de la materia: identidad, pauta editorial y estructura local.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Plantillas .tex locales: metadatos curriculares y formato institucional."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se integran reglas transversales estables desde actividad origen sin copiar contenido tematico.",
      "Ciclo 13: se refuerza gate de JSON parseable y normalizacion previa como condicion de propagacion.",
      "Ciclo 13: se consolida patron argumentativo reusable para reportes y presentaciones.",
      "Ciclo 13: se mantiene estrategia conservadora con marcacion explicita de supuestos abiertos."
    ]
  }
}