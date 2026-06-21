{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se preserva identidad UnADM, estructura editorial y control de calidad sin recortar reglas útiles.",
    "Se aplica deduplicación lossless y se eliminan repeticiones semánticas.",
    "Se mantiene regla crítica: no propagar contenido no parseable.",
    "Se conserva separación entre bibliografía base de asignatura y bibliografía específica por actividad.",
    "Supuesto: falta consigna y rúbrica local de Actividad 5; se mantiene estructura base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con claridad, fundamento, evidencia y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta validación local.",
    "No usar trazas de modelos como fuentes académicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmaciones, evidencia e inferencia.",
    "Alinear cada sección al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Validar JSON parseable antes de guardar o propagar."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Mantener trazabilidad entre consigna, desarrollo y criterio de evaluación.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas de actividades hermanas.",
    "No arrastrar bibliografía exclusiva de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar coherencia jurídica mínima entre premisas y conclusión.",
    "Rechazar respuestas no estructuradas antes de reutilizarlas.",
    "Aplicar revisión manual extra cuando exista historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres canónicos de archivos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de asignatura y bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente orientado a Semana 7 hasta validar pertinencia para Actividad 5.",
    "Conservar claves ya usadas en .tex para estabilidad de compilación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No transferir redacción literal, conclusiones específicas ni bibliografía exclusiva entre hermanos.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación semántica en cada ciclo.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si el entregable requerido es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía limpia de Interpretación jurídica (Semana 7) aplica a Actividad 5."
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Garantizar consistencia institucional, argumentativa y técnica.",
      "Asegurar transferencia profesional del razonamiento jurídico."
    ],
    "style_markers": [
      "Encuadre inicial breve y preciso.",
      "Secciones funcionales, no ornamentales.",
      "Afirmación con respaldo y cierre inferencial.",
      "Supuestos explícitos cuando falten datos locales.",
      "Cierre con aplicabilidad jurídica."
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
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Bibliografía base vs bibliografía específica"
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
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y criterios de integridad."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis depende de una pregunta o conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base de asignatura",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna concreta."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "El refuerzo lateral conserva patrones comunes sin copiar contenido exclusivo."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Historial de ciclos: incidentes de parseo justifican gate técnico estricto.",
        "Token Slug sin expandir en README/programa: requiere validación de nombre .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 53: deduplicación semántica integral aplicada sin pérdida funcional.",
      "Ciclo 53: se reforzó regla de no transferencia de conclusiones y bibliografía exclusiva entre hermanos.",
      "Ciclo 53: se mantuvo prioridad de normalización JSON antes de propagación recursiva.",
      "Ciclo 53: se preservaron ejes editoriales troncales de Filosofía del Derecho."
    ]
  }
}