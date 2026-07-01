{
  "summary": [
    "Se consolida memoria de materia para Derecho administrativo y control con union-dedupe lossless.",
    "Se preserva identidad UnADM y alineacion curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Se sincronizan abstracciones editoriales transversales desde Filosofia del Derecho sin trasladar doctrina especifica.",
    "Se refuerzan ejes estables: problema, conceptos, fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene alerta institucional: no propagar salidas no estructuradas ni JSON no parseable.",
    "Se conserva la regla local de corregir placeholders, tokens sin expandir y rutas corruptas antes de publicar."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Ubicar la materia en semestre 6, bloque 1, obligatoria, 8 creditos, segun malla local.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas Codex o GPT-Pro como provisionales hasta confirmacion local.",
    "Declarar cuando una regla provenga de fuente provisional."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar con: problema, conceptos, normas, doctrina, analisis propio y cierre.",
    "Alinear entregables con planeacion semanal y programa analitico local.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Corregir artefactos de estructura en README antes de publicar indices.",
    "Resolver tokens PowerShell sin expandir por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con saltos de linea o caracteres espurios en README. [supuesto]"
  ],
  "activity_rules": [
    "Explicitar el producto solicitado antes del desarrollo.",
    "Identificar si el producto es reporte, presentacion o visual.",
    "Vincular el tema de actividad con control administrativo y practica profesional.",
    "Incluir postura academica propia en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Formular criterio juridico transferible a la practica profesional.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No omitir conclusion final orientada a aplicacion juridica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Detener propagacion si hay campos criticos vacios.",
    "Revisar estructura minima completa antes de aplicar memoria.",
    "Verificar integridad academica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Confirmar que afirmaciones sin respaldo esten marcadas como [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analitico local.",
    "Verificar que el producto corresponda a la consigna de la actividad."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol.",
    "Mantener formato letterpaper segun archivo base.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y figura docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar Actividad X por numero y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir Nombre por definir por el nombre oficial de la figura docente antes de entregar.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir en README y programa analitico antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Usar la malla curricular local como fuente de ubicacion curricular.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes especificas solo si fueron consultadas o proporcionadas.",
    "No inventar fuentes para llenar bibliografia.",
    "No agregar referencias sin evidencia documental.",
    "Conservar metadatos minimos: autor, titulo, anio, medio y nota de consulta.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Confirmar convencion final del archivo de referencias si se usa carpeta separada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar normalizacion manual cuando la fuente sea provisional.",
    "Mantener estrategia union-dedupe lossless en fusiones futuras.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido doctrinal especifico de otras materias.",
    "No propagar contenido especifico de actividad a materias laterales.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Revisar contexto local antes de adoptar reglas heredadas."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales Codex o GPT-Pro.",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convencion final del archivo o carpeta de referencias de la materia.",
    "Verificar si el anio de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir son artefacto de generacion a corregir. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]",
    "Confirmar fuentes obligatorias de cada semana antes de crear actividades.",
    "Confirmar rubrica especifica de cada actividad antes de ajustar profundidad argumentativa."
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
        "Normalizacion estructurada antes de propagar.",
        "No uso de fuentes inventadas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "Coursecode local: LDE-S6B1."
      ]
    },
    "essence": [
      "Identidad UnADM.",
      "Integridad academica.",
      "Problema juridico o social.",
      "Control administrativo.",
      "Marco normativo y doctrinal.",
      "Fuentes verificables.",
      "Analisis propio.",
      "Criterio juridico aplicado.",
      "Conclusion transferible.",
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico, evidencia y transferencia profesional.",
      "Transformar la planeacion semanal en reportes, presentaciones y productos visuales.",
      "Integrar problema, conceptos, fuentes, analisis propio y cierre argumentativo.",
      "Vincular el aprendizaje con control administrativo y practica profesional.",
      "Evitar productos meramente descriptivos.",
      "Construir criterio juridico propio con respaldo documental."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Encuadre breve del problema.",
      "Secciones visibles y ordenadas.",
      "Conceptos definidos antes del analisis.",
      "Marco normativo o doctrinal explicitado.",
      "Citas verificables en afirmaciones sustantivas.",
      "Postura del estudiante diferenciada del resumen.",
      "Cierre con criterio juridico aplicado.",
      "Marcado explicito de [supuesto] cuando falte evidencia.",
      "Consistencia entre README, .tex y .bib."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion -> evidencia verificable -> interpretacion juridica -> implicacion practica.",
      "Consigna -> objetivo -> producto -> desarrollo -> cierre.",
      "Norma o doctrina -> caso o problema -> criterio del estudiante.",
      "Fuente institucional -> ubicacion curricular -> identidad del entregable.",
      "Pregunta guia -> desarrollo argumentado -> respuesta final coherente.",
      "Descripcion minima -> valoracion juridica -> transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Licenciatura en Derecho",
        "Derecho administrativo y control",
        "Semestre 6 bloque 1",
        "Malla curricular de Derecho",
        "Planeacion semanal",
        "Programa analitico local",
        "Problema juridico",
        "Problema social",
        "Control administrativo",
        "Marco normativo",
        "Marco doctrinal",
        "Conceptos juridicos",
        "Fuentes verificables",
        "Integridad academica",
        "Analisis propio",
        "Postura academica",
        "Conclusion juridica",
        "Conclusion transferible",
        "Practica profesional",
        "Reporte",
        "Presentacion",
        "Producto visual",
        "README de materia",
        "Plantilla LaTeX",
        "Archivo BibTeX local",
        "JSON parseable",
        "Normalizacion manual",
        "Tokens sin expandir",
        "Rutas corruptas",
        "Fuentes provisionales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Portada y metadatos",
          "kind": "develops",
          "justification": "La plantilla local exige datos institucionales visibles."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Semestre 6 bloque 1",
          "kind": "supports",
          "justification": "El README local cita la malla como fuente de ubicacion curricular."
        },
        {
          "source": "Programa analitico local",
          "target": "Planeacion semanal",
          "kind": "supports",
          "justification": "El programa indica transformar planeacion en productos academicos."
        },
        {
          "source": "Planeacion semanal",
          "target": "Tipo de producto",
          "kind": "depends_on",
          "justification": "La consigna define si procede reporte, presentacion o producto visual."
        },
        {
          "source": "Problema juridico",
          "target": "Marco normativo",
          "kind": "develops",
          "justification": "El problema orienta las normas pertinentes para el analisis."
        },
        {
          "source": "Marco normativo",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio juridico debe construirse sobre fuentes pertinentes."
        },
        {
          "source": "Marco doctrinal",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La doctrina permite interpretar conceptos y justificar postura."
        },
        {
          "source": "Fuentes verificables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Las citas verificables evitan afirmaciones sin respaldo."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento del estudiante."
        },
        {
          "source": "Conclusion juridica",
          "target": "Practica profesional",
          "kind": "develops",
          "justification": "El cierre debe transferir el criterio al ejercicio juridico."
        },
        {
          "source": "Control administrativo",
          "target": "Practica profesional",
          "kind": "develops",
          "justification": "La materia exige vincular actividades con aplicacion administrativa."
        },
        {
          "source": "Archivo BibTeX local",
          "target": "Fuentes verificables",
          "kind": "supports",
          "justification": "El .bib local registra la bibliografia base y especifica."
        },
        {
          "source": "README de materia",
          "target": "Carpeta de materia",
          "kind": "develops",
          "justification": "El README declara la carpeta como punto de entrada canonico."
        },
        {
          "source": "Tokens sin expandir",
          "target": "Compilacion LaTeX",
          "kind": "contrasts",
          "justification": "Los placeholders rompen nombres de archivo y referencias."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La propagacion solo procede con estructura valida."
        },
        {
          "source": "Fuentes provisionales",
          "target": "Normalizacion manual",
          "kind": "depends_on",
          "justification": "Las reglas heredadas no verificadas requieren confirmacion local."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 6, bloque 1, obligatoria, 8 creditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canonico.",
        "README local: integridad academica, citas verificables y conclusion juridica con criterio propio.",
        "Programa analitico local: productos con claridad, fundamento juridico, evidencia y transferencia profesional.",
        "Programa analitico local: ejes de trabajo problema, conceptos, producto, analisis y conclusion.",
        "derecho-administrativo-y-control.bib: entradas base unadmSitioWeb y unadmMallaDerecho2024.",
        "Plantilla .tex local: documenttitle, documentsubtitle, coursename y coursecode LDE-S6B1.",
        "Plantilla .tex local: figura docente pendiente como Nombre por definir.",
        "Memoria institucional heredada: salida sin JSON parseable desde Codex para UnADM.",
        "Memoria transversal: bloquear propagacion si la salida no es JSON parseable.",
        "Memoria transversal: no inventar referencias y usar solo fuentes consultables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se conserva alineacion curricular local de Derecho administrativo y control.",
      "Ciclo 1: se incorporan solo abstracciones editoriales estables desde Filosofia del Derecho.",
      "Ciclo 1: se excluye doctrina especifica de Filosofia del Derecho por no ser equivalente al destino.",
      "Ciclo 1: se deduplican reglas repetidas sin eliminar obligaciones utiles.",
      "Ciclo 1: se refuerza gate de JSON parseable antes de propagacion.",
      "Ciclo 1: se mantiene alerta por fuentes provisionales Codex y GPT-Pro.",
      "Ciclo 1: se preserva correccion de tokens sin expandir y rutas corruptas como tarea local.",
      "Ciclo 1: se refuerza patron problema-marco-analisis-conclusion aplicada."
    ]
  }
}