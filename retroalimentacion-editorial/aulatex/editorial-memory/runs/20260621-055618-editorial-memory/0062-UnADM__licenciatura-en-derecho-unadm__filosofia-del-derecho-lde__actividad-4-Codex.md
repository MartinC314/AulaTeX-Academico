{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM, ubicación curricular y pauta editorial canónica de la asignatura.",
    "Se refuerza gate crítico: no propagar nada sin JSON parseable y estructura mínima completa.",
    "Se transfieren solo patrones reutilizables desde Actividad 1: estructura, calidad, trazabilidad y argumentación.",
    "Supuesto: la consigna específica de Actividad 4 no está visible; se mantiene plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica alineada con UnADM.",
    "Vincular toda entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica documental.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "No trasladar conclusiones específicas de Actividad 1 a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Exigir estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y entradas reales en .bib."
  ],
  "latex_rules": [
    "Usar español con acentos y codificación consistente en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves activas sin migración completa.",
    "Citar en .tex solo claves existentes en .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens de plantilla sin expandir en README y programa antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables: UnADM, SCJN, UNAM-IIJ.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece asociado a Semana 7; verificar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas y no contenido específico de un hermano.",
    "Mantener unión-dedupe sin regresión de reglas útiles previas.",
    "Si falta consigna local, propagar plantilla estructural y abrir preguntas.",
    "Preservar trazabilidad de supuestos y estado provisional de fuentes heredadas.",
    "Aplicar refuerzo-lateral: consolidar ADN común sin copiar redacción literal."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y criterios.",
    "Confirmar rúbrica docente específica para calibrar profundidad argumentativa.",
    "Confirmar nombre canónico final del .bib cuando el token de plantilla se resuelva.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere .bib incremental propio.",
    "Confirmar si las fuentes periodísticas actuales son aceptadas por la rúbrica o solo apoyo contextual."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro.",
        "Jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Entrada canónica en carpeta de asignatura.",
        "Normalización obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
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
      "Convertir planeación semanal en productos académicos trazables y útiles para práctica jurídica.",
      "Garantizar calidad editorial reproducible en actividades hermanas sin perder identidad institucional."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Citas explícitas y verificables.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problematizar contexto.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Fijar postura justificada.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON",
        "Trazabilidad bibliográfica",
        "Relación problema-evidencia-conclusión",
        "Cinco ejes del programa analítico"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad bibliográfica",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad académica y citas verificables."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay propagación segura."
        },
        {
          "source": "Cinco ejes del programa analítico",
          "target": "Relación problema-evidencia-conclusión",
          "kind": "develops",
          "justification": "Los ejes ordenan la argumentación y el cierre jurídico."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Relación problema-evidencia-conclusión",
          "kind": "supports",
          "justification": "La conclusión sólida depende de evidencia verificable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canónica, integridad académica y conclusión jurídica propia.",
        "Programa analítico: propósito editorial y cinco ejes de trabajo.",
        "Antecedentes de salidas no parseables: se mantiene gate JSON estricto.",
        "Token Slug sin resolver en README/programa: requiere validación local."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de tono, estructura y calidad.",
      "Se eliminó transferencia de contenido específico de Actividad 1 no reutilizable.",
      "Se preservaron controles críticos: JSON, supuestos, citas y .bib.",
      "Se añadió relación explícita entre ejes curriculares y patrón argumentativo.",
      "Se mantuvo estado provisional de datos no verificados."
    ]
  }
}