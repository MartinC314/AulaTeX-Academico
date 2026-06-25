```json
{
  "summary": [
    "Se refuerza el cerebro editorial de la materia con abstracciones transversales estables.",
    "Se heredan ejes editoriales, gates de calidad y normalización estructurada desde actividad origen.",
    "La sincronización es conservadora: no se traslada contenido literal ni disciplina ajena.",
    "Se consolida identidad UnADM y patrón argumentativo reusable en actividades futuras."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear toda producción a Licenciatura en Derecho.",
    "Marcar como [supuesto] cualquier dato no visible en la consigna local.",
    "Tratar herencias no verificadas como provisionales hasta confirmación.",
    "Usar la carpeta de materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Usar el modelo transversal de cinco ejes: problema, conceptos, producto, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones funcionales y trazables.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el entregable al producto indicado en la planeación semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Explicitar postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y cierre."
  ],
  "quality_gates": [
    "Bloquear persistencia si la salida no es JSON parseable.",
    "Normalizar herencia no estructurada antes de propagar.",
    "Confirmar trazabilidad entre objetivo, evidencia y conclusión.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No degradar reglas útiles previas durante unión-dedupe."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX local con metadatos completos.",
    "Usar español académico con acentos correctos.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el .bib canónico local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales.",
    "No inventar referencias; declarar [supuesto] si falta una fuente.",
    "Separar bibliografía base de fuentes específicas de actividad.",
    "Conservar metadatos mínimos completos en cada entrada."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos laterales.",
    "Evitar transferir redacción literal entre materias no equivalentes.",
    "Aplicar propagación recursiva solo tras validación de estructura.",
    "Reutilizar gates de calidad institucional en actividades hijas.",
    "Normalizar manualmente herencias de ciclos previos si se reutilizan."
  ],
  "open_questions": [
    "Confirmar rúbrica específica de evaluación por actividad.",
    "Confirmar estilo de citación jurídica obligatorio.",
    "Definir alcance de fuentes: federales, locales o mixtas.",
    "Confirmar formato principal solicitado en cada actividad.",
    "Verificar nombre canónico definitivo del archivo .bib."
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
        "Integridad académica",
        "Citas verificables",
        "Carpeta como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 4, bloque 1",
        "Asignatura obligatoria",
        "Enfoque en contratos y obligaciones"
      ]
    },
    "essence": [
      "Modelo transversal de cinco ejes editoriales.",
      "Análisis jurídico propio sustentado.",
      "Conclusión operativa y transferible.",
      "Normalización estructurada como condición de memoria.",
      "Identidad institucional persistente."
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial entre actividades y materia.",
      "Facilitar reutilización segura de reglas editoriales.",
      "Evitar contaminación disciplinar en propagación lateral.",
      "Asegurar productos académicos verificables y transferibles."
    ],
    "style_markers": [
      "Supuestos explícitamente etiquetados.",
      "Secciones claras y funcionales.",
      "Cierre jurídico aplicado.",
      "Consistencia entre reporte, presentación y bibliografía."
    ],
    "argumentative_patterns": [
      "Problema delimitado al inicio.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio con evidencia.",
      "Conclusión jurídica aplicable.",
      "Trazabilidad entre objetivo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Contratos",
        "Obligaciones",
        "Problema jurídico",
        "Análisis jurídico propio",
        "Conclusión transferible",
        "Normalización estructurada",
        "Modelo transversal de cinco ejes"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige rigor y citas verificables."
        },
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
          "justification": "La conclusión surge del razonamiento sustentado."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "Evita propagar salidas no confiables."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia.",
        "Archivo .bib local con fuentes institucionales.",
        "Gates de calidad heredados y validados."
      ]
    },
    "reinforcement_log": [
      "Se heredan ejes editoriales sin pérdida.",
      "Se deduplican reglas repetidas sin recorte.",
      "Se refuerza normalización previa a propagación.",
      "Se consolida cerebro editorial mínimo de materia."
    ]
  }
}
```