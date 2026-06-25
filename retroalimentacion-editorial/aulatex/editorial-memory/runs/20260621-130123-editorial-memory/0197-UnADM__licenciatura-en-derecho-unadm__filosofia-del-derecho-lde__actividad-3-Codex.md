{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se conserva política de supuestos para datos no visibles en la consigna local.",
    "Se aplica deduplicación lossless sin eliminar reglas útiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no confirmado por consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedentes provisionales, no como fuentes académicas.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "No asumir semana, formato o producto de actividad-3 sin evidencia local.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar diferencias de actividad-3 como [supuesto] hasta confirmación oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir fuentes académicas/normativas/jurisprudenciales de antecedentes editoriales.",
    "Aplicar no-regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos, sin referencias rotas y sin tokens sin expandir.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar rutas y nombres de archivo con evidencia local antes de corregir.",
    "Usar archivo .tex de reporte o presentación según consigna confirmada."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar en .bib solo entradas efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de asignatura y bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON parseable y estructura completa.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "No propagar conclusiones específicas ni bibliografía exclusiva entre hermanos.",
    "Propagar bandera de riesgo cuando existan incidencias previas de parseo.",
    "Mantener compresión por unión+deduplicación lossless.",
    "Cuando falten datos locales, propagar preguntas abiertas en lugar de contenido inventado."
  ],
  "open_questions": [
    "[supuesto] Falta consigna textual exacta de actividad-3; confirmar objetivo y entregable.",
    "Confirmar formato requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar bibliografía obligatoria de actividad-3.",
    "[supuesto] Confirmar si filosofia-del-derecho-clean.bib (Semana 7) aplica o no a actividad-3.",
    "Confirmar nombre canónico final del .bib operativo de la asignatura."
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
        "Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico que activa el análisis.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio sustentado.",
      "Cierre jurídico transferible.",
      "Normalización estructurada para memoria reusable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Asegurar consistencia editorial entre actividades de la misma asignatura.",
      "Preservar continuidad institucional sin sacrificar precisión local."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Afirmaciones con cita verificable.",
      "Supuestos marcados de forma explícita.",
      "Conclusión jurídica aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y rigor."
        },
        {
          "source": "Normalización JSON",
          "target": "Bibliografía verificable",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay trazabilidad confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis nace de una delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación fundada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema-conceptos-fuentes-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicación de reglas repetidas en identidad, estructura, calidad y bibliografía.",
      "Ciclo 6: conservación explícita de no-regresión y política de supuestos.",
      "Ciclo 6: transferencia lateral controlada sin copiar contenido específico de actividad-1."
    ]
  }
}