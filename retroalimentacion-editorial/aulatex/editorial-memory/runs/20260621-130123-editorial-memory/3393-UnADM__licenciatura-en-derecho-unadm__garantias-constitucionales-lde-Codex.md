{
  "summary": [
    "Se sincroniza memoria transversal desde actividad no equivalente con estrategia conservadora.",
    "Se preservan reglas útiles previas por unión y deduplicación sin regresión.",
    "Se refuerza ADN editorial común: identidad UnADM, estructura reusable, evidencia verificable y cierre jurídico.",
    "Se mantiene separación entre control editorial transversal y contenido disciplinar local.",
    "Se conserva alerta institucional: bloquear propagación con entradas no parseables."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local del destino: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "No transferir contenido disciplinar de Filosofía del Derecho a Garantías constitucionales sin validación expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeación semanal.",
    "Mantener separación entre reporte, presentación, programa analítico y bibliografía.",
    "Corregir placeholders y nombres truncados en README y programa analítico antes de reutilizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir hechos, normas, doctrina y opinión propia.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Compilar sin errores críticos ni referencias rotas.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "No introducir paquetes no estándar sin justificación verificable.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Verificar y reparar truncamientos en macros de portada del .tex local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Mantener claves BibTeX descriptivas y estables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables ya validadas.",
    "No propagar contenido temático entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual.",
    "Aplicar compresión lossless por unión-dedupe en cada ciclo.",
    "Conservar alertas históricas de riesgo de parseo como control institucional.",
    "Etiquetar ciclos con necesidad de normalización manual cuando llegue entrada no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad en Garantías constitucionales.",
    "Confirmar figura docente en la plantilla .tex.",
    "Confirmar estilo de citación exigido por la materia.",
    "Confirmar si la fecha de entrega debe ser fija o \\today.",
    "Confirmar corrección final de truncamientos en reporte-garantias-constitucionales.tex.",
    "Supuesto: la transferencia actual aplica solo como control editorial transversal."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Trazabilidad entre consigna, fuentes y producto.",
        "Normalización estructurada antes de propagar.",
        "Marcado explícito de [Supuesto]."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantías constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Marco conceptual y normativo.",
      "Análisis propio sustentado.",
      "Conclusión jurídica transferible.",
      "Consistencia cita-texto-bibliografía."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Estandarizar calidad editorial sin perder contexto local.",
      "Permitir propagación transversal segura entre nodos."
    ],
    "style_markers": [
      "Frases breves y verificables.",
      "Separación clara entre marco normativo y postura personal.",
      "Cierre con aplicación jurídica concreta.",
      "Sin literalidad heredada entre materias distintas."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Conceptos y marco normativo delimitados.",
      "Análisis propio con evidencia.",
      "Conclusión aplicable a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia cita-texto-bib",
        "Propagación recursiva segura"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia verificable y trazabilidad."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica debe sostenerse en norma o doctrina."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Reglas transversales estables",
          "target": "Sincronización editorial",
          "kind": "develops",
          "justification": "La transversalidad útil surge de abstracciones, no de contenido temático."
        }
      ],
      "evidence": [
        "README local con ubicación curricular y pauta editorial.",
        "Programa analítico con ejes de trabajo comunes.",
        "garantias-constitucionales.bib con base institucional.",
        "Histórico institucional: bloqueo por JSON no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicación completa de reglas repetidas.",
      "Ciclo 13: se mantiene no regresión de quality gates institucionales.",
      "Ciclo 13: se refuerza separación entre transferencia editorial y contenido disciplinar.",
      "Ciclo 13: se añaden controles explícitos para placeholders y truncamientos locales."
    ]
  }
}