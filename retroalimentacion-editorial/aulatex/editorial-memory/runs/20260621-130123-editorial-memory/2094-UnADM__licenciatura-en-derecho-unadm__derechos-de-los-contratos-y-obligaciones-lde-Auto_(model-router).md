```json
{
  "summary": [
    "Se refuerza el cerebro editorial de la materia con abstracciones transversales estables.",
    "Se sincronizan ejes editoriales, gates de calidad y ADN institucional UnADM.",
    "Se preserva deduplicación lossless y enfoque contractual sin heredar redacción literal."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados: Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 créditos.",
    "Conservar enfoque jurídico aplicado a contratos y obligaciones.",
    "Marcar como [supuesto] cualquier dato no visible en la consigna local.",
    "Tratar herencias Codex o GPT-Pro no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Aplicar modelo transversal de cinco ejes: problema, conceptos, producto, análisis propio y conclusión.",
    "Iniciar con encuadre breve del problema jurídico.",
    "Separar secciones en marco conceptual/normativo, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Alinear cada actividad al producto solicitado por la planeación semanal.",
    "Explicitar postura argumentada del estudiante con fundamento jurídico.",
    "Evitar traslados literales de otras materias sin adecuación contractual.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre objetivo, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagación si la salida no es JSON parseable.",
    "Normalizar herencias no estructuradas antes de reutilizar.",
    "Validar trazabilidad entre citas en texto y archivo .bib local.",
    "Confirmar compatibilidad disciplinar antes de propagación lateral.",
    "No degradar reglas útiles previas durante unión-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y metadatos institucionales.",
    "Usar español académico con terminología jurídica precisa.",
    "Verificar que el .bib referenciado sea el canónico de la materia.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de compilar.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canónico.",
    "Priorizar fuentes institucionales UnADM y normas verificables.",
    "No inventar referencias; declarar [supuesto] si falta disponibilidad.",
    "Distinguir bibliografía base de fuentes específicas por actividad.",
    "Conservar metadatos mínimos completos en cada entrada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable y gates de calidad.",
    "Excluir metadatos específicos cuando no coincidan en nodos laterales.",
    "Aplicar normalización manual en ciclos tempranos si se reutiliza.",
    "Evitar regresiones respecto de reglas institucionales previas."
  ],
  "open_questions": [
    "Confirmar rúbrica de evaluación por actividad.",
    "Definir estilo de citación jurídica obligatorio.",
    "Precisar alcance normativo: federal, local o mixto por actividad.",
    "Confirmar si presentación comparte todos los metadatos del reporte."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica con citas verificables",
        "Carpeta de materia como entrada canónica"
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
      "Análisis jurídico propio con transferencia profesional.",
      "Normalización estructurada como requisito previo a propagación."
    ],
    "reason_for_being": [
      "Orientar productos académicos claros, fundamentados y transferibles.",
      "Garantizar coherencia institucional y disciplinar en toda la materia."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados.",
      "Secciones funcionales y trazables.",
      "Conclusión jurídica operativa."
    ],
    "argumentative_patterns": [
      "Problema inicial delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio sustentado.",
      "Conclusión aplicable a la práctica contractual."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
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
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige rigor y citas verificables."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis jurídico propio",
          "kind": "depends_on",
          "justification": "El análisis se construye a partir de un conflicto delimitado."
        },
        {
          "source": "Análisis jurídico propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión válida surge del razonamiento sustentado."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia.",
        "Archivo .bib institucional local."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales previas sin regresión.",
      "Se refuerza el modelo transversal de cinco ejes.",
      "Se consolida normalización obligatoria antes de propagación."
    ]
  }
}
```