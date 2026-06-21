{
  "summary": [
    "Se refuerza continuidad editorial entre actividades hermanas sin copiar contenido específico.",
    "Se preserva identidad UnADM y marco curricular: Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene regla crítica: normalizar y validar JSON antes de propagación recursiva.",
    "Se consolidan ejes troncales reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Supuesto: falta consigna local de Actividad 5; se conservan reglas base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear toda actividad con identidad institucional UnADM.",
    "Vincular explícitamente el trabajo a Licenciatura en Derecho y Filosofía del Derecho.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas desde Actividad 1.",
    "No reutilizar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar aguas abajo.",
    "Exigir respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas sin normalización previa.",
    "Comprobar que el producto responde a la consigna y no solo al tema general."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en el .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos, referencias rotas ni rutas anómalas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como contextual a Semana 7 hasta confirmar uso en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo reglas generales reutilizables.",
    "No transferir redacción literal, conclusiones concretas ni bibliografía exclusiva de un hermano.",
    "Aplicar unión y deduplicación lossless; evitar recorte semántico.",
    "Mantener bandera histórica de riesgo por salidas no parseables en ciclos previos.",
    "Agregar solo mejoras verificables contra README y programa analítico."
  ],
  "open_questions": [
    "Supuesto: falta enunciado textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica de evaluación de Actividad 5 para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 5 requiere reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si fuentes de Semana 7 son pertinentes para Actividad 5."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Carpeta de asignatura como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 1, bloque 2, obligatoria, 8 créditos",
        "Asignatura: Filosofía del Derecho"
      ]
    },
    "essence": [
      "Resolver un problema jurídico con fundamento",
      "Usar conceptos y marco normativo pertinentes",
      "Sostener análisis propio con evidencia verificable",
      "Entregar un producto alineado a planeación semanal",
      "Concluir con transferencia a práctica profesional"
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos",
      "Estandarizar calidad jurídica y trazabilidad de evidencia",
      "Preservar identidad institucional en todas las actividades"
    ],
    "style_markers": [
      "Encuadre breve al inicio",
      "Secciones funcionales y explícitas",
      "Postura personal sustentada",
      "Supuestos marcados cuando falte información"
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión",
      "Afirmación -> evidencia -> inferencia jurídica",
      "Contraste doctrinal breve -> toma de postura -> aplicación práctica"
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
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional define tono, forma y criterios mínimos."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis se construye desde una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere trazabilidad de fuentes."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta curso; la específica responde a cada consigna."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial de parseo exige gate técnico antes de propagación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 47: deduplicación de reglas repetidas sin pérdida semántica.",
      "Ciclo 47: transferencia lateral restringida a patrones reutilizables.",
      "Ciclo 47: se evita copiar conclusiones o bibliografía exclusiva de Actividad 1.",
      "Ciclo 47: se mantiene control estricto de JSON parseable antes de propagación."
    ]
  }
}