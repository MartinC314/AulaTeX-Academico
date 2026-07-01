{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia de Derecho fiscal y tributario.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se refuerza compresión lossless por unión-deduplicación y política de no regresión.",
    "Se mantiene obligación de normalizar salidas no estructuradas antes de propagar.",
    "Se agregan mejoras verificables del contexto local: semestre 6, bloque 1, obligatoria, 8 créditos, y .bib local."
  ],
  "identity_rules": [
    "Conservar identidad institucional UnADM en tono, portada y formato.",
    "Vincular la materia a Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en consigna o rúbrica.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener separación entre reporte .tex, presentación .tex y bibliografía .bib local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otras semanas sin confirmación de consigna.",
    "Vincular argumentos fiscales y tributarios con aplicación profesional concreta."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de la actividad local.",
    "Corregir placeholders, rutas truncadas y tokens sin expandir en README y programa analítico."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar metadatos de portada y bloque authortable antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o datos ultralocales de actividades ajenas.",
    "Reutilizar gates institucionales sin reducir especificidad local del destino.",
    "Aplicar normalización manual si la entrada heredada llega ambigua o no estructurada."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de la primera actividad de Derecho fiscal y tributario.",
    "Confirmar producto exacto solicitado por la planeación semanal vigente.",
    "Confirmar rúbrica de evaluación para calibrar profundidad argumentativa.",
    "Confirmar formato de citación requerido por la asignatura.",
    "Confirmar si autor y matrícula deben permanecer en plantillas compartidas."
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en entregables con fundamento jurídico, evidencia y transferencia profesional.",
      "Estandarizar calidad editorial sin perder contexto local de cada actividad."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones nítidas y trazables.",
      "Conclusión operativa para práctica jurídica.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual y normativo.",
      "De la evidencia verificable al análisis propio.",
      "Del análisis a una conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM.",
        "Estructura argumentativa jurídica.",
        "Normalización de salidas estructuradas.",
        "Trazabilidad bibliográfica.",
        "Aplicación profesional en contexto fiscal y tributario."
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "supports",
          "justification": "La identidad institucional define tono, formato y estándares de entrega."
        },
        {
          "source": "Normalización de salidas estructuradas",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON válido no hay transferencia confiable entre nodos."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Calidad académica",
          "kind": "supports",
          "justification": "La verificación cita-.bib evita afirmaciones sin sustento."
        },
        {
          "source": "Estructura argumentativa jurídica",
          "target": "Aplicación profesional en contexto fiscal y tributario",
          "kind": "develops",
          "justification": "La secuencia problema-análisis-conclusión facilita transferibilidad práctica."
        }
      ],
      "evidence": [
        "README de la materia confirma ubicación curricular y pauta editorial.",
        "Programa analítico confirma ejes de trabajo reutilizables.",
        "derecho-fiscal-y-tributario.bib contiene base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida semántica.",
      "Se conservaron gates críticos heredados: JSON parseable y normalización previa.",
      "Se reforzó convergencia transversal en identidad, estructura y calidad.",
      "Se mantuvieron abiertos vacíos de contexto local como preguntas explícitas."
    ]
  }
}