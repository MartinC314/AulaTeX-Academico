{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preserva nucleo editorial estable: problema, conceptos y normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate critico de normalizacion: no propagar salidas no estructuradas.",
    "Se consolida uso de carpeta de materia como entrada canonica.",
    "Se refuerza correccion de placeholders y rutas corruptas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre canonico exacto de la materia destino.",
    "Conservar contexto curricular local verificado: semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "No modificar datos de alumno, matricula o figura docente sin verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: marco conceptual-normativo, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Alinear el producto final a la planeacion o rubrica vigente."
  ],
  "activity_rules": [
    "Identificar primero consigna, rubrica y tipo de entrega.",
    "Evitar redaccion solo descriptiva; incluir postura argumentada.",
    "Sustentar afirmaciones juridicas con fuentes verificables.",
    "No transferir contenido tematico de otra materia sin validar pertinencia.",
    "Cerrar cada actividad con conclusion juridica transferible a practica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar esquema minimo completo antes de guardar memoria.",
    "Exigir respaldo o marca [supuesto] en afirmaciones no verificadas.",
    "Verificar correspondencia entre consigna, producto y evidencia citada."
  ],
  "latex_rules": [
    "Mantener espanol academico con acentos y codificacion consistente.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar archivo .bib canonico local de la materia destino.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar consistencia entre nombre de archivos, slug y metadatos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Agregar solo fuentes consultables y pertinentes a la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Mantener separacion entre bibliografia base y bibliografia especifica por actividad.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico no equivalente.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Si reaparece salida no estructurada, forzar normalizacion manual previa."
  ],
  "open_questions": [
    "Confirmar consignas y rubricas especificas de actividades locales de la materia destino.",
    "Confirmar vigencia de datos de plantilla de autor y matricula. [supuesto]",
    "Validar correccion definitiva de rutas corruptas en README.",
    "Validar reemplazo definitivo de placeholders de slug .bib en documentos guia.",
    "Confirmar si el codigo LDE-S3B1 es obligatorio en todos los productos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos juridicos consistentes y verificables.",
      "Sostener continuidad editorial institucional entre actividades, materia y nivel carrera."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion explicita entre fundamento y postura propia.",
      "Etiquetado visible de [supuesto] cuando falte confirmacion."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma, doctrina o fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion JSON",
        "Consistencia LaTeX/BibTeX"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El marco institucional define tono, forma y exigencia academica."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad de evidencia y citas",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad confiable."
        },
        {
          "source": "Consistencia LaTeX/BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y mantiene verificabilidad."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion solida resulta de problema, fundamento y analisis."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local del destino.",
        "Archivo bib local con fuentes institucionales base.",
        "Historial de salidas no parseables que exige normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 16: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 16: se preservan todos los gates de calidad criticos heredados.",
      "Ciclo 16: se refuerza control de placeholders y rutas como requisito operativo."
    ]
  }
}