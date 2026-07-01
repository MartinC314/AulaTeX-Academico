```json
{
  "summary": [
    "Se consolida sincronización transversal desde actividad origen hacia materia destino.",
    "Se preservan ejes editoriales estables reutilizables sin transferir contenido temático.",
    "Se refuerza ADN editorial UnADM con enfoque conservador y progresivo.",
    "La compresión se realiza por unión y deduplicación sin pérdida.",
    "Se mantiene cerebro editorial mínimo funcional para la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar solo el contexto curricular verificado del destino.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Tratar fuentes provisionales como procedencia, no como identidad.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Organizar entregas con problema, conceptos, análisis propio y conclusión jurídica.",
    "Alinear siempre la estructura al producto solicitado en la planeación.",
    "Separar claramente reporte, presentación y otros productos.",
    "Iniciar con encuadre breve del problema jurídico o social."
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
    "Revisar estructura mínima completa antes de reutilizar.",
    "Marcar faltantes como pendientes sin inventar contenido.",
    "Validar consistencia cita-bibliografía.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local sin romper identidad institucional.",
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos ni referencias rotas.",
    "No introducir comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos completos.",
    "Validar que toda cita exista en el archivo .bib."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar trasladar redacción literal o contenido temático específico.",
    "Preservar reglas útiles previas sin regresión.",
    "Normalizar manualmente memorias heredadas del ciclo 1 si se reutilizan.",
    "Propagar recursivamente solo después de validar JSON y estructura."
  ],
  "open_questions": [
    "Confirmar si existen reglas editoriales locales adicionales no documentadas.",
    "Definir formato estándar de conclusión jurídica para la materia.",
    "Confirmar criterios editoriales sobre uso de acentos en nombres de archivo.",
    "Revisar y corregir tokens sin expandir en README y programa analítico."
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
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Bases de derecho internacional público."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Estructura argumentativa jurídica reutilizable.",
      "Evidencia verificable como base del análisis.",
      "Conclusión jurídica transferible a la práctica.",
      "Normalización como condición de propagación."
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente de la materia.",
      "Garantizar coherencia, calidad y trazabilidad académica.",
      "Facilitar reutilización transversal sin pérdida de identidad.",
      "Asegurar alineación entre consigna, desarrollo y cierre."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema → conceptos → norma/doctrina → análisis → conclusión.",
      "Afirmación → evidencia → interpretación → postura propia.",
      "Consigna → desarrollo alineado → verificación final."
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
          "justification": "La forma del entregable se define por el producto solicitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida requiere respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analítico destino.",
        "Bibliografía local institucional.",
        "Reglas de calidad heredadas UnADM."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas editoriales repetidas.",
      "Se reforzó separación entre identidad y procedencia.",
      "Se consolidó grafo conceptual transversal.",
      "Se mantuvo estrategia conservadora sin regresión."
    ]
  }
}
```