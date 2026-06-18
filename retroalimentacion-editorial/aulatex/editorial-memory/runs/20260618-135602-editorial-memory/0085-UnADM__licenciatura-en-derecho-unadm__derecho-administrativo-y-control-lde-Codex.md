{
  "summary": [
    "Consolidar memoria de la materia con union-dedupe lossless y sin regresion.",
    "Preservar alerta institucional por salidas no JSON parseables antes de propagar.",
    "Mantener alineacion curricular local: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Reutilizar solo reglas editoriales generales desde Filosofia del derecho; no trasladar doctrina no verificada.",
    "Corregir artefactos locales de README/programa en nombres de archivo y tokens sin expandir. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Declarar cuando una regla provenga de fuente provisional. [supuesto]",
    "Marcar como provisional cualquier regla originada en Codex desde ingenieria-en-sistemas-computacionales. [supuesto]",
    "Fuente provisional: GPT-Pro desde Actividad 1",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales"
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear entregables a la planeacion semanal y al programa analitico local.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Organizar cada producto con: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Corregir artefactos de estructura en README antes de publicar indices.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Resolver tokens PowerShell sin expandir en README y programa analitico por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con caracteres espurios o saltos de linea en README (reporte-, referencias-). [supuesto]"
  ],
  "activity_rules": [
    "Explicitar el producto solicitado antes del desarrollo.",
    "Incluir postura academica propia en cada actividad.",
    "Formular criterio juridico transferible a la practica profesional.",
    "Vincular el tema con control administrativo y practica profesional.",
    "No omitir conclusion final orientada a aplicacion juridica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "Estructurar productos con ejes: problema, conceptos/normas/doctrina, producto, analisis propio y conclusion transferible."
  ],
  "quality_gates": [
    "Revisar que la salida sea JSON parseable antes de aplicar memoria aguas abajo.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Detener propagacion si hay respuesta no estructurada o campos criticos vacios.",
    "Verificar integridad academica: citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas.",
    "Revisar que reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol y formato letterpaper segun archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar Actividad X por numero y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Completar figura docente antes de entregar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Incluir datos minimos verificables: autor, titulo, anio, medio y nota de consulta.",
    "No agregar referencias sin evidencia documental.",
    "Usar malla curricular local como fuente de ubicacion curricular.",
    "Agregar fuentes especificas solo si fueron consultadas o proporcionadas.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de estructura JSON.",
    "Aplicar normalizacion manual cuando la fuente sea provisional.",
    "Mantener estrategia de compresion union-dedupe lossless en fusiones futuras.",
    "Propagar a laterales solo reglas editoriales compartibles, no contenido especifico de actividad.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Ciclo 1 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales (Codex/GPT-Pro).",
    "Confirmar nombre oficial de la figura docente en plantilla.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convencion final del archivo de referencias en la materia.",
    "Verificar si el anio de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir son artefacto de generacion a corregir. [supuesto]"
  ]
}