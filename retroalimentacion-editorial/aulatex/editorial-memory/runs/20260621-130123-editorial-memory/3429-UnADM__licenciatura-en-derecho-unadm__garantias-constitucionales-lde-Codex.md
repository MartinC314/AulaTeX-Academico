{
  "summary": [
    "Se consolida sincronizacion transversal con reglas editoriales estables y sin traslado disciplinar entre materias.",
    "Se preserva identidad UnADM y contexto curricular local de Garantias constitucionales.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion recursiva.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion de reglas utiles.",
    "Se detecta memoria origen parseable en este ciclo; deja de ser vacio contextual total.",
    "Supuesto: la consigna local de actividades especificas aun no esta disponible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir contenido disciplinar de Filosofia del Derecho a Garantias constitucionales sin validacion expresa.",
    "Citar malla-curricular-derecho-unadm.pdf cuando se declare ubicacion curricular."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Corregir placeholders y truncamientos en README y programa analitico antes de usarlos como indice operativo."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Evitar afirmar contenido constitucional sin fundamento normativo o bibliografico.",
    "Verificar que el producto corresponda a la consigna de la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar congruencia entre metadatos de portada y datos curriculares locales.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar clase article en espanol, letterpaper y oneside segun plantilla local.",
    "Completar campos de portada: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matricula, semestre/bloque, tipo y creditos correctos.",
    "Usar acentos y codificacion consistentes en .tex y .bib.",
    "No introducir paquetes no estandar sin necesidad verificable.",
    "Compilar sin errores criticos, sin referencias rotas y sin comandos truncados.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar cierre completo de macros de portada antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "Mantener entradas institucionales base ya presentes.",
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Usar claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar identificador, emisor y fecha en normas juridicas usadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales ya validadas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion y de contenido tematico de otra asignatura.",
    "Mantener alertas institucionales sobre JSON no parseable como control transversal.",
    "Etiquetar ciclos con necesidad de normalizacion manual cuando llegue herencia no estructurada.",
    "Si un nodo destino estuviera vacio, inicializar cerebro minimo con identidad, estructura y gates."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad de Garantias constitucionales.",
    "Confirmar nombre definitivo de figura docente en plantilla.",
    "Confirmar si la fecha de entrega debe ser fija o \\today.",
    "Confirmar estilo de citacion exigido por la materia.",
    "Verificar correccion total de truncamientos en reporte-garantias-constitucionales.tex.",
    "Supuesto: las reglas transferidas operan como marco editorial, no como temario disciplinar."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Marcado explicito de [Supuesto].",
        "Separacion entre memoria local y herencia transversal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible.",
      "Consistencia cita-texto-bib.",
      "Compresion lossless por deduplicacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para practica juridica.",
      "Sostener un cerebro editorial persistente sin regresiones.",
      "Sincronizar transversalmente reglas estables entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Trazabilidad entre consigna, fuentes y producto.",
      "Diferenciacion clara entre marco normativo y opinion personal.",
      "Cierre con aplicacion juridica concreta."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado.",
      "Conclusion aplicable a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-texto-bib",
        "Compresion lossless por union-dedupe"
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
          "justification": "La identidad exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis parte de una pregunta delimitada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere fundamento verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        },
        {
          "source": "Compresion lossless por union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Permite consolidar sin recortar reglas utiles."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Memoria origen parseable de actividad 1 con reglas transversales reutilizables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se preservan reglas previas validas y se deduplican duplicados semanticos.",
      "Ciclo 22: se refuerzan gates de JSON parse