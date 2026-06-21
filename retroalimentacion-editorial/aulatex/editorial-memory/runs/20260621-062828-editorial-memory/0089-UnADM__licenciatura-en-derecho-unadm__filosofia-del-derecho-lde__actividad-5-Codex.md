{
  "summary": [
    "Se consolida memoria lateral para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular de Filosofía del Derecho.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene control estricto de normalización JSON antes de propagación.",
    "Se transfiere solo patrón reutilizable desde Actividad 1, sin copiar conclusiones ni bibliografía exclusiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia jurídica.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta dato operativo, registrar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revisión manual extra si hay historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivos.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y requiere validación de pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin pérdida semántica.",
    "Propagar solo patrones generales cuando falte consigna textual local.",
    "No propagar como académicas fuentes de memoria no verificadas.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 5 requiere reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 5 reutiliza bibliografía existente o requiere .bib propio."
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
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos con estructura argumentativa sólida.",
      "Asegurar coherencia entre consigna, desarrollo, evidencia y cierre jurídico.",
      "Sostener continuidad editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve y preciso al inicio.",
      "Secciones funcionales sin ornamento innecesario.",
      "Postura propia sustentada en evidencia.",
      "Supuestos explícitos cuando falte información local.",
      "Cierre con aplicabilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Ejes troncales de actividad jurídica",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Producto alineado a consigna"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Producto alineado a consigna",
          "kind": "supports",
          "justification": "La pauta institucional define tono, rigor y forma del entregable."
        },
        {
          "source": "Ejes troncales de actividad jurídica",
          "target": "Producto alineado a consigna",
          "kind": "develops",
          "justification": "La estructura problema-conceptos-evidencia-análisis-cierre guía la construcción del producto."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La validez argumentativa exige respaldo verificable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica depende de la consigna concreta."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de salidas no parseables justifica gate estricto de normalización estructurada.",
        "Marcadores Slug sin expandir en README justifican validación de nombres canónicos de archivos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 89: deduplicación completa de reglas repetidas sin recorte semántico.",
      "Ciclo 89: refuerzo lateral de patrones reutilizables entre actividades hermanas.",
      "Ciclo 89: se evita transferencia de conclusiones específicas y bibliografía exclusiva de Actividad 1.",
      "Ciclo 89: se mantienen supuestos abiertos por ausencia de consigna local de Actividad 5."
    ]
  }
}