{
  "summary": [
    "Se consolida sincronización transversal desde actividad de Filosofía del Derecho hacia materia Economía LDE.",
    "Se preservan reglas estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene política de normalización JSON obligatoria antes de propagación.",
    "Se corrigen artefactos de plantilla en README y programa analítico con tokens sin expandir.",
    "Se aplica compresión lossless por unión y deduplicación sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular verificado de Economía LDE: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en consigna o planeación.",
    "Tratar salidas de modelos heredadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al entregable solicitado en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar cada actividad a reporte, presentación o producto visual según consigna.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir datos económicos, conceptos jurídicos y argumento propio."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar que cada afirmación tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y economia.bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Mantener español, acentos correctos y paper letter salvo instrucción oficial distinta.",
    "Conservar plantilla base y evitar cambios de clase o paquetes sin justificación verificable.",
    "Mantener metadatos completos de portada: alumno, matrícula, figura docente, semestre, bloque, tipo y créditos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canónico de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "Agregar solo referencias realmente usadas en cada actividad.",
    "No inventar fuentes ni usar salidas de modelos como bibliografía académica.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL y nota de consulta cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "No transferir redacción literal ni datos específicos de actividad origen.",
    "Reforzar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener estrategia progresiva y conservadora con política sin regresión.",
    "Si falta contexto local, crear mínimo viable y dejar vacíos explícitos en preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar guía formal adicional de formato para Economía LDE.",
    "Confirmar nombre final de figura docente para portada.",
    "Confirmar periodicidad de actualización de year y fecha de consulta en unadmSitioWeb.",
    "Supuesto: economia.bib es el nombre canónico definitivo; validar en README limpio.",
    "Confirmar si existen rúbricas por actividad que modifiquen profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Directo y verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Economía LDE: semestre 3, bloque 2, obligatoria, 8 créditos.",
        "Planeación semanal como guía del tipo de producto."
      ]
    },
    "essence": [
      "Problema jurídico o social inicial.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables.",
      "Asegurar coherencia entre identidad institucional y argumentación jurídica aplicada.",
      "Sostener una memoria editorial reusable sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Secciones explícitas y orden lógico.",
      "Frases cortas con foco en acción editorial.",
      "Supuestos marcados cuando falte evidencia local.",
      "Criterio propio respaldado por fuentes."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar objetivo.",
      "Exponer marco conceptual o normativo.",
      "Argumentar con evidencia.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Evidencia verificable",
        "Análisis jurídico aplicado",
        "Conclusión transferible",
        "Compresión unión-dedupe"
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
          "justification": "El marco institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis jurídico aplicado",
          "kind": "depends_on",
          "justification": "Sin respaldo, el análisis se vuelve opinión no evaluable."
        },
        {
          "source": "Análisis jurídico aplicado",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión profesional deriva del razonamiento sustentado."
        },
        {
          "source": "Normalización JSON",
          "target": "Compresión unión-dedupe",
          "kind": "supports",
          "justification": "La estructura estable permite deduplicar sin pérdida."
        }
      ],
      "evidence": [
        "README de economía-lde con ubicación curricular y pauta editorial.",
        "programa-analitico-economia.md con propósito y cinco ejes.",
        "economia.bib con base institucional verificable.",
        "Regla heredada persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se mantiene núcleo transversal sin mover contenido específico de Filosofía del Derecho.",
      "Ciclo 14: se refuerza gate de parseo JSON como condición previa de propagación recursiva.",
      "Ciclo 14: se agrega corrección de tokens Slug no expandidos como mejora verificable.",
      "Ciclo 14: deduplicación semántica aplicada en identidad, estructura y calidad."
    ]
  }
}