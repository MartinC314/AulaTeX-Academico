```json
{
  "summary": [
    "Se refuerza el cerebro editorial de la materia con abstracciones transversales estables.",
    "Se preserva identidad UnADM, normalización estructurada y cinco ejes editoriales.",
    "Se sincronizan patrones argumentativos y gates de calidad aplicables a contratos y obligaciones."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Marcar como [supuesto] cualquier dato no visible en la consigna local.",
    "Tratar herencias Codex o GPT-Pro no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Aplicar el modelo transversal de cinco ejes en toda actividad.",
    "Iniciar con encuadre breve del problema jurídico.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagación si la salida no es JSON parseable.",
    "Normalizar toda herencia no estructurada antes de reutilizarla.",
    "Confirmar trazabilidad entre objetivo, evidencia, argumento y cierre.",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "No degradar reglas útiles previas durante unión-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y metadatos institucionales.",
    "Mantener codificación y acentos correctos en español.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa analítico y nombres de archivo.",
    "Verificar que el .bib canónico sea derechos-de-los-contratos-y-obligaciones.bib.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normativa verificable.",
    "No inventar referencias; declarar [supuesto] si falta acceso.",
    "Distinguir bibliografía base de fuentes específicas por actividad.",
    "Conservar metadatos mínimos completos en cada entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Aplicar lateralmente tras validar compatibilidad disciplinar.",
    "Excluir redacción literal o contenido doctrinal específico de otras materias.",
    "Mantener compresión lossless por deduplicación."
  ],
  "open_questions": [
    "Confirmar guía formal de citación jurídica obligatoria para la materia.",
    "Precisar alcance de fuentes: federales, locales o mixtas según actividad.",
    "Confirmar rúbrica de evaluación por actividad.",
    "Confirmar formato requerido del producto principal en cada semana."
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
        "Semestre 4, bloque 1",
        "Enfoque en contratos y obligaciones"
      ]
    },
    "essence": [
      "Modelo transversal de cinco ejes editoriales",
      "Análisis jurídico aplicado",
      "Transferencia a la práctica profesional"
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y evidencia.",
      "Estandarizar calidad editorial entre actividades y materias LDE."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados",
      "Secciones funcionales y trazables",
      "Conclusión jurídica operativa"
    ],
    "argumentative_patterns": [
      "Problema inicial delimitado",
      "Marco conceptual y normativo pertinente",
      "Análisis propio sustentado",
      "Conclusión transferible"
    ],
    "knowledge_graph": {
      "concepts": [
        "Problema jurídico",
        "Contratos",
        "Obligaciones",
        "Análisis jurídico propio",
        "Conclusión transferible",
        "Normalización estructurada"
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
          "justification": "El análisis parte de un conflicto delimitado."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión válida surge del razonamiento sustentado."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "Evita contaminación editorial entre nodos."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia.",
        "Archivo .bib institucional local."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales UnADM.",
      "Se refuerza el modelo transversal de cinco ejes.",
      "Se consolida normalización obligatoria previa a propagación."
    ]
  }
}
```