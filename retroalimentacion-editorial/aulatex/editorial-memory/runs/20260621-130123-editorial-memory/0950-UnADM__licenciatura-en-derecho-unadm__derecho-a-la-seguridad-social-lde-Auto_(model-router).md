```json
{
  "summary": [
    "Se consolida cerebro editorial de la materia Derecho a la Seguridad Social con identidad UnADM.",
    "Se sincronizan abstracciones editoriales estables desde un nodo no equivalente sin mezclar contenido temático.",
    "Se preserva patrón transversal: problema, marco, evidencia, análisis propio y conclusión jurídica.",
    "Se refuerza control institucional: JSON parseable, normalización previa y compresión union-dedupe.",
    "Se mantiene enfoque progresivo y conservador sin regresión de reglas válidas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de la materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "No sobrescribir reglas válidas previas; unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de la materia como canon estructural.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, análisis, evidencia y conclusión.",
    "Usar estructura mínima: portada, desarrollo por ejes, conclusión y referencias.",
    "Mantener consistencia entre reporte, presentación y programa analítico.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Delimitar problema jurídico o social desde el inicio.",
    "Vincular desarrollo con normas, doctrina y datos pertinentes.",
    "Incluir postura académica propia sustentada.",
    "Distinguir hechos, conceptos, normas y opinión.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "Ajustar formato al producto solicitado en la planeación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Verificar coherencia entre objetivo, desarrollo y conclusión.",
    "Confirmar respaldo verificable o marca de [supuesto] en afirmaciones relevantes.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Evitar eliminación de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales consistentes en todos los .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo referencias verificables y consultables.",
    "No inventar fuentes; marcar faltantes como pendientes.",
    "Mantener metadatos mínimos completos en cada entrada."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferencia de redacción literal o contenido temático ajeno.",
    "Propagar reglas generales de identidad, estructura y calidad.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida para la materia [supuesto].",
    "Definir figura docente en plantilla cuando exista dato oficial.",
    "Verificar vigencia de fuentes normativas antes de entrega final.",
    "Confirmar productos específicos solicitados por cada planeación."
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
        "Normalización estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia: Derecho a la Seguridad Social",
        "Semestre 2, bloque 1, obligatoria, 8 créditos",
        "Uso del programa analítico como guía"
      ]
    },
    "essence": [
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio sustentado",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Convertir consignas en productos jurídicos verificables.",
      "Asegurar coherencia institucional y calidad académica.",
      "Facilitar reutilización editorial sin pérdida ni regresión."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación clara entre marco, análisis y cierre",
      "Etiquetado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo y doctrinal",
      "Contrastar evidencia relevante",
      "Fijar postura propia sustentada",
      "Concluir con implicación práctica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "JSON parseable",
        "Compresión union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una cuestión jurídica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La reutilización segura exige estructura válida."
        },
        {
          "source": "Compresión union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas útiles sin pérdida ni duplicación."
        }
      ],
      "evidence": [
        "README y programa analítico del destino definen estructura y propósito.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Reglas institucionales UnADM vigentes y verificables."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales y de calidad sin regresión.",
      "Se refuerza patrón editorial transversal reusable.",
      "Se mantiene separación temática entre materias no equivalentes.",
      "Se consolida cerebro editorial mínimo reconstruible."
    ]
  }
}
```