```json
{
  "summary": [
    "Se refuerza la sincronización transversal entre actividades y materias no equivalentes.",
    "Se heredan abstracciones editoriales estables sin transferir contenido temático.",
    "Se consolida el patrón común: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Se preserva identidad UnADM, control de calidad y compresión lossless por unión-dedupe.",
    "La materia destino mantiene autonomía temática en seguridad social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "Usar carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear toda entrega al patrón transversal de cinco ejes.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar claramente marco normativo, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "Tomar README y programa analítico del destino como canon local."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Incluir postura académica propia sustentada.",
    "Evitar productos solo descriptivos.",
    "Verificar coherencia entre problema, desarrollo y conclusión.",
    "Ajustar formato al producto solicitado en la planeación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Confirmar estructura mínima completa antes de propagar.",
    "Validar que toda afirmación tenga respaldo o marca [supuesto].",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresión sobre reglas útiles previas."
  ],
  "latex_rules": [
    "Mantener codificación correcta en español.",
    "Conservar claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Normalizar nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Conservar metadatos mínimos completos.",
    "Distinguir bibliografía base de bibliografía de actividad.",
    "Usar el .bib local del destino como fuente central.",
    "Marcar fuentes faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables.",
    "Evitar transferir redacción literal entre nodos no equivalentes.",
    "Propagar recursivamente solo tras validación de JSON y estructura.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Mantener bandera de riesgo por salidas no parseables previas."
  ],
  "open_questions": [
    "Confirmar rúbricas específicas de actividades de seguridad social.",
    "Definir norma de citación requerida por la materia [supuesto].",
    "Confirmar productos exactos solicitados en planeaciones.",
    "Verificar vigencia de fuentes provisionales heredadas [supuesto]."
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
        "Normalización estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia: Derecho a la Seguridad Social",
        "Semestre 2, bloque 1, obligatoria, 8 créditos"
      ]
    },
    "essence": [
      "Problema jurídico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Análisis propio",
      "Conclusión jurídica transferible"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente reutilizable.",
      "Garantizar coherencia institucional y calidad académica.",
      "Facilitar transferencia profesional del aprendizaje."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco, análisis y cierre",
      "Marcado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo",
      "Contrastar evidencia",
      "Fijar postura propia",
      "Concluir con implicación práctica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible"
      ],
      "citations": [
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
          "justification": "La conclusión válida depende del fundamento legal."
        }
      ],
      "evidence": [
        "README y programa analítico del destino",
        "Archivo .bib local de seguridad social"
      ]
    },
    "reinforcement_log": [
      "Se hereda patrón editorial transversal sin mezclar contenidos.",
      "Se preservan reglas locales del destino.",
      "Se refuerza control de calidad y estructura común."
    ]
  }
}
```