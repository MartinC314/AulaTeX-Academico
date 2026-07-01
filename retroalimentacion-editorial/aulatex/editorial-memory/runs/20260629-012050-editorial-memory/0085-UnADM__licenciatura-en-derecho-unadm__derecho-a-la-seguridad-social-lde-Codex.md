{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron comun reusable: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva alerta de normalizacion manual para salidas no parseables de ciclos previos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad de origen cuando una regla sea provisional."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar el problema juridico desde el inicio.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivo y resolver marcadores o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias realmente consultables y verificables.",
    "No inventar fuentes.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y estables.",
    "Transferir abstracciones editoriales; no transferir redaccion literal ni contenido tematico de origen.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Conservar bandera de riesgo por antecedentes de salida no parseable en ciclos previos."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar rubrica oficial por actividad para ajustar profundidad argumentativa [supuesto].",
    "Confirmar datos pendientes de plantilla (figura docente) cuando exista fuente oficial.",
    "Verificar si persiste alguna fuente provisional heredada fuera del dominio Derecho [supuesto]."
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
      "Problema juridico delimitado.",
      "Marco normativo y doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables y utiles para practica profesional.",
      "Preservar identidad institucional y calidad tecnica en cada entrega LaTeX.",
      "Garantizar memoria editorial persistente sin perdida ni regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de reglas provisionales."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
      "Contrastar evidencia pertinente.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
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
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida y sin duplicados."
        }
      ],
      "evidence": [
        "README local define estructura canonica y control editorial.",
        "Programa analitico local define proposito y ejes juridicos.",
        "Archivo .bib local confirma base normativa verificable.",
        "Historial institucional reporta salidas no parseables que exigen normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se reforzo patron transversal comun sin contaminar tematica local del destino.",
      "Ciclo 2: se mantuvo control estricto de JSON parseable y normalizacion previa a propagacion.",
      "Ciclo 2: se consolidaron reglas de identidad, estructura, calidad y bibliografia con union-dedupe.",
      "Ciclo 2: se preservaron reglas utiles heredadas y se marcaron vacios como [supuesto]."
    ]
  }
}