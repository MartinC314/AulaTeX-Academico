{
  "summary": [
    "Se mantiene identidad UnADM y foco juridico del destino.",
    "Se refuerza sincronizacion transversal con reglas estables no tematicas.",
    "Se conserva compresion lossless por union-dedupe sin regresion.",
    "Se mantiene alerta por salidas no parseables heredadas y normalizacion manual.",
    "Se consolida patron editorial comun: problema, fundamento, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres y rutas de archivo antes de compilar.",
    "Resolver tokens sin expandir en README y programa analitico si aparecen."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar nuevas fuentes solo cuando sean verificables y pertinentes."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino.",
    "Propagar primero identidad, estructura reusable y gates de calidad.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Aplicar estrategia progresiva y conservadora: sumar, validar, no recortar.",
    "Mantener bitacora de refuerzos por ciclo para trazabilidad."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida en la materia [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es oficial o solo interno [supuesto].",
    "Verificar vigencia de fuentes provisionales heredadas desde otros dominios [supuesto].",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa.",
    "Validar si todas las plantillas de actividad de README ya existen en repositorio local."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia pertinente y trazable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles.",
      "Preservar identidad institucional con calidad tecnica en LaTeX.",
      "Permitir propagacion segura por memoria estructurada y parseable."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Sostener postura propia con citas.",
      "Concluir con implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay analisis consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica exige respaldo trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        },
        {
          "source": "Identidad UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El enfoque institucional orienta utilidad profesional."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "derecho-a-la-seguridad-social.bib confirma base normativa local.",
        "Memoria origen confirma patron comun de cinco ejes y control de calidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 45: se reforzaron reglas transversales estables sin mezclar contenido tematico no equivalente.",
      "Ciclo 45: se mantuvo compresion lossless por union-dedupe.",
      "Ciclo 45: se preservaron alertas de parseo y normalizacion manual.",
      "Ciclo 45: se reforzo grafo conceptual minimo para propagacion recursiva segura."
    ]
  }
}