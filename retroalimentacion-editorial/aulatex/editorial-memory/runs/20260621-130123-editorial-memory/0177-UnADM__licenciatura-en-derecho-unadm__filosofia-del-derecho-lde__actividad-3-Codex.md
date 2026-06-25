{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1 sin copiar contenido específico.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes editoriales persistentes: problema, conceptos y fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se aplica deduplicación lossless y no regresión de reglas útiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales previas como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin eliminar ninguna útil.",
    "No copiar redacción literal, conclusiones específicas ni bibliografía exclusiva del nodo hermano.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
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
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrarlas sin necesidad verificada.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos y rutas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib por Slug institucional."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a interpretación jurídica y su uso en actividad-3 depende de coincidencia temática."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo por historial de salidas no estructuradas.",
    "Propagar reglas específicas de Filosofía del Derecho solo a nodos de la misma asignatura."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar bibliografía obligatoria de la semana correspondiente.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica u otro tema.",
    "Confirmar archivo .tex principal y artefacto final de actividad-3."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos claros y fundamentados.",
      "Asegurar trazabilidad entre afirmaciones, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Supuestos marcados cuando falte evidencia local.",
      "Citas verificables en afirmaciones relevantes.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo de actividad -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
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
        "filosofia-del-derecho-clean.bib [supuesto de uso condicionado]"
      ],
      "relations": [
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
          "justification": "El análisis deriva de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión se sostiene con argumentación y evidencia."
        },
        {
          "source": "Identidad UnADM",
          "target": "Bibliografía verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad académica y citas comprobables."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica con criterio propio.",
        "Programa analítico: ejes de trabajo y propósito editorial.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se transfieren patrones estables desde actividad-1 a actividad-3 por analogía controlada.",
      "Se elimina duplicación semántica y se conserva cobertura total de reglas útiles.",
      "Se refuerza separación entre memoria editorial y evidencia académica.",
      "Se mantiene incertidumbre explícita donde faltan datos locales."
    ]
  }
}