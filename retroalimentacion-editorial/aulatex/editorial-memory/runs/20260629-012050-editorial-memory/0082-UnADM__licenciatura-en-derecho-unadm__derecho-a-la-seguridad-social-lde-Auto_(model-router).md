```json
{
  "summary": [
    "Se sincroniza ADN editorial estable desde actividad transversal sin mezclar contenido tematico.",
    "Se refuerza patron comun UnADM: problema, fundamento, evidencia, analisis propio y conclusion.",
    "Se preserva identidad institucional, estructura reusable y control de calidad.",
    "La compresion aplicada es union-dedupe sin regresion ni recorte.",
    "El destino mantiene cerebro editorial minimo y expandible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino; marcar divergencias como [supuesto].",
    "Conservar trazabilidad de reglas heredadas provisionales.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Usar README de materia como canon estructural local.",
    "Alinear toda entrega a cinco ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Separar claramente marco, analisis propio y cierre.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Definir objetivo y problema juridico desde el inicio.",
    "Sustentar afirmaciones con normas, doctrina o evidencia verificable.",
    "Incluir postura academica propia; evitar solo descripcion.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente salidas no estructuradas del ciclo 1.",
    "Confirmar respaldo o marca [supuesto] en toda afirmacion relevante.",
    "Verificar coherencia entre consigna, desarrollo y conclusion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales consistentes en todos los .tex.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente central.",
    "No inventar referencias; agregar solo fuentes verificables.",
    "Mantener metadatos minimos completos en cada entrada.",
    "Validar correspondencia entre citas en texto y BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Evitar transferir redaccion literal o contenido tematico ajeno.",
    "Propagar recursivamente solo tras validacion estructural.",
    "Mantener bandera de riesgo por antecedentes no parseables en ciclo 1."
  ],
  "open_questions": [
    "Confirmar norma de citacion juridica exigida por la materia [supuesto].",
    "Verificar consignas locales de actividades para ajustar profundidad.",
    "Confirmar datos pendientes de plantilla institucional."
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
        "Integridad academica con citas verificables",
        "Normalizacion estructurada obligatoria"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Materia destino con datos curriculares oficiales",
        "Ejes juridicos definidos por programa analitico"
      ]
    },
    "essence": [
      "Problema juridico delimitado",
      "Marco normativo verificable",
      "Evidencia pertinente",
      "Analisis propio sustentado",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Servir como cerebro editorial persistente y reusable.",
      "Garantizar coherencia institucional y calidad academica.",
      "Permitir sincronizacion transversal sin perdida de identidad."
    ],
    "style_markers": [
      "Frases cortas y accionables",
      "Etiquetado explicito de [supuesto]",
      "Separacion visible entre marco, analisis y cierre",
      "Cierre con utilidad profesional"
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo",
      "Exponer marco normativo",
      "Contrastar evidencia",
      "Fijar postura propia",
      "Concluir con implicacion practica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        }
      ],
      "evidence": [
        "README y programa analitico del destino definen estructura y ejes.",
        "Reglas institucionales UnADM heredadas y validadas.",
        "Control de calidad aplicado en ciclo 1."
      ]
    },
    "reinforcement_log": [
      "Se refuerza patron editorial comun transversal.",
      "Se preserva identidad UnADM sin mezclar contenidos.",
      "Se consolida compresion lossless por deduplicacion."
    ]
  }
}
```