{
  "summary": [
    "Consolidar memoria de materia de Filosofía del Derecho con identidad UnADM y trazabilidad desde actividad-1.",
    "Aplicar compresión lossless por unión y deduplicación, sin regresión de reglas útiles.",
    "Mantener normalización obligatoria para insumos no JSON parseable antes de propagación.",
    "Preservar ejes editoriales nucleares: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción, formato y tono.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica de asignatura.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1. [supuesto]",
    "Validar que el producto corresponda exactamente a la consigna de cada actividad.",
    "Agregar solo bibliografía específica de actividad cuando sea verificable."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Confirmar preservación de reglas útiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas anómalas antes de consolidar canon de archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Registrar claves recurrentes y trazables sin duplicación semántica.",
    "No completar entradas truncadas sin verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Elevar al ancestro solo reglas generales y reutilizables validadas localmente.",
    "Propagar recursivamente después de validar JSON, estructura y trazabilidad de citas.",
    "Evitar propagar nombres de archivo anómalos hasta corregirlos localmente.",
    "Reusar puertas de calidad institucionales sin perder especificidad de la materia.",
    "Mantener etiqueta de compresión union-dedupe lossless en saltos posteriores."
  ],
  "open_questions": [
    "Confirmar nombre canónico definitivo del .bib de materia (filosofia-del-derecho.bib vs clean). [supuesto]",
    "Confirmar consigna textual exacta de actividad-1 para fijar producto primario.",
    "Confirmar si la bibliografía de Semana 7 se reutiliza formalmente en actividad-1. [supuesto]",
    "Completar y verificar la entrada scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Resolver definitivamente placeholders de Slug en README y programa analítico."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como disparador del análisis.",
      "Marco conceptual, normativo y doctrinal verificable.",
      "Análisis propio con postura académica explícita.",
      "Conclusión jurídica aplicable a práctica profesional.",
      "Trazabilidad editorial entre consigna, desarrollo y evidencia."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Estandarizar calidad argumentativa y técnica en LaTeX.",
      "Preservar memoria editorial persistente sin pérdida de conocimiento útil."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Uso explícito de evidencia.",
      "Marcado explícito de [supuesto] cuando falte verificación.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> análisis crítico -> conclusión transferible.",
      "Afirmación sustantiva -> cita verificable -> interpretación propia.",
      "Consigna específica -> formato correcto de entregable -> validación de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Ejes editoriales de cinco pasos"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación fundamenta la construcción de argumentos jurídicos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar normas, razones y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra discusión axiológica y validez normativa."
        },
        {
          "source": "Conclusión jurídica transferible",
          "target": "Marco normativo/doctrinal",
          "kind": "depends_on",
          "justification": "La conclusión válida exige soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Bib local: claves jurídicas recurrentes verificables.",
        "Memoria de actividad-1: patrón estable problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se preservó contenido válido sin recorte semántico.",
      "Se elevaron patrones reutilizables del nodo actividad al nodo materia.",
      "Se conservaron riesgos de ingesta no parseable como control operativo persistente.",
      "Se reforzó trazabilidad entre identidad institucional, estructura argumentativa y control bibliográfico."
    ]
  }
}