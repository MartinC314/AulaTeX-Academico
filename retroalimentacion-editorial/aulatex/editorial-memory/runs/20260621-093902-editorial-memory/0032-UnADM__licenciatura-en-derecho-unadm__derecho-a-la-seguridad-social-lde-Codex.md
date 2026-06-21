{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho y Derecho a la Seguridad Social.",
    "Se preservan reglas estables reutilizables: identidad UnADM, estructura por ejes, evidencia verificable y cierre juridico.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se refuerza bloqueo de propagacion para salidas no JSON parseable y normalizacion previa obligatoria.",
    "No se transfiere contenido tematico especifico de Filosofia; solo abstracciones editoriales estables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar solo union-dedupe."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Alinear cada entrega a ejes estables: problema, conceptos/norma, evidencia, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en marco conceptual-normativo, analisis y cierre.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar formato y alcance al producto solicitado por la planeacion semanal."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Resolver marcadores o tokens sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas generales validadas, no redaccion literal.",
    "Mantener reglas curriculares especificas solo dentro de la misma materia.",
    "Transferir transversalmente patrones de calidad, estructura y trazabilidad.",
    "Preservar alerta historica: ciclo 1 requiere normalizacion manual si reaparece.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial o solo operativo [supuesto].",
    "Confirmar datos faltantes de plantilla (figura docente) cuando exista fuente oficial.",
    "Verificar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto]."
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
      "Marco normativo y conceptual pertinente.",
      "Evidencia verificable y trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables sin perder identidad institucional.",
      "Sostener memoria editorial persistente con compresion lossless y sin regresion.",
      "Habilitar propagacion segura entre nodos mediante reglas estructurales estables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Encuadrar problema y objetivo.",
      "Exponer marco normativo/doctrinal aplicable.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia con sustento.",
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
        "Conclusion juridica transferible"
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
          "source": "Identidad institucional UnADM",
          "target": "Coherencia editorial transversal",
          "kind": "supports",
          "justification": "Mantiene tono, formato y trazabilidad comun entre nodos."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion confiable."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicacion ni perdida."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes juridicos de la materia.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Historial institucional exige normalizacion de salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 32: se transfirieron solo abstracciones estables por relacion transversal.",
      "Ciclo 32: se preservaron reglas locales del destino sin mezclar contenido tematico de Filosofia.",
      "Ciclo 32: se reforzaron gates de JSON parseable, evidencia y trazabilidad [supuesto].",
      "Ciclo 32: se mantuvo estrategia progresiva y conservadora sin eliminacion de reglas utiles."
    ]
  }
}