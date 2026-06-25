{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se refuerzan reglas editoriales estables de identidad, estructura, calidad y trazabilidad.",
    "No se transfiere contenido disciplinar de Filosofia del Derecho al nodo de Garantias constitucionales.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se conserva alerta institucional sobre entradas no parseables y necesidad de normalizacion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Garantias constitucionales, Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar contenido disciplinar entre materias sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "Verificar que el producto entregado corresponda a la consigna de la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla local y metadatos curriculares correctos.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "No introducir paquetes no estandar sin justificacion verificable.",
    "Compilar sin errores criticos, sin referencias rotas y sin placeholders literales.",
    "Corregir truncamientos en portada y macros antes de compilar.",
    "Resolver tokens sin expandir en README y programa analitico antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM, normas vigentes y doctrina verificable.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales validadas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico de nodos no equivalentes.",
    "Mantener etiquetado de riesgo para herencias con origen no parseable.",
    "Si falta contexto local de actividad, conservar cerebro editorial minimo y abrir vacios."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna local de la primera actividad de Garantias constitucionales.",
    "Confirmar rubrica de evaluacion y formato de citacion exigido en la materia.",
    "Confirmar nombre de figura docente en plantilla.",
    "Confirmar correccion completa del truncamiento en reporte-garantias-constitucionales.tex.",
    "Confirmar reemplazo total de placeholders de Slug en README y programa analitico."
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
        "Integridad academica y citas verificables.",
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Trazabilidad entre consigna, fuentes y producto."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para practica juridica.",
      "Asegurar consistencia editorial transversal sin contaminar contenido disciplinar entre materias."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Separacion clara entre marco normativo y postura personal.",
      "Cierre con aplicacion juridica concreta.",
      "Sin placeholders tecnicos en entrega final."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio con evidencia.",
      "Conclusion aplicable."
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema definido no hay eje argumentativo."
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
          "justification": "Solo se propaga memoria confiable cuando el formato es valido."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo comunes.",
        "garantias-constitucionales.bib con base institucional.",
        "Regla institucional persistente: bloquear propagacion ante JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se consolida transferencia transversal solo con abstracciones estables.",
      "Ciclo 19: se preservan reglas utiles previas y se elimina duplicidad semantica.",
      "Ciclo 19: se refuerza gate de JSON parseable y normalizacion obligatoria.",
      "Ciclo 19: se mantiene separacion entre contenido editorial reusable y contenido disciplinar local."
    ]
  }
}