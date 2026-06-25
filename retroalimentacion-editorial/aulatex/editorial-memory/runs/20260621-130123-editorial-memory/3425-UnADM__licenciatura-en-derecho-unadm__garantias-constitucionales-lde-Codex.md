{
  "summary": [
    "Se consolida sincronizacion transversal hacia Garantias constitucionales con union-dedupe y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se mantiene estrategia conservadora: transferir solo abstracciones editoriales, no contenido disciplinar de Filosofia del Derecho.",
    "Se refuerza normalizacion obligatoria: no propagar si la salida no es JSON parseable.",
    "Se confirma contexto local del destino: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local del destino: Garantias constitucionales, LDE-S2B1, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Conservar coherencia con Licenciatura en Derecho en todo producto.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] cualquier dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar contenido disciplinar de Filosofia del Derecho al destino sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Conservar nombres de archivo base locales salvo requerimiento explicito."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "Confirmar que cada entrega corresponda a la consigna de la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagacion automatica si la entrada o salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar memoria aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar congruencia entre portada y datos curriculares de la materia.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos, sin referencias rotas y sin placeholders literales.",
    "Mantener clase article en espanol, letterpaper y oneside segun plantilla local.",
    "Completar campos de portada antes de entrega: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matricula, semestre/bloque, tipo y creditos correctos.",
    "No introducir paquetes no estandar sin justificacion tecnica verificable.",
    "Corregir truncamientos y tokens sin expandir en README, programa analitico y portada."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Usar claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar identificador, emisor y fecha cuando se cite normativa."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir con nodos no equivalentes solo patrones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenidos tematicos de otra materia.",
    "Mantener alertas institucionales de riesgo por herencias no parseables (Codex, GPT-Pro).",
    "Preservar reglas previas utiles y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad en Garantias constitucionales.",
    "Confirmar si la fecha en portada debe ser automatica o fija por entrega.",
    "Confirmar estilo de citacion requerido (APA, juridico mexicano u otro).",
    "Verificar y corregir truncamientos detectados en README y reporte .tex.",
    "Resolver placeholders de Slug en README y programa analitico hacia garantias-constitucionales.bib.",
    "Confirmar nombre de figura docente en plantilla."
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
      "Problema juridico o social claro.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Consistencia cita-texto-bib."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos evaluables con fundamento juridico y criterio propio.",
      "Asegurar trazabilidad entre consigna, fuentes, argumentacion y conclusion.",
      "Permitir propagacion recursiva segura mediante memoria estructurada y validada."
    ],
    "style_markers": [
      "Frases cortas y verificables.",
      "Separacion explicita entre norma, doctrina, hecho y opinion.",
      "Cierre con aplicacion juridica concreta.",
      "Sin placeholders ni tokens sin expandir en artefactos finales."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Conceptos y marco normativo.",
      "Analisis propio con evidencia.",
      "Conclusion transferible a practica profesional."
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
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema definido no hay analisis juridico enfocado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere sustento normativo verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "La propagacion recursiva solo es confiable con JSON valido."
        },
        {
          "source": "Consistencia cita-texto-bib",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La consistencia formal evita afirmaciones sin respaldo."
        }
      ],
      "evidence": [
        "README local con identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo y proposito editorial.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Regla institucional heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recortar cobertura util.",
      "Se reforzo gate de JSON parseable como condicion de propagacion recursiva.",
      "Se mantuvo separacion entre herencia transversal y contenido disciplinar local.",
      "Se agrego enfoque en consistencia cita-texto-bib como control transversal estable.",
      "Se preservo contexto curricular local del destino y se marcaron vacios como [Supuesto]."
    ]
  }
}