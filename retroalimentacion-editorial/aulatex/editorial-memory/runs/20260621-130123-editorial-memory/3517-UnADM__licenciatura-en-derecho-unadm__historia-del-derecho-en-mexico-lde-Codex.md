{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de origen hacia materia destino sin copiar contenido tematico.",
    "Se preservan reglas utiles previas y se deduplican en formato accionable.",
    "Se mantiene prioridad institucional UnADM, cinco ejes editoriales y control de calidad estructural.",
    "Se refuerza normalizacion obligatoria ante salidas no JSON parseables.",
    "Se confirma base local verificable en README, programa analitico, plantillas .tex y .bib del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de materia: Historia del Derecho en Mexico [supuesto: acentuacion pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio y conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "No transferir redaccion literal ni contenidos tematicos de materias no equivalentes sin evidencia local."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Adaptar salida a reporte, presentacion o producto visual segun consigna.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar estructura minima completa del esquema editorial antes de propagar.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion por union-dedupe sin recortar reglas utiles previas.",
    "Revisar placeholders de Slug y errores de render en README/programa antes de automatizar."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base para entregas tipo reporte.",
    "Usar presentacion-historia-del-derecho-en-mexico.tex para entregas tipo presentacion.",
    "Conservar metadatos institucionales: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "Actualizar solo campos variables por actividad; no eliminar campos institucionales.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local canonico.",
    "Conservar fuentes institucionales existentes y malla curricular.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Incluir trazabilidad minima con origen y fecha de consulta cuando aplique.",
    "No propagar bibliografia especifica de Filosofia del Derecho sin consulta efectiva local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables ya validadas.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir datos curriculares especificos entre materias laterales no equivalentes.",
    "Mantener alerta historica por salidas no JSON parseables en ciclos previos.",
    "Si falta contexto local de actividad en destino, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional: Mexico o Mexico.",
    "Confirmar nombre oficial de figura docente para plantillas.",
    "Confirmar si coursecode LDE-S1B1 es oficial o local [supuesto].",
    "Corregir en README/programa los placeholders Slug no expandidos y saltos de linea anomalos [supuesto].",
    "Confirmar fuente operativa definitiva para reemplazar referencias provisionales de motor."
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
      "Sostener argumentacion con conceptos, norma, doctrina y evidencia.",
      "Convertir planeacion semanal en productos evaluables con cierre juridico propio.",
      "Preservar trazabilidad editorial y bibliografica en todo ciclo."
    ],
    "reason_for_being": [
      "Garantizar entregas consistentes, verificables y transferibles dentro del ecosistema UnADM.",
      "Evitar regresiones editoriales mediante union-dedupe y control de calidad estructural.",
      "Permitir propagacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explicito antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Citas explicitas y verificables.",
      "Cierre con implicacion practica juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema y objetivo al inicio.",
      "Marco conceptual y normativo pertinente.",
      "Contraste de evidencia con postura propia.",
      "Conclusion juridica transferible a la practica.",
      "Verificacion final de coherencia entre consigna y producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia entre consigna y producto",
        "Propagacion transversal conservadora"
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
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los cinco ejes ordenan contenido y evitan desviaciones de consigna."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura entre nodos."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de fuentes consultables y metadatos minimos."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Coherencia entre consigna y producto",
          "kind": "develops",
          "justification": "Transferir solo abstracciones estables evita contaminar contexto tematico local."
        }
      ],
      "evidence": [
        "README de materia: identidad, estructura y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Plantillas .tex locales: metadatos institucionales y estructura de entrega.",
        "Regla heredada estable: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se integran abstracciones estables del origen sin trasladar contenido tematico especifico.",
      "Ciclo 22: se refuerzan gates de JSON, supuestos explicitos y consistencia cita-.bib.",
      "Ciclo 22: se mantiene estrategia progresiva y conservadora con deduplicacion lossless."
    ]
  }
}