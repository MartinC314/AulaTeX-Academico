{
  "summary": [
    "Se consolida memoria lateral para Actividad 5 con deduplicación lossless y sin recorte útil.",
    "Se preserva identidad UnADM y contexto curricular: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene control obligatorio de normalización JSON parseable antes de propagación recursiva.",
    "Se evita transferir redacción literal, conclusiones específicas o bibliografía exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofía del Derecho.",
    "Conservar encuadre jurídico-académico con claridad y precisión.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local.",
    "Basar ubicación curricular en README y malla curricular institucional."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir explícitamente afirmaciones, evidencia y conclusión.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Si falta consigna, usar estructura base y declarar supuestos."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5 sin romper reglas troncales.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Mantener trazabilidad entre instrucción, desarrollo y criterio de evaluación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar respuestas no estructuradas antes de reutilización recursiva.",
    "Verificar que el producto responda al problema y no solo a resumen conceptual.",
    "Aplicar revisión manual extra si hay historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas para evitar ruptura de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Validar nombres reales de archivos cuando README tenga tokens sin expandir.",
    "Resolver o documentar tokens tipo $(@{...}.Slug) antes de automatizar rutas.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Agregar al .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente específico de otra semana hasta confirmar pertinencia.",
    "Conservar claves originales cuando ya están usadas en .tex."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales recurrentes.",
    "Evitar copiar conclusiones locales o bibliografía exclusiva entre hermanos.",
    "Aplicar unión y deduplicación sin perder reglas útiles previas.",
    "Mantener bandera histórica de riesgo por salidas no parseables en ciclos previos.",
    "Cuando falten datos locales, propagar preguntas abiertas y plantilla base."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica específica para ajustar profundidad argumentativa.",
    "Confirmar formato principal requerido: reporte, presentación o recurso visual.",
    "Confirmar nombre canónico final del .bib de asignatura.",
    "Confirmar si la bibliografía de Interpretación jurídica (Semana 7) aplica a Actividad 5.",
    "Supuesto: la continuidad editorial entre actividades se mantiene salvo instrucción contraria en consigna."
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
      "Problema jurídico como detonante.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Análisis propio con postura.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar continuidad editorial entre actividades sin contaminación de contenido específico.",
      "Proteger calidad formal, argumentativa y técnica del ecosistema LaTeX."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales, no ornamentales.",
      "Inferencias jurídicas explícitas.",
      "Uso explícito de supuestos cuando falte dato.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Transferencia del argumento a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
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
          "justification": "Define tono, forma y criterio académico del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere conflicto o pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez de la conclusión depende de respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Bibliografía específica de actividad",
          "target": "Bibliografía base",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la específica responde a la consigna local."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes: problema, conceptos, fuentes, análisis y cierre.",
        "Historial de parseo exige puerta de calidad estructural antes de propagar.",
        "Tokens Slug sin expandir en README justifican validación manual de rutas y .bib."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura total útil.",
      "Se reforzó separación entre patrones transferibles y contenido específico de actividad hermana.",
      "Se conservó control de supuestos para datos no visibles en consigna.",
      "Se mantuvo gate técnico-editorial de JSON parseable como condición de propagación."
    ]
  }
}