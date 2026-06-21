{
  "summary": [
    "Consolidar memoria de materia con abstracción ascendente desde Actividad 1.",
    "Preservar reglas útiles previas sin regresión y con deduplicación lossless.",
    "Mantener normalización estructurada obligatoria antes de cualquier propagación.",
    "Sostener ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Registrar salidas no JSON parseable como riesgo de ingesta, sin perder contenido útil."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redacción y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar trazabilidad de fuentes provisionales heredadas (Codex, GPT-Pro) hasta sustitución verificada. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el entregable al tipo de producto solicitado por la planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de la materia.",
    "No adoptar placeholders o nombres anómalos del README como canónicos. [supuesto]"
  ],
  "activity_rules": [
    "Delimitar problema jurídico o social al inicio de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1. [supuesto]",
    "Validar que el producto final corresponda a la consigna específica de la actividad.",
    "Elevar al nivel materia solo patrones reutilizables, no redacción literal de una actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Verificar correspondencia entre producto entregado y consigna de la actividad.",
    "Confirmar que no se eliminen reglas útiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrarlas sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Separar entregables por tipo en archivos .tex dedicados (reporte, presentación).",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas con caracteres anómalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "No completar entradas truncadas sin verificación local. [supuesto]",
    "Mantener trazabilidad de claves recurrentes ya validadas en la materia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir hacia ancestros identidad, patrones argumentativos y reglas de calidad reutilizables.",
    "Evitar propagar detalles locales no verificados como canon global. [supuesto]",
    "Mantener compresión por unión-deduplicación sin pérdida semántica.",
    "Aplicar normalización manual en ciclos con insumos no estructurados.",
    "Conservar trazabilidad conceptual y de citas recurrentes en saltos ascendentes."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para cerrar supuestos de formato.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Determinar si filosofia-del-derecho-clean.bib es auxiliar de semana o canon de materia. [supuesto]",
    "Verificar y completar entrada truncada scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Sustituir fuentes provisionales heredadas por fuentes verificadas locales."
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
        "Carpeta de materia como entrada canónica editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como disparador del análisis.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable con cita explícita.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables y útiles.",
      "Garantizar rigor argumentativo y verificabilidad de fuentes.",
      "Sostener continuidad editorial entre actividades y materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar críticamente con postura propia.",
      "Concluir con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Trazabilidad actividad-tex-bib",
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
          "justification": "La interpretación fundamenta la construcción de razones jurídicas."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar validez, coherencia y consecuencias."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión requiere soporte verificable en normas y doctrina."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia articula el debate entre validez normativa y axiología."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Bib local: claves recurrentes y verificables en UNAM/SCJN.",
        "Actividad 1: patrón reusable problema-conceptos-evidencia-análisis-conclusión."
      ]
    },
    "reinforcement_log": [
      "Se elevó al ancestro el patrón argumentativo reusable sin copiar redacción literal.",
      "Se reforzó regla de bloqueo por JSON no parseable y normalización previa.",
      "Se preservó trazabilidad curricular y bibliográfica con marca de supuestos.",
      "Se deduplicaron variantes manteniendo cobertura semántica completa."
    ]
  }
}