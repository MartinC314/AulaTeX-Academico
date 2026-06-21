{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reutilizable desde Actividad 1.",
    "Se mantiene identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se preservan ejes editoriales estables: problema, conceptos y fuentes, análisis propio y conclusión jurídica.",
    "Se refuerza regla de normalización: no propagar si la salida no es JSON parseable.",
    "Se mantiene compresión lossless por unión y deduplicación sin recorte.",
    "Se marca como supuesto toda inferencia no confirmada por consigna local de Actividad 3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad hermana sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva sin evidencia local.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de Actividad 3 sin consigna confirmada."
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
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico antes de automatizar rutas.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Registrar en .bib solo entradas efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a actividad de interpretación jurídica (Semana 7) y requiere confirmación para Actividad 3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar normalización manual cuando exista antecedente de salida no estructurada.",
    "Reforzar reglas institucionales comunes en nodos hermanos de la misma asignatura.",
    "Conservar trazabilidad de cambios en cada ciclo de refuerzo lateral."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica específica de evaluación para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si aplica bibliografía depurada de Semana 7 a Actividad 3.",
    "Confirmar nombre final del .bib canónico si se corrigen tokens Slug."
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Estandarizar calidad editorial sin perder adaptación local por actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas y orden lógico.",
      "Afirmaciones con cita verificable.",
      "Supuestos marcados de forma explícita.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura propia.",
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
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay auditoría ni propagación confiable."
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
          "justification": "La conclusión válida requiere argumentación y evidencia."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: propósito de transformación del producto y ejes de trabajo.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Bibliografía local: uso condicionado de .bib depurado según consigna de actividad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 60: deduplicación lossless aplicada sin eliminar reglas útiles previas.",
      "Ciclo 60: se reforzó no-regresión y normalización obligatoria antes de propagación recursiva.",
      "Ciclo 60: se transfirieron patrones reutilizables desde nodo hermano sin copiar contenido específico.",
      "Ciclo 60: se mantuvieron supuestos explícitos por falta de consigna local confirmada."
    ]
  }
}