{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron transversal estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se conserva normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se preserva compresion lossless por union-dedupe sin regresion.",
    "Se prioriza estructura canonica local de la materia y no se transfiere redaccion literal entre nodos no equivalentes."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia destino como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema juridico y pregunta guia al inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar salidas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo con marcadores corruptos antes de compilar.",
    "Mantener metadatos institucionales consistentes en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Registrar en .bib solo fuentes especificas de actividad cuando esten verificadas.",
    "Distinguir bibliografia base de materia frente a bibliografia puntual de actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Reutilizar reglas de identidad, estructura, calidad y trazabilidad de supuestos.",
    "Aplicar propagacion recursiva solo tras validar JSON y estructura.",
    "Mantener bandera de riesgo historica por ciclos con salida no parseable."
  ],
  "open_questions": [
    "Confirmar si existe norma de citacion obligatoria especifica para la materia [supuesto].",
    "Confirmar rubrica oficial de evaluacion por actividad en esta materia.",
    "Confirmar si el codigo local de curso LDE-S2B1 es oficial en documentos de entrega [supuesto].",
    "Verificar vigencia de reglas provisionales heredadas desde nodos ajenos a Derecho [supuesto]."
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
      "Evidencia y citas trazables.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Sostener coherencia institucional y calidad tecnica en toda entrega.",
      "Permitir reutilizacion segura entre nodos mediante reglas estables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Separacion explicita entre marco, analisis y cierre.",
      "Etiquetado de [supuesto] cuando falte verificacion.",
      "Cierre con transferencia practica."
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
          "justification": "Sin delimitacion del problema no hay argumentacion valida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere base legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicados."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos base.",
        "Programa analitico local define proposito y ejes de trabajo.",
        ".bib local contiene fuentes normativas e institucionales verificables.",
        "Historico institucional confirma necesidad de normalizacion ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se consolidan solo abstracciones estables de origen transversal.",
      "Ciclo 13: se preservan reglas locales del destino sin mezclar contenido tematico de filosofia.",
      "Ciclo 13: se refuerzan gates de JSON parseable, soporte de afirmaciones y control bibliografico.",
      "Ciclo 13: se mantiene estrategia progresiva y conservadora sin regresion."
    ]
  }
}