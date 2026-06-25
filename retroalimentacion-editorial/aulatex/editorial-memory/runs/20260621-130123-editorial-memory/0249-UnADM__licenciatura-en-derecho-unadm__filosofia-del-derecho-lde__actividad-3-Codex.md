{
  "summary": [
    "Se consolida refuerzo lateral para actividad-3 con transferencia reusable desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes editoriales estables: problema, conceptos y fuentes, análisis propio y conclusión jurídica.",
    "Se aplica deduplicación lossless sin eliminar reglas útiles previas.",
    "Se mantiene política de supuestos cuando falte consigna local de actividad-3.",
    "Se corrige como supuesto la aplicabilidad de bibliografía depurada de Semana 7 a actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Registrar incidencias de parseo como metadato técnico, no como evidencia académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia con README y programa analítico."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "No asumir consigna, semana o formato de actividad-3 sin evidencia local.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar como supuesto cualquier diferencia específica de actividad-3 hasta confirmación oficial."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir fuentes académicas, normativas, jurisprudenciales y antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya usadas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos antes de referenciarlos.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes efectivamente citadas en la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; confirmar aplicabilidad a actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nodos hermanos solo patrones generales reutilizables.",
    "No propagar conclusiones específicas ni bibliografía exclusiva entre hermanos.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Conservar bandera de riesgo cuando exista historial de salida no estructurada.",
    "Propagar supuestos siempre etiquetados como supuestos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega de actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 reutiliza bibliografía depurada de Semana 7 o requiere .bib propio.",
    "Confirmar archivo .tex principal canónico para actividad-3."
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
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Asegurar trazabilidad editorial entre objetivo, desarrollo y cierre.",
      "Mantener continuidad institucional sin perder especificidad por actividad."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas con orden lógico.",
      "Afirmaciones relevantes con cita verificable.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo congruente -> cierre transferible."
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
        "filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable entre nodos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico: propósito y ejes de trabajo.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: transferencia lateral controlada desde actividad-1 a actividad-3.",
      "Se preservaron reglas institucionales, estructurales y de calidad sin recorte.",
      "Se deduplicaron variantes ortográficas y acentuales sin pérdida de contenido.",
      "Se mantuvieron supuestos abiertos donde falta consigna local.",
      "Se evitó migrar contenido específico no reusable entre nodos hermanos."
    ]
  }
}