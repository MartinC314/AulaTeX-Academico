{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia electiva con transferencia de abstracciones estables.",
    "Se preservan reglas útiles previas del destino y se deduplican sin recorte.",
    "Se refuerzan identidad UnADM, estructura reusable, gates de calidad y grafo conceptual.",
    "Se mantiene estrategia progresiva y conservadora con normalización obligatoria antes de propagar.",
    "Se marcan como supuestos los vacíos locales de nombre oficial, créditos y consignas específicas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar encuadre de Licenciatura en Derecho, semestre 7, bloque 2, tipo electiva.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Usar la carpeta de la materia como punto de entrada canónico.",
    "Conservar autoría y matrícula en portada cuando aplique.",
    "Marcar como supuesto todo dato no visible en consigna, rúbrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad entre consigna, desarrollo y resultado."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "No asumir que bibliografía de otra semana o asignatura aplica automáticamente.",
    "Vincular cada actividad con el problema jurídico o social que la activa."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalización manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que rutas y nombres de archivo existan localmente antes de publicar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 y portada académica completa.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "No compilar con placeholders o tokens sin expandir.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Verificar disponibilidad y fecha de consulta en fuentes web."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y deduplicadas.",
    "Compartir solo abstracciones estables en nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico de otra asignatura.",
    "Mantener bandera de normalización manual para ciclos heredados no estructurados.",
    "Separar reglas institucionales de reglas temáticas en propagación lateral."
  ],
  "open_questions": [
    "Supuesto: faltan créditos oficiales de la electiva en README y portada.",
    "Supuesto: falta confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar figura docente en plantilla base.",
    "Confirmar consignas y rúbricas locales de actividades para ajustar profundidad argumentativa.",
    "Confirmar corrección total de placeholders en README y programa analítico."
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
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos trazables.",
      "Asegurar calidad editorial reusable entre actividades y formatos.",
      "Preservar identidad institucional con criterio jurídico aplicado."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas.",
      "Supuestos etiquetados.",
      "Cierre práctico-profesional."
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
        "alineación con consigna",
        "conclusión transferible"
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
          "kind": "depends_on",
          "justification": "Sin estructura no hay trazabilidad de fuentes ni validación."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia exige respaldo documental."
        },
        {
          "source": "postura argumentada",
          "target": "conclusión transferible",
          "kind": "develops",
          "justification": "El análisis propio habilita cierre aplicable a práctica jurídica."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y punto de entrada canónico.",
        "Programa analítico local fija ejes de problema, conceptos, producto, análisis y cierre.",
        "Bibliografía local contiene base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se consolidan reglas transversales estables sin importar contenido temático de Filosofía del Derecho.",
      "Ciclo 5: se preservan gates de parseo JSON y normalización como condición de propagación.",
      "Ciclo 5: se mantiene compresión lossless por unión y deduplicación sin eliminar reglas útiles previas."
    ]
  }
}