{
  "summary": [
    "Se refuerza memoria lateral de Actividad 5 con patrones reutilizables de Actividad 1.",
    "Se preserva identidad UnADM y ubicación curricular validada en README y programa analítico.",
    "Se mantiene compresión lossless por deduplicación y unión de reglas sin recorte útil.",
    "Se conserva regla crítica: no propagar si la salida no es JSON parseable.",
    "Se evita copiar conclusiones específicas o bibliografía exclusiva entre actividades hermanas.",
    "Supuesto: falta consigna y rúbrica local de Actividad 5; se mantiene estructura base verificable."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y jurídico-académico.",
    "Vincular toda entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica de contexto y fuentes.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "No usar trazas de modelo como fuente académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5 sin romper reglas troncales de asignatura.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta información operativa, registrar supuesto y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación cuando la salida no sea JSON parseable.",
    "Validar presencia de estructura mínima completa antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Revisar manualmente memoria con historial de incidentes de parseo.",
    "Rechazar salidas no estructuradas aguas abajo."
  ],
  "latex_rules": [
    "Usar acentos y codificación española consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib; verificar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en la actividad.",
    "No inventar referencias ni metadatos.",
    "Mantener metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como posible archivo temático de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y verificadas.",
    "Preservar reglas útiles previas; agregar solo mejoras comprobables.",
    "Aplicar deduplicación semántica antes de transferir a nodos hermanos.",
    "No transferir redacción literal ni conclusiones específicas de otra actividad.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos.",
    "Cuando falte dato local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar si el entregable es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 aplica o no a Actividad 5.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
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
      "Conceptos y marco normativo o doctrinal pertinente.",
      "Evidencia verificable con trazabilidad.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Mantener continuidad editorial entre actividades sin copiar contenido específico.",
      "Garantizar calidad técnica, argumentativa y documental."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos marcados cuando falte dato.",
      "Cierre con aplicación profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia cita-.bib",
        "Supuestos explícitos"
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
          "justification": "Define tono, formato y criterio académico."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis parte de una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere respaldo trazable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta, la específica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial del nodo exige gate estricto de JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 34: se consolidan reglas hermanas reutilizables sin copiar contenido específico.",
      "Ciclo 34: se depuran duplicados y se preserva totalidad normativa útil.",
      "Ciclo 34: se mantiene prioridad de normalización estructurada previa a propagación.",
      "Ciclo 34: se refuerza separación entre bibliografía base y bibliografía por actividad."
    ]
  }
}