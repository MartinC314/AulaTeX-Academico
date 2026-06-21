{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 5 sin copiar redacción ni conclusiones de Actividad 1.",
    "Se preserva identidad UnADM y ubicación curricular de Filosofía del Derecho.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene separación entre bibliografía base y bibliografía específica por actividad.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear todo contenido con UnADM y Licenciatura en Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar memorias de modelos previos como provisionales, no como fuentes académicas."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Alinear formato final al producto pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5 cuando esté disponible.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin validar pertinencia.",
    "Registrar supuesto operativo si falta dato de alcance."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de propagación recursiva.",
    "Verificar correspondencia del producto con la consigna local."
  ],
  "latex_rules": [
    "Usar acentos y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo obras realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra actividad/semana y requiere validación previa."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables, no contenido específico de Actividad 1.",
    "Aplicar deduplicación lossless por unión semántica y normalización.",
    "No degradar reglas útiles previas; solo añadir mejoras verificables.",
    "Mantener bandera de riesgo por incidentes históricos de parseo.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener trazabilidad de supuestos en saltos recursivos."
  ],
  "open_questions": [
    "Confirmar enunciado completo de Actividad 5.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar tipo de entregable requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib en la asignatura.",
    "Confirmar si fuentes de Semana 7 son pertinentes para Actividad 5.",
    "Supuesto: documentos con marcadores sin expandir en README requieren saneamiento."
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
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar consistencia entre identidad institucional, argumento y evidencia.",
      "Garantizar propagación confiable mediante estructura validable."
    ],
    "style_markers": [
      "Inicio con encuadre breve.",
      "Secciones funcionales sin relleno.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falte información.",
      "Cierre con aplicabilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Conclusión -> transferencia a práctica jurídica."
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
        "Bibliografía específica por actividad"
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
          "justification": "La pauta institucional fija tono, forma y criterio académico."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis parte de una pregunta jurídica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión exige respaldo trazable y pertinente."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia segura."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica por actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna puntual."
        },
        {
          "source": "Ejes troncales de asignatura",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "El salto lateral conserva patrones editoriales reutilizables."
        }
      ],
      "evidence": [
        "README define identidad UnADM e integridad académica.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial registra incidentes de salida no parseable y exige gate de estructura.",
        "README y programa muestran tokens Slug sin expandir; requiere saneamiento."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes de tono, estructura y calidad.",
      "Se preservaron reglas útiles previas sin recorte de capacidades.",
      "Se agregó refuerzo explícito de transferencia lateral controlada.",
      "Se retiró dependencia de conclusiones y bibliografía exclusivas del nodo hermano.",
      "Se mantuvieron supuestos abiertos donde faltan datos locales verificables."
    ]
  }
}