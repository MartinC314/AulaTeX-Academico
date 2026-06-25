{
  "summary": [
    "Se consolida refuerzo lateral de actividad-1 hacia actividad-3 sin copiar contenido específico.",
    "Se preservan reglas institucionales, estructurales y de calidad con deduplicación lossless.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se conserva política de supuestos para todo dato no confirmado localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Heredar reglas válidas del nodo hermano sin copiar redacción literal ni conclusiones específicas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, consigna o formato de actividad-3 sin evidencia local [supuesto]."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas o nombres de archivo solo con verificación local."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de asignatura y bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresión por unión y deduplicación sin pérdida.",
    "Mantener bandera de riesgo cuando existan antecedentes de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3 (reporte, presentación u otro).",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si la bibliografía depurada de interpretación jurídica aplica a actividad-3 [supuesto]."
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
      "Transformar planeación semanal en productos académicos sólidos.",
      "Asegurar fundamento jurídico, evidencia y transferencia profesional.",
      "Estandarizar calidad editorial sin perder flexibilidad por actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas y orden lógico.",
      "Afirmaciones con respaldo verificable.",
      "Supuestos marcados de forma visible.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis propio -> conclusión.",
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
        "filosofia-del-derecho-clean.bib [uso condicionado][supuesto]"
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
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay trazabilidad editorial confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se activa al delimitar el problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes de trabajo y propósito editorial.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: consolidación lateral sin regresión.",
      "Se eliminaron duplicados semánticos y ortográficos sin pérdida de reglas útiles.",
      "Se reforzó separación entre memoria editorial y fuente académica.",
      "Se mantuvo compatibilidad con propagación recursiva y control de supuestos."
    ]
  }
}