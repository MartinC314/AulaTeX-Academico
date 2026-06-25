{
  "summary": [
    "Se mantiene sincronización transversal conservadora entre nodos no equivalentes.",
    "Se preserva identidad UnADM y contexto local de Derecho fiscal y tributario.",
    "Se refuerza compresión lossless por unión y deduplicación sin recorte.",
    "Se conserva regla de bloqueo por salida no JSON parseable.",
    "Se agrega corrección verificable de rutas truncadas y tokens slug sin expandir en README y programa analítico.",
    "Supuesto: la consigna de actividades específicas del destino no está visible."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Mantener contexto curricular local: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar clave de curso LDE-S6B1 cuando aplique.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Verificar datos personales y figura docente antes de entrega final."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear producto final con planeación semanal y consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación entre reporte .tex, presentación .tex y .bib local.",
    "Usar programa analítico como guía editorial de la materia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Vincular análisis fiscal-tributario con aplicación profesional concreta.",
    "Desarrollar el producto exacto solicitado por la actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Verificar consistencia entre metadatos de portada y programa analítico.",
    "Corregir placeholders, rutas truncadas y tokens sin expandir antes de publicar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Completar campos pendientes de plantilla antes de compilar.",
    "Cerrar correctamente entornos tabular y documento.",
    "Corregir bloque authortable truncado.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo truncados en README (reporte y referencias)."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar malla curricular solo para respaldo de datos curriculares."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables en saltos transversales.",
    "No propagar contenido temático específico de Filosofía del Derecho al destino fiscal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener estrategia progresiva y conservadora sin regresión."
  ],
  "open_questions": [
    "Confirmar consigna y rúbrica de la próxima actividad local.",
    "Confirmar formato de citación exigido por la asignatura.",
    "Confirmar si autor y matrícula deben permanecer en plantillas compartidas.",
    "Confirmar nombre de figura docente para portada.",
    "Supuesto: derecho-fiscal-y-tributario.bib seguirá como archivo canónico en todas las actividades."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con trazabilidad de fuentes.",
        "Supuestos etiquetados y verificables.",
        "Entrada canónica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Clave local LDE-S6B1."
      ]
    },
    "essence": [
      "Problema jurídico inicial.",
      "Marco conceptual y normativo.",
      "Análisis propio con evidencia.",
      "Conclusión transferible a práctica jurídica.",
      "Consistencia técnica entre .tex y .bib."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Asegurar calidad editorial persistente y reusable.",
      "Mantener coherencia institucional y profesional en todas las entregas."
    ],
    "style_markers": [
      "Supuestos siempre marcados.",
      "Sin afirmaciones sin fuente.",
      "Estructura funcional en secciones.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema breve y concreto al inicio.",
      "Delimitación de conceptos y normas pertinentes.",
      "Contraste de fuentes con postura propia.",
      "Conclusión con implicación práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Problema jurídico",
        "Marco normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia .tex/.bib"
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
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentativa parte de un conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere fundamento normativo."
        },
        {
          "source": "Normalización JSON",
          "target": "Consistencia .tex/.bib",
          "kind": "develops",
          "justification": "La estructura formal reduce errores de propagación y edición."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "derecho-fiscal-y-tributario.bib con fuentes institucionales.",
        "Detección de rutas truncadas y slug sin expandir en archivos de contexto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se conserva núcleo institucional y gates críticos sin eliminar reglas útiles.",
      "Ciclo 21: se deduplican reglas repetidas con compresión lossless.",
      "Ciclo 21: se transfiere patrón metodológico desde Filosofía sin arrastrar contenido temático no equivalente.",
      "Ciclo 21: se refuerzan correcciones verificables de README/programa por rutas y tokens rotos."
    ]
  }
}