```json
{
  "summary": [
    "Se sincroniza ADN editorial transversal desde actividad de Filosofía del Derecho hacia la materia Derecho a la Seguridad Social.",
    "Se preservan reglas institucionales UnADM, estructura por ejes y control de calidad.",
    "La transferencia es por abstracciones editoriales estables, no por contenido temático.",
    "Se refuerza patrón común: problema, fundamento, evidencia, análisis propio y conclusión jurídica.",
    "Compresión aplicada por unión y deduplicación sin pérdida ni regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de la materia como punto de entrada canónico.",
    "Marcar como [supuesto] cualquier dato no visible en consigna o fuente local.",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales."
  ],
  "structure_rules": [
    "Alinear cada producto a cinco ejes: problema, conceptos/norma, producto, análisis y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar claramente marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Tomar README y programa analítico como canon estructural local."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Vincular el desarrollo con normas, doctrina o datos verificables.",
    "Incluir postura académica propia, no solo descripción.",
    "Verificar coherencia entre problema, desarrollo y conclusión.",
    "Ajustar formato y alcance al producto solicitado por la planeación semanal."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmación relevante tenga respaldo o marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Evitar eliminación de reglas útiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificación correcta en español en archivos .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "No inventar referencias; marcar faltantes como pendientes.",
    "Conservar metadatos mínimos verificables en cada entrada.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Verificar que cada cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales validadas a nodos laterales compatibles.",
    "Evitar transferir redacción literal o contenido temático ajeno.",
    "Aplicar compresión lossless por unión-dedupe en cada ciclo.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable.",
    "Propagar recursivamente solo después de validación estructural completa."
  ],
  "open_questions": [
    "Confirmar norma de citación requerida para la materia [supuesto].",
    "Definir figura docente en plantilla cuando exista dato oficial.",
    "Verificar si persisten fuentes provisionales heredadas no jurídicas [supuesto].",
    "Confirmar productos específicos de Actividad 1 en la materia destino."
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
      "Servir como cerebro editorial persistente para productos jurídicos UnADM.",
      "Garantizar coherencia, verificabilidad y transferencia profesional.",
      "Permitir reutilización segura entre materias no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Separación visible entre marco, análisis y cierre",
      "Marcado explícito de [supuesto]",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo y doctrinal",
      "Contrastar evidencia relevante",
      "Fijar postura propia sustentada",
      "Concluir con implicación jurídica práctica"
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
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico definen estructura canónica.",
        "Archivo .bib local confirma base normativa.",
        "Reglas heredadas validadas por deduplicación sin pérdida."
      ]
    },
    "reinforcement_log": [
      "Se reforzó patrón editorial común entre Filosofía del Derecho y Seguridad Social.",
      "Se preservó identidad UnADM sin mezclar contenido temático.",
      "Se consolidó control de calidad y propagación segura en ciclo 8."
    ]
  }
}
```