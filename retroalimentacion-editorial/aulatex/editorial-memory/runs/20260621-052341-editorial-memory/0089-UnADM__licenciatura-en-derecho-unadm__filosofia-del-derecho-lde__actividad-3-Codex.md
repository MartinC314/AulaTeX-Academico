{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 sin copiar redacción específica.",
    "Se preservan reglas institucionales UnADM, estructura base y control de calidad sin regresión.",
    "Se mantiene compresión lossless por deduplicación y normalización JSON obligatoria.",
    "Se refuerza política de supuestos para datos no visibles en la consigna local.",
    "Se mantiene separación entre memoria editorial y evidencia académica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no confirmado en la consigna local.",
    "Tratar memorias heredadas de herramientas como antecedentes editoriales provisionales, no como fuentes académicas.",
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
    "Heredar patrones reutilizables de actividad-1 sin copiar conclusiones específicas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir tema, semana o formato de actividad-3 sin evidencia local.",
    "Registrar diferencias de actividad-3 como supuestos hasta confirmar guía oficial."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente salidas no estructuradas antes de reutilización."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar al .bib solo fuentes realmente citadas en actividad-3.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a otra actividad y se usa solo si coincide con citas reales."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener bandera de riesgo si hubo incidencias de parseo en ciclos previos.",
    "Aplicar deduplicación por unión semántica y conservar granularidad útil.",
    "Escalar preguntas abiertas cuando falte consigna textual local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar archivo .tex principal de actividad-3.",
    "Confirmar si la bibliografía depurada de Semana 7 aplica o no a actividad-3."
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
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada previa a propagación."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos verificables.",
      "Asegurar fundamento jurídico, evidencia y transferencia profesional.",
      "Preservar consistencia editorial entre actividades hermanas sin pérdida de reglas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Supuestos marcados cuando falte evidencia local.",
      "Citas verificables en afirmaciones relevantes.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
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
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor formal."
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
          "justification": "El análisis parte de una delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes de trabajo y propósito de transformación del producto.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 89: deduplicación semántica aplicada sin eliminar reglas válidas previas.",
      "Ciclo 89: se refuerza transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 89: se mantiene separación entre antecedentes editoriales y fuentes académicas.",
      "Ciclo 89: se preserva política de supuestos y no invención de fuentes."
    ]
  }
}