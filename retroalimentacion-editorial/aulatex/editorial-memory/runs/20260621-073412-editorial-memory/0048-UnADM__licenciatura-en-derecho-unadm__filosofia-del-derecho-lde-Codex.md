{
  "summary": [
    "Se consolida la memoria de materia con abstracción ascendente desde Actividad 1.",
    "Se preservan reglas útiles previas sin regresión y con deduplicación lossless.",
    "Se fija normalización obligatoria para insumos no JSON parseable antes de propagar.",
    "Se mantienen ejes editoriales base: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza trazabilidad entre consigna, producto, archivo .tex y .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Alinear cada entrega al producto solicitado por planeación semanal.",
    "Mantener separación de productos: reporte, presentación, programa analítico y bibliografía."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores para actividades previas. [supuesto]",
    "Agregar fuentes específicas por actividad en .bib de materia cuando sean verificables.",
    "Confirmar correspondencia exacta del producto con la consigna de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilización.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar no eliminación de reglas útiles heredadas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir nombres/rutas anómalas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib canónico de la asignatura.",
    "Mantener trazables claves recurrentes y verificar entradas truncadas antes de completar. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Elevar al ancestro reglas transferibles de identidad, calidad y patrón argumentativo.",
    "No propagar literalidad de redacción de actividades; propagar patrones reutilizables.",
    "Aplicar unión-dedupe lossless en cada salto para evitar regresiones.",
    "Conservar trazabilidad de citas recurrentes al subir de actividad a materia.",
    "Si falta consigna textual, propagar solo reglas generales verificadas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para cerrar supuestos.",
    "Confirmar nombre canónico final del .bib de la materia.",
    "Confirmar si filosofia-del-derecho-clean.bib es solo de Semana 7 o reutilizable en otras actividades. [supuesto]",
    "Completar verificación de entrada truncada scjnIncapacidadResistencia2019. [supuesto]",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y verificables.",
      "Garantizar coherencia entre identidad UnADM, método jurídico y producción en LaTeX.",
      "Sostener una memoria editorial persistente, acumulativa y sin pérdida útil."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado explícito y estable.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de [supuesto] cuando aplica.",
      "Trazabilidad cita-evidencia-conclusión."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Marco conceptual y normativo.",
      "Evaluación crítica de argumentos y fuentes.",
      "Toma de postura propia fundamentada.",
      "Conclusión aplicable a práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad editorial .tex/.bib"
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
          "justification": "La interpretación aporta criterios para construir argumentos jurídicos sólidos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar validez, coherencia y consecuencias normativas."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión profesional exige fundamento verificable."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra el debate sobre validez, justicia y dimensión axiológica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Regla persistente: normalizar insumos no JSON parseable antes de propagación.",
        "Bibliografía local: claves jurídicas recurrentes y verificables en .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 48: se elevan patrones de Actividad 1 a materia sin copiar redacción literal.",
      "Ciclo 48: se deduplican reglas repetidas y se conserva cobertura útil total.",
      "Ciclo 48: se mantiene bloqueo por JSON no parseable como puerta de calidad crítica.",
      "Ciclo 48: se refuerza trazabilidad entre consigna, argumentación y evidencia bibliográfica."
    ]
  }
}