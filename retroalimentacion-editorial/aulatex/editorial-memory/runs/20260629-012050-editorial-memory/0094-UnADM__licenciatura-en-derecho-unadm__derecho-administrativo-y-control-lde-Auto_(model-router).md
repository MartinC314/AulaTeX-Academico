{
  "summary": [
    "Se consolida memoria editorial de materia para Derecho administrativo y control.",
    "Se aplica sincronizacion transversal desde Filosofia del Derecho solo con abstracciones estables.",
    "Se conserva identidad UnADM y alineacion curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales: problema, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Se mantiene alerta institucional ante salidas no estructuradas o JSON no parseable.",
    "Se preserva compresion union-dedupe sin regresion.",
    "No se traslada doctrina sustantiva de Filosofia del Derecho al destino sin verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Alinear la materia con semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Declarar como provisional toda regla heredada no verificada localmente.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales. [supuesto]",
    "Fuente provisional: GPT-Pro desde Actividad 1. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como fuente de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Organizar cada producto con problema, conceptos, normas, doctrina, fuentes, analisis propio y conclusion juridica.",
    "Alinear entregables a la planeacion semanal y al programa analitico local.",
    "Adaptar la estructura al producto solicitado: reporte, presentacion o visual.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Resolver tokens PowerShell sin expandir en README y programa analitico por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con caracteres espurios o saltos de linea en README. [supuesto]",
    "Verificar que reporte-, presentacion-, referencias- y .bib coincidan con la convencion local."
  ],
  "activity_rules": [
    "Explicitar el producto solicitado antes del desarrollo.",
    "Verificar que el producto corresponda a la consigna de actividad.",
    "Vincular el tema con control administrativo y practica profesional.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura academica propia del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Formular criterio juridico transferible a la practica profesional.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de otras semanas correspondan a una actividad concreta.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "No omitir conclusion final orientada a aplicacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar memoria aguas abajo.",
    "Detener propagacion si hay respuesta no estructurada o campos criticos vacios.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Verificar integridad academica con citas verificables y sin fuentes inventadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Revisar que reglas heredadas no contradigan el programa analitico local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar respuesta no estructurada antes de reutilizarla.",
    "Confirmar que la entrega use el nombre real de actividad y no Actividad X."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol.",
    "Mantener formato letterpaper segun archivo base.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y docente en portada.",
    "Asegurar coherencia entre documenttitle, documentsubtitle y actividad real.",
    "Reemplazar Actividad X por numero y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir Nombre por definir por el nombre oficial de la figura docente antes de entregar.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Priorizar materiales juridicos verificables cuando la consigna lo requiera.",
    "No inventar fuentes para llenar bibliografia.",
    "Agregar fuentes especificas solo si fueron consultadas o proporcionadas.",
    "Conservar metadatos minimos: autor, titulo, anio, medio o editorial, URL o archivo, nota de consulta.",
    "Usar la malla curricular local como fuente de ubicacion curricular.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir bibliografia de Filosofia del Derecho como bibliografia local del destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido especifico de actividad a laterales.",
    "No trasladar doctrina sustantiva entre materias sin evidencia local.",
    "Aplicar normalizacion manual cuando la fuente sea provisional.",
    "Mantener estrategia union-dedupe lossless en fusiones futuras.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Reutilizar gates institucionales de calidad sin reducir especificidad local."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales Codex y GPT-Pro.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convencion final del archivo de referencias en la materia.",
    "Verificar si el anio de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir en README y programa son artefacto de generacion a corregir. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]",
    "Confirmar fuentes obligatorias por actividad antes de crear bibliografia especifica.",
    "Confirmar producto exacto solicitado en cada actividad semanal."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez innecesaria.",
        "Aplicado a practica profesional."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "No uso de fuentes inventadas.",
        "Marcado explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "Coursecode local: LDE-S6B1.",
        "Producto adaptable a reporte, presentacion o visual."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad academica.",
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Fuentes verificables.",
      "Analisis propio.",
      "Control administrativo.",
      "Conclusion juridica transferible.",
      "Practica profesional."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Vincular cada actividad con control administrativo y practica juridica.",
      "Evitar productos meramente descriptivos.",
      "Construir criterio juridico aplicable."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Encuadre breve del problema.",
      "Secciones visibles y ordenadas.",
      "Marco normativo o doctrinal verificable.",
      "Citas explicitas y trazables.",
      "Postura academica propia.",
      "Cierre con criterio juridico aplicado.",
      "Marcado [supuesto] cuando falte evidencia.",
      "Nombre exacto de materia en metadatos.",
      "Consistencia entre README, .tex y .bib."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion -> evidencia verificable -> interpretacion juridica -> implicacion practica.",
      "Consigna -> producto solicitado -> estructura editorial -> entrega verificable.",
      "Fuente local -> dato curricular -> metadato LaTeX -> portada consistente.",
      "Planeacion semanal -> objetivo puntual -> desarrollo -> cierre juridico.",
      "Regla heredada -> verificacion local -> adopcion o marca provisional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Materia obligatoria de 8 creditos",
        "Malla curricular de Derecho",
        "Programa analitico local",
        "Planeacion semanal",
        "Problema juridico",
        "Control administrativo",
        "Marco normativo",
        "Marco doctrinal",
        "Fuentes verificables",
        "Analisis propio",
        "Postura academica",
        "Conclusion transferible",
        "Practica profesional",
        "Integridad academica",
        "JSON parseable",
        "Normalizacion estructurada",
        "README canonico",
        "Plantilla LaTeX",
        "Archivo BibTeX local",
        "Tokens sin expandir",
        "Fuentes provisionales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "El README local declara semestre 6 y bloque 1 con fuente en la malla curricular."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Materia obligatoria de 8 creditos",
          "kind": "supports",
          "justification": "El README local declara tipo obligatoria y 8 creditos con fuente institucional."
        },
        {
          "source": "Programa analitico local",
          "target": "Ejes editoriales",
          "kind": "develops",
          "justification": "El programa enumera problema, conceptos, producto, analisis propio y conclusion."
        },
        {
          "source": "Planeacion semanal",
          "target": "Producto solicitado",
          "kind": "depends_on",
          "justification": "El programa indica transformar la planeacion en reporte, presentacion o producto visual."
        },
        {
          "source": "Marco normativo",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio juridico requiere fundamento verificable antes de argumentar."
        },
        {
          "source": "Marco doctrinal",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La doctrina pertinente ayuda a construir postura academica."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento del estudiante."
        },
        {
          "source": "Control administrativo",
          "target": "Practica profesional",
          "kind": "develops",
          "justification": "La materia exige aplicar el criterio juridico a problemas administrativos."
        },
        {
          "source": "Integridad academica",
          "target": "Fuentes verificables",
          "kind": "depends_on",
          "justification": "Las afirmaciones deben sostenerse con citas y referencias consultables."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Citas verificables",
          "kind": "supports",
          "justification": "El .bib local conserva las entradas institucionales y futuras fuentes de actividad."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "La memoria institucional bloquea salidas no estructuradas antes de aplicar aguas abajo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Las reglas heredadas requieren estructura minima completa antes de reutilizarse."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Consistencia documental",
          "kind": "contrasts",
          "justification": "Los placeholders en README y programa contradicen nombres canonicos de archivos."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Verificacion local",
          "kind": "depends_on",
          "justification": "Las reglas heredadas no verificadas deben confirmarse antes de volverse definitivas."
        }
      ],
      "evidence": [
        "README.md: materia de la Licenciatura en Derecho de la UnADM.",
        "README.md: semestre 6, bloque 1, obligatoria, 8 creditos.",
        "README.md: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README.md: carpeta como punto de entrada canonico.",
        "README.md: integridad academica, citas verificables y conclusion juridica con criterio propio.",
        "README.md: tokens sin expandir y nombres con caracteres espurios en estructura. [supuesto]",
        "programa-analitico-derecho-administrativo-y-control.md: funcion editorial con claridad, fundamento juridico, evidencia y transferencia profesional.",
        "programa-analitico-derecho-administrativo-y-control.md: reportes, presentaciones y productos visuales.",
        "programa-analitico-derecho-administrativo-y-control.md: ejes de problema, conceptos, producto, analisis propio y conclusion.",
        "derecho-administrativo-y-control.bib: entrada unadmSitioWeb.",
        "derecho-administrativo-y-control.bib: entrada unadmMallaDerecho2024.",
        "reporte-derecho-administrativo-y-control.tex: documenttitle de plantilla base.",
        "reporte-derecho-administrativo-y-control.tex: documentsubtitle Actividad X pendiente de ajuste.",
        "reporte-derecho-administrativo-y-control.tex: coursecode LDE-S6B1.",
        "reporte-derecho-administrativo-y-control.tex: figura docente Nombre por definir.",
        "Memoria institucional heredada: revisar respuesta no estructurada antes de aplicar aguas abajo.",
        "Memoria de origen transversal: bloquear propagacion si la salida no es JSON parseable.",
        "Memoria de origen transversal: no inventar referencias.",
        "Memoria de origen transversal: sustentar afirmaciones con fuentes verificables y cita explicita."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 consolida reglas duplicadas mediante union-dedupe.",
      "Se refuerza identidad UnADM sin trasladar contenido doctrinal de otra materia.",
      "Se preserva alineacion curricular local verificada en README.",
      "Se fortalecen gates de JSON parseable y normalizacion estructurada.",
      "Se integra pauta transversal de problema, fuentes, analisis propio y conclusion.",
      "Se mantiene alerta sobre fuentes provisionales Codex y GPT-Pro.",
      "Se convierte el error de tokens sin expandir en gate documental.",
      "Se preserva derecho-administrativo-y-control.bib como archivo BibTeX local.",
      "Se registran unadmSitioWeb y unadmMallaDerecho2024 como citas locales disponibles.",
      "Se evita propagar bibliografia sustantiva de Filosofia del Derecho al destino."
    ]
  }
}