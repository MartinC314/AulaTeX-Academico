{
  "summary": [
    "Sincronización transversal aplicada con transferencia de abstracciones estables.",
    "Se conserva identidad UnADM y ubicación curricular local verificada.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene bloqueo de propagación para salidas no JSON parseables.",
    "Se preserva estrategia progresiva y conservadora sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Mantener ubicación curricular local: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar código local LDE-S7B1 cuando aplique.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Transformar planeación en reporte o presentación según consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validación de consigna."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que el producto final corresponda a la consigna de la actividad."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir en README y programa analítico antes de automatizar rutas.",
    "Corregir placeholders en metadatos de portada y tabla de autor antes de entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Usar derecho-de-la-propiedad-y-registro.bib como archivo local canónico de la materia.",
    "Agregar fuentes específicas de cada actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no ambiguas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No transferir redacción literal ni datos hiperlocales de archivos.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar rúbrica de evaluación específica de la materia.",
    "Confirmar estilo de citación jurídica requerido por figura docente.",
    "Confirmar producto exacto por actividad: reporte, presentación u otro.",
    "Supuesto: falta consigna textual detallada de próximas actividades.",
    "Confirmar resolución final de placeholders locales como Figura docente."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Accionable y verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Sin propagación de salidas no parseables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la propiedad y registro.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico.",
      "Marco conceptual y normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Sostener consistencia institucional y técnica en toda entrega."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados explícitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al análisis propio.",
      "Del análisis a una conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Trazabilidad bibliográfica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor formal."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis responde a una pregunta jurídica definida."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión requiere fundamento jurídico explícito."
        },
        {
          "source": "Evidencia verificable",
          "target": "Trazabilidad bibliográfica",
          "kind": "develops",
          "justification": "Las citas consistentes conectan afirmaciones con fuentes."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "Archivo BibTeX local de la materia."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se conservaron gates críticos heredados de calidad institucional.",
      "Se reforzó transferencia transversal en nivel abstracto, no literal.",
      "Se mantuvo compatibilidad con contexto curricular local del destino."
    ]
  }
}