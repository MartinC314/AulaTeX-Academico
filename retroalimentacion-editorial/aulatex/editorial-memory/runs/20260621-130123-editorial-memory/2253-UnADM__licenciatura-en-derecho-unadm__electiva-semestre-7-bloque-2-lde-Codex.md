{
  "summary": [
    "Se sincroniza transferencia transversal desde actividad de Filosofía del Derecho a materia electiva con solo abstracciones estables.",
    "Se conserva identidad UnADM, normalización estructurada obligatoria y compresión lossless por unión-dedupe.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene estrategia progresiva y conservadora sin importar contenido temático específico no equivalente.",
    "Se prioriza control de calidad JSON parseable antes de propagación recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar encuadre local: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rúbrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener trazabilidad entre consigna, desarrollo y cierre."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar fuentes específicas de cada actividad en el .bib local de la materia.",
    "No asumir que bibliografía de otra asignatura aplica automáticamente.",
    "Etiquetar supuestos cuando falte contexto de actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalización manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar coherencia entre objetivo, evidencia, análisis y conclusión.",
    "Verificar correspondencia del entregable con la consigna vigente."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 y portada académica completa.",
    "Usar article con spanish, letterpaper y oneside salvo instrucción distinta.",
    "No compilar con placeholders tipo $(@{...}) sin normalizar.",
    "Corregir nombres rotos en README y programa analítico antes de referenciar archivos.",
    "Mantener claves BibTeX estables y compilación sin referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, generales y no duplicadas.",
    "Compartir entre nodos no equivalentes solo identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redacción literal o contenido temático específico de Filosofía del Derecho.",
    "Mantener bandera de normalización manual para ciclos con insumos no estructurados.",
    "Preservar reglas útiles previas; solo agregar mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: faltan créditos oficiales de la electiva en README y portada; confirmar.",
    "Supuesto: falta nombre oficial final de la electiva en malla curricular; confirmar.",
    "Confirmar figura docente en plantilla base.",
    "Confirmar corrección definitiva de placeholders en README y programa analítico.",
    "Confirmar política local para year vs fecha de consulta en fuentes web institucionales."
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
        "Normalización estructurada previa a propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Producción orientada a planeación semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos trazables y útiles.",
      "Asegurar calidad editorial reproducible entre actividades y formatos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas.",
      "Supuestos etiquetados.",
      "Cierre con implicación práctica."
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
          "justification": "Delimita formato, alcance y trazabilidad del entregable."
        },
        {
          "source": "normalización estructurada",
          "target": "evidencia verificable",
          "kind": "supports",
          "justification": "Reduce ruido y asegura control de respaldo documental."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia exige respaldo explícito."
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
          "justification": "La transferencia profesional depende de responder al objetivo pedido."
        }
      ],
      "evidence": [
        "README local de electiva confirma identidad y punto de entrada canónico.",
        "Programa analítico local define ejes de trabajo reutilizables.",
        "Bibliografía local contiene base institucional verificable.",
        "Origen aporta reglas estructurales estables y quality gates transferibles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicación completa de reglas repetidas del origen y destino.",
      "Ciclo 14: se transfirieron solo abstracciones estables por relación transversal.",
      "Ciclo 14: se preservaron gates críticos de parseo JSON y normalización manual.",
      "Ciclo 14: se evitó importar contenido temático específico no equivalente."
    ]
  }
}