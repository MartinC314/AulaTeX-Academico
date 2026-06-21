{
  "summary": [
    "Se refuerza continuidad editorial entre actividades hermanas sin copiar contenido específico.",
    "Se preservan reglas troncales UnADM: identidad institucional, estructura argumentativa y control de calidad.",
    "Se consolida deduplicación lossless y se eliminan redundancias formales, no reglas útiles.",
    "Se mantiene control estricto de salida JSON parseable antes de propagación recursiva.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular explícitamente la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias heredadas de modelos como provisionales hasta verificación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir afirmación, evidencia e inferencia jurídica en cada bloque central.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar conclusiones específicas ni bibliografía exclusiva desde Actividad 1.",
    "Si falta instrucción, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revisión manual extra en memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No reutilizar automáticamente bibliografía de Semana 7 sin confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas y parseables.",
    "Preservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar unión con deduplicación semántica para compresión lossless.",
    "Evitar transferir redacción literal, conclusiones puntuales o citas exclusivas entre hermanos.",
    "Mantener bandera histórica de riesgo por salidas no estructuradas en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 5 exige reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar pertinencia de fuentes de Interpretación jurídica (Semana 7) para Actividad 5."
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
      "Problema jurídico o social como punto de partida.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Análisis propio del estudiante.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en entregables académicos sólidos.",
      "Sostener coherencia entre consigna, argumentación y evidencia.",
      "Garantizar calidad editorial y técnica en LaTeX y bibliografía."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales sin ornamento.",
      "Supuestos explícitos cuando falte información local.",
      "Cierre con postura jurídica propia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Transferencia del razonamiento a práctica profesional."
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
          "justification": "La identidad institucional define forma, tono y criterios mínimos."
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
          "justification": "La conclusión jurídica exige respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base",
          "target": "Bibliografía específica de actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial de parseo obliga gate técnico de estructura antes de propagar.",
        "README y programa muestran token Slug sin expandir; requiere saneamiento editorial."
      ]
    },
    "reinforcement_log": [
      "Se conservaron todas las reglas válidas del origen aplicables lateralmente.",
      "Se deduplicaron variantes ortográficas y repeticiones sin pérdida semántica.",
      "Se reforzó separación entre patrones reutilizables y contenido específico de actividad hermana.",
      "Se mantuvo trazabilidad de supuestos por ausencia de consigna local completa.",
      "Se fortaleció el vínculo entre calidad editorial y calidad técnica de compilación."
    ]
  }
}