{
  "summary": [
    "Se consolida en la materia la memoria ascendente de Actividad 1 sin regresión.",
    "Se preservan ejes editoriales transferibles: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene normalización obligatoria para insumos no JSON parseable antes de propagar.",
    "Se refuerza trazabilidad entre consigna, producto .tex y soporte .bib.",
    "Se conserva identidad UnADM con alineación curricular verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios académicos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de materia como entrada canónica editorial.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el tipo de producto a la planeación semanal."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1. [supuesto]",
    "Validar que el entregable corresponda a la consigna específica de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas anómalas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Registrar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de materia vs bibliografía específica de actividad.",
    "No completar entradas truncadas sin verificación local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales verificadas en README, programa analítico y .bib local.",
    "Elevar patrones editoriales, no redacciones literales del nodo hijo.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Preservar trazabilidad de citas recurrentes al subir al ancestro.",
    "Registrar incidencias de ingesta no parseable como riesgo, sin perder reglas útiles."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para fijar producto final.",
    "Confirmar nombre canónico definitivo del .bib de la materia.",
    "Determinar si filosofia-del-derecho-clean.bib se limita a Semana 7 o se integra parcialmente a base general. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019. [supuesto]",
    "Corregir definitivamente placeholders/tokens en README y programa analítico."
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
        "Materia como punto de entrada canónico."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Formación jurídica con análisis crítico del fenómeno normativo.",
      "Integración de teoría, marco normativo y argumentación aplicada.",
      "Producción académica con evidencia verificable y criterio propio."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos trazables.",
      "Garantizar consistencia entre problema, evidencia y conclusión jurídica.",
      "Sostener continuidad editorial entre actividades y nivel materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Postura propia explícita.",
      "Conclusión jurídica transferible.",
      "Marcado de supuestos cuando falte evidencia directa."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual-normativo.",
      "Analizar con postura propia.",
      "Sustentar con citas verificables.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Problema jurídico o social",
        "Evidencia verificable",
        "Conclusión jurídica transferible"
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
          "justification": "La interpretación provee criterios para construir argumentos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar razones y consecuencias normativas."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión válida exige sustento normativo verificable."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra discusión de validez, justicia y contenido axiológico."
        }
      ],
      "evidence": [
        "README de materia: identidad curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Actividad 1: patrón estable problema-conceptos-evidencia-análisis-conclusión.",
        "Bibliografía local: claves jurídicas recurrentes en UNAM/SCJN y normativa vigente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 97: se elevaron patrones reutilizables desde actividad al nivel materia.",
      "Ciclo 97: se deduplicaron reglas sin pérdida semántica.",
      "Ciclo 97: se preservaron controles de calidad de parseo y normalización.",
      "Ciclo 97: se mantuvo trazabilidad de citas y conceptos recurrentes."
    ]
  }
}