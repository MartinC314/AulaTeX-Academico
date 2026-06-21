{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita migrar contenido tematico exclusivo de Filosofia al nodo de Antropologia.",
    "Se refuerza normalizacion de salidas no estructuradas y parseo JSON obligatorio.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reutilizable."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar afirmaciones sin respaldo o sin marca de supuesto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Verificar correspondencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar codificacion en espanol consistente en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) en README, programa y rutas.",
    "Corregir nombres de archivo con caracteres truncados antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener trazabilidad de procedencia cuando se use archivo local institucional."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenidos tematicos de otra materia.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Preservar reglas utiles previas sin eliminacion en ciclos futuros."
  ],
  "open_questions": [
    "Supuesto: falta confirmacion formal del estandar de citacion unico para la licenciatura.",
    "Supuesto: falta confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar rubricas especificas por actividad para ajustar profundidad argumentativa.",
    "Confirmar si la conclusion juridica aplica en todas las actividades antropologicas.",
    "Confirmar si existen fuentes base obligatorias adicionales a las institucionales."
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
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Contexto local: semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema.",
      "Conceptos.",
      "Evidencia.",
      "Analisis propio.",
      "Conclusion transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia argumentativa con identidad institucional.",
      "Permitir propagacion transversal sin contaminar contexto disciplinar local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
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
        "Transferencia transversal conservadora"
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
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento sustentado."
        },
        {
          "source": "Transferencia transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Mantiene continuidad editorial entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README de materia destino con identidad UnADM y pauta editorial.",
        "Programa analitico destino con ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local con fuentes institucionales base verificables.",
        "Historial de alertas por salidas no JSON parseables en memoria heredada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 86: deduplicacion completa de reglas repetidas.",
      "Ciclo 86: refuerzo de gates JSON y normalizacion previa a propagacion.",
      "Ciclo 86: transferencia de patrones argumentativos estables desde Filosofia a Antropologia.",
      "Ciclo 86: bloqueo explicito de traspaso tematico disciplinar no equivalente.",
      "Ciclo 86: conservacion de reglas utiles previas sin eliminacion."
    ]
  }
}