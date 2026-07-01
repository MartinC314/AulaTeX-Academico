{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reutilizable desde actividad-1.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa y controles de calidad sin regresión.",
    "Se deduplican reglas por unión lossless y se corrigen variantes repetidas de acentuación.",
    "Se mantiene bloqueo de propagación ante salidas no JSON parseables.",
    "Se conserva política de supuestos para toda falta de consigna local verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmar guía oficial."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir fuentes académicas, normativas, jurisprudenciales y antecedentes editoriales.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas si ya están citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas y nombres de archivo solo con verificación local."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de asignatura y bibliografía específica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de actividad-3 [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar conclusiones temáticas ni bibliografía exclusiva de una actividad a otra.",
    "Mantener compresión por unión-deduplicación lossless.",
    "Conservar bandera de riesgo cuando existan incidencias previas de parseo.",
    "Aplicar normalización manual en ciclo con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica o a otra unidad.",
    "Confirmar bibliografía obligatoria específica de actividad-3.",
    "Confirmar archivo .tex principal de actividad-3."
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
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Asegurar fundamento jurídico, evidencia y transferencia profesional.",
      "Mantener continuidad editorial entre actividades hermanas sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas con orden lógico.",
      "Afirmación con evidencia y cita.",
      "Supuestos marcados cuando falte dato local.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo definido -> desarrollo consistente -> cierre coherente."
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
          "justification": "La pauta institucional exige trazabilidad y rigor de fuentes."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay auditoría editorial confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de un problema delimitado y evita resumen vacío."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema-conceptos-producto-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se consolidaron duplicados ortográficos y semánticos sin pérdida de reglas.",
      "Se reforzó no regresión y política de supuestos.",
      "Se preservó separación entre memoria editorial y evidencia académica.",
      "Se mantuvo transferencia lateral por analogía controlada."
    ]
  }
}