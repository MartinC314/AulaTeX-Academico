{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se mantiene identidad UnADM, contexto curricular y ejes editoriales sin regresión.",
    "Se preserva regla crítica: no propagar sin JSON parseable y estructura mínima completa.",
    "Se aplica compresión lossless por deduplicación y unión de reglas válidas.",
    "Se evita copiar conclusiones o bibliografía exclusiva entre nodos hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex o GPT-Pro como antecedentes provisionales, no como fuentes académicas.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables entre actividades hermanas.",
    "No copiar redacción literal ni conclusiones específicas de actividad-1.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir tema, semana o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir fuentes académicas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad verificada.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar rutas y nombres de archivo antes de referenciarlos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Propagar a nodos hermano solo patrones generales de identidad, estructura y calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo cuando existan incidencias previas de parseo."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad-3; confirmar producto exacto solicitado.",
    "Confirmar si actividad-3 requiere reporte, presentación u otro formato.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a actividad-3.",
    "Confirmar si la bibliografía depurada de Semana 7 aplica o no a actividad-3.",
    "Confirmar nombre canónico final del .bib de la asignatura tras resolver token Slug."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar trazabilidad entre afirmaciones, evidencia y conclusión.",
      "Preservar coherencia institucional y calidad técnica en LaTeX."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas y orden lógico.",
      "Uso de citas verificables en afirmaciones relevantes.",
      "Supuestos marcados de forma explícita.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo consistente -> cierre verificable."
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
        "malla-curricular-derecho-unadm.pdf"
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
          "justification": "La conclusión depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica con criterio propio.",
        "Programa analítico: ejes problema, conceptos, evidencia, análisis y cierre.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicación completa de reglas repetidas en origen y destino.",
      "Ciclo 3: se reforzó no regresión y normalización obligatoria antes de propagar.",
      "Ciclo 3: se mantuvo transferencia lateral sin copiar contenido específico de actividad-1.",
      "Ciclo 3: se preservaron preguntas abiertas donde faltan datos locales."
    ]
  }
}