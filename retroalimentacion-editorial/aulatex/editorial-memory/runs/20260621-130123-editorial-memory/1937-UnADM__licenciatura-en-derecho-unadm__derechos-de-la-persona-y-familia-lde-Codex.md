{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia Derechos de la persona y familia sin arrastrar contenido temático no equivalente.",
    "Se conserva identidad UnADM y ubicación curricular local del destino: Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
    "Se refuerza núcleo editorial estable: problema, conceptos y normas, evidencia, análisis propio, conclusión jurídica transferible.",
    "Se mantiene gate crítico: no propagar ni reutilizar salidas no estructuradas sin normalización previa.",
    "Se consolida corrección de placeholders y rutas corruptas en README/programa analítico como requisito operativo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar nombre canónico de asignatura: Derechos de la persona y familia.",
    "Conservar contexto curricular local verificado en README y malla institucional.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "Mantener carpeta de la materia como punto de entrada canónico.",
    "No reemplazar datos de autoría de plantilla sin verificación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Organizar en secciones: marco conceptual-normativo, análisis propio, cierre.",
    "Alinear siempre el desarrollo al producto solicitado por la planeación o consigna.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional.",
    "Mantener trazabilidad explícita entre consigna, desarrollo y conclusión."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guía, argumentos y cierre.",
    "No transferir contenido doctrinal de otra materia sin validación de pertinencia local. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa del esquema de memoria antes de guardar.",
    "Exigir respaldo o marca [supuesto] en afirmaciones no verificadas.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia exacta entre actividad y producto entregable."
  ],
  "latex_rules": [
    "Conservar configuración base article, spanish, letterpaper, oneside salvo consigna contraria.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores críticos, sin referencias rotas y sin placeholders dinámicos.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar nombres de archivo canónicos y sin saltos corruptos en rutas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canónico local.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Agregar solo referencias consultables y pertinentes a cada actividad.",
    "No inventar fuentes ni claves de cita.",
    "Conservar metadatos mínimos: autor, título, año y fuente/URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables: identidad, estructura, calidad y método argumentativo.",
    "Evitar propagación de redacción literal o contenido temático de Filosofía del Derecho.",
    "Aplicar unión-deduplicación sin pérdida y sin regresión de reglas útiles.",
    "Etiquetar como provisionales reglas heredadas sin evidencia documental local.",
    "En ciclo 1 mantener estrategia conservadora con validación manual previa."
  ],
  "open_questions": [
    "Confirmar consignas y rúbricas vigentes de actividades de la materia destino.",
    "Confirmar vigencia de datos de plantilla de alumno/docente. [supuesto]",
    "Confirmar corrección final de nombres corruptos en README (reporte/referencias).",
    "Confirmar si coursecode LDE-S3B1 es obligatorio en todos los entregables.",
    "Confirmar política local de uso de portada/presentación por actividad."
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
        "Semestre 3, bloque 1, obligatoria seriada, 8 créditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y trazabilidad argumentativa.",
      "Estandarizar calidad editorial reusable en actividades heterogéneas sin perder contexto local."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separación nítida entre marco conceptual y postura propia.",
      "Etiquetado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma/doctrina/fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa jurídica",
        "Integridad de evidencia y citas",
        "Normalización de memoria JSON",
        "Consistencia técnica LaTeX y BibTeX"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa jurídica",
          "kind": "supports",
          "justification": "El marco institucional define tono y formato de argumentación."
        },
        {
          "source": "Normalización de memoria JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilización segura."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de sustento verificable."
        },
        {
          "source": "Consistencia técnica LaTeX y BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y pérdida de trazabilidad."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analítico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib con entradas institucionales base."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas del origen y destino sin recorte semántico.",
      "Se transfirieron solo patrones editoriales estables y transversales.",
      "Se evitó migrar contenido específico de Filosofía del Derecho por no equivalencia temática.",
      "Se reforzó gate de normalización JSON por historial de salidas no parseables.",
      "Se mantuvieron vacíos locales abiertos donde falta consigna verificable."
    ]
  }
}