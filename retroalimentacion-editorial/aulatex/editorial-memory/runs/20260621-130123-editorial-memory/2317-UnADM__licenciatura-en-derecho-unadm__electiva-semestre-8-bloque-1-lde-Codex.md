{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless entre actividad de origen y materia destino.",
    "Se preservan reglas institucionales UnADM, estructura reusable y control de calidad sin regresion.",
    "Se transfieren solo abstracciones estables; no se traslada contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerza normalizacion de placeholders y literales corruptos detectados en README y programa analitico del destino.",
    "Supuesto: el destino no define aun creditos oficiales ni nombre docente; se mantienen como pendientes."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener codigo provisional LDE-S8B1 hasta confirmacion oficial distinta.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No renombrar asignatura ni metadatos curriculares sin evidencia oficial."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos o fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Diferenciar claramente resumen de fuentes y postura propia.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar la carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local.",
    "No transferir redaccion literal desde nodos no equivalentes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de entrega final.",
    "Confirmar que rutas locales citadas existan y sean accesibles."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Completar campos pendientes de portada antes de entrega: figura docente y creditos si aplica.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico del destino.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas de identidad, estructura y calidad.",
    "Evitar propagar metadatos o contenidos tematicos propios de Filosofia del Derecho al destino electivo.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Mantener antecedente institucional: respuestas no estructuradas requieren normalizacion manual previa.",
    "Si falta consigna local, propagar solo patrones argumentativos estables y marcar supuestos."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la asignatura y codigo oficial si difieren del provisional.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar si existe consigna local de actividad que exija formato distinto de reporte o presentacion.",
    "Confirmar sustitucion definitiva de placeholders Slug en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Juridicamente preciso",
        "Claro y verificable",
        "Sobrio ante datos no confirmados"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Carpeta de materia como entrada canonica",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8, bloque 1, tipo Electiva",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema",
      "Conceptos y fuentes",
      "Analisis propio",
      "Conclusion juridica transferible",
      "Normalizacion estructurada antes de propagar"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y trazabilidad.",
      "Garantizar calidad institucional reusable entre nodos no equivalentes sin contaminar contexto."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables y reutilizables",
      "Postura propia sustentada",
      "Cierre juridico transferible",
      "Supuestos marcados"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia verificable -> inferencia juridica",
      "Descripcion breve -> posicion critica -> implicacion practica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y criterios minimos de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones y evita resumen sin fundamento."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin formato parseable no hay reutilizacion confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Previene errores por tokens sin expandir y rutas corruptas."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Ordena el desarrollo hacia aplicacion profesional."
        }
      ],
      "evidence": [
        "README local contiene placeholders Slug sin expandir.",
        "Programa analitico local fija ejes editoriales estables.",
        "Archivo bibliografico local ya define claves institucionales base.",
        "Antecedente heredado de salidas no parseables exige gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion semantica completada sin eliminar reglas utiles previas.",
      "Ciclo 8: reforzada regla de propagar solo abstracciones estables entre nodos transversales.",
      "Ciclo 8: reforzado gate de JSON parseable y consistencia cita-.bib.",
      "Ciclo 8: mantenidos vacios locales como preguntas abiertas con marca de supuesto."
    ]
  }
}