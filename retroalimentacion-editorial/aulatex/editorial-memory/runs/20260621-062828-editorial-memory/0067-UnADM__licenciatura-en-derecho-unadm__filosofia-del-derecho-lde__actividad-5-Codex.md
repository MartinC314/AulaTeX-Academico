{
  "summary": [
    "Se refuerza continuidad editorial entre actividades hermanas sin copiar contenido específico.",
    "Se preservan reglas válidas de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se consolida deduplicación lossless y se eliminan ambigüedades de transferencia entre actividades.",
    "Se mantiene como obligatorio el control de JSON parseable antes de cualquier propagación.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene plantilla base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM y enfoque jurídico-académico.",
    "Vincular siempre a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como insumo técnico provisional, no como fuente académica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmación, evidencia e inferencia.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear el formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5.",
    "Evitar texto solo descriptivo; incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "No arrastrar conclusiones ni bibliografía exclusiva de Actividad 1.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de guardar o propagar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar contradicciones con reglas institucionales consolidadas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir tokens sin expandir en rutas o nombres de archivo del README.",
    "Supuesto: nombre canónico esperado del .bib es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Agregar al .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Mantener metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Confirmar pertinencia antes de reutilizar bibliografía de Semana 7 en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas reutilizables y verificadas.",
    "No transferir redacción literal ni conclusiones específicas entre hermanos.",
    "Mantener unión por deduplicación sin pérdida de reglas útiles previas.",
    "Aplicar normalización manual si aparece salida no estructurada en nodos vecinos.",
    "Conservar bandera histórica de riesgo por incidentes de parseo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico definitivo del archivo .bib en la asignatura.",
    "Confirmar qué fuentes de filosofia-del-derecho-clean.bib son pertinentes para Actividad 5."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos y trazables.",
      "Sostener continuidad editorial entre actividades sin contaminar especificidad local.",
      "Garantizar estructura, rigor argumentativo y utilidad profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falten datos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-.bib"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "La identidad institucional fija tono, rigor y formato."
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
          "justification": "La conclusión sólida requiere soporte trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        }
      ],
      "evidence": [
        "README: exige identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: define ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de ciclos: incidentes de parseo obligan gate técnico estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 67: refuerzo lateral aplicado con analogía controlada entre hermanos.",
      "Se preservaron reglas troncales y se deduplicaron variantes redundantes.",
      "Se evitó transferencia de contenido específico de Actividad 1.",
      "Se añadieron validaciones explícitas de pertinencia bibliográfica por actividad."
    ]
  }
}