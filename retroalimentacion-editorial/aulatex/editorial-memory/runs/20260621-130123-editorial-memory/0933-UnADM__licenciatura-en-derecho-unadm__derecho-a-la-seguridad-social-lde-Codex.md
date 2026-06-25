{
  "summary": [
    "Se sincroniza memoria transversal sin mezclar contenido tematico de Filosofia del Derecho en Seguridad Social.",
    "Se preservan reglas utiles previas del destino y del marco institucional UnADM por union-dedupe.",
    "Se refuerza patron editorial estable: problema, fundamento, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene gate critico: no propagar si la salida no es JSON parseable.",
    "Se actualiza canon local con README y programa analitico del destino como fuentes rectoras."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia del destino como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar sin regresion."
  ],
  "structure_rules": [
    "Tomar README de la materia como canon de estructura de archivos y productos.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, evidencia, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en encuadre, marco normativo/doctrinal, analisis propio, cierre y referencias.",
    "Ajustar el formato final al producto solicitado en planeacion semanal."
  ],
  "activity_rules": [
    "Delimitar desde el inicio el problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas; exigir analisis argumentado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar correspondencia entre citas en texto y archivo .bib local.",
    "Confirmar compresion lossless por union-dedupe, sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener consistencia de metadatos institucionales y curriculares en .tex.",
    "Usar codificacion y acentos correctos en español para .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Resolver marcadores o tokens sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia frente a bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables, no redaccion literal.",
    "Propagar reglas curriculares especificas solo dentro de la misma materia.",
    "Propagar transversalmente reglas generales de integridad, estructura y calidad.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos tempranos.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin reemplazar."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, juridica mexicana o institucional) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial o auxiliar interno [supuesto].",
    "Confirmar campos obligatorios de portada para actividades evaluables (figura docente, grupo, matricula) [supuesto].",
    "Confirmar si cada actividad debe usar .bib unico de materia o anexar .bib especifico [supuesto]."
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
      "Marco normativo y doctrinal verificable.",
      "Evidencia trazable en fuentes reales.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables con utilidad academica y profesional.",
      "Sostener continuidad editorial entre actividades, materia y nivel institucional sin perder contexto local."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con transferencia a practica juridica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
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
          "source": "JSON parseable",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion confiable."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin perdida ni duplicado."
        },
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
          "justification": "La conclusion necesita fundamento legal verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia transversal de entregas",
          "kind": "supports",
          "justification": "Asegura consistencia entre nodos no equivalentes."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo derecho-a-la-seguridad-social.bib confirma base normativa local.",
        "Historial institucional registra riesgo por salidas no parseables y exige normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: transferencia transversal conservadora aplicada.",
      "Se mantuvieron reglas locales del destino y se agregaron solo abstracciones estables del origen.",
      "Se elimino duplicacion semantica en formulaciones repetidas.",
      "No se incorporaron fuentes nuevas no verificadas.",
      "Se preservo politica de no regresion y compresion lossless por deduplicacion."
    ]
  }
}