{
  "summary": [
    "Se consolida refuerzo lateral reusable de actividad-1 hacia actividad-3 sin copiar redacción específica.",
    "Se preserva identidad UnADM y contexto curricular validado en README y programa analítico.",
    "Se mantienen ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se refuerza regla crítica: normalizar y validar JSON antes de propagación recursiva.",
    "Se mantiene compresión lossless por unión y deduplicación sin regresión de reglas útiles.",
    "Supuesto: la consigna concreta de actividad-3 aún no está visible localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables entre actividades hermanas.",
    "No copiar conclusiones específicas ni redacción literal del nodo hermano.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir fuentes académicas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a otra actividad temática y su uso en actividad-3 debe confirmarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Propagar laterales con analogía controlada y sin sobreajuste temático.",
    "Reutilizar reglas institucionales y de calidad como núcleo estable.",
    "Evitar propagar supuestos como hechos confirmados.",
    "Conservar bandera de riesgo cuando exista antecedente de salida no estructurada.",
    "Aplicar deduplicación semántica continua en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar bibliografía obligatoria de la semana correspondiente.",
    "Confirmar si actividad-3 reutiliza .bib general o requiere set específico.",
    "Confirmar archivo .tex principal definitivo para actividad-3."
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
      "Problema jurídico o social como detonante.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con claridad y fundamento jurídico.",
      "Asegurar trazabilidad entre afirmaciones, evidencia y conclusión.",
      "Mantener continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas y orden lógico.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre aplicable a práctica profesional.",
      "Consistencia entre objetivo, desarrollo y cierre."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Delimitación de alcance -> desarrollo -> transferencia práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable",
        "No regresión editorial"
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
          "target": "Bibliografía verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad académica y citas comprobables."
        },
        {
          "source": "Normalización JSON",
          "target": "No regresión editorial",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable ni control de cambios."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se articula desde la delimitación del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica propia.",
        "Programa analítico: propósito y ejes de trabajo editoriales.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Contexto local: Slug no expandido requiere normalización técnica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 100: deduplicación semántica completada sin pérdida de reglas útiles.",
      "Ciclo 100: transferidos patrones laterales reutilizables desde actividad-1.",
      "Ciclo 100: evitada transferencia de conclusiones y bibliografía exclusiva no confirmada.",
      "Ciclo 100: reforzada política de supuestos y validación estructural previa a propagación."
    ]
  }
}