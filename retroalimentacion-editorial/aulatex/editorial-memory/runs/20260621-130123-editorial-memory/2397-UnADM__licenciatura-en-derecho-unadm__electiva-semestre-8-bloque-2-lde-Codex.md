{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia electiva sin transferir contenido temático específico.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, análisis propio, conclusión jurídica y normalización estructurada.",
    "Se refuerza control de calidad: JSON parseable, trazabilidad cita-texto-bib y marcado explícito de [supuesto].",
    "Se mantiene estrategia conservadora y progresiva: unión-dedupe sin regresión de reglas útiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Fijar autor y matrícula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Usar código de curso LDE-S8B2 en metadatos.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "Corregir placeholders y nombres truncados en rutas y archivos antes de entrega."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal al producto concreto solicitado.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Vincular conceptos, normas, doctrina o datos con el problema tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No trasladar contenido específico de otras materias sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar estructura mínima completa antes de aplicar aguas abajo.",
    "Validar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar ausencia de tokens sin expandir y placeholders visibles.",
    "Comprobar correspondencia entre producto entregado y consigna vigente.",
    "No aceptar afirmaciones sin respaldo o sin marca de [supuesto]."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base local.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres truncados detectados en estructura (por ejemplo, eporte/eferencias)."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Mantener correspondencia entre claves citadas y entradas .bib.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar [supuesto] si falta un dato bibliográfico verificable."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redacción literal o contenido temático local no verificable.",
    "Mantener compresión lossless por unión-dedupe y sin regresiones.",
    "Conservar etiqueta de herencia provisional hasta validación manual local.",
    "Usar ciclo 1 histórico solo como alerta de normalización, no como evidencia final."
  ],
  "open_questions": [
    "[supuesto] Confirmar créditos oficiales de la materia para completar metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente en portada.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar política local para year y fecha de consulta del sitio UnADM.",
    "[supuesto] Confirmar si todas las actividades usarán reporte y presentación o habrá otros artefactos."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de materia como entrada canónica.",
        "Control visible de supuestos.",
        "Trazabilidad entre documentos locales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Código LDE-S8B2.",
        "[supuesto] Créditos por confirmar."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y fundamento normativo.",
      "Producto alineado a consigna.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada previa a propagación."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables jurídicos claros, verificables y argumentados.",
      "Asegurar consistencia editorial transversal sin perder contexto local."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas y ordenadas.",
      "Postura propia sustentada.",
      "Cierre con transferencia profesional.",
      "Marcado explícito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> postura -> conclusión.",
      "Afirmación jurídica -> evidencia verificable -> inferencia razonada.",
      "Evitar descripción pura; priorizar juicio jurídico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Integridad académica",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Compresión unión-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva segura",
          "kind": "supports",
          "justification": "Reduce errores heredados y evita memoria no parseable."
        },
        {
          "source": "Integridad académica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia explícita."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión útil deriva de razonamiento, no de resumen."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de pendientes."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "Bibliografía local: claves institucionales verificables.",
        "Histórico heredado: necesidad de normalización cuando hubo salida no JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se consolidan reglas transversales estables sin mover contenido temático de Filosofía del Derecho.",
      "Ciclo 6: se refuerza gate de JSON parseable como condición previa de propagación.",
      "Ciclo 6: se mantiene estrategia conservadora con unión-dedupe y sin regresión."
    ]
  }
}