{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 5 con deduplicación lossless.",
    "Se preservan reglas troncales reutilizables: identidad UnADM, estructura argumentativa, control de calidad y normalización JSON.",
    "Se mantiene restricción de no transferir redacción literal, conclusiones específicas ni bibliografía exclusiva entre actividades hermanas.",
    "Supuesto: falta consigna y rúbrica local de Actividad 5; se conserva plantilla editorial base con preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia jurídica.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta información operativa, registrar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responda a la consigna local y no a otra actividad.",
    "Aplicar revisión manual extra en memoria con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Supuesto: .bib canónico esperado filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en la actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar solo patrones reutilizables; no contenido específico entre hermanos.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin recorte semántico.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar si el formato requerido es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si bibliografía de Semana 7 aplica o no a Actividad 5."
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
      "Conceptos y marco normativo/doctrinal pertinentes.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, desarrollo, evidencia y cierre.",
      "Sostener continuidad editorial entre actividades sin contaminar contenido específico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales.",
      "Supuestos explícitos cuando falten datos.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> postura propia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, formato y criterios mínimos del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida exige respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema, conceptos, fuentes, análisis y cierre.",
        "Historial: incidentes de parseo obligan gate estricto de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicación integral aplicada sin pérdida de reglas útiles.",
      "Ciclo 20: se reforzó transferencia lateral controlada entre nodos hermanos.",
      "Ciclo 20: se bloquearon traslados de contenido específico no reutilizable.",
      "Ciclo 20: se mantuvieron supuestos abiertos por falta de consigna local verificable."
    ]
  }
}