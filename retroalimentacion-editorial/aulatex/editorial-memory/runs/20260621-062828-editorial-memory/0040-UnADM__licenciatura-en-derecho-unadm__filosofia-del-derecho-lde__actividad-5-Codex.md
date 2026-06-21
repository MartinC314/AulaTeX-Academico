{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y ubicación curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se conservan ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva de un nodo hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular cada entrega a Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otras semanas sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falten instrucciones locales."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar manualmente memoria con historial de incidentes de parseo.",
    "Comprobar que el producto responde a la consigna y no solo resume conceptos."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente consultadas y citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a otra actividad/semana; verificar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener unión y deduplicación sin recorte semántico.",
    "Preservar reglas útiles previas; agregar solo mejoras verificables.",
    "Propagar patrones generales cuando falte consigna textual local.",
    "No propagar como académicas fuentes provisionales de memoria técnica.",
    "Mantener bandera de riesgo por incidentes históricos de parseo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica específica de evaluación de Actividad 5.",
    "Confirmar si el producto requerido es reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar pertinencia de bibliografía limpia de Semana 7 para Actividad 5.",
    "Supuesto: README mantiene tokens sin expandir; validar rutas canónicas."
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
      "Conceptos y marco normativo o doctrinal pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico sólido.",
      "Asegurar trazabilidad entre consigna, desarrollo y cierre.",
      "Sostener consistencia institucional, argumentativa y técnica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales sin ornamento.",
      "Supuestos explícitos cuando falte información.",
      "Citas trazables y cierre con criterio propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Transferencia a práctica profesional."
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
          "justification": "La pauta institucional define tono y forma del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay análisis jurídico pertinente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La transferencia confiable exige estructura parseable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta la materia; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de ciclos: incidentes de parseo obligan gate técnico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 40: deduplicación de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 40: se preservan ejes troncales heredados de Actividad 1 sin copiar contenido específico.",
      "Ciclo 40: se refuerza distinción entre bibliografía base y específica.",
      "Ciclo 40: se mantiene control de JSON parseable como prerrequisito de propagación."
    ]
  }
}