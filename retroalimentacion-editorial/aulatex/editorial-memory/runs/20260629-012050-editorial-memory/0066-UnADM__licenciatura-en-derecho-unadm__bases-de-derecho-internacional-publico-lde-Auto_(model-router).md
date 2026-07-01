```json
{
  "summary": [
    "Se refuerza la sincronización transversal entre actividad origen y materia destino.",
    "Se transfieren abstracciones editoriales estables sin contenido temático.",
    "Se consolida ADN editorial conservador para Derecho Internacional Público.",
    "Se preserva identidad UnADM y contexto curricular local verificado.",
    "Se mantiene compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar solo contexto curricular verificado del nodo destino.",
    "No mezclar metadatos curriculares entre materias.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canónica.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones: conceptos, norma/doctrina, análisis propio y cierre.",
    "Alinear siempre al producto solicitado por la planeación.",
    "Cerrar con conclusión jurídica transferible a la práctica."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre consigna, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Marcar faltantes como pendientes sin inventar contenido.",
    "Validar consistencia cita-bibliografía.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Reutilizar plantillas .tex locales sin alterar identidad.",
    "Usar codificación correcta en español en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Mantener nombres de archivo locales verificados.",
    "No introducir comandos no estándar sin justificación."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en el .bib local.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM.",
    "Conservar metadatos mínimos completos.",
    "Validar que toda cita exista en el .bib."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar traslado de contenido temático entre materias.",
    "Normalizar manualmente memorias del ciclo 1 si se reutilizan.",
    "Preservar reglas útiles previas sin regresión.",
    "Propagar recursivamente solo tras validación."
  ],
  "open_questions": [
    "Confirmar rúbricas específicas de actividades del destino.",
    "Definir formato mínimo de conclusión jurídica por actividad.",
    "Confirmar normalización final de nombres de archivo con acentos.",
    "Verificar tokens sin expandir en README y programa analítico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica verificable",
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 4, bloque 1",
        "Asignatura: Bases de derecho internacional público"
      ]
    },
    "essence": [
      "Problema jurídico como detonador",
      "Estructura argumentativa clara",
      "Evidencia verificable",
      "Análisis propio",
      "Conclusión transferible"
    ],
    "reason_for_being": [
      "Guiar productos académicos con rigor jurídico",
      "Asegurar coherencia entre consigna y entrega",
      "Facilitar transferencia a la práctica profesional"
    ],
    "style_markers": [
      "Objetivo explícito al inicio",
      "Secciones funcionales",
      "Supuestos siempre etiquetados",
      "Cierre con criterio jurídico aplicable"
    ],
    "argumentative_patterns": [
      "Problema → conceptos → norma/doctrina → análisis → conclusión",
      "Afirmación → evidencia → interpretación → postura propia"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa jurídica",
        "Evidencia verificable",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia cita-bibliografía"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa jurídica",
          "kind": "depends_on",
          "justification": "La forma del entregable deriva del producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión válida requiere respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        }
      ],
      "evidence": [
        "README y programa analítico del destino",
        "Bibliografía institucional local",
        "Reglas de calidad heredadas UnADM"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes editoriales comunes sin contaminar contenido.",
      "Se mantiene estrategia conservadora y transversal.",
      "Se preserva ADN institucional UnADM."
    ]
  }
}
```