{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se transfieren solo abstracciones editoriales estables desde actividad origen.",
    "Se preserva identidad UnADM y contexto curricular local de la materia destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de cualquier propagacion.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Persisten alertas tecnicas locales: rutas truncadas, placeholders sin resolver y plantilla .tex incompleta [supuesto verificado en contexto local]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o guia oficial.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No declarar oficial el codigo LDE-S6B1 sin evidencia documental explicita [supuesto].",
    "No cambiar la convencion local danos/daños sin confirmacion documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la planeacion semanal y la consigna vigente.",
    "Mantener separacion editorial entre reporte, presentacion, programa analitico y .bib.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Formular un problema juridico vinculado a responsabilidad civil y daño.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Separar fundamento juridico, evidencia y postura academica.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar contenido tematico de Filosofia del Derecho si no es funcional al objetivo local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion juridica tenga fuente o marca de analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver antes de compilar."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres truncados de archivos antes de referenciarlos.",
    "Completar plantilla .tex truncada en authortable antes de compilar [supuesto verificado]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; registrar vacios como preguntas abiertas.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y no redaccion literal.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Aplicar union-dedupe sin recorte semantico en cada ciclo.",
    "Mantener alertas de normalizacion manual por antecedentes de salida no estructurada.",
    "Evitar trasladar detalle tematico puntual entre nodos no equivalentes."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato para actividades de esta materia.",
    "Confirmar si LDE-S6B1 es codigo oficial o interno [supuesto].",
    "Confirmar convencion definitiva de nombres: danos vs daños.",
    "Confirmar producto exacto por actividad segun planeacion semanal.",
    "Validar y corregir placeholders de .bib en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la responsabilidad civil y danos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Compatibilidad entre consigna y producto."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para practica juridica.",
      "Sostener una memoria editorial persistente sin perdida de reglas utiles.",
      "Asegurar trazabilidad entre evidencia, argumento y conclusion."
    ],
    "style_markers": [
      "Supuestos declarados de forma explicita.",
      "Secciones funcionales y verificables.",
      "Cierre con criterio juridico propio.",
      "Sin extrapolacion tematica no justificada."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo con fuentes.",
      "Analisis propio con postura.",
      "Conclusion aplicada a contexto profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad academica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "El marco institucional exige trazabilidad, formato consistente y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar salidas ambiguas y mantiene control de calidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema definido no hay analisis juridico focalizado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere base normativa y doctrinal."
        },
        {
          "source": "Daño",
          "target": "Responsabilidad civil",
          "kind": "depends_on",
          "justification": "La atribucion de responsabilidad se articula desde la nocion juridica de daño."
        },
        {
          "source": "Estructura reusable",
          "target": "Calidad de producto academico",
          "kind": "develops",
          "justification": "La secuencia problema-marco-analisis-cierre mejora coherencia y evaluabilidad."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo .bib local con entradas institucionales.",
        "Plantilla .tex local truncada en authortable [supuesto verificado en archivo].",
        "Memoria origen con gates de JSON y normalizacion estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se consolidan reglas transversales estables sin traslado literal de contenido de actividad.",
      "Ciclo 8: se mantiene gate duro de JSON parseable y estructura minima.",
      "Ciclo 8: se preservan alertas tecnicas locales de truncamiento y placeholders.",
      "Ciclo 8: se refuerza patron argumentativo reusable para reportes y presentaciones.",
      "Ciclo 8: deduplicacion aplicada sin eliminar reglas utiles previas."
    ]
  }
}