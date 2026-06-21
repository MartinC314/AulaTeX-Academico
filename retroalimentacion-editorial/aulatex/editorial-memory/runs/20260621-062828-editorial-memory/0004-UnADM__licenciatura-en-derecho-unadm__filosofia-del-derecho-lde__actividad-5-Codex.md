{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM y contexto curricular de Filosofía del Derecho.",
    "Se refuerzan ejes editoriales recurrentes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene gate estricto de normalización JSON antes de propagación recursiva.",
    "Se limita transferencia a patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva de Actividad 1.",
    "Se marca como supuesto la falta de consigna y rúbrica local de Actividad 5."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear contenido con UnADM y Licenciatura en Derecho.",
    "Vincular actividad a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales, no como fuentes académicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en cada bloque.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear estructura al producto real solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si falta información de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar salidas no estructuradas antes de reutilización recursiva.",
    "Comprobar que el producto responde al problema y no solo enumera conceptos."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin necesidad editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres canónicos de archivos cuando README tenga tokens sin expandir.",
    "Resolver marcadores tipo $(@{...}.Slug) antes de cerrar rutas finales."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar campos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación sin pérdida semántica.",
    "Mantener bandera de riesgo histórico por incidentes de parseo.",
    "En saltos entre hermanos, transferir patrones, no contenido conclusivo local.",
    "Si falta consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta enunciado textual de Actividad 5; confirmar producto exacto.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar si el formato requerido es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5."
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
      "Conceptos y marco normativo/doctrinal pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar coherencia entre consigna, argumento y cierre profesional."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Postura personal sustentada.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "cpeum2026",
        "LeyGeneralVictimas"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Problema jurídico",
          "kind": "supports",
          "justification": "Define tono, rigor y encuadre del planteamiento."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica exige respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a consigna local."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial reporta incidentes de salida no parseable; se mantiene control de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicación de reglas repetidas en destino y origen.",
      "Ciclo 4: refuerzo lateral de patrones reutilizables entre actividades hermanas.",
      "Ciclo 4: preservación de gates de calidad y parseo como regla no negociable.",
      "Ciclo 4: mantenimiento de supuestos abiertos por falta de consigna local verificable."
    ]
  }
}