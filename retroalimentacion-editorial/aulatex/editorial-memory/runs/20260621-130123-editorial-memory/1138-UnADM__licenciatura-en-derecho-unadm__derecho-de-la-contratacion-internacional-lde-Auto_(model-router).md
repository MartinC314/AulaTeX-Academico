```json
{
  "summary": [
    "Se consolida un cerebro editorial mínimo para la materia Derecho de la Contratación Internacional.",
    "Se sincronizan abstracciones editoriales estables desde una actividad no equivalente.",
    "Se preservan reglas UnADM, estructura reusable y gates de calidad sin regresión.",
    "La compresión aplicada es lossless por unión y deduplicación semántica.",
    "Se mantiene incidente histórico de salidas no JSON parseables como alerta activa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar el nombre exacto de la asignatura en todos los artefactos.",
    "Vincular toda entrega a la Licenciatura en Derecho.",
    "Marcar como supuesto cualquier dato no confirmado por planeación oficial.",
    "Conservar trazabilidad explícita de reglas heredadas entre nodos.",
    "Usar la carpeta de la materia como punto de entrada canónico."
  ],
  "structure_rules": [
    "Alinear toda entrega al esquema base: problema, conceptos o normas, análisis propio y conclusión.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar claramente marco normativo/doctrinal y postura propia.",
    "Cerrar siempre con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el formato final al producto solicitado por la planeación."
  ],
  "activity_rules": [
    "Identificar el problema jurídico o social que activa la actividad.",
    "Sustentar cada afirmación con norma, doctrina o evidencia verificable.",
    "Diferenciar resumen descriptivo y criterio propio del estudiante.",
    "Declarar límites del análisis cuando falte información en la consigna.",
    "Incluir el producto exacto solicitado por la planeación semanal."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar memoria.",
    "Confirmar respaldo bibliográfico de toda afirmación normativa.",
    "Verificar consistencia entre README, programa analítico y plantilla LaTeX.",
    "No propagar rutas o archivos con placeholders sin normalización previa."
  ],
  "latex_rules": [
    "Mantener clase article en español con formato letterpaper.",
    "Conservar macros institucionales de curso y universidad.",
    "Evitar cambios de paquetes sin justificación editorial verificable.",
    "Usar nombres de archivo normalizados y sin tokens sin expandir.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el BibTeX local de la materia como repositorio principal.",
    "No inventar fuentes; registrar solo documentos consultables.",
    "Priorizar fuentes institucionales UnADM y derecho aplicable.",
    "Agregar fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas si no fueron usadas en la actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "No sobrescribir reglas locales más específicas.",
    "Aplicar deduplicación semántica, no recorte textual.",
    "Mantener alertas de incidentes institucionales hasta su resolución.",
    "Propagar recursivamente solo tras validación de JSON y estructura."
  ],
  "open_questions": [
    "Confirmar planeación oficial de actividades de la asignatura.",
    "Definir formato uniforme de citas jurídicas.",
    "Confirmar checklist mínimo por tipo de producto.",
    "Resolver definitivamente placeholders y rutas corruptas del README.",
    "Confirmar resolución del incidente histórico de JSON no parseable."
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
        "Entrada canónica por carpeta de materia",
        "Trazabilidad de herencia editorial"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2",
        "Asignatura obligatoria de 8 créditos",
        "Enfoque en transferencia profesional"
      ]
    },
    "essence": [
      "Problema jurídico como detonador del análisis",
      "Marco normativo y doctrinal verificable",
      "Postura académica propia",
      "Conclusión jurídica aplicable",
      "Identidad institucional consistente"
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad, fundamento jurídico y transferencia profesional.",
      "Convertir planeaciones en entregables estructurados y evaluables."
    ],
    "style_markers": [
      "Supuestos explícitos cuando falte información",
      "Separación clara entre descripción y análisis",
      "Cierre con criterio jurídico aplicable",
      "Consistencia terminológica e institucional"
    ],
    "argumentative_patterns": [
      "Problema → marco normativo → evidencia → análisis → conclusión",
      "Afirmación jurídica → fuente → interpretación propia",
      "Consigna → producto alineado → validación final"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica",
        "Normalización estructurada",
        "Compresión lossless",
        "Trazabilidad editorial"
      ],
      "citations": [
        "unadmMallaDerecho2024",
        "unadmSitioWeb"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se activa por una cuestión jurídica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica",
          "kind": "supports",
          "justification": "La conclusión debe sostenerse en norma o doctrina verificable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay reutilización segura."
        }
      ],
      "evidence": [
        "README y programa analítico de la materia",
        "BibTeX local institucional",
        "Registros de incidentes de salida no estructurada"
      ]
    },
    "reinforcement_log": [
      "Se refuerza identidad UnADM en nodo de materia.",
      "Se estabilizan ejes editoriales transferibles.",
      "Se mantiene gate de bloqueo por JSON no parseable.",
      "Se preserva trazabilidad desde nodo de actividad origen."
    ]
  }
}
```