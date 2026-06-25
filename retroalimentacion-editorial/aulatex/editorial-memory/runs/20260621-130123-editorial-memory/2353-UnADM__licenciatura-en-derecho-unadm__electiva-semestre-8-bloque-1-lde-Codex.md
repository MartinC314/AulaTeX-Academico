{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, estructura reusable y control de calidad.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se evita migrar contenido tematico especifico por no equivalencia de nodos.",
    "Se refuerza normalizacion de placeholders y control de salida JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Conservar autoria y matricula de plantilla mientras no exista instruccion institucional en contrario."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular cada actividad con un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con evidencia o marca de supuesto.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y literales corruptos en rutas o nombres de archivo antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de materia sin comandos no estandar injustificados.",
    "Usar codificacion compatible con espanol y acentos correctos en .tex y .bib.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Completar campos pendientes de portada antes de entrega final.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables segun consigna.",
    "No inventar referencias; incluir solo obras consultables.",
    "Registrar fuentes especificas por actividad y distinguirlas de bibliografia base.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura, calidad y trazabilidad.",
    "No propagar metadatos o contenidos tematicos especificos entre nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Mantener antecedente de normalizacion manual para salidas no estructuradas.",
    "Priorizar grafo conceptual transversal sobre redaccion literal."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva siguen no confirmados.",
    "Supuesto: nombre oficial definitivo de la electiva sigue no confirmado.",
    "Confirmar figura docente para portada.",
    "Confirmar si existe consigna local que exija formatos distintos a reporte/presentacion.",
    "Confirmar que no queden placeholders Slug en README y programa analitico."
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
        "Entrada canonica por carpeta de materia",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8, bloque 1, tipo Electiva",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y fuentes pertinentes",
      "Analisis propio con postura argumentada",
      "Conclusion juridica transferible",
      "Trazabilidad y normalizacion editorial"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia argumentativa y calidad formal en cada entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura propia sustentada",
      "Supuestos marcados",
      "Cierre juridico aplicable"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia -> inferencia juridica",
      "Descripcion breve -> critica propia -> implicacion practica"
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
          "justification": "Fija tono, formato y criterios minimos de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones y evita contenido descriptivo sin respaldo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "La propagacion confiable requiere estructura parseable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Normalizacion JSON",
          "kind": "supports",
          "justification": "Reduce errores de automatizacion y mejora consistencia documental."
        }
      ],
      "evidence": [
        "README y programa analitico del destino incluyen placeholders Slug a normalizar.",
        "Plantilla .tex local confirma identidad institucional y metadatos curriculares base.",
        "Archivo .bib local contiene claves institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 17: se conserva regla de bloqueo por JSON no parseable.",
      "Ciclo 17: se mantiene no invencion de fuentes y trazabilidad cita-.bib.",
      "Ciclo 17: se evita traslado de contenido tematico especifico de Filosofia del Derecho."
    ]
  }
}