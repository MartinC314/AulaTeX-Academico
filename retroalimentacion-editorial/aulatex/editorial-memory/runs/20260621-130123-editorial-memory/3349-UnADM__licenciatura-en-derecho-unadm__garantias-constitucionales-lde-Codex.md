{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable, calidad y trazabilidad.",
    "Se transfiere solo abstraccion editorial desde actividad origen no equivalente.",
    "Se mantiene bloqueo institucional ante entradas no JSON parseables.",
    "Se refuerza normalizacion previa a propagacion recursiva.",
    "Se crea y mantiene cerebro editorial minimo de materia con vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado de la materia destino.",
    "Conservar coherencia con Licenciatura en Derecho en todo producto.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir contenido disciplinar de Filosofia del Derecho a Garantias constitucionales sin validacion expresa.",
    "Usar la carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Corregir placeholders y truncamientos en README, programa y plantillas antes de reutilizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Vincular cada afirmacion juridica relevante con norma o fuente identificable.",
    "Ajustar profundidad y formato a la consigna local de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y parametros base de la plantilla local salvo requerimiento verificado.",
    "Completar campos de portada y tabla de autor antes de entrega.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar cierre de macros y truncamientos en portada.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo y referencias."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como supuesto cualquier inferencia sobre archivo .bib cuando no haya confirmacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre nodos no equivalentes solo patrones editoriales estables.",
    "Evitar traslado de contenido tematico entre materias sin validacion local.",
    "Reutilizar controles institucionales de calidad en nodos laterales y superiores.",
    "Mantener alerta persistente de riesgo por fuentes heredadas no parseables.",
    "Conservar estrategia progresiva y conservadora en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad de Garantias constitucionales.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar figura docente y politica de fecha en portada.",
    "Confirmar si el estilo de citacion requerido es APA, juridico mexicano u otro.",
    "Confirmar que el truncamiento de \\universityname en la plantilla ya fue corregido.",
    "Supuesto: el .bib canonico local es garantias-constitucionales.bib por contexto de carpeta."
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
        "Normalizacion estructurada antes de propagar.",
        "Trazabilidad entre consigna, fuentes y producto."
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
      "Conceptos y marco normativo verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Control estructural y bibliografico estricto."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Preservar identidad UnADM con rigor juridico y tecnico.",
      "Asegurar propagacion confiable mediante JSON y gates de calidad."
    ],
    "style_markers": [
      "Frases precisas y accionables.",
      "Marcado explicito de supuestos.",
      "Separacion entre marco normativo y postura personal.",
      "Cierre con aplicacion juridica concreta."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio con evidencia.",
      "Conclusion aplicable a practica profesional."
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
        "Propagacion conservadora entre nodos no equivalentes"
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
          "justification": "La identidad institucional exige evidencia verificable y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe fundarse en norma o doctrina verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion conservadora entre nodos no equivalentes",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Regla institucional persistente: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza union-dedupe sin regresion.",
      "Ciclo 2: se preservan reglas utiles previas y se elimina duplicidad literal.",
      "Ciclo 2: se mantiene transferencia solo de abstracciones editoriales estables.",
      "Ciclo 2: se sostienen vacios locales como preguntas abiertas, sin invencion de fuentes."
    ]
  }
}