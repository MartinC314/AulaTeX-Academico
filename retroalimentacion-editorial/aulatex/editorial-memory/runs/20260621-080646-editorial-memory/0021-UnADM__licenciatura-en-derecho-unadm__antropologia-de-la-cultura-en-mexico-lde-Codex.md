{
  "summary": [
    "Sincronizacion transversal consolidada para materia destino con union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM y gates de calidad ya vigentes.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "No se trasladan contenidos tematicos exclusivos de Filosofia del Derecho al destino.",
    "Se refuerza normalizacion: bloquear propagacion si no hay JSON parseable.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
    "Se confirma contexto local: semestre 4, bloque 2, obligatoria, 8 creditos [verificado en README].",
    "Se detectan placeholders y rutas truncadas en README/programa; requieren resolucion previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar nombre canonico de materia: Antropologia de la cultura en Mexico.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No heredar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir cada entrega con objetivo puntual y problema juridico o social.",
    "Estructurar en bloques: conceptos, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable semanal real.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura.",
    "Resolver nombres truncados o placeholders antes de editar rutas finales."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a practica juridica.",
    "Integrar puentes argumentativos entre enfoque cultural y juridico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente cualquier salida no estructurada heredada.",
    "Validar consistencia entre metadatos del documento y malla curricular local.",
    "Verificar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Comprobar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como referencia.",
    "Conservar configuracion en espanol y acentos correctos en .tex/.bib.",
    "Mantener clase y formato actuales salvo justificacion academica.",
    "Actualizar documenttitle/documentsubtitle por actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales.",
    "Corregir rutas con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de assets locales cuando se citen archivos internos."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no literales.",
    "Compartir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferencia de contenido disciplinar especifico de Filosofia del Derecho.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Aplicar estrategia conservadora: agregar sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar estandar unico de citas para la licenciatura (supuesto: no unificado).",
    "Confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad.",
    "Confirmar si conclusion juridica aplica a todas las actividades antropologicas.",
    "Confirmar resolucion definitiva de placeholders Slug en README y programa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a toda propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar consistencia institucional, metodologica y tecnica en toda entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Puente cultura-derecho"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio personal se fortalece con fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Puente cultura-derecho",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Evita reduccionismo y mejora pertinencia disciplinar."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico confirma ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local incluye unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla heredada estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se refuerzan gates de parseo y normalizacion sin regresion.",
      "Ciclo 21: se transfieren patrones argumentativos generales desde Filosofia del Derecho.",
      "Ciclo 21: se excluye contenido tematico no transversal del origen.",
      "Ciclo 21: se mantiene estado provisional para fuentes heredadas no verificadas."
    ]
  }
}