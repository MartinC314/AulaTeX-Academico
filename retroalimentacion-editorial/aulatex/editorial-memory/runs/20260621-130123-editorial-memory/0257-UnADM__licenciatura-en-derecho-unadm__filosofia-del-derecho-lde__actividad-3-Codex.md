{
  "summary": [
    "Se consolida memoria lateral reutilizable de actividad-1 hacia actividad-3 sin copiar contenido específico.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se aplica deduplicación lossless y no regresión de reglas útiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar salidas heredadas de herramientas como antecedente editorial provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
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
    "Heredar patrones válidos de actividad-1 sin copiar redacción literal.",
    "No transferir conclusiones específicas de un nodo hermano a otro.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir evidencia académica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin migración total.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar en .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib puede no corresponder a actividad-3 si fue curado para otra semana."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones institucionales, estructurales y de calidad reutilizables.",
    "No propagar bibliografía exclusiva de un hermano como obligatoria para otro.",
    "Propagar supuestos siempre etiquetados como supuestos.",
    "Mantener compresión por unión y deduplicación sin pérdida semántica.",
    "Aplicar normalización manual cuando existan incidencias de parseo en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido para actividad-3.",
    "Confirmar rúbrica específica de evaluación de actividad-3.",
    "Confirmar fuentes obligatorias de la semana de actividad-3.",
    "Confirmar si actividad-3 usa bibliografía base o requiere .bib específico.",
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
      "Problema jurídico o social bien delimitado.",
      "Conceptos y fuentes pertinentes al objetivo.",
      "Análisis propio con postura académica.",
      "Cierre con conclusión jurídica transferible.",
      "Rastreabilidad completa entre afirmación y evidencia."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar consistencia editorial entre actividades de la misma asignatura.",
      "Preservar calidad institucional en producción LaTeX jurídica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Supuestos marcados cuando falte evidencia local.",
      "Citas verificables en afirmaciones relevantes.",
      "Cierre aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable",
        "Supuestos marcados"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicabilidad]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige evidencia verificable y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay trazabilidad editorial confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se construye desde una delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: propósito y ejes de trabajo estables.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes con variantes ortográficas.",
      "Se mantuvieron reglas de no regresión y normalización previa.",
      "Se reforzó transferencia lateral solo de patrones reutilizables.",
      "Se evitó migrar bibliografía o conclusiones específicas de actividad-1 a actividad-3.",
      "Se añadieron supuestos explícitos donde faltan datos locales."
    ]
  }
}