{
  "summary": [
    "Consolidar memoria de la materia con compresion union-dedupe lossless y sin regresion.",
    "Preservar alerta institucional por salidas no JSON parseables desde Codex, GPT-Pro, Auto (model-router) y Claude Foundry.",
    "Validar respuestas no estructuradas y campos criticos vacios antes de cualquier propagacion.",
    "Alinear la materia con semestre 6, bloque 1, obligatoria y 8 creditos segun malla local.",
    "Reutilizar solo reglas editoriales generales desde Filosofia del derecho.",
    "No trasladar doctrina ni contenido sustantivo no verificado desde otras materias.",
    "Corregir artefactos locales en README y programa analitico: tokens sin expandir y nombres de archivo rotos. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Declarar cuando una regla provenga de fuente provisional.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Fuente provisional: Auto (model-router) desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1.",
    "Marcar como provisional cualquier regla originada en Codex, GPT-Pro, Auto (model-router) o Claude Foundry. [supuesto]"
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear entregables a la planeacion semanal y al programa analitico local.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Organizar cada producto con: problema, conceptos/fuentes/normas/doctrina, producto solicitado, analisis propio y conclusion juridica transferible.",
    "Explicitar si el producto es reporte, presentacion o visual.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Resolver tokens sin expandir en README y programa analitico por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Tratar tokens PowerShell sin expandir como artefactos de generacion. [supuesto]",
    "Corregir nombres de archivo con caracteres espurios o saltos de linea en README. [supuesto]",
    "Corregir entradas rotas reportadas como reporte- y referencias- en README. [supuesto]"
  ],
  "activity_rules": [
    "Explicitar el producto solicitado antes del desarrollo.",
    "Incluir postura academica propia en cada actividad.",
    "Formular criterio juridico transferible a la practica profesional.",
    "Vincular el tema de actividad con control administrativo y practica profesional.",
    "No omitir conclusion final orientada a aplicacion juridica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias."
  ],
  "quality_gates": [
    "Revisar que la salida sea JSON parseable antes de aplicar memoria aguas abajo.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Detener propagacion si hay respuesta no estructurada.",
    "Detener propagacion si hay campos criticos vacios.",
    "Verificar integridad academica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas antes de publicar indices.",
    "Revisar que las reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol y formato letterpaper segun archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar \"Actividad X\" por numero y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir \"Nombre por definir\" por el nombre oficial de la figura docente antes de entregar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Usar la malla curricular local como fuente de ubicacion curricular.",
    "Incluir datos minimos verificables: autor, titulo, anio, medio y nota de consulta.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes especificas solo si fueron consultadas o proporcionadas.",
    "No inventar fuentes ni agregar referencias sin evidencia documental."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de estructura JSON.",
    "Propagar a laterales solo reglas editoriales compartibles.",
    "No propagar contenido especifico de actividad a laterales.",
    "Aplicar normalizacion manual cuando la fuente sea provisional.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "En ciclos siguientes, verificar que la deduplicacion no elimine reglas utiles previas.",
    "Mantener estrategia de compresion union-dedupe lossless en fusiones futuras.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales (Codex/GPT-Pro/Auto/Claude Foundry).",
    "Confirmar nombre oficial de la figura docente en plantilla de reporte.",
    "Confirmar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convencion final del archivo de referencias (referencias-derecho-administrativo-y-control u otra).",
    "Verificar si el anio de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens sin expandir en README/programa son artefacto de generacion a corregir. [supuesto]"
  ]
}