{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad de Filosofía hacia materia de Derecho fiscal sin trasladar contenido temático literal.",
    "Se conserva compresión lossless por unión y deduplicación sin regresión.",
    "Se refuerza normalización obligatoria de salidas no estructuradas antes de propagación recursiva.",
    "Se mantienen ejes editoriales estables: problema, conceptos/normas, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se prioriza contexto local del destino para datos curriculares y operativos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares verificados del destino: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica editorial.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No transferir datos personales de plantilla como regla global; verificar antes de publicar."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto final con la consigna y planeación semanal.",
    "Mantener separación entre reporte .tex, presentación .tex y .bib local.",
    "Corregir rutas y tokens sin expandir en README y programa analítico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Vincular el análisis fiscal-tributario con aplicación profesional concreta.",
    "Cerrar con conclusión jurídica transferible a la práctica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no existan placeholders o tokens sin resolver en README/.tex/.bib.",
    "Comprobar integridad de compilación LaTeX y cierre de entornos."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Completar campos pendientes de plantilla antes de compilar.",
    "Cerrar correctamente entornos tabular y documento.",
    "Resolver expresiones tipo $(@{...}.Slug) en nombres de archivo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No transferir bibliografía temática de Filosofía como obligatoria en Fiscal."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir a nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redacción literal o ejemplos temáticos locales.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas útiles."
  ],
  "open_questions": [
    "[supuesto] Confirmar si persiste requisito de clave de curso LDE-S6B1 en todas las actividades.",
    "[supuesto] Confirmar formato de citación exigido por la asignatura.",
    "Confirmar nombre final de figura docente en plantilla.",
    "Confirmar política de anonimización para autor y matrícula en plantillas compartidas."
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
      "Resolver problemas jurídicos con fundamento verificable.",
      "Convertir planeación en productos académicos evaluables.",
      "Sostener análisis propio con cierre transferible."
    ],
    "reason_for_being": [
      "Operar como cerebro editorial persistente con continuidad institucional.",
      "Asegurar calidad técnica y argumentativa antes de cada propagación."
    ],
    "style_markers": [
      "Problema inicial breve.",
      "Marco normativo explícito.",
      "Postura propia no descriptiva.",
      "Conclusión profesional aplicable.",
      "Sin placeholders ni fuentes inventadas."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> evidencia -> análisis propio -> conclusión.",
      "Cada afirmación relevante con respaldo o marca de supuesto.",
      "Coherencia total entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Trazabilidad de fuentes",
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
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La argumentación requiere conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La validez práctica exige fundamento jurídico explícito."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analítico local.",
        "derecho-fiscal-y-tributario.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicación completa de reglas repetidas.",
      "Ciclo 14: preservadas reglas útiles previas sin recorte.",
      "Ciclo 14: transferidas solo abstracciones estables entre nodos transversales.",
      "Ciclo 14: mantenidos gates críticos de JSON, supuestos y consistencia .tex/.bib."
    ]
  }
}