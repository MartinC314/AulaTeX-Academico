{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de reglas estables.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se refuerza requisito de JSON parseable antes de propagacion recursiva.",
    "Se confirma canon local del destino: README, programa analitico y .bib de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin regresion."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Alinear cada entrega a ejes: problema, fundamento conceptual-normativo, evidencia, analisis propio y conclusion juridica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Ajustar formato final al producto solicitado en planeacion semanal.",
    "Registrar solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Vincular desarrollo con normas, doctrina y datos pertinentes al tema.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar coherencia entre objetivo, desarrollo y conclusion.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar correspondencia entre citas en texto y entradas del .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener metadatos institucionales y de curso consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Resolver marcadores o tokens sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Priorizar fuentes institucionales UnADM y marcos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar referencias nuevas solo si son verificables y pertinentes al producto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir a laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Preservar reglas locales de seguridad social como capa prioritaria del destino.",
    "Mantener bandera historica de riesgo por salidas no parseables en ciclos previos.",
    "Aplicar siempre compresion lossless por union-dedupe."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o juridica institucional) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todas las plantillas [supuesto].",
    "Confirmar datos faltantes de figura docente para portada cuando exista fuente oficial.",
    "Validar si todas las actividades requieren reporte, presentacion o ambos segun planeacion.",
    "Verificar vigencia periodica de URLs normativas en el .bib local."
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
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia pertinente y trazable.",
      "Analisis propio con postura sustentada.",
      "Conclusion juridica aplicable a practica profesional."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables.",
      "Asegurar coherencia entre identidad institucional, estructura academica y calidad tecnica.",
      "Permitir propagacion segura de memoria editorial entre nodos compatibles."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo-doctrinal.",
      "Contrastar evidencia relevante.",
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
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica gana validez con evidencia trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos y control editorial.",
        "Programa analitico define proposito y ejes de trabajo de la materia.",
        "Bib local contiene base normativa e institucional verificable.",
        "Historial institucional registra riesgo por salidas no parseables y exige normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida de contenido util.",
      "Se mantuvieron reglas nucleares heredadas: JSON parseable, normalizacion y trazabilidad.",
      "Se transfirieron solo abstracciones estables desde actividad de Filosofia del Derecho.",
      "Se evito trasladar contenido tematico especifico no pertinente a Seguridad Social.",
      "Se reforzo ADN editorial con foco en identidad, estructura reusable y gates de calidad."
    ]
  }
}