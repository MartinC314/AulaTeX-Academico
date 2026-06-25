```json
{
  "summary": [
    "Se consolida memoria editorial transversal desde actividad hacia materia no equivalente.",
    "Se preservan reglas institucionales UnADM y estructura académica estable.",
    "Se refuerza ADN editorial reusable sin transferir contenido temático específico.",
    "Se mantiene estrategia conservadora con normalización obligatoria previa a propagación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear todo entregable a Licenciatura en Derecho y a la materia destino.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Estructurar cada actividad con: problema, conceptos o normas, evidencia, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener consistencia entre README, programa analítico, .tex y .bib.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada propia; evitar resumen descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y cierre.",
    "Distinguir evidencia citada de interpretación propia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Evitar regresión de reglas útiles heredadas."
  ],
  "latex_rules": [
    "Usar español correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Corregir macros incompletas o truncadas antes de compilar.",
    "Validar compilación sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local confirmado de la materia.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Agregar fecha de consulta en recursos web."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o contenido temático específico.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Mantener alerta institucional por salidas no estructuradas hasta confirmación."
  ],
  "open_questions": [
    "Confirmar resolución definitiva de incidencias históricas de salida no JSON parseable.",
    "Definir plantilla oficial de presentación si difiere del reporte.",
    "Confirmar corrección final de placeholders de slug en README y programa.",
    "Verificar macros faltantes en plantilla .tex de la materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 créditos.",
        "Materia mercantil con enfoque práctico."
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida.",
      "Marco conceptual y normativo verificable.",
      "Análisis propio con respaldo.",
      "Conclusión aplicable a la práctica profesional."
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y transversal.",
      "Garantizar coherencia institucional y calidad académica.",
      "Facilitar reutilización estructural entre asignaturas."
    ],
    "style_markers": [
      "Apertura breve y contextual.",
      "Secciones explícitas y ordenadas.",
      "Uso explícito de supuestos cuando falte evidencia.",
      "Cierre con implicación profesional."
    ],
    "argumentative_patterns": [
      "Problema → marco normativo → contraste de evidencia → postura propia → conclusión.",
      "Afirmación jurídica siempre con respaldo verificable.",
      "Priorizar análisis sobre descripción."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Problema jurídico",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización estructurada",
        "JSON parseable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentación pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La aplicación profesional requiere base normativa."
        },
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación segura exige estructura válida."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino.",
        ".bib local con fuentes institucionales UnADM."
      ]
    },
    "reinforcement_log": [
      "Se refuerza identidad UnADM sin importar la asignatura.",
      "Se preserva estructura académica estable entre nodos.",
      "Se evita transferencia temática inapropiada.",
      "Se consolida normalización como gate crítico."
    ]
  }
}
```