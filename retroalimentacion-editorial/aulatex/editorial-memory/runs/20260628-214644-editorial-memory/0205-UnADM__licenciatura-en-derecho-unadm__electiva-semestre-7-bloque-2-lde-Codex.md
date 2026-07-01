{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad hacia materia con abstracciones estables y sin arrastre tematico especifico.",
    "Se preservan reglas utiles previas del destino y se refuerza compresion lossless por union-dedupe.",
    "Se mantiene gate critico de normalizacion: no propagar insumos no JSON parseable.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantienen como supuestos los datos curriculares o de consigna no confirmados localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar encuadre local del destino: Licenciatura en Derecho, semestre 7, bloque 2, tipo electiva.",
    "No mezclar identidad curricular de otras carreras o materias.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar la carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Registrar supuestos operativos cuando falten instrucciones de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion recursiva.",
    "Validar estructura minima completa del esquema editorial antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "No compilar con placeholders o tokens sin expandir en nombres o rutas.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales pertinentes al encargo local.",
    "Centralizar referencias de la materia en electiva-semestre-7-bloque-2.bib.",
    "Agregar fuentes especificas de cada actividad como entradas BibTeX completas.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y deduplicadas.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferencia de contenido tematico literal de Filosofia del Derecho a la electiva.",
    "Mantener bandera de normalizacion manual para ciclos con insumos no estructurados.",
    "Preservar reglas utiles previas del destino sin regresion."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales para README y portada.",
    "Confirmar figura docente en plantilla base.",
    "Corregir placeholders en README y programa analitico para nombre canonico del .bib.",
    "Supuesto: no hay consigna local de actividades especificas aun; confirmar formatos por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Normalizacion obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Producto alineado a planeacion semanal.",
        "Supuesto: creditos pendientes de confirmacion local."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos claros, fundados y transferibles.",
      "Asegurar continuidad editorial entre actividades y materia con reglas reutilizables."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos etiquetados cuando falta evidencia.",
      "Separacion clara entre marco conceptual, analisis y cierre.",
      "Sin redaccion literal heredada entre nodos transversales."
    ],
    "argumentative_patterns": [
      "Problema y objetivo primero.",
      "Marco conceptual y normativo despues.",
      "Contraste de fuentes con postura propia.",
      "Cierre con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "JSON parseable",
        "Normalizacion editorial",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Normalizacion editorial",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis se construye desde un problema concreto."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura requiere respaldo comprobable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad academica institucional exige trazabilidad de fuentes."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo .bib local de la electiva.",
        "Regla consolidada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se integra memoria de actividad con transferencia conservadora de abstracciones.",
      "Ciclo 2: se mantiene gate de parseo JSON y normalizacion manual para insumos heredados.",
      "Ciclo 2: se evita importar contenido tematico especifico no transversal.",
      "Ciclo 2: se refuerza grafo conceptual minimo reutilizable para actividades hijas."
    ]
  }
}