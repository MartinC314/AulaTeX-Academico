```json
{
  "summary": [
    "Se consolida un cerebro editorial transversal para la materia Derecho de la empresa y emprendimiento.",
    "Se transfieren abstracciones estables desde una actividad no equivalente.",
    "Se refuerza el marco reusable: problema, conceptos, evidencia, análisis propio y conclusión.",
    "Se preserva identidad institucional UnADM y control de supuestos.",
    "No se transfiere contenido doctrinal específico de Filosofía del Derecho.",
    "La compresión se realiza por unión y deduplicación, sin recorte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar el nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa académico.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canónico.",
    "Alinear cada entrega al esquema reusable: problema, conceptos, evidencia, análisis propio y conclusión.",
    "Conservar correspondencia entre .tex, presentación y .bib de la materia.",
    "Usar el programa analítico local para orientar productos académicos.",
    "Resolver tokens de plantilla sin expandir antes de compilar o propagar."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar el problema jurídico o social que activa la actividad.",
    "Distinguir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir análisis propio con postura argumentada.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "No eliminar reglas útiles previas durante fusión por unión-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Corregir placeholders y artefactos de plantilla antes de generar entregables."
  ],
  "latex_rules": [
    "Mantener plantilla base con metadatos institucionales completos.",
    "Actualizar títulos y subtítulos por actividad concreta.",
    "Verificar compilación sin errores críticos ni entornos abiertos.",
    "Usar codificación correcta en español.",
    "Mantener claves BibTeX estables y rutas de archivos existentes."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM.",
    "Registrar fuentes específicas de cada actividad en el .bib de la materia.",
    "Conservar metadatos mínimos completos.",
    "No citar fuentes no agregadas al .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos no equivalentes.",
    "Propagar recursivamente solo tras validar JSON y estructura mínima.",
    "Evitar transferir redacción literal o doctrina específica entre materias.",
    "Reforzar identidad, estructura reusable y gates de calidad en nodos vecinos."
  ],
  "open_questions": [
    "Confirmar consignas específicas de actividades de la materia destino.",
    "Confirmar rúbricas locales para ajustar profundidad argumentativa.",
    "Confirmar nombre canónico final del archivo .bib tras expansión de Slug.",
    "Confirmar parametrización del autor por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico",
        "Claro",
        "Jurídicamente preciso",
        "Argumentativo",
        "Orientado a transferencia profesional"
      ],
      "institutional": [
        "Alineación explícita con UnADM",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Carpeta de materia como entrada canónica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 6, bloque 2",
        "Materia obligatoria",
        "Enfoque aplicado"
      ]
    },
    "essence": [
      "Identidad institucional UnADM",
      "Normalización estructurada",
      "Problema jurídico",
      "Evidencia verificable",
      "Análisis propio",
      "Conclusión jurídica transferible",
      "Control de supuestos"
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad y fundamento jurídico.",
      "Transformar planeación semanal en entregables estructurados.",
      "Asegurar transferencia profesional en el cierre."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Supuestos explícitos",
      "Sin afirmaciones sin fuente",
      "Cierre aplicado a la práctica"
    ],
    "argumentative_patterns": [
      "Problema → conceptos → evidencia → análisis propio → conclusión",
      "Marco normativo como soporte del criterio personal",
      "Coherencia entre pregunta guía y conclusión"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Problema jurídico",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Integridad bibliográfica",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Define tono, formato y trazabilidad comunes."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no se propaga memoria."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias."
        }
      ],
      "evidence": [
        "README local de la materia",
        "Programa analítico local",
        "Archivo .bib institucional",
        "Reglas institucionales UnADM consolidadas"
      ]
    },
    "reinforcement_log": [
      "Se refuerza el marco reusable transversal.",
      "Se preservan reglas institucionales previas.",
      "Se evita regresión y transferencia doctrinal indebida.",
      "Se consolida memoria mínima para materia destino."
    ]
  }
}
```