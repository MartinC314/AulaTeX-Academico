{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y control de calidad JSON.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho hacia Antropologia.",
    "Se evita migrar contenido tematico exclusivo del nodo origen.",
    "Se refuerza marcado de supuestos y uso de fuentes heredadas como provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de rutas y nombres antes de compilar o propagar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar extrapolar fuentes de otras semanas sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar consistencia entre metadatos del documento y malla curricular local.",
    "Verificar correspondencia entre citas en texto y archivo .bib.",
    "Exigir marca de supuesto en toda afirmacion no verificable.",
    "No promover reglas provisionales a definitivas sin evidencia local."
  ],
  "latex_rules": [
    "Usar configuracion de espanol y acentos coherentes en .tex y .bib.",
    "Mantener clase y parametros base de plantilla salvo justificacion academica.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Mantener claves BibTeX estables.",
    "Corregir rutas con caracteres truncados o placeholders dinamicos.",
    "Actualizar documenttitle y documentsubtitle segun actividad real."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar bibliografia especifica por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia en notas cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar copiar redaccion literal entre nodos no equivalentes.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Si falta contexto local, conservar cerebro minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion de la materia destino.",
    "Confirmar estandar institucional unico de citacion para la licenciatura.",
    "Confirmar si coursecode LDE-S4B2 es oficial o convencional local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades antropologicas.",
    "Supuesto: claves y fuentes heredadas de GPT-Pro siguen en estado provisional."
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
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Sincronizacion transversal conservadora sin contaminar contexto disciplinar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Preservar coherencia institucional, metodologica y tecnica en LaTeX.",
      "Sostener calidad argumentativa con evidencia trazable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos etiquetados de forma visible.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
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
        "Supuestos marcados"
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
          "justification": "Sin parseo valido no hay reutilizacion segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables."
        }
      ],
      "evidence": [
        "README local de Antropologia: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local con unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria heredada: alerta de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 91: deduplicacion completa de reglas repetidas.",
      "Ciclo 91: transferidas abstracciones estables desde actividad origen.",
      "Ciclo 91: bloqueada transferencia de contenidos tematicos no transversales.",
      "Ciclo 91: reforzado gate de JSON parseable y marcado de supuestos."
    ]
  }
}