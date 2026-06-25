```json
{
  "summary": [
    "Se consolida memoria transversal desde actividad origen hacia materia destino.",
    "Se preservan reglas institucionales UnADM y ejes editoriales reutilizables.",
    "No se transfiere contenido temático específico entre materias no equivalentes.",
    "Se refuerza cerebro editorial mínimo del destino con abstracciones estables.",
    "Compresión lossless aplicada por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "No mezclar contexto curricular del origen con el destino.",
    "Usar solo contexto curricular verificado localmente en el destino.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional.",
    "Marcar como supuesto cualquier dato no visible en la consigna local."
  ],
  "structure_rules": [
    "Usar carpeta de materia como punto de entrada canónico.",
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Incluir postura académica propia, no solo descripción.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre consigna, desarrollo y conclusión.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de reutilizar.",
    "Bloquear afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de propagación."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener codificación correcta y acentos en español.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "No copiar bloques completos de LaTeX entre nodos."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos jurídicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos completos en cada entrada.",
    "Validar que las claves citadas existan en el .bib."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos transversales.",
    "Evitar transferencia de redacción literal o contenido temático específico.",
    "Preservar reglas útiles previas aunque se reubiquen por categoría.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo.",
    "Documentar incidencias históricas de salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades futuras en la materia destino.",
    "Definir formato mínimo estándar de conclusión jurídica por tipo de evidencia.",
    "Confirmar criterios editoriales sobre acentos en nombres de archivos.",
    "Verificar resolución completa de tokens sin expandir en README y programa.",
    "Confirmar si se requieren reglas adicionales específicas de derecho internacional público."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro y jurídicamente preciso",
        "Argumentativo con criterio propio",
        "Conservador ante evidencia incompleta"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Normalización estructurada obligatoria",
        "Trazabilidad de fuentes provisionales"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 4, bloque 1, obligatoria",
        "Asignatura: Bases de derecho internacional público",
        "Contexto curricular verificado localmente"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Estructura argumentativa jurídica reusable",
      "Evidencia verificable como soporte",
      "Postura académica propia",
      "Conclusión transferible a la práctica"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente para productos académicos en LaTeX",
      "Garantizar consistencia institucional y calidad argumentativa",
      "Facilitar transferencia segura de reglas entre nodos",
      "Evitar regresiones y contaminación temática"
    ],
    "style_markers": [
      "Objetivo explícito al inicio",
      "Secciones funcionales y no redundantes",
      "Supuestos siempre etiquetados",
      "Cierre con criterio jurídico aplicable"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión",
      "Afirmación -> evidencia -> interpretación -> posición propia",
      "Consigna -> desarrollo alineado -> verificación final"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa jurídica",
        "Evidencia verificable",
        "Conclusión jurídica transferible",
        "Normalización JSON",
        "Consistencia cita-bibliografía"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Estructura argumentativa jurídica",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "Una conclusión válida requiere desarrollo estructurado previo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "El respaldo documental evita afirmaciones infundadas."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La transferencia segura exige salida parseable."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino",
        "Bibliografía institucional UnADM",
        "Reglas heredadas validadas por deduplicación"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes editoriales comunes entre materias.",
      "Se mantiene estrategia conservadora sin traslado temático.",
      "Se consolida cerebro editorial mínimo del destino.",
      "Se preservan reglas históricas útiles sin eliminación."
    ]
  }
}
```