{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia de Derecho fiscal y tributario sin trasladar redacción literal.",
    "Se conserva identidad UnADM, estructura reusable y compresión lossless por unión-deduplicación.",
    "Se refuerzan gates de calidad: JSON válido, supuestos explícitos, trazabilidad de fuentes y consistencia .tex/.bib.",
    "Se consolida un cerebro editorial mínimo del destino con ADN argumentativo aplicable a actividades fiscales futuras.",
    "Supuesto: no se transfiere bibliografía temática de Filosofía como obligatoria en Fiscal; solo patrón metodológico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la planeación semanal y la consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas solo descriptivas.",
    "Vincular el análisis fiscal-tributario con aplicación profesional concreta."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders, slugs o rutas truncadas antes de publicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Cerrar entornos truncados de tabla o documento antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones estables.",
    "Evitar transferir contenido temático específico de otra materia.",
    "Aplicar estrategia conservadora: reforzar reglas útiles sin regresión.",
    "Si falta consigna local, propagar solo reglas generales y abrir vacíos."
  ],
  "open_questions": [
    "Confirmar rúbrica de evaluación específica de Derecho fiscal y tributario.",
    "Confirmar formato de citación exigido por la asignatura.",
    "Confirmar si autor y matrícula deben permanecer en plantillas compartidas.",
    "Resolver definitivamente rutas truncadas en README (reporte y referencias).",
    "Confirmar figura docente y cerrar bloque authortable del reporte."
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
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social de inicio.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeación.",
      "Análisis propio con postura.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusión.",
      "Sostener calidad editorial uniforme en toda la suite LaTeX."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Secciones funcionales y cierre profesional.",
      "Sin contenido de relleno descriptivo."
    ],
    "argumentative_patterns": [
      "Problema inicial breve y concreto.",
      "Marco conceptual y normativo delimitado.",
      "Contraste de fuentes y postura propia.",
      "Cierre con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Problema jurídico",
        "Marco normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia .tex/.bib",
        "Normalización JSON"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La argumentación se estructura desde una pregunta o conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere fundamento normativo explícito."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura entre nodos."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito, ejes de trabajo y regla bibliográfica local.",
        "derecho-fiscal-y-tributario.bib: base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se preservó contenido útil previo.",
      "Se reforzó el núcleo transversal problema-conceptos-evidencia-análisis-conclusión.",
      "Se evitó traspasar bibliografía temática de Filosofía a Fiscal sin validación local.",
      "Se mantuvo política de no propagación de salidas no estructuradas."
    ]
  }
}