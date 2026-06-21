{
  "summary": [
    "Se consolida memoria lateral para Actividad 5 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM, ubicación curricular y punto de entrada canónico de asignatura.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene gate crítico: no propagar sin JSON parseable y estructura mínima completa.",
    "Se conserva regla de transferencia: mover patrones reutilizables, no copiar conclusiones ni bibliografía exclusiva del hermano.",
    "Supuesto: falta consigna y rúbrica local de Actividad 5; se mantiene plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal académico y precisión jurídica.",
    "Alinear cada entrega con UnADM y Licenciatura en Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Alinear forma del entregable al producto pedido en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de relleno.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar memoria no estructurada hasta normalización manual.",
    "Comprobar que el producto responde a la consigna y no solo resume."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos si README contiene tokens sin expandir.",
    "Resolver marcadores tipo $(@{...}.Slug) antes de fijar rutas canónicas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente usadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente de otra semana hasta confirmación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Preservar reglas útiles previas; agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación semántica, no recorte.",
    "Mantener bandera histórica de riesgo por incidentes de parseo.",
    "Transferir identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Si falta dato local, propagar pregunta abierta en lugar de contenido inventado."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar archivo .bib canónico final de la asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5.",
    "Confirmar corrección de rutas con caracteres anómalos en README."
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
      "Resolver un problema jurídico con estructura argumentativa verificable.",
      "Conectar conceptos y marco normativo con análisis propio.",
      "Cerrar con conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminación específica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Postura propia sustentada.",
      "Supuestos marcados cuando falte información.",
      "Control formal de estructura antes de propagar."
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
          "target": "Estructura argumentativa",
          "kind": "supports",
          "justification": "La pauta institucional define forma, tono y exigencia de cierre jurídico."
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
          "justification": "Sin parseo correcto no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta el curso; la específica responde a la consigna concreta."
        },
        {
          "source": "Actividad 1",
          "target": "Actividad 5",
          "kind": "develops",
          "justification": "Se transfieren patrones estables, no redacción ni conclusiones particulares."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de parseo exige gate de normalización estructural.",
        "Token Slug sin expandir en README justifica validación de rutas y .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 73: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 73: se reforzó control de JSON parseable como prerequisito de propagación.",
      "Ciclo 73: se mantuvo separación entre bibliografía base y bibliografía específica.",
      "Ciclo 73: se preservó continuidad institucional y curricular entre nodos hermanos.",
      "Ciclo 73: se conservaron supuestos abiertos por falta de consigna local verificable."
    ]
  }
}