```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad origen hacia materia destino.",
    "Se preservan ejes editoriales estables: problema, conceptos o normas, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza identidad institucional UnADM y estructura reusable sin transferir redacción literal.",
    "Se mantiene estrategia conservadora: no se eliminan reglas útiles previas.",
    "Se consolida cerebro editorial mínimo para la materia destino.",
    "Se mantiene alerta institucional sobre salidas no JSON parseables.",
    "Se prioriza grafo conceptual, gates de calidad y patrones argumentativos.",
    "Se aplica compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Alinear contenidos a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono jurídico-formal con criterio académico propio.",
    "Usar carpeta de materia como entrada canónica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Etiquetar fuentes heredadas no verificadas como provisionales.",
    "Evitar asumir consignas o rúbricas no confirmadas."
  ],
  "structure_rules": [
    "Abrir cada actividad con encuadre del problema jurídico o social.",
    "Separar secciones: conceptos o normas, evidencia, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear estructura al producto solicitado por la planeación.",
    "Mantener consistencia entre README, programa, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema concreto.",
    "Vincular argumentos con normas y doctrina verificables.",
    "Distinguir evidencia citada de interpretación propia.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otras semanas sin confirmación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas y .bib.",
    "No permitir referencias inventadas.",
    "Revisar que no exista regresión de reglas heredadas."
  ],
  "latex_rules": [
    "Mantener codificación correcta para español en .tex y .bib.",
    "Conservar claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación.",
    "Corregir macros truncadas antes de compilar.",
    "Validar compilación sin errores críticos.",
    "Resolver placeholders de slug en nombres de archivo."
  ],
  "bibliography_rules": [
    "Usar el .bib local confirmado de la materia destino.",
    "Registrar fuentes específicas por actividad.",
    "Priorizar fuentes institucionales UnADM y normativas verificables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos completos.",
    "Agregar fecha de consulta en recursos web."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o detalles locales de archivo.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener alerta institucional de normalización manual por ciclos.",
    "Usar compresión unión-dedupe en cada fusión."
  ],
  "open_questions": [
    "Confirmar consignas y rúbricas reales de actividades de la materia destino.",
    "Verificar si la incidencia histórica de salida no JSON parseable está resuelta.",
    "Confirmar plantilla oficial de presentación si difiere del reporte.",
    "Validar nombres finales de archivos y macros en plantilla LaTeX.",
    "Confirmar fuentes obligatorias por semana."
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
        "Integridad académica con citas verificables",
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2",
        "Materia obligatoria con enfoque profesional"
      ]
    },
    "essence": [
      "Problema jurídico como punto de partida",
      "Conceptos y normas como marco",
      "Evidencia verificable",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos",
      "Garantizar trazabilidad entre problema, análisis y conclusión",
      "Facilitar transferencia a la práctica jurídica"
    ],
    "style_markers": [
      "Secciones claras y orden argumentativo estable",
      "Supuestos marcados explícitamente",
      "Afirmaciones con respaldo verificable",
      "Cierre con postura jurídica propia"
    ],
    "argumentative_patterns": [
      "Delimitar problema",
      "Definir conceptos y marco normativo",
      "Contrastar evidencia",
      "Desarrollar análisis propio",
      "Concluir con aplicabilidad profesional"
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional UnADM",
        "integridad académica",
        "trazabilidad de fuentes",
        "problema jurídico",
        "análisis propio",
        "conclusión jurídica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional UnADM",
          "target": "integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige rigor y citas verificables."
        },
        {
          "source": "problema jurídico",
          "target": "análisis propio",
          "kind": "develops",
          "justification": "El análisis se construye a partir del problema delimitado."
        },
        {
          "source": "trazabilidad de fuentes",
          "target": "conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de evidencia rastreable."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia destino",
        ".bib local confirmado",
        "Reglas institucionales heredadas UnADM"
      ]
    },
    "reinforcement_log": [
      "Se refuerzan ejes editoriales comunes entre asignaturas.",
      "Se mantiene gate crítico de JSON parseable.",
      "Se consolida identidad UnADM como núcleo transversal.",
      "No se eliminan reglas útiles previas."
    ]
  }
}
```