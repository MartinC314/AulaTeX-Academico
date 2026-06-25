{
  "summary": [
    "Se consolida sincronización transversal entre actividad y materia sin trasladar redacción literal.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa y normalización previa a propagación.",
    "Se refuerza compresión lossless por unión y deduplicación sin regresión.",
    "Se mantiene gate crítico: bloquear propagación si no hay JSON parseable.",
    "Se incorporan mejoras verificables del contexto local: resolver tokens Slug y corregir nombres de archivo corruptos en README."
  ],
  "identity_rules": [
    "Mantener identidad explícita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Conservar ubicación curricular: semestre 7, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener estructura reusable para reporte y presentación."
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
    "Confirmar correspondencia del producto final con la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener clase y metadatos base de la materia salvo instrucción docente distinta.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres corruptos detectados en README (supuesto: 'reporte-' y 'referencias-' perdieron la letra inicial).",
    "Evitar placeholders sin resolver en portada y tabla de autor."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar fuentes específicas de cada actividad en derecho-de-la-propiedad-y-registro.bib.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos transversales.",
    "No transferir detalles temáticos propios de Filosofía del Derecho al contenido disciplinar de Propiedad y Registro.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Conservar reglas útiles previas aunque su origen sea provisional, marcadas como provisionales."
  ],
  "open_questions": [
    "Supuesto: falta rúbrica local detallada por actividad; confirmar criterios de evaluación.",
    "Confirmar si cada actividad exige reporte, presentación u otro producto principal.",
    "Confirmar figura docente para reemplazar placeholder en authortable.",
    "Confirmar si existe formato de citación jurídica específico exigido por docente.",
    "Confirmar corrección definitiva de rutas con tokens Slug y nombres truncados en README."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 créditos.",
        "Materia: Derecho de la propiedad y registro."
      ]
    },
    "essence": [
      "Problema jurídico.",
      "Conceptos y fundamento normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar trazabilidad entre consigna, desarrollo argumentativo y cierre jurídico."
    ],
    "style_markers": [
      "Frases breves y accionables.",
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
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible"
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
          "justification": "La pauta institucional exige evidencia y formato verificable."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad bibliográfica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay validación automática confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La coherencia texto-.bib evita afirmaciones no verificables."
        }
      ],
      "evidence": [
        "README de la materia: identidad, estructura y pauta editorial.",
        "Programa analítico: propósito y ejes de trabajo.",
        "derecho-de-la-propiedad-y-registro.bib: claves institucionales verificables.",
        "Regla heredada estable: bloquear propagación ante salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicación aplicada sin pérdida de reglas útiles.",
      "Ciclo 3: se preservan gates institucionales heredados y vigentes.",
      "Ciclo 3: se agregan mejoras locales verificables sobre tokens Slug y nombres corruptos.",
      "Ciclo 3: transferencia transversal limitada a abstracciones estables."
    ]
  }
}