{
  "summary": [
    "Memoria lateral consolidada para actividad-3 con deduplicación lossless desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantienen ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene regla dura: no propagar sin JSON parseable y estructura mínima completa.",
    "Se conserva política de supuestos: no inventar consigna, formato ni bibliografía específica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedentes provisionales, no como fuentes académicas.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas reutilizables de actividad-1 sin copiar redacción literal.",
    "No trasladar conclusiones específicas ni bibliografía exclusiva de un hermano a otro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir fuentes académicas/normativas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; confirmar aplicabilidad a actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión + deduplicación lossless en cada ciclo.",
    "Conservar bandera de riesgo cuando exista antecedente de salida no estructurada.",
    "Reforzar reglas institucionales en nodos hermanos de la misma asignatura."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega de actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de actividad-3.",
    "Confirmar si actividad-3 reutiliza bibliografía existente o requiere .bib propio.",
    "Confirmar nombre canónico final del .bib de asignatura tras resolver token Slug."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en entregables académicos sólidos.",
      "Garantizar fundamento jurídico y evidencia verificable.",
      "Conectar aprendizaje con práctica profesional jurídica."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas con orden lógico.",
      "Afirmaciones con cita verificable.",
      "Supuestos marcados de forma explícita.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
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
        "Bibliografía verificable",
        "Política de supuestos"
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
          "justification": "La pauta institucional exige citas verificables y rigor académico."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se construye desde la delimitación del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        },
        {
          "source": "Política de supuestos",
          "target": "Bibliografía verificable",
          "kind": "supports",
          "justification": "Evita inventar fuentes o trasladar bibliografía no confirmada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica con criterio propio.",
        "Programa analítico: ejes de trabajo y propósito editorial.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Nota local: .clean.bib orientado a Interpretación jurídica (Semana 7) [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: deduplicación completa de reglas duplicadas por acento/variación.",
      "Ciclo 62: preservadas reglas útiles previas sin regresión.",
      "Ciclo 62: reforzada transferencia lateral por patrones reutilizables.",
      "Ciclo 62: mantenida separación entre memoria editorial y evidencia académica.",
      "Ciclo 62: añadidas preguntas abiertas donde faltan datos locales."
    ]
  }
}