{
  "summary": [
    "Se mantiene sincronización transversal con compresión lossless por unión-deduplicación.",
    "Se conserva identidad UnADM y contexto curricular local verificado del destino.",
    "Se refuerzan ejes editoriales reutilizables: problema, marco conceptual-normativo, análisis propio y conclusión jurídica.",
    "Se preserva regla crítica de normalizar salidas no JSON antes de propagación recursiva.",
    "Se evita transferir contenido temático específico de Filosofía; se transfieren solo abstracciones estables."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Usar contexto local: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Verificar datos personales y figura docente antes de entrega final."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la planeación semanal y la consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación entre reporte, presentación y bibliografía local."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas solo descriptivas.",
    "Vincular argumentos fiscal-tributarios con aplicación profesional concreta.",
    "No asumir fuentes de otras materias como obligatorias en el destino."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre metadatos de portada y programa analítico.",
    "Corregir rutas o tokens sin expandir antes de publicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Completar campos pendientes de plantilla antes de compilar.",
    "Cerrar correctamente todos los entornos LaTeX truncados.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar la malla curricular solo para respaldo de ubicación curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir a nodos laterales solo reglas abstractas y estables.",
    "Evitar trasladar redacción literal o bibliografía temática no equivalente.",
    "Mantener estrategia conservadora: sin regresión y sin borrado de reglas útiles.",
    "Aplicar normalización manual cuando aparezcan salidas heredadas ambiguas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades específicas de la materia destino.",
    "Confirmar formato de citación exigido por Derecho fiscal y tributario.",
    "Confirmar nombre final de figura docente en plantilla.",
    "Confirmar si autor y matrícula deben mantenerse en plantillas compartidas.",
    "Confirmar si se requiere bibliografía fiscal base adicional por unidad."
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
        "Integridad académica con trazabilidad de fuentes.",
        "Supuestos etiquetados y verificables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico inicial claro.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio sustentado.",
      "Conclusión jurídica aplicable.",
      "Consistencia técnica entre .tex y .bib."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia institucional, metodológica y técnica en toda entrega.",
      "Permitir propagación segura entre nodos sin pérdida editorial."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Sin afirmaciones sin fuente.",
      "Sin relleno descriptivo.",
      "Cierre profesional con implicación práctica."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco -> análisis -> conclusión.",
      "Norma o doctrina -> contraste -> postura propia.",
      "Conclusión respaldada por evidencia citada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia .tex/.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentativa requiere conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida exige fundamento normativo."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Consistencia .tex/.bib",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La trazabilidad documental depende de citas y referencias coherentes."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analítico editorial de Derecho fiscal y tributario.",
        "Archivo derecho-fiscal-y-tributario.bib.",
        "Regla persistente: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicación completa sin recorte semántico.",
      "Ciclo 5: preservadas reglas útiles previas y consolidada sintaxis accionable.",
      "Ciclo 5: reforzada transferencia transversal por abstracciones estables, no por contenido temático de origen."
    ]
  }
}