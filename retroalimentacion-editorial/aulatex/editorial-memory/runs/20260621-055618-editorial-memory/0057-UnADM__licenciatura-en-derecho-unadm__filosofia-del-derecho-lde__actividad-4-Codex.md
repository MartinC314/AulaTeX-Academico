{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 4 con deduplicación lossless.",
    "Se preserva ADN editorial UnADM: identidad institucional, estructura argumentativa y trazabilidad.",
    "Se mantiene validación JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva del hermano.",
    "Supuesto: la consigna específica de Actividad 4 sigue no visible y requiere confirmación local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato académico.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Vincular contexto curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Explicitar problema, conceptos, evidencia y análisis propio en cada entrega.",
    "Evitar productos solo descriptivos o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Adaptar formato final según consigna: reporte, presentación o producto visual.",
    "Supuesto: confirmar tipo de producto exacto para Actividad 4 antes de cierre editorial."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables; no renombrarlas sin necesidad.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivo cuando README tenga tokens sin resolver.",
    "Resolver o documentar tokens tipo $(@{...}.Slug) antes de automatizar compilación."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib canónico de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra actividad temática; validar aplicabilidad en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener unión-dedupe sin regresiones de reglas útiles previas.",
    "Propagar lateralmente patrones de identidad, estructura y calidad, no contenido específico.",
    "Conservar banderas de normalización manual para ciclos con salidas no estructuradas.",
    "Si faltan datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar formato requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de Actividad 4.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del .bib cuando README use plantilla sin resolver.",
    "Confirmar si la bibliografía limpia actual aplica o si se requiere .bib incremental."
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
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
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
      "Transformar planeación semanal en productos académicos verificables.",
      "Garantizar claridad jurídica, evidencia y transferencia profesional."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales con lógica jurídica.",
      "Cita explícita en afirmaciones clave.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar fuentes con análisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusión aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Validación JSON",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato académico",
          "kind": "supports",
          "justification": "Define coherencia editorial transversal."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Integridad académica",
          "target": "Conclusión jurídica propia",
          "kind": "supports",
          "justification": "La conclusión exige sustento verificable."
        },
        {
          "source": "Relación problema-evidencia-conclusión",
          "target": "Calidad argumentativa",
          "kind": "develops",
          "justification": "Estructura mínima recurrente en la asignatura."
        }
      ],
      "evidence": [
        "Pauta editorial de README: identidad, integridad, citas verificables y conclusión propia.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables: gate JSON obligatorio."
      ]
    },
    "reinforcement_log": [
      "Ciclo 57: se refuerzan reglas comunes entre hermanos sin copiar contenido específico.",
      "Ciclo 57: se deduplican variantes ortográficas y semánticas conservando cobertura.",
      "Ciclo 57: se mantiene etiqueta de supuestos para datos no visibles.",
      "Ciclo 57: se preservan controles técnicos de LaTeX y bibliografía para estabilidad."
    ]
  }
}