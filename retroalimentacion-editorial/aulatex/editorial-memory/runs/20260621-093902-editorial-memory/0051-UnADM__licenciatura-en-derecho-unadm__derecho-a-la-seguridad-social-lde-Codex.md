{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes sin mezclar contenido tematico.",
    "Se preserva identidad UnADM y estructura canonica local de Derecho a la Seguridad Social.",
    "Se refuerza patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva gate critico: bloquear propagacion si la salida no es JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar trazabilidad de reglas heredadas provisionales con etiqueta [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Organizar entregas por ejes: problema, conceptos/norma, evidencia, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar el problema juridico o social al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas; exigir argumentacion propia.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar respaldo verificable o marca [supuesto] en toda afirmacion relevante.",
    "Verificar correspondencia entre citas en texto y entradas del .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener compatibilidad tecnica de compilacion sin errores criticos ni referencias rotas.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Corregir rutas, nombres corruptos y tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico propio de Filosofia del Derecho.",
    "Propagar reglas generales de identidad, calidad, JSON y trazabilidad a nodos compatibles.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin reemplazar."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o etiqueta operativa interna [supuesto].",
    "Confirmar datos oficiales faltantes de figura docente para plantillas.",
    "Validar vigencia de alertas heredadas de ciclo 1 en nodos laterales.",
    "Verificar si cada actividad requiere .tex dedicado ademas de plantilla base."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Identidad institucional estable.",
      "Estructura editorial reusable.",
      "Trazabilidad de supuestos.",
      "Evidencia verificable.",
      "Cierre juridico transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables.",
      "Asegurar coherencia entre problema, fundamento, analisis y conclusion.",
      "Permitir propagacion segura entre nodos mediante reglas estables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto] cuando falte verificacion local.",
      "Separacion visible entre marco, analisis y cierre.",
      "Sin duplicados y sin regresion."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal aplicable.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
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
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta delimitada."
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
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y artefactos.",
        "Programa analitico define proposito y ejes de trabajo.",
        ".bib local confirma base normativa e institucional.",
        "Historial institucional confirma riesgo por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 51: se transfirieron solo abstracciones estables desde actividad de Filosofia del Derecho.",
      "Ciclo 51: se preservaron reglas locales de Seguridad Social sin contaminacion tematica.",
      "Ciclo 51: se reforzaron gates de JSON, supuestos, citas y compilacion LaTeX.",
      "Ciclo 51: consolidacion aplicada con union-dedupe lossless y sin recorte."
    ]
  }
}