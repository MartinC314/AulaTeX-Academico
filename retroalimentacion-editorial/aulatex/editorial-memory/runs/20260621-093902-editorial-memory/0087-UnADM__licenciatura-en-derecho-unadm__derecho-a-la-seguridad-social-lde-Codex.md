{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia hacia materia de Seguridad Social sin mezclar contenido tematico.",
    "Se preservan reglas utiles previas del destino y se refuerzan abstracciones estables: identidad, estructura, calidad y trazabilidad.",
    "Se mantiene compresion lossless por union-dedupe y bloqueo de propagacion ante salida no parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar sin regresion.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README de materia y programa analitico como canon estructural local.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, evidencia, analisis propio y conclusion.",
    "Separar secciones minimas: encuadre, desarrollo, cierre y referencias.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte y presentacion."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Vincular desarrollo con marco normativo y doctrinal pertinente a seguridad social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos, norma, doctrina y opinion propia.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No asumir fuentes de otras semanas o materias como obligatorias sin verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Confirmar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener metadatos institucionales y curriculares consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Normalizar nombres de archivos cuando existan marcadores o tokens sin expandir.",
    "No copiar bloques LaTeX completos entre nodos; transferir solo reglas."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables y no redaccion literal.",
    "Propagar reglas curriculares especificas solo dentro de la misma materia.",
    "Propagar a laterales compatibles reglas generales de integridad, JSON y control bibliografico.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclos tempranos.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin sustituir contexto local."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa [supuesto].",
    "Confirmar datos oficiales de figura docente para portada cuando existan [supuesto].",
    "Verificar si persiste alguna fuente provisional heredada ajena a Derecho y depurarla [supuesto]."
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
      "Evidencia pertinente y trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util para practica profesional.",
      "Sostener continuidad editorial entre actividades con identidad institucional estable."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
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
          "justification": "No hay analisis solido sin pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana validez con respaldo trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README y programa analitico del destino definen canon estructural y ejes de trabajo.",
        "El .bib local del destino confirma base normativa e institucional verificable.",
        "Memoria heredada confirma necesidad de normalizacion ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se agrego patron transversal estable problema-conceptos-evidencia-analisis-conclusion.",
      "Se mantuvieron reglas locales de seguridad social y se evito traslado de contenido tematico de filosofia.",
      "Se reforzo gate de JSON parseable como condicion de propagacion recursiva."
    ]
  }
}