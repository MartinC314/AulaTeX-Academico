{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstracción ascendente y deduplicación lossless.",
    "Se preservan reglas útiles previas sin regresión y se normalizan variantes duplicadas.",
    "Se mantiene identidad UnADM, trazabilidad curricular y control de ingesta no estructurada.",
    "Se elevan patrones reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redacción y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencias provisionales heredadas de Codex y GPT-Pro hasta sustitución verificada. [supuesto]",
    "No eliminar reglas heredadas de control de calidad y normalización."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de la materia.",
    "Separar entregables por tipo: reporte y presentación en archivos dedicados.",
    "Tratar nombres anómalos y placeholders del README como pendientes, no como canon. [supuesto]"
  ],
  "activity_rules": [
    "Delimitar el problema jurídico o social al inicio de cada actividad.",
    "Integrar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Validar que el producto corresponda a la consigna específica de la actividad.",
    "No asumir que fuentes de semanas posteriores aplican automáticamente a actividad-1.",
    "Agregar fuentes específicas de actividad solo cuando sean verificables."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar coherencia curricular con README y programa analítico.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar en cada ciclo que no se eliminen reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves citadas sin migración completa.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Preservar rutas y nombres canónicos para evitar roturas de compilación.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en nombres de archivo antes de compilar.",
    "Mantener compatibilidad entre claves citadas y entradas disponibles en .bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con trazabilidad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Conservar y deduplicar entradas existentes sin pérdida de información.",
    "No completar entradas BibTeX truncadas sin verificación local.",
    "Tratar filosofia-del-derecho-clean.bib como depurado de apoyo mientras se confirma el canónico. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar al ancestro reglas generales y transferibles, no redacción literal de actividades.",
    "Mantener compresión por unión-deduplicación sin recorte semántico.",
    "Reusar puertas de calidad institucionales en nodos laterales de Derecho.",
    "Evitar propagar nombres de archivo anómalos hasta resolverlos localmente.",
    "Conservar trazabilidad de citas recurrentes al subir de actividad a materia.",
    "Aplicar normalización manual en ciclos con insumos no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 y su producto requerido. [supuesto]",
    "Confirmar rúbrica de evaluación específica para profundidad argumentativa. [supuesto]",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si actividad-1 reutiliza bibliografía existente o requiere .bib propio.",
    "Completar y verificar campos de scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Resolver definitivamente placeholders $(@{...}.Slug) en README y programa analítico."
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
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en entregables sólidos y trazables.",
      "Garantizar fundamento jurídico, claridad argumentativa e integridad académica.",
      "Sostener una memoria editorial persistente y reusable entre actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explícito de [supuesto].",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Analizar críticamente con postura propia.",
      "Concluir con aplicabilidad profesional.",
      "Verificar coherencia interna de principio a cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad actividad-.tex-.bib",
        "Normalización de insumos no estructurados"
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
          "justification": "La interpretación aporta base para justificar razones jurídicas."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar validez, alcance y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra el debate entre validez normativa y dimensión axiológica."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión profesional exige respaldo normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: claves jurídicas recurrentes.",
        "Actividad-1: patrón problema-conceptos-evidencia-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicación integral de reglas repetidas y variantes ortográficas.",
      "Ciclo 7: transferencia ascendente de patrones argumentativos desde actividad-1 a materia.",
      "Ciclo 7: conservación explícita de reglas de normalización y no regresión.",
      "Ciclo 7: refuerzo de trazabilidad bibliográfica y control de placeholders.",
      "Ciclo 7: consolidación de citas recurrentes sin inventar fuentes."
    ]
  }
}