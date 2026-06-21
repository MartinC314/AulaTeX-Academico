{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM y marco curricular: Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantienen ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se refuerza control de normalización: no propagar si no hay JSON parseable y estructura mínima completa.",
    "Se transfieren solo patrones reutilizables desde Actividad 1; no se copian conclusiones ni bibliografía exclusiva."
  ],
  "identity_rules": [
    "Mantener tono formal académico, claro y jurídicamente preciso.",
    "Alinear contenido con UnADM y Licenciatura en Derecho.",
    "Vincular actividad a Filosofía del Derecho con contexto curricular oficial.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local.",
    "No usar fuentes de memoria técnica como fuentes académicas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Si falta consigna, usar estructura base y declarar supuestos."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Mantener trazabilidad entre instrucción, desarrollo y criterio de evaluación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema completo antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y entradas .bib.",
    "Rechazar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Aplicar revisión manual extra en memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Mantener acentos y codificación española consistentes en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir nombres de archivo con marcadores sin expandir antes de compilar.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por Slug en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Mantener metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 y requiere validación de pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Preservar reglas útiles previas; agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación semántica, no recorte.",
    "Transferir patrones de identidad, estructura, calidad y relaciones recurrentes.",
    "No transferir redacción literal ni conclusiones específicas entre hermanos.",
    "Mantener bandera de riesgo histórico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si las fuentes de Semana 7 son pertinentes para Actividad 5."
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
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos con fundamento jurídico y utilidad profesional.",
      "Asegurar consistencia editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos declarados cuando falte información.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura -> transferencia práctica."
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
          "justification": "La pauta institucional define tono, formato y estándar académico."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión sólida exige respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseabilidad no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial registra incidentes de salida no parseable y obliga gate estructural."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicación semántica aplicada en reglas repetidas.",
      "Ciclo 20: se preservan reglas institucionales y de calidad sin regresión.",
      "Ciclo 20: se agrega refuerzo de transferencia lateral controlada entre nodos hermano.",
      "Ciclo 20: se mantienen supuestos abiertos donde falta consigna local."
    ]
  }
}