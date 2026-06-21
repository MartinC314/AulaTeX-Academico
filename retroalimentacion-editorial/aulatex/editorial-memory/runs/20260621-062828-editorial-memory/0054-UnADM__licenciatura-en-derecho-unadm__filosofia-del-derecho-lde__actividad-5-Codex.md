{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 5 sin copiar contenido específico.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se deduplica memoria previa con compresión lossless por unión de reglas equivalentes.",
    "Supuesto: falta consigna local de Actividad 5; se mantiene estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Respetar ubicación curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia jurídica.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el desarrollo al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas de Actividad 1.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar memoria no estructurada hasta normalización.",
    "Evitar regresiones de reglas útiles ya consolidadas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar en repositorio."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; validar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir patrones reutilizables, no redacción literal ni conclusiones específicas.",
    "Aplicar unión y deduplicación semántica en nodos hermanos.",
    "Conservar traza de incidentes históricos de parseo como bandera de riesgo.",
    "Si falta consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar enunciado textual de Actividad 5.",
    "Confirmar rúbrica específica de evaluación para Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografía de Semana 7 aplica o no a Actividad 5."
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
      "Problema jurídico como punto de partida.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con cita.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos jurídicos sólidos.",
      "Asegurar trazabilidad entre consigna, argumentación y cierre.",
      "Mantener continuidad editorial entre actividades hermanas sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre inicial breve y preciso.",
      "Secciones funcionales y explícitas.",
      "Postura propia sustentada.",
      "Uso explícito de supuestos cuando falte información."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Estructura de actividad jurídica",
        "Evidencia verificable",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Transferencia lateral controlada"
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
          "target": "Estructura de actividad jurídica",
          "kind": "supports",
          "justification": "La pauta institucional define tono, rigor y forma del entregable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La validez argumentativa depende de respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay propagación confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta continuidad; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de parseo obliga gate estricto de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 54: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 54: se refuerza transferencia por patrones, no por copia literal entre hermanos.",
      "Ciclo 54: se mantiene bandera de riesgo por incidentes previos de JSON no parseable.",
      "Ciclo 54: se conservan supuestos abiertos por ausencia de consigna local verificable."
    ]
  }
}