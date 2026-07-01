{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y control JSON parseable.",
    "Se refuerza patron reusable: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene separacion entre abstracciones editoriales estables y contenido tematico no equivalente.",
    "Se conserva alerta tecnica local: truncamientos y placeholders deben resolverse antes de compilar o propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato e integridad academica.",
    "Usar contexto local del destino: Licenciatura en Derecho, materia de responsabilidad civil y danos.",
    "Priorizar metadatos curriculares locales sobre metadatos heredados de otros nodos.",
    "Marcar como supuesto todo dato no confirmado por consigna o documento oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta validacion local.",
    "No declarar oficial el codigo de curso LDE-S6B1 sin confirmacion documental."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion explicita entre reporte, presentacion, programa analitico y bibliografia local."
  ],
  "activity_rules": [
    "Exigir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables o marcar analisis propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Adaptar reglas heredadas solo como abstracciones compatibles con responsabilidad civil y danos.",
    "Evitar arrastre de contenido tematico de Filosofia del Derecho cuando no sea aplicable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar no regresion de reglas utiles previas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver antes de propagar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: la plantilla .tex local esta truncada en authortable y debe completarse antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y material juridico verificable.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener como base confirmada: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y transversales, no redaccion literal.",
    "Aplicar compresion lossless por union y deduplicacion, sin recorte semantico.",
    "Mantener normalizacion manual mientras existan antecedentes de salida no estructurada.",
    "Propagar control tecnico de truncamientos/placeholders como gate general de calidad.",
    "Conservar prioridad del contexto local del destino en saltos entre nodos no equivalentes."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de la materia destino.",
    "Confirmar convencion canonica de nombres danos versus daños en todo el arbol.",
    "Confirmar si LDE-S6B1 es codigo oficial o solo etiqueta local. [supuesto activo]",
    "Resolver placeholders de .bib en README y programa analitico.",
    "Completar bloque authortable truncado en la plantilla .tex."
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
        "Materia: Derecho de la responsabilidad civil y danos.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento conceptual y normativo verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Calidad tecnica y trazabilidad editorial."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para practica juridica.",
      "Sostener coherencia institucional y calidad transversal entre nodos.",
      "Permitir propagacion segura por reglas estables y deduplicadas."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Secciones explicitas y ordenadas.",
      "Supuestos siempre marcados.",
      "Citas trazables al .bib local.",
      "Sin contenido ornamental ni relleno."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Desarrollar marco conceptual/normativo.",
      "Contrastar evidencia y elaborar postura propia.",
      "Cerrar con conclusion juridica aplicable.",
      "Verificar correspondencia con consigna y producto solicitado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Responsabilidad civil y danos",
        "Integridad de citacion",
        "Compresion lossless por deduplicacion"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis parte de una pregunta delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Calidad editorial",
          "kind": "supports",
          "justification": "Define tono, formato e integridad academica."
        },
        {
          "source": "Reglas heredadas de Filosofia del Derecho",
          "target": "Responsabilidad civil y danos",
          "kind": "contrasts",
          "justification": "Solo se transfieren abstracciones estables, no tematica puntual."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Memoria persistente",
          "kind": "develops",
          "justification": "Reduce ruido sin perder reglas utiles."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local del destino.",
        "Archivo .bib local con unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen con gates de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se consolida base minima de cerebro editorial de materia con deduplicacion.",
      "Ciclo 1: se preservan gates criticos de estructura, trazabilidad y no regresion.",
      "Ciclo 1: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 1: se mantienen abiertos vacios de contexto local pendientes de verificacion."
    ]
  }
}