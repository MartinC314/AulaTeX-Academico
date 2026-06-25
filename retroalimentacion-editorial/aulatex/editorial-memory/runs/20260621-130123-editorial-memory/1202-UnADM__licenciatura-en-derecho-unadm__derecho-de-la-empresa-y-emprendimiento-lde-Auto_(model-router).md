```json
{
  "summary": [
    "Se consolida cerebro editorial mínimo transversal para la materia destino.",
    "Se transfieren abstracciones editoriales estables desde actividad no equivalente.",
    "Se preservan reglas institucionales UnADM y normalización estructurada.",
    "Se refuerza marco reusable: problema, conceptos, evidencia, análisis propio y conclusión.",
    "No se transfiere contenido doctrinal específico por no equivalencia disciplinar.",
    "Compresión aplicada por unión y deduplicación sin recorte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa académico.",
    "Respetar contexto curricular local confirmado.",
    "Marcar como supuesto cualquier dato no visible en consigna o archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canónico.",
    "Alinear entregables al flujo: problema, conceptos, evidencia, análisis propio, conclusión.",
    "Separar secciones de forma explícita y consistente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Conservar correspondencia entre .tex, presentación y .bib."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar problema jurídico o social activador.",
    "Distinguir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir análisis propio con postura argumentada.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "No eliminar reglas útiles previas durante fusión.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto."
  ],
  "latex_rules": [
    "Mantener plantilla base con metadatos institucionales completos.",
    "Corregir tokens de plantilla sin expandir antes de compilar.",
    "Usar codificación y acentos correctos en español.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Actualizar títulos y subtítulos por actividad."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Registrar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redacción literal o doctrina específica.",
    "Exigir normalización manual previa en ciclos iniciales.",
    "Propagar transversalmente identidad, estructura y gates de calidad."
  ],
  "open_questions": [
    "Confirmar rúbrica específica de evaluación de la materia.",
    "Confirmar si existe guía de citación jurídica distinta a la general.",
    "Confirmar parametrización del autor por actividad.",
    "Confirmar resolución definitiva de tokens Slug en README y programa analítico."
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
        "Trazabilidad bibliográfica",
        "Entrada canónica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre avanzado",
        "Enfoque aplicado",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Identidad institucional UnADM",
      "Normalización estructurada",
      "Problema jurídico",
      "Evidencia verificable",
      "Análisis propio",
      "Conclusión jurídica transferible",
      "Control explícito de supuestos"
    ],
    "reason_for_being": [
      "Orientar productos académicos con claridad y fundamento jurídico.",
      "Transformar planeación semanal en entregables estructurados.",
      "Asegurar transferencia del aprendizaje a la práctica profesional."
    ],
    "style_markers": [
      "Frases cortas y directas",
      "Supuestos marcados explícitamente",
      "Sin afirmaciones sin fuente",
      "Cierre aplicado a contexto profesional"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> análisis propio -> conclusión",
      "Marco normativo como soporte del criterio personal",
      "Coherencia entre pregunta guía y cierre"
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
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura válida no se transfiere memoria de forma segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere respaldo normativo y documental."
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
        "Programa analítico editorial",
        "Archivo .bib institucional"
      ]
    },
    "reinforcement_log": [
      "Se refuerza marco reusable transversal.",
      "Se preservan reglas institucionales UnADM.",
      "Se evita regresión y transferencia doctrinal indebida."
    ]
  }
}
```