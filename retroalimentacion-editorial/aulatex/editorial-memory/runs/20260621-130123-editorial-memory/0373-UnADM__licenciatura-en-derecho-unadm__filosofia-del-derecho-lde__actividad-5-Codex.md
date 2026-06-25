{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 5 sin copiar redacción ni conclusiones específicas.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa y compuertas de calidad ya validadas.",
    "Se aplica deduplicación lossless y se corrigen duplicados semánticos del destino.",
    "Se mantiene el control de normalización JSON como requisito previo de propagación recursiva.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva plantilla editorial base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmaciones, evidencia y conclusión en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta alcance, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 5.",
    "Aplicar revisión manual extra si existe historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7; confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y relaciones conceptuales.",
    "Evitar copiar conclusiones específicas y bibliografía exclusiva entre nodos hermanos.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar deduplicación por unión semántica sin recortar contenido válido.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar si el formato principal es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 5 requiere bibliografía propia o reutiliza parte de la base existente."
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
      "Transformar la planeación semanal en productos académicos con fundamento jurídico, evidencia y cierre argumentativo.",
      "Asegurar continuidad editorial entre actividades sin perder especificidad local.",
      "Garantizar trazabilidad entre consigna, desarrollo, fuentes y conclusión."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales sin ornamentación.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falten datos.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> postura justificada.",
      "Conclusión -> transferencia a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib",
        "Bibliografía base",
        "Bibliografía específica de actividad"
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
          "justification": "La pauta institucional define tono, forma y criterios mínimos del entregable."
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
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna concreta."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de ciclos: incidentes de salida no parseable obligan compuerta de estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se unifican reglas duplicadas por forma y acento sin pérdida semántica.",
      "Ciclo 6: se refuerza transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 6: se mantiene alerta de parseo y verificación local de fuentes heredadas.",
      "Ciclo 6: se preserva separación entre bibliografía base y bibliografía por actividad."
    ]
  }
}