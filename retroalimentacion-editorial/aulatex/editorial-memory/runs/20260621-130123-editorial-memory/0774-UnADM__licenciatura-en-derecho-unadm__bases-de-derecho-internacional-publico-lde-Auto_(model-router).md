```json
{
  "summary": [
    "Se refuerza sincronización transversal entre actividad origen y materia destino.",
    "Se transfieren solo abstracciones editoriales estables y verificadas.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se consolida cerebro editorial mínimo reforzado para Derecho Internacional Público.",
    "Compresión aplicada por unión y deduplicación sin pérdida."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar exclusivamente contexto curricular verificado del destino.",
    "No mezclar metadatos curriculares entre materias.",
    "Tratar fuentes heredadas como procedencia hasta verificación local.",
    "Marcar como supuesto cualquier dato no visible en consigna local."
  ],
  "structure_rules": [
    "Usar carpeta de materia como punto de entrada canónico.",
    "Estructurar entregables en problema, conceptos, evidencia, análisis y conclusión.",
    "Alinear estructura al producto solicitado en planeación semanal.",
    "Conservar separación entre reporte, presentación y bibliografía.",
    "Iniciar con encuadre breve del problema jurídico o social."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Incluir postura argumentada propia, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables.",
    "Distinguir hechos, normas, doctrina y criterio propio.",
    "Cerrar con conclusión jurídica transferible a la práctica."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar coherencia entre consigna, desarrollo y conclusión.",
    "Confirmar consistencia cita-bibliografía antes de cierre.",
    "Marcar faltantes como pendientes sin inventar contenido.",
    "Normalizar respuestas no estructuradas antes de reutilizar."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener codificación y acentos correctos en español.",
    "Cerrar correctamente entornos antes de compilar.",
    "No introducir comandos no estándar sin justificación.",
    "Verificar nombres de archivos y tokens sin expandir."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en el .bib local del destino.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Validar que todas las claves citadas existan en el .bib.",
    "Distinguir bibliografía base de bibliografía específica."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales verificadas entre nodos transversales.",
    "Evitar trasladar contenido temático específico del origen.",
    "Preservar reglas útiles previas sin regresión.",
    "Aplicar normalización manual a memorias de ciclos iniciales.",
    "Mantener estrategia progresiva y conservadora."
  ],
  "open_questions": [
    "Confirmar rúbricas específicas de actividades del destino.",
    "Definir formato mínimo esperado de conclusión jurídica.",
    "Validar criterio editorial sobre uso de acentos en nombres oficiales.",
    "Confirmar actividades que requieran producto distinto a reporte.",
    "Revisar y corregir tokens sin expandir en README."
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
        "Integridad académica y trazabilidad.",
        "Normalización estructurada obligatoria."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1.",
        "Asignatura: Bases de derecho internacional público."
      ]
    },
    "essence": [
      "Problema jurídico como detonante.",
      "Estructura argumentativa jurídica.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión transferible."
    ],
    "reason_for_being": [
      "Orientar productos académicos claros y fundamentados.",
      "Asegurar transferencia a la práctica jurídica.",
      "Garantizar coherencia editorial transversal."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Supuestos siempre etiquetados.",
      "Cierre con criterio jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema → conceptos → norma/doctrina → análisis → conclusión.",
      "Afirmación → evidencia → interpretación → posición propia.",
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
          "justification": "La conclusión válida requiere respaldo documental."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        }
      ],
      "evidence": [
        "README y programa analítico del destino.",
        "Bibliografía institucional UnADM.",
        "Reglas de calidad heredadas y verificadas."
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes editoriales comunes sin trasladar contenido temático.",
      "Se preserva identidad UnADM y contexto curricular del destino.",
      "Se consolida cerebro editorial estable para propagación futura."
    ]
  }
}
```