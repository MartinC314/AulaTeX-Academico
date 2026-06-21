{
  "summary": [
    "Se consolida transferencia lateral desde Actividad 1 a Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene gate crítico: bloquear propagación si no hay JSON parseable y estructura mínima completa.",
    "Se conserva regla de no inventar fuentes ni trasladar bibliografía exclusiva entre actividades hermanas sin verificación local.",
    "Supuesto: falta consigna y rúbrica específicas de Actividad 5; se mantiene estructura base con preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular cada entrega a Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "Citar la malla curricular como respaldo del encuadre curricular."
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
    "Adaptar el contenido al enunciado real de Actividad 5 sin romper reglas troncales de asignatura.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas de Actividad 1.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Exigir estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilización recursiva.",
    "Comprobar que el producto responda a la consigna local y no a otra actividad."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres de archivo en README por presencia de tokens sin expandir.",
    "Supuesto: .bib canónico esperado por Slug es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Transferir patrones reutilizables, no redacción literal ni conclusiones locales.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar deduplicación por unión semántica y canónica de reglas repetidas.",
    "Mantener bandera histórica de riesgo por incidentes de parseo en ciclos previos.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar tipo de producto principal: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 reutiliza .bib existente o requiere subconjunto propio.",
    "Confirmar nombre canónico final del .bib en presencia de token Slug sin expandir en README."
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
      "Problema jurídico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable y trazable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico evaluable.",
      "Asegurar consistencia entre consigna, argumentación y cierre jurídico.",
      "Sostener continuidad editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales.",
      "Inferencias explícitas.",
      "Supuestos marcados cuando falten datos.",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> postura propia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
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
          "justification": "Define tono, formato y criterios de integridad."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis parte de una pregunta o conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna local."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El marco alimenta la argumentación del estudiante."
        }
      ],
      "evidence": [
        "README: exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico: fija ejes problema, conceptos, fuentes, análisis y cierre.",
        "Historial de ciclos: hubo salidas no parseables; se mantiene gate de normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 49: deduplicación canónica aplicada sin pérdida de reglas útiles.",
      "Ciclo 49: reforzada separación entre patrones transferibles y contenido específico de actividad hermana.",
      "Ciclo 49: mantenida política de supuestos explícitos ante ausencia de consigna local.",
      "Ciclo 49: consolidado control de calidad JSON como prerequisito de propagación."
    ]
  }
}