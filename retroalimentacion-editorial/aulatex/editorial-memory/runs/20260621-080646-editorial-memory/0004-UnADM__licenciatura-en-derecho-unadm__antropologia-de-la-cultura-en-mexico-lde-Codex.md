{
  "summary": [
    "Sincronizacion transversal ciclo 4 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y adscripcion a Licenciatura en Derecho.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita migrar contenido tematico especifico de Filosofia al nodo de Antropologia.",
    "Se refuerzan gates de JSON parseable, estructura minima y trazabilidad de fuentes.",
    "Se mantiene alerta por salidas heredadas no estructuradas como riesgo operativo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar materia destino: Antropologia de la cultura en Mexico.",
    "Conservar adscripcion: Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de otra materia al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar entregas solo descriptivas.",
    "Integrar conceptos antropologicos, culturales, juridicos o sociales pertinentes.",
    "No asumir fuentes de semanas o materias distintas sin validar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna real de actividad.",
    "No promover reglas provisionales a definitivas sin verificacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y configuracion base de la plantilla salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener campos institucionales completos y consistentes.",
    "Resolver placeholders y tokens dinamicos antes de compilar.",
    "Corregir rutas truncadas o caracteres anomalo en nombres de archivo.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Agregar entradas especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia en notas cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal y contenidos tematicos locales.",
    "Conservar metodo union-dedupe lossless sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales para calibrar formato final.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "Confirmar si la clave LDE-S4B2 es oficial institucional o convencion local.",
    "Confirmar politica final para nombres canonicos de .bib cuando hay placeholders."
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
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener coherencia argumentativa con identidad institucional.",
      "Garantizar calidad estructural antes de propagacion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales.",
      "Supuestos marcados.",
      "Cierre profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> desarrollo -> verificacion de coherencia final."
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
        "Sincronizacion transversal conservadora"
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana solidez con sustento."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite reglas estables entre materias."
        }
      ],
      "evidence": [
        "README y programa analitico del destino definen identidad, ejes y estructura.",
        "Archivo .bib local contiene fuentes base institucionales verificables.",
        "Memoria origen aporta patrones argumentativos reutilizables no tematicos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte semantico.",
      "Se conservaron alertas historicas de salida no estructurada.",
      "Se reforzo marcaje de supuestos para datos no confirmados.",
      "Se mantuvo frontera entre abstracciones transferibles y contenido disciplinar local."
    ]
  }
}