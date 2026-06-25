{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia de Derechos de autor sin recorte.",
    "Se preserva identidad UnADM, estructura reusable y control de calidad institucional.",
    "Se mantiene estrategia conservadora: herencias no verificadas quedan como provisionales.",
    "Se refuerza normalización obligatoria antes de propagación recursiva.",
    "Se corrigen abstracciones estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar herencia Codex y GPT-Pro como provisional hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Agregar fuentes específicas por actividad al .bib local.",
    "No asumir fuentes de otras semanas o materias sin confirmación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analítico para tokens sin expandir y nombres corruptos."
  ],
  "latex_rules": [
    "Usar español y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "No dejar comandos incompletos en preámbulo [supuesto: existe un usepackage truncado en reporte].",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos pertinentes.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Evitar redacción literal; mover reglas reutilizables de identidad, estructura y calidad.",
    "Mantener bandera de normalización manual para herencias antiguas no estructuradas.",
    "No propagar datos personales del alumno."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Confirmar nombre de figura docente para eliminar marcador pendiente.",
    "Confirmar si Roma Norte, Ciudad de México debe quedar fijo en plantilla.",
    "Validar sustitución total de tokens Slug por derechos-de-autor.bib.",
    "Corregir nombres de archivo corruptos en README (eporte, eferencias).",
    "Validar orden de paquetes respecto a \\input{template} en esta plantilla."
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
        "Normalización estructurada previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 créditos.",
        "Materia destino: Derechos de autor."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y trazables.",
      "Conservar consistencia editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Declarar supuestos explícitamente.",
      "Usar estructura funcional repetible.",
      "Mantener trazabilidad entre portada, contenido y referencias."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Análisis con postura propia.",
      "Cierre con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Integridad bibliográfica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Propagación segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Toda afirmación debe tener respaldo trazable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La postura argumentada sostiene un cierre profesional útil."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia transversal de la suite",
          "kind": "supports",
          "justification": "Permite coherencia entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README de Derechos de autor define ubicación curricular y pauta editorial.",
        "Programa analítico fija ejes problema-conceptos-producto-análisis-cierre.",
        "derechos-de-autor.bib contiene base institucional verificable.",
        "Se detectan tokens Slug sin expandir en README y programa analítico.",
        "Se detecta comando LaTeX incompleto en reporte [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se deduplican reglas repetidas sin pérdida semántica.",
      "Ciclo 12: se refuerzan gates de JSON parseable y estructura mínima.",
      "Ciclo 12: se mantiene herencia provisional Codex/GPT-Pro sin validación local.",
      "Ciclo 12: se prioriza transferencia de abstracciones estables, no texto literal."
    ]
  }
}