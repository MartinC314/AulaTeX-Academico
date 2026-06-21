{
  "summary": [
    "Se refuerza memoria lateral entre actividades con deduplicación lossless y sin recorte semántico.",
    "Se preservan ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene identidad UnADM y ubicación curricular verificable desde README y programa analítico.",
    "Se conserva gate crítico: no propagar si no hay JSON parseable y estructura mínima completa.",
    "Se transfiere solo patrón reutilizable; no se copian conclusiones específicas ni bibliografía exclusiva del nodo hermano.",
    "Supuesto: falta consigna y rúbrica local de Actividad 5; se mantiene plantilla base con preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con criterio propio.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5 sin romper reglas troncales.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte información de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilizar.",
    "Aplicar revisión manual extra en nodos con historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Corregir rutas o nombres con caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib, por Slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente temático de otra semana hasta confirmación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Aplicar unión y deduplicación sin eliminar reglas útiles previas.",
    "Propagar solo patrones generales cuando falte consigna textual local.",
    "Mantener bandera de riesgo histórico por salidas no parseables previas.",
    "No propagar como académica ninguna fuente marcada como provisional de memoria."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar formato exigido: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 usa bibliografía propia o reutiliza base existente.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura."
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
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Garantizar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falten datos.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Ejes editoriales troncales",
        "Consistencia cita-.bib",
        "Bibliografía base vs específica"
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
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, integridad y forma del producto."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-.bib",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "La conclusión jurídica exige respaldo verificable."
        },
        {
          "source": "Bibliografía base vs específica",
          "target": "Pertinencia de Actividad 5",
          "kind": "depends_on",
          "justification": "Evita reutilización automática de fuentes no alineadas."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de parseo obliga gate técnico antes de propagación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 99: se consolidan reglas compartidas entre hermanos por analogía controlada.",
      "Se deduplican variantes repetidas y se conserva contenido útil sin pérdida.",
      "Se retienen supuestos abiertos por falta de consigna local verificable.",
      "Se excluye transferencia de conclusiones y bibliografía exclusiva de Actividad 1."
    ]
  }
}