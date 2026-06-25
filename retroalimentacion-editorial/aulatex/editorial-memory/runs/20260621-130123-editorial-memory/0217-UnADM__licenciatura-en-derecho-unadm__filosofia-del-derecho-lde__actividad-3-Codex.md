{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, análisis propio, conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se aplica deduplicación lossless sin eliminar reglas útiles previas."
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
    "Heredar solo patrones reutilizables entre actividades hermanas.",
    "No copiar redacción literal ni conclusiones específicas de otra actividad.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir consigna, semana o formato de actividad-3 sin evidencia local [supuesto]."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente usadas por la actividad.",
    "No inventar referencias ni usar memoria editorial como bibliografía académica.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib pertenece a Semana 7 y su uso en actividad-3 debe confirmarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales y de calidad sin perder especificidad local.",
    "Propagar solo reglas generales cuando falte consigna textual local.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresión por unión y deduplicación lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de actividad-3.",
    "Confirmar si actividad-3 usa bibliografía propia o reutiliza parcialmente la depurada."
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
      "Conceptos, normas y doctrina pertinentes con evidencia.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica.",
      "Normalización estructurada para memoria persistente."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos verificables.",
      "Asegurar coherencia editorial entre actividades de la misma asignatura.",
      "Sostener calidad técnica LaTeX y trazabilidad bibliográfica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico con criterio propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre transferible."
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
          "justification": "La pauta institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Normalización JSON",
          "target": "Bibliografía verificable",
          "kind": "depends_on",
          "justification": "La trazabilidad automática requiere estructura parseable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis debe responder a una pregunta delimitada."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El cierre depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: ejes de trabajo y propósito de transformación del producto.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicación completa de reglas repetidas.",
      "Ciclo 11: preservación de reglas útiles previas sin recorte.",
      "Ciclo 11: transferencia lateral controlada sin copiar contenido específico de actividad-1.",
      "Ciclo 11: fortalecida política de supuestos para datos no confirmados."
    ]
  }
}