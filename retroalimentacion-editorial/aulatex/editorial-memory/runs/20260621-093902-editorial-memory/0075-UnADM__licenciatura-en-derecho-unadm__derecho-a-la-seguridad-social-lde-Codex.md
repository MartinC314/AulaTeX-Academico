{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Seguridad Social sin mezclar contenido tematico.",
    "Se preservan reglas utiles del destino y se refuerza patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se confirma normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se integra canon local del destino desde README y programa analitico como base operativa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Alinear cada entrega a ejes: problema, conceptos o norma, producto, analisis y conclusion.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Alinear formato y alcance al producto solicitado en planeacion semanal.",
    "Registrar solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema juridico al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar rutas, nombres y tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Agregar solo referencias realmente consultables con metadatos minimos completos.",
    "No inventar fuentes.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Reutilizar gates de calidad, identidad y estructura en nodos laterales compatibles.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables en ciclos tempranos.",
    "Aplicar propagacion recursiva solo tras validar JSON y estructura.",
    "Conservar trazabilidad de reglas provisionales con etiqueta [supuesto]."
  ],
  "open_questions": [
    "Confirmar si LDE-S2B1 es codigo oficial institucional o etiqueta local [supuesto].",
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar datos oficiales de figura docente para portada cuando existan.",
    "Confirmar si todas las plantillas de Actividad 1 del README ya estan materializadas.",
    "Verificar vigencia periodica de URLs normativas en .bib local."
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
      "Convertir cada consigna en producto juridico verificable y util profesionalmente.",
      "Preservar identidad institucional con control tecnico de calidad editorial.",
      "Garantizar memoria persistente sin perdida por deduplicacion."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con implicacion practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y conceptos clave.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con consecuencia juridica aplicable."
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
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura requiere estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Evita regresiones y conserva reglas nucleares."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana solidez con respaldo trazable."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y archivos base.",
        "Programa analitico define proposito y ejes juridicos del destino.",
        "Bib local contiene base institucional y normativa verificable.",
        "Historial de ciclos reporta salidas no parseables y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 75: se preservan reglas locales del destino y se incorporan abstracciones estables del origen.",
      "Ciclo 75: se refuerza gate JSON parseable como requisito de propagacion recursiva.",
      "Ciclo 75: se evita transferencia de contenido tematico de Filosofia y se mantiene enfoque de Seguridad Social.",
      "Ciclo 75: se consolida ADN editorial minimo, reconstruible y sin regresion."
    ]
  }
}