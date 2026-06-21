{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza normalización estructurada y validación JSON estricta antes de propagar.",
    "Supuesto: la consigna local completa de Actividad 4 no está visible."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar extrapolar fuentes de otras semanas sin validación local.",
    "Confirmar que el producto entregado corresponde a la consigna de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificación correctos en español en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar rupturas de compilación.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivo del README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar rutas finales."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretación jurídica de Semana 7; validar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir patrones reutilizables, no redacción literal ni conclusiones específicas.",
    "Preservar reglas útiles previas y evitar regresiones.",
    "Aplicar unión y deduplicación semántica en nodos hermanos.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar tipo de producto requerido: reporte, presentación u otro.",
    "Confirmar rúbrica y criterios de evaluación específicos.",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si Actividad 4 reutiliza bibliografía existente o requiere .bib incremental."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro.",
        "Jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización obligatoria antes de propagar.",
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Conceptos y marco normativo con evidencia.",
      "Análisis propio con postura académica.",
      "Cierre con conclusión jurídica aplicable.",
      "Trazabilidad técnica y editorial en LaTeX y bibliografía."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar coherencia entre contenido, fuentes y formato.",
      "Garantizar transferibilidad profesional del razonamiento jurídico."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Distinción entre hechos, conceptos y argumentos.",
      "Citas explícitas para cada afirmación sustantiva.",
      "Supuestos marcados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar fuentes y desarrollar análisis propio.",
      "Fijar postura razonada.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Integridad académica",
        "Normalización estructurada",
        "Validación JSON",
        "Coherencia problema-evidencia-conclusión"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Coherencia problema-evidencia-conclusión",
          "kind": "develops",
          "justification": "Los ejes ordenan el argumento de inicio a cierre."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay propagación segura."
        },
        {
          "source": "Integridad académica",
          "target": "Coherencia problema-evidencia-conclusión",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo verificable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico: cinco ejes de trabajo estables.",
        "Historial: antecedentes de salidas no parseables requieren gate técnico estricto."
      ]
    },
    "reinforcement_log": [
      "Se eliminó duplicación superficial y se conservó contenido útil.",
      "Se reforzaron reglas técnicas de parseo y normalización.",
      "Se preservó separación entre patrón reusable y contenido específico de actividad hermana.",
      "Se añadieron supuestos explícitos donde falta evidencia local."
    ]
  }
}