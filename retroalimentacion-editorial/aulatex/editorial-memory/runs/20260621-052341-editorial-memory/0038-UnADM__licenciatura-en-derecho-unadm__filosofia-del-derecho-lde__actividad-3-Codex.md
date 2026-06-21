{
  "summary": [
    "Se consolida transferencia lateral desde actividad-1 a actividad-3 con deduplicación lossless.",
    "Se preservan reglas institucionales UnADM, estructura mínima y control de supuestos.",
    "Se refuerza bloqueo por salida no JSON parseable antes de propagación recursiva.",
    "Se mantiene que bibliografía de Semana 7 es de uso condicionado para actividad-3 [supuesto].",
    "Se evita copiar conclusiones o redacción específica entre actividades hermanas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como [supuesto] cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1.",
    "No copiar redacción literal ni conclusiones específicas del nodo hermano.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Confirmar trazabilidad entre afirmaciones y evidencia citada.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir fuentes académicas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como [supuesto] archivo .bib canónico: filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib de asignatura solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como uso condicionado por actividad [supuesto: Semana 7]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura mínima completa.",
    "Transferir a nodos hermanos solo reglas generales y patrones argumentativos.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión-deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo cuando existan antecedentes de parseo fallido."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega de actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica específica para calibrar profundidad argumentativa.",
    "Confirmar bibliografía obligatoria propia de actividad-3.",
    "Confirmar si aplica o no bibliografía depurada de Interpretación jurídica (Semana 7).",
    "Confirmar nombre final canónico del .bib de asignatura."
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
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos.",
      "Asegurar claridad, fundamento jurídico y transferencia profesional.",
      "Conservar memoria editorial estable y reutilizable entre actividades."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Citas en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre aplicable a práctica jurídica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
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
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable entre nodos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis deriva de la delimitación del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad académica.",
        "Programa analítico define ejes: problema, conceptos, producto, análisis y conclusión.",
        "Regla persistente de calidad: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 38: consolidación lateral sin regresión desde actividad-1 a actividad-3.",
      "Ciclo 38: deduplicación de reglas repetidas con preservación semántica.",
      "Ciclo 38: refuerzo de política de supuestos y de separación entre memoria editorial y fuente académica."
    ]
  }
}