{
  "summary": [
    "Se consolida memoria de materia desde Actividad 1 con abstracción ascendente y deduplicación lossless.",
    "Se preservan reglas útiles previas sin regresión y se normalizan variantes duplicadas.",
    "Se mantiene identidad UnADM, trazabilidad curricular y punto de entrada canónico en carpeta de materia.",
    "Se fijan ejes editoriales transferibles: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva riesgo de ingesta por salidas no JSON parseable y su tratamiento obligatorio."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción, tono y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica de entregables y memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento fuente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar trazabilidad de fuentes provisionales heredadas (Codex, GPT-Pro) hasta sustitución verificada. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el tipo de producto a la planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de la materia.",
    "Separar entregables por tipo en archivos dedicados: reporte y presentación."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado y pregunta guía explícita.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1 sin evidencia. [supuesto]",
    "Confirmar que el producto corresponde a la consigna específica de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Verificar correspondencia del producto con la consigna de actividad.",
    "Evitar regresión: no eliminar reglas útiles heredadas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tratar nombres anómalos del README como pendientes de corrección, no como canónicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con trazabilidad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, editorial/fuente o URL.",
    "No completar entradas truncadas del .bib sin verificación local. [supuesto]",
    "Mantener claves ya citadas para evitar roturas de compilación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Elevar al ancestro patrones editoriales y de calidad, no redacción literal de actividades.",
    "Propagar reglas generales cuando falte consigna textual específica.",
    "Reutilizar puertas de calidad institucional sin perder especificidad local.",
    "Registrar incidencias de ingesta no parseable como riesgo persistente y controlado.",
    "Transferir citas recurrentes y relaciones conceptuales como trazas de conocimiento."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para cerrar ambigüedad de formato. [supuesto]",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Determinar si filosofia-del-derecho-clean.bib se limita a Semana 7 o se reutiliza en otras actividades. [supuesto]",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019.",
    "Corregir definitivamente placeholders y nombres anómalos en README/programa analítico."
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
        "Carpeta de materia como punto de entrada canónico."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como detonante.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en entregables académicos sólidos.",
      "Asegurar claridad argumentativa, fundamento jurídico y aplicabilidad profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explícito.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explícito de [supuesto].",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Marco conceptual y normativo.",
      "Análisis crítico con postura propia.",
      "Síntesis conclusiva aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Problema-conceptos-evidencia-análisis-conclusión"
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
          "justification": "La interpretación sustenta la construcción de razones jurídicas."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar validez y consecuencias."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "El campo integra debate axiológico y normativo."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión exige sustento verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Archivos .bib locales: trazabilidad de claves y fuentes jurídicas.",
        "Memoria de Actividad 1: patrón editorial estable transferible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: se eleva patrón de Actividad 1 a materia sin copia literal.",
      "Ciclo 69: deduplicación semántica y normalización ortográfica sin pérdida.",
      "Ciclo 69: se preserva control de calidad de JSON parseable como puerta obligatoria.",
      "Ciclo 69: se mantiene política de fuentes provisionales con marca [supuesto].",
      "Ciclo 69: se refuerza trazabilidad entre consigna, .tex y .bib."
    ]
  }
}