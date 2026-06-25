{
  "summary": [
    "Se consolida sincronización transversal desde Actividad 1 de Filosofía del Derecho hacia materia electiva con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM, normalización estructurada obligatoria y compresión lossless por unión-dedupe sin regresión.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se mantiene separación entre reglas institucionales reutilizables y contenido temático no equivalente entre nodos.",
    "Se detecta destino con contexto local mínimo válido; se mantienen vacíos locales abiertos con marca de supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre curricular del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rúbrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones trazables: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar en .bib local solo fuentes realmente usadas en cada actividad.",
    "No asumir que bibliografía de otra semana o asignatura aplica automáticamente."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalización manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que rutas y nombres de archivos existan y no contengan placeholders sin resolver."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 y configuración article/spanish/letterpaper/oneside salvo instrucción contraria.",
    "Conservar portada académica completa y actualizar campos pendientes.",
    "No compilar con tokens sin expandir tipo $(@{...}.Slug).",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores críticos ni referencias cruzadas rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL y nota de consulta cuando aplique.",
    "Distinguir bibliografía base de la materia y bibliografía específica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y deduplicadas.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Evitar propagar redacción literal o temas específicos de Filosofía del Derecho a la electiva sin validación local.",
    "Mantener alerta histórica de ciclos con salidas no estructuradas para normalización manual previa.",
    "Aplicar estrategia progresiva y conservadora: sumar mejoras verificables sin eliminar reglas útiles previas."
  ],
  "open_questions": [
    "Supuesto: créditos oficiales de la electiva siguen vacíos en README y portada; confirmar.",
    "Supuesto: falta nombre oficial de la asignatura electiva en malla para fijar rotulado final.",
    "Supuesto: figura docente permanece como placeholder; confirmar dato final.",
    "Confirmar limpieza completa de placeholders en README y programa analítico.",
    "Confirmar política local sobre year fijo vs fecha de consulta en entradas web institucionales."
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
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Producción orientada a planeación semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo/doctrinal pertinentes.",
      "Evidencia verificable.",
      "Análisis propio con postura.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos y verificables.",
      "Asegurar continuidad editorial transversal sin contaminación temática entre nodos no equivalentes."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y trazables.",
      "Supuestos etiquetados cuando falte información.",
      "Cierre con implicación jurídica práctica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación propia.",
      "Consigna -> objetivo -> verificación de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalización estructurada",
        "evidencia verificable",
        "postura argumentada",
        "conclusión transferible",
        "alineación con consigna"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional",
          "target": "alineación con consigna",
          "kind": "supports",
          "justification": "Define límites formales y curriculares del entregable."
        },
        {
          "source": "normalización estructurada",
          "target": "evidencia verificable",
          "kind": "supports",
          "justification": "Reduce ruido y mejora trazabilidad de respaldo documental."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere sustento explícito."
        },
        {
          "source": "postura argumentada",
          "target": "conclusión transferible",
          "kind": "develops",
          "justification": "El análisis propio permite cierre útil para práctica jurídica."
        },
        {
          "source": "alineación con consigna",
          "target": "conclusión transferible",
          "kind": "depends_on",
          "justification": "Sin ajuste a consigna no hay transferencia válida del resultado."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y carpeta canónica.",
        "Programa analítico local define ejes editoriales reutilizables.",
        "Bibliografía local contiene base institucional mínima verificable.",
        "Memoria de origen aporta reglas estructurales estables y gates de calidad transferibles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se deduplican reglas repetidas y se conserva contenido útil previo.",
      "Ciclo 6: se refuerza gate de JSON parseable como condición de propagación recursiva.",
      "Ciclo 6: se mantiene separación entre abstracciones estables y contenido temático no equivalente.",
      "Ciclo 6: se preservan supuestos abiertos del destino sin cerrarlos con datos no verificados."
    ]
  }
}