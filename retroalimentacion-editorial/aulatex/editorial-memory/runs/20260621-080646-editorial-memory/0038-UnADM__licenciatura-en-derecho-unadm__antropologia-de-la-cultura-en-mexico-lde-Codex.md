{
  "summary": [
    "Sincronizacion transversal completada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto local de Antropologia de la cultura en Mexico.",
    "Se incorporan del origen solo abstracciones estables: objetivo puntual, postura propia, evidencia verificable y coherencia argumento-conclusion.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable y necesidad de normalizacion previa.",
    "Se refuerza resolucion de placeholders de slug y rutas truncadas detectadas en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No transferir metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/teorico, analisis propio y cierre.",
    "Alinear el artefacto al producto pedido por la planeacion semanal.",
    "Separar reporte, presentacion y bibliografia como artefactos distintos.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar extrapolar contenidos tematicos exclusivos de otra asignatura.",
    "Marcar [Supuesto] cuando falte dato de consigna o rubrica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre metadatos del documento y la materia destino.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Revisar que no existan placeholders sin resolver en README, programa, .tex y .bib."
  ],
  "latex_rules": [
    "Usar codificacion en espanol coherente en .tex y .bib.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener coursename y coursecode locales salvo instruccion institucional.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombre literal.",
    "Corregir rutas truncadas o caracteres anomalos antes de compilar.",
    "Compilar sin errores criticos, sin referencias rotas y sin claves BibTeX faltantes."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferencia literal o tematica entre materias no equivalentes.",
    "Conservar alertas historicas de parseo como control transversal.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "No eliminar reglas utiles previas durante futuros ciclos."
  ],
  "open_questions": [
    "Confirmar rubrica oficial de evaluacion para actividades de esta materia.",
    "Confirmar estandar unico de citacion institucional (APA u otro).",
    "Confirmar si la conclusion juridica aplica a todas las actividades antropologicas o solo a algunas.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Supuesto: el nombre canonico del .bib es antropologia-de-la-cultura-en-mexico.bib; validar contra plantilla dinamica."
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
      "Problema juridico o social.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, sustentados y utiles para la practica profesional.",
      "Asegurar consistencia editorial transversal sin perder contexto local de materia."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor juridico aplicado."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Resolucion de placeholders",
        "Reglas heredadas provisionales"
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
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica gana solidez con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita errores de rutas, nombres y compilacion."
        },
        {
          "source": "Reglas heredadas provisionales",
          "target": "Identidad institucional UnADM",
          "kind": "contrasts",
          "justification": "Lo heredado se conserva, pero no se vuelve definitivo sin validacion local."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        "Archivo .bib local con entradas institucionales verificables.",
        "Historial de alertas por salidas no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 38: se consolida transferencia transversal de abstracciones estables desde actividad de Filosofia del Derecho.",
      "Ciclo 38: se evita migrar contenido tematico especifico de Filosofia al nodo de Antropologia.",
      "Ciclo 38: se refuerzan gates de parseo JSON, normalizacion y trazabilidad bibliografica.",
      "Ciclo 38: se mantiene politica de no regresion y union-dedupe lossless."
    ]
  }
}