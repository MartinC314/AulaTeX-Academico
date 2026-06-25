```json
{
  "summary": [
    "Se consolida cerebro editorial minimo para materia destino con sincronizacion transversal.",
    "Se transfieren solo abstracciones editoriales estables desde actividad no equivalente.",
    "Se preservan reglas UnADM, estructura reusable y gates de calidad sin contenido doctrinal.",
    "Compresion aplicada por union-dedupe, sin regresion ni recorte.",
    "Se refuerza enfoque de semestre avanzado con transferencia profesional."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Respetar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Marcar como supuesto todo dato no confirmado por archivo local o consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear entregables al flujo reusable: problema, conceptos, evidencia, analisis propio, conclusion.",
    "Separar claramente marco normativo/doctrinal del analisis propio.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el producto final a la planeacion semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Identificar problema juridico o social relevante al ambito empresarial.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Conectar la conclusion con aplicacion practica empresarial."
  ],
  "quality_gates": [
    "Bloquear consolidacion si la salida no es JSON parseable.",
    "No eliminar reglas utiles previas durante fusion.",
    "Validar estructura minima completa antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar correspondencia entre consigna, desarrollo y conclusion."
  ],
  "latex_rules": [
    "Mantener consistencia de metadatos institucionales en macros.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens de plantilla sin expandir antes de compilar.",
    "Usar codificacion y acentos correctos en español."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y normatividad aplicable.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Distinguir bibliografia base de bibliografia de actividad."
  ],
  "propagation_hints": [
    "Propagar lateralmente solo abstracciones editoriales estables.",
    "Evitar transferir contenido doctrinal de materias no equivalentes.",
    "Exigir normalizacion manual previa en ciclos con salidas no estructuradas.",
    "Propagar gates de calidad y estructura reusable a materias hermanas.",
    "No propagar datos curriculares locales sin confirmacion."
  ],
  "open_questions": [
    "Confirmar consignas especificas de las primeras actividades de la materia.",
    "Confirmar guia de citacion juridica aplicable al ambito empresarial.",
    "Confirmar si el autor en plantilla debe parametrizarse por actividad.",
    "Confirmar correccion de tokens Slug en README y programa analitico.",
    "Confirmar fuentes obligatorias indicadas por la planeacion semanal."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica",
        "Trazabilidad bibliografica"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre avanzado",
        "Enfoque de transferencia profesional"
      ]
    },
    "essence": [
      "Problema juridico contextualizado",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica aplicable",
      "Control explicito de supuestos"
    ],
    "reason_for_being": [
      "Orientar productos academicos con fundamento juridico y aplicacion practica.",
      "Unificar criterios editoriales entre materias UnADM.",
      "Garantizar calidad y reutilizacion segura de memoria editorial."
    ],
    "style_markers": [
      "Frases cortas y directas",
      "Separacion clara entre hechos y opinion",
      "Cierre con transferencia profesional",
      "Consistencia estructural entre actividades"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion",
      "Marco normativo como soporte del criterio personal",
      "Coherencia entre pregunta guia y respuesta final"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no se transfiere memoria."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo normativo y documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias."
        }
      ],
      "evidence": [
        "README y programa analitico locales",
        "Bibliografia institucional UnADM",
        "Reglas editoriales consolidadas por union-dedupe"
      ]
    },
    "reinforcement_log": [
      "Se refuerza marco reusable transversal sin contenido doctrinal especifico.",
      "Se preservan gates de calidad y normalizacion estructurada.",
      "Se consolida identidad UnADM para materias de semestre avanzado."
    ]
  }
}
```