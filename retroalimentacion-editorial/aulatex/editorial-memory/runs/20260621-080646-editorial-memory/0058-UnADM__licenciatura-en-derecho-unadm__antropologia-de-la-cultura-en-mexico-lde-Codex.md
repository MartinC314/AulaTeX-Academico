{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y validacion JSON.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho.",
    "Se evita transferir contenido tematico exclusivo de otra asignatura.",
    "Se refuerza normalizacion de placeholders y rutas corruptas en README/programa/.tex/.bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares especificos de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas locales."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar asumir fuentes de otras semanas o materias sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener clase y formato de plantilla local salvo justificacion academica.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README/programa/rutas.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Actualizar documenttitle y documentsubtitle por actividad real."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido doctrinal especifico de otra materia.",
    "Conservar alertas historicas de parseo como control institucional transversal.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar rubrica de evaluacion especifica de la materia destino.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Supuesto: confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Confirmar si existe listado obligatorio de fuentes antropologicas base para esta asignatura."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro, preciso y argumentativo."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion transferible.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Compresion lossless por union-dedupe."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Sostener continuidad editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con valor profesional juridico.",
      "Sin relleno descriptivo."
    ],
    "argumentative_patterns": [
      "Afirmacion relevante -> fuente verificable -> interpretacion propia.",
      "Problema contextual -> marco conceptual -> evaluacion critica -> cierre aplicable.",
      "Coherencia estricta entre consigna, desarrollo y conclusion."
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
        "Abstracciones editoriales estables"
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
          "justification": "Sin parseo valido no hay memoria reutilizable confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura del estudiante requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La transferencia profesional surge del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        }
      ],
      "evidence": [
        "README local: pauta editorial y ubicacion curricular verificable.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local: existencia de unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: regla estable de bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 58: se consolidan reglas transversales estables sin migrar doctrina especifica de Filosofia del Derecho.",
      "Ciclo 58: se refuerza gate de JSON parseable como precondicion de propagacion recursiva.",
      "Ciclo 58: se mantiene alerta de fuentes heredadas no verificadas como provisionales."
    ]
  }
}