{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM y ubicación curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene gate crítico: no propagar si la salida no es JSON parseable.",
    "Se mantiene regla de marcar supuestos cuando falte consigna local de Actividad 5.",
    "Se limita transferencia a patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva de un hermano."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en todo entregable.",
    "Alinear contenido con Filosofía del Derecho de la Licenciatura en Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Sostener enfoque jurídico-académico con claridad y precisión.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia en bloques claros.",
    "Alinear estructura al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta dato operativo, registrar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar que el esquema requerido esté completo antes de guardar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar contradicciones con reglas institucionales vigentes.",
    "Aplicar revisión manual extra en memorias con historial de parseo fallido."
  ],
  "latex_rules": [
    "Usar acentos y codificación española de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir en README y programa analítico antes de automatizar nombres.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta confirmación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura completa.",
    "Reutilizar reglas troncales de identidad, estructura y calidad sin bajar especificidad.",
    "Aplicar unión y deduplicación; no eliminar reglas útiles previas.",
    "Transferir patrones, no redacción literal ni cierres sustantivos del hermano.",
    "Mantener bandera histórica de riesgo por incidentes de salida no parseable."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 5 exige reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib por tokens sin expandir en README.",
    "Confirmar si la bibliografía de Semana 7 aplica total, parcial o no aplica a Actividad 5."
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
      "Problema jurídico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Mantener continuidad editorial entre actividades sin copiar contenido específico.",
      "Garantizar calidad estructural y argumentativa antes de propagación."
    ],
    "style_markers": [
      "Inicio con encuadre breve.",
      "Secciones funcionales, no ornamentales.",
      "Postura propia sustentada en evidencia.",
      "Uso explícito de supuestos ante vacíos de consigna."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con transferencia a práctica profesional."
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
          "justification": "Define tono, forma y estándar de integridad."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida exige respaldo."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo correcto no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad académica.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial documenta incidentes de salida no parseable.",
        "Tokens sin expandir en README justifican validación manual de nombres."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicación integral de reglas repetidas en destino.",
      "Ciclo 13: refuerzo lateral de ejes troncales sin copiar conclusiones de Actividad 1.",
      "Ciclo 13: mantenimiento de gates de parseo JSON y consistencia cita-.bib.",
      "Ciclo 13: consolidación de supuestos explícitos por falta de consigna local completa."
    ]
  }
}