{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reutilizable desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes editoriales estables: problema, conceptos y fuentes, análisis propio, conclusión jurídica.",
    "Se aplica compresión lossless por unión y deduplicación sin recorte.",
    "Se conservan supuestos explícitos cuando falta consigna local de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "No asumir consigna, semana o formato de actividad-3 sin evidencia local.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Si faltan datos locales, usar estructura base y dejar supuestos explícitos."
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
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y su uso en actividad-3 debe confirmarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables de identidad, estructura, calidad y método.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar normalización manual cuando exista antecedente de salida no estructurada.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica o a otro tema.",
    "Confirmar archivo .tex principal y .bib operativo para actividad-3."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a práctica profesional."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico sólido y verificable.",
      "Asegurar trazabilidad entre afirmaciones, evidencia y cierre jurídico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones sustantivas.",
      "Supuestos marcados cuando falta evidencia local.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable",
        "Supuestos explícitos"
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
          "justification": "La pauta institucional exige integridad académica y citas verificables."
        },
        {
          "source": "Normalización JSON",
          "target": "Supuestos explícitos",
          "kind": "supports",
          "justification": "La estructura normalizada obliga a declarar incertidumbre sin inventar datos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis necesita delimitación previa del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida deriva de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La solidez del cierre depende de evidencia rastreable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes problema-conceptos-producto-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 56: deduplicación completa de reglas repetidas con conservación semántica.",
      "Ciclo 56: se mantiene política de no invención y marcado de supuestos.",
      "Ciclo 56: se refuerza transferencia lateral por patrones reutilizables, no por contenido específico."
    ]
  }
}