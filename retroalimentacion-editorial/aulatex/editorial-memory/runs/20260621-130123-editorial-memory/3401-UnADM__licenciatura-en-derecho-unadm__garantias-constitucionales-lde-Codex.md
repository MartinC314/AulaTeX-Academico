{
  "summary": [
    "Se sincroniza memoria transversal desde actividad no equivalente con estrategia conservadora.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se bloquea propagacion si falta JSON parseable o estructura minima.",
    "Se evita transferir contenido disciplinar de Filosofia del Derecho a Garantias constitucionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Garantias constitucionales, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Conservar coherencia con Licenciatura en Derecho en todo producto.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar contenido disciplinar entre materias sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Corregir placeholders y nombres truncados en README y programa analitico antes de reutilizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "Ajustar profundidad y formato a la consigna especifica de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion automatica si la entrada o salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales.",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Compilar sin errores criticos y sin referencias rotas.",
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "No introducir paquetes no estandar sin justificacion verificable.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir truncamientos en macros de portada antes de compilar.",
    "Verificar nombres de archivos locales antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Agregar identificador, emisor y fecha en normas juridicas citadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal y contenido tematico de materias no equivalentes.",
    "Mantener alerta institucional de riesgo por salidas no estructuradas heredadas.",
    "Etiquetar ciclos con necesidad de normalizacion manual cuando llegue herencia incompleta."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna local de la primera actividad en Garantias constitucionales.",
    "[Supuesto] Falta confirmar si la fecha debe ser automatica o fija por entrega.",
    "[Supuesto] Falta confirmar estilo de citacion requerido por la materia.",
    "Confirmar correccion completa del truncamiento en portada de reporte-garantias-constitucionales.tex.",
    "Confirmar reemplazo completo de placeholders Slug en README y programa analitico."
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
        "Marcado explicito de [Supuesto].",
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
      "Problema juridico o social claro.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Consistencia cita-texto-bib."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Garantizar calidad editorial reutilizable entre actividades y nodos.",
      "Sostener sincronizacion transversal sin contaminar contenido disciplinar local."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Secciones funcionales y ordenadas.",
      "Separacion explicita entre norma, doctrina y opinion.",
      "Cierre con aplicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial breve.",
      "Delimitar objetivo de analisis.",
      "Exponer marco normativo o doctrinal.",
      "Desarrollar postura propia con evidencia.",
      "Cerrar con conclusion aplicable."
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
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema definido no hay argumentacion focalizada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere sustento verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Solo estructura valida permite transferencia confiable."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Contenido disciplinar local",
          "kind": "contrasts",
          "justification": "Se transfieren reglas editoriales, no temas de otra materia."
        }
      ],
      "evidence": [
        "README local de Garantias constitucionales con identidad y ubicacion curricular.",
        "Programa analitico local con ejes editoriales comunes.",
        "garantias-constitucionales.bib con base institucional existente.",
        "Memoria origen valida en reglas generales de estructura y calidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza union-dedupe y no regresion.",
      "Ciclo 15: se preserva regla de bloqueo por JSON no parseable.",
      "Ciclo 15: se refuerza marcado de [Supuesto] para datos no visibles.",
      "Ciclo 15: se mantiene separacion entre herencia transversal y contenido disciplinar local."
    ]
  }
}