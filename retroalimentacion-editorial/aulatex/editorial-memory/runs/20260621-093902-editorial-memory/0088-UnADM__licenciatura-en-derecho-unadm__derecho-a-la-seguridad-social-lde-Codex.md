{
  "summary": [
    "Se conserva identidad UnADM y enfoque juridico de la materia destino.",
    "Se refuerza sincronizacion transversal con reglas estables de estructura y calidad.",
    "Se mantiene compresion lossless por union-dedupe sin recorte.",
    "Se preserva control de riesgo por salidas no parseables en ciclos previos.",
    "Se integra patron comun reutilizable: problema, fundamento, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, evidencia, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en marco conceptual-normativo, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar al inicio el problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente toda salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Comprobar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivos y corregir marcadores corruptos antes de compilar.",
    "Mantener metadatos institucionales y curriculares consistentes en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; agregar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Validar que toda cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Propagar reglas curriculares solo dentro de la misma materia.",
    "Propagar transversalmente reglas de calidad, JSON parseable y trazabilidad de supuestos.",
    "Mantener bandera de riesgo de ciclos con salida no parseable hasta saneamiento completo.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin regresion."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 sigue vigente en plantillas [supuesto].",
    "Verificar si las plantillas Actividad-1 ya existen y son canonicas en todos los artefactos.",
    "Confirmar campos pendientes de portada (figura docente) para cierre operativo.",
    "Validar vigencia periodica de URLs normativas en .bib local."
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
      "Fundamento normativo verificable.",
      "Evidencia pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para la practica.",
      "Preservar continuidad editorial entre actividades sin perder contexto local.",
      "Garantizar trazabilidad, verificabilidad y consistencia institucional."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Seguridad social en Mexico"
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
          "justification": "Sin delimitacion del problema no hay analisis pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura legible y estable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Seguridad social en Mexico",
          "kind": "develops",
          "justification": "La materia aplica el marco editorial institucional al contenido disciplinar local."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y artefactos.",
        "Programa analitico define proposito y ejes de trabajo juridico.",
        "Archivo .bib local contiene base institucional y normativa verificable.",
        "Historial previo registra necesidad de normalizacion por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates criticos de parseo JSON y normalizacion.",
      "Se reforzo patron transversal reusable sin mezclar contenido literal del origen.",
      "Se mantuvo prioridad del contexto local del destino sobre herencias no verificadas.",
      "Se preservo politica de no regresion editorial en ciclo 88."
    ]
  }
}