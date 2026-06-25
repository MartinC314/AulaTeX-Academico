{
  "summary": [
    "Se mantiene memoria de materia con base verificable en README, programa analitico, plantillas .tex y .bib local.",
    "Se refuerza sincronizacion transversal desde Filosofia del Derecho con solo abstracciones estables.",
    "Se conserva regla de normalizacion estructurada obligatoria ante salidas no JSON parseables.",
    "Se deduplican reglas repetidas sin recorte de contenido util previo.",
    "Se preservan cinco ejes editoriales como columna reusable entre actividades y materias.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de materia: Historia del Derecho en Mexico [supuesto: acentuacion institucional pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y profundidad al producto solicitado en planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Usar cinco ejes editoriales como estructura base reusable.",
    "Evitar mezcla de contenido de otras materias sin evidencia local verificable."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Adaptar salida al tipo de producto: reporte, presentacion o visual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar esquema minimo completo antes de propagar.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Revisar placeholders y errores de render en rutas y nombres de archivo antes de automatizar."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentacion como base editable.",
    "Conservar metadatos institucionales: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores por actividad.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir anomalias de render como saltos en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Registrar fuentes especificas por actividad sin sobrescribir bibliografia base.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva en destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales verificables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico no equivalente.",
    "Mantener alerta historica de salidas no parseables en nodos vecinos.",
    "Aplicar estrategia progresiva y conservadora: sumar mejoras verificables sin regresion.",
    "Si falta contexto local de actividad, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional: Mexico o México en nombre de materia.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla.",
    "Definir nombre oficial de figura docente para plantillas.",
    "Confirmar correccion definitiva de placeholders Slug en README y programa.",
    "Confirmar lineamiento local para separar bibliografia base y bibliografia por actividad."
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
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como armazon estable.",
      "Coherencia entre consigna, desarrollo y producto.",
      "Evidencia verificable mas analisis propio.",
      "Cierre con transferencia a practica juridica.",
      "Control de calidad estructural antes de propagacion."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, verificables y juridicamente utiles.",
      "Preservar identidad UnADM con rigor metodologico y trazabilidad editorial.",
      "Habilitar reutilizacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Objetivo explicito.",
      "Bloques funcionales trazables.",
      "Citas explicitas.",
      "Supuestos marcados.",
      "Conclusion juridica aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> conceptos/marco -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion juridica siempre acompanada de soporte verificable.",
      "Contraste entre fuentes y postura estudiantil, no solo resumen.",
      "Cierre orientado a implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Coherencia consigna-producto",
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Los ejes ordenan desarrollo y evitan desviaciones."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de fuentes consultables y metadatos."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "develops",
          "justification": "La identidad institucional exige rigor formal y cita verificable."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y estructura canonica.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Historial de salidas no parseables: requiere gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion lossless aplicada sobre reglas repetidas.",
      "Ciclo 9: se reforzo transferencia transversal de abstracciones estables.",
      "Ciclo 9: se mantuvo prohibicion de inventar fuentes y de copiar contenido tematico no equivalente.",
      "Ciclo 9: se consolidaron gates de JSON parseable, supuestos y coherencia cita-.bib."
    ]
  }
}