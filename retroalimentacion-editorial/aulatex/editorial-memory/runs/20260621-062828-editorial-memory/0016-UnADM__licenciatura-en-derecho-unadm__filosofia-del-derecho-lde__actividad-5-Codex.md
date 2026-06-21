{
  "summary": [
    "Memoria lateral consolidada para Actividad 5 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular de Derecho.",
    "Se refuerzan ejes troncales: problema, conceptos, evidencia, análisis y conclusión jurídica.",
    "Se mantiene normalización JSON obligatoria antes de propagación.",
    "Se transfiere solo patrón reusable; no se copian conclusiones ni bibliografía exclusiva de Actividad 1.",
    "Se mantienen supuestos explícitos cuando falta consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofía del Derecho.",
    "Conservar ubicación curricular: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar memorias de modelos previos como provisionales, no como fuente académica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia en cada bloque.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Si falta instrucción local, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto responde a la consigna y no solo enumera conceptos.",
    "Aplicar revisión manual extra en memoria con historial de parseo defectuoso."
  ],
  "latex_rules": [
    "Usar acentuación y codificación en español de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas para evitar compilación rota.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib hasta verificación local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente semanal y confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión y deduplicación; evitar regresiones editoriales.",
    "Transferir patrones, no redacción literal ni conclusiones específicas.",
    "No propagar fuentes provisionales como evidencia académica.",
    "Mantener bandera de riesgo histórico por incidentes de salida no parseable."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto.",
    "Confirmar rúbrica específica para calibrar profundidad argumentativa.",
    "Confirmar si Actividad 5 exige reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si la bibliografía de Semana 7 aplica total o parcialmente a Actividad 5."
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
      "Problema jurídico o social bien delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio sustentado en evidencia.",
      "Cierre con conclusión jurídica aplicable.",
      "Normalización estructural obligatoria antes de propagar."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener continuidad editorial entre actividades hermanas sin copiar contenido específico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y explícitas.",
      "Supuestos marcados cuando falten datos.",
      "Citas verificables con correspondencia .bib.",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> postura propia.",
      "Regla general -> aplicación al caso -> implicación práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Conceptos y doctrina",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La pauta institucional fija tono, rigor y formato."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis depende de una pregunta jurídica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere respaldo comprobable."
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
          "justification": "La base orienta; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README establece identidad UnADM y conclusión jurídica propia.",
        "Programa analítico define ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de incidentes confirma gate de JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicación integral sin pérdida de reglas válidas.",
      "Ciclo 16: se refuerza transferencia lateral por patrones reutilizables.",
      "Ciclo 16: se mantiene separación entre memoria editorial y fuentes académicas.",
      "Ciclo 16: se conserva política de supuestos explícitos por falta de consigna local."
    ]
  }
}