{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de origen a materia destino sin trasladar contenido tematico no verificable.",
    "Se preservan reglas estables: identidad UnADM, normalizacion estructurada, ejes editoriales y control de supuestos.",
    "Se refuerza control operativo de placeholders y nombres truncados detectados en README y programa del destino.",
    "Se mantiene estrategia conservadora: union-dedupe lossless, sin regresion de reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la consigna semanal vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal al producto concreto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar resumen descriptivo puro.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de otras semanas o materias aplican automaticamente.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Corregir nombres de archivo truncados antes de compilar o publicar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Reemplazar tokens tipo $(@{...}.Slug) por nombres literales.",
    "Corregir entradas de estructura con nombres truncados como eporte/eferencias."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "No inventar referencias.",
    "Agregar entradas BibTeX solo con metadatos verificables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Mantener correspondencia exacta entre claves citadas y claves declaradas."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar redaccion literal ni contenido tematico especifico del origen.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Aplicar normalizacion manual a herencias historicas no estructuradas de ciclo 1.",
    "Mantener compresion lossless por union-dedupe en cada ciclo.",
    "Evitar regresiones: nunca eliminar reglas utiles previamente validadas."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia para completar metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente en front matter.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si la bibliografia base debe ampliarse con lineamientos propios de esta electiva."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8.",
        "Bloque 2.",
        "Tipo Electiva.",
        "Codigo de curso LDE-S8B2.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Trazabilidad cita-texto-bib."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para la practica.",
      "Sostener calidad editorial uniforme en toda la materia con reglas reutilizables y auditables."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y ordenadas.",
      "Postura propia respaldada por evidencia.",
      "Cierre aplicado a practica juridica.",
      "Marcado visible de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> inferencia propia.",
      "Evitar descripcion pura; priorizar juicio juridico razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Trazabilidad cita-texto-bib",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Correccion de placeholders"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Reduce herencia de errores no parseables."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre texto y fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de pendientes."
        }
      ],
      "evidence": [
        "README y programa local fijan ejes de problema, fuentes, analisis y cierre.",
        "Destino contiene tokens sin expandir y nombres truncados; riesgo operativo confirmado.",
        "Regla historica valida: no reutilizar salidas no estructuradas sin normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se consolidan reglas transversales estables sin mover contenido disciplinar especifico del origen.",
      "Ciclo 13: se refuerza gate de JSON parseable y estructura minima antes de propagacion recursiva.",
      "Ciclo 13: se mantiene union-dedupe lossless y no regresion de reglas utiles.",
      "Ciclo 13: se prioriza correccion de placeholders y coherencia documental local."
    ]
  }
}