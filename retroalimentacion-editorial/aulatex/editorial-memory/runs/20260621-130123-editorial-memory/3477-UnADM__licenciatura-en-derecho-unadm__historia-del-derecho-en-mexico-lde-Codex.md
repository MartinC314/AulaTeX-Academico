{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de Filosofia del Derecho hacia materia Historia del Derecho en Mexico.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y control de calidad.",
    "Se mantiene politica de compresion lossless por union-dedupe sin recorte de reglas utiles.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos.",
    "Se refuerza base minima verificable del destino con README, programa analitico, plantilla LaTeX y .bib local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre de materia local: Historia del Derecho en Mexico.",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No propagar datos curriculares de una materia a otra sin evidencia documental local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear siempre el entregable al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Aplicar cinco ejes editoriales como estructura transversal reusable."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar formato segun consigna: reporte, presentacion o producto visual.",
    "No asumir fuentes o materiales de semanas distintas sin confirmacion.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Revisar placeholders o tokens sin expandir antes de automatizar."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentacion segun el tipo de entrega.",
    "Conservar metadatos institucionales: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "No eliminar campos institucionales; solo actualizar valores concretos por actividad.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y creditos.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo y placeholders de Slug en README y programa antes de compilar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Mantener trazabilidad: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No transferir bibliografia tematica de Filosofia del Derecho sin consulta efectiva en la materia destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables y verificables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar redaccion literal y contenido tematico especifico entre nodos no equivalentes.",
    "Mantener alerta historica de salidas no parseables en niveles superiores y laterales.",
    "Aplicar estrategia progresiva y conservadora: reforzar lo estable, abrir vacios locales como preguntas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional de Mexico/Mexico en nombre de materia.",
    "Confirmar si LDE-S1B1 es codigo oficial o clave local de plantilla. [supuesto]",
    "Definir nombre oficial de figura docente para plantillas.",
    "Validar y corregir entradas con render anomalo en README (eporte, eferencias). [supuesto]",
    "Confirmar fuente operativa definitiva de memoria heredada (Codex/GPT-Pro). [supuesto]",
    "Confirmar consigna local de primera actividad para ajustar granularidad de estructura."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias no verificadas."
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
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como nucleo reusable.",
      "Problema, conceptos y evidencia, analisis propio, cierre juridico.",
      "Coherencia entre consigna, producto y aparato de citas.",
      "Sincronizacion transversal sin contaminar contenido tematico entre materias."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para practica juridica.",
      "Asegurar continuidad editorial institucional con trazabilidad y control formal.",
      "Permitir propagacion recursiva segura mediante estructura parseable y reglas estables."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo explicito.",
      "Secciones funcionales con trazabilidad.",
      "Citas verificables en cada afirmacion sustantiva.",
      "Cierre con criterio juridico propio.",
      "Etiquetado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Definir conceptos y marco normativo relevante.",
      "Contrastar evidencia con postura propia.",
      "Concluir con implicacion juridica practica.",
      "Verificar correspondencia entre pregunta guia y conclusion."
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
          "justification": "La identidad institucional exige verificabilidad y formato consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan contenido y reducen desviaciones."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay propagacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La integridad depende de fuentes consultables y metadatos completos."
        },
        {
          "source": "Coherencia entre consigna y producto",
          "target": "Propagacion transversal conservadora",
          "kind": "develops",
          "justification": "La regla local validada se vuelve abstraccion reusable."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de Historia del Derecho en Mexico.",
        "historia-del-derecho-en-mexico.bib con fuentes institucionales.",
        "Plantillas LaTeX de reporte y presentacion.",
        "Memoria origen: ejes editoriales, calidad y normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicadas reglas repetidas y mantenidas reglas utiles sin recorte.",
      "Ciclo 12: transferidas solo abstracciones estables entre nodos no equivalentes.",
      "Ciclo 12: reforzados quality gates de parseo JSON y normalizacion previa.",
      "Ciclo 12: preservada separacion entre contenido tematico local y reglas transversales."
    ]
  }
}