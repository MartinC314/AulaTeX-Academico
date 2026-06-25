```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad de Filosofía del Derecho hacia la materia de Contratos y Obligaciones.",
    "Se preservan reglas institucionales UnADM y el modelo de cinco ejes como abstracción estable.",
    "Se refuerza normalización estructurada y control de calidad previo a propagación recursiva.",
    "La transferencia evita redacción literal y se limita a patrones editoriales reutilizables.",
    "Se consolida cerebro editorial mínimo y conservador para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Marcar explícitamente como [supuesto] todo dato no visible en la consigna local.",
    "Tratar herencias Codex o GPT-Pro no verificadas como provisionales.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Conservar enfoque jurídico aplicado a contratos y obligaciones.",
    "No trasladar contenido doctrinal de otras materias sin adecuación disciplinar."
  ],
  "structure_rules": [
    "Aplicar modelo transversal de cinco ejes: problema, conceptos, producto, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear siempre el entregable al producto de la planeación semanal."
  ],
  "activity_rules": [
    "Explicitar postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir claramente problema, norma o doctrina y criterio propio.",
    "Evitar reutilizar fuentes o enfoques de semanas o materias no correspondientes."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar trazabilidad entre objetivo, evidencia, argumento y cierre.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "No degradar reglas útiles previas durante unión y deduplicación."
  ],
  "latex_rules": [
    "Usar plantilla LaTeX base local de la materia según consigna.",
    "Mantener metadatos completos: curso, autor, universidad y ubicación.",
    "Verificar que el archivo .bib referenciado sea el canónico local.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "No inventar referencias; declarar [supuesto] si falta disponibilidad.",
    "Distinguir bibliografía base de fuentes específicas de actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos no equivalentes.",
    "Validar compatibilidad disciplinar antes de propagación lateral.",
    "Propagar recursivamente solo tras validar JSON y estructura mínima.",
    "Evitar transferir redacción literal o ejemplos doctrinales específicos.",
    "Aplicar estrategia progresiva y conservadora en ciclos posteriores."
  ],
  "open_questions": [
    "Confirmar rúbrica de evaluación específica por actividad en la materia.",
    "Definir si existe guía formal de citación jurídica obligatoria.",
    "Precisar alcance de fuentes: federales, locales o mixtas según actividad.",
    "Confirmar si presentaciones comparten metadatos completos del reporte."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 4, bloque 1",
        "Asignatura obligatoria",
        "Enfoque en contratos y obligaciones"
      ]
    },
    "essence": [
      "Modelo transversal de cinco ejes editoriales.",
      "Normalización estructurada como condición de propagación.",
      "Argumentación jurídica con transferencia profesional.",
      "Identidad UnADM como marco constante."
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial entre materias jurídicas.",
      "Facilitar reutilización de estructuras y controles de calidad.",
      "Evitar contaminación entre disciplinas por copia literal.",
      "Sostener productos académicos verificables y profesionales."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados.",
      "Secciones funcionales y trazables.",
      "Conclusión jurídica operativa.",
      "Evitar redundancia mediante deduplicación lossless."
    ],
    "argumentative_patterns": [
      "Problema delimitado → marco normativo → análisis propio → conclusión.",
      "Postura del estudiante sustentada en evidencia.",
      "Cierre orientado a la práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema jurídico",
        "Contratos",
        "Obligaciones",
        "Análisis jurídico propio",
        "Conclusión transferible",
        "Normalización estructurada",
        "Identidad UnADM"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis jurídico propio",
          "kind": "depends_on",
          "justification": "El análisis se activa a partir de un conflicto delimitado."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión surge del razonamiento sustentado."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas y formato verificables."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "Evita contaminación por salidas no parseables."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia confirman cinco ejes.",
        "Archivo .bib local confirma fuentes institucionales base.",
        "Reglas heredadas de Filosofía del Derecho validadas como abstracciones estables."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales UnADM sin regresión.",
      "Se deduplican ejes editoriales comunes entre nodos.",
      "Se refuerza control de calidad previo a propagación.",
      "Se mantiene compatibilidad disciplinar en transferencia transversal."
    ]
  }
}
```