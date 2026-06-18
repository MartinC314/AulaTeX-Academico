{
  "summary": [
    "Se consolida memoria base para la materia Derecho administrativo y control con compresion union-dedupe y sin regresion.",
    "Se preserva alerta institucional: validar respuestas no estructuradas antes de propagacion.",
    "Se alinea la materia con semestre 6, bloque 1, tipo obligatoria y creditos 8 segun malla local.",
    "Mantener alerta por antecedente de salida no JSON parseable desde Codex para UnADM.",
    "Reutilizar solo reglas editoriales generales desde Filosofia del derecho; no trasladar contenido doctrinal no verificado."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre de materia exacto: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Declarar cuando una regla provenga de fuente provisional. [supuesto]",
    "Marcar como provisional cualquier regla originada en Codex desde ingenieria-en-sistemas-computacionales. [supuesto]"
  ],
  "structure_rules": [
    "Organizar cada producto con: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Alinear entregables a la planeacion semanal y al programa analitico local.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Corregir artefactos de estructura en README antes de publicar indices.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Resolver tokens PowerShell sin expandir en README y programa analitico (p.ej. $(@{...}.Slug)) por el slug literal. [supuesto]",
    "Corregir nombres de archivo con saltos de linea/espurios en README (reporte-, referencias-)."
  ],
  "activity_rules": [
    "Cada actividad debe incluir postura academica propia y criterio juridico transferible.",
    "Vincular el tema de actividad con control administrativo y practica profesional.",
    "Explicitar el producto solicitado (reporte, presentacion o visual) antes del desarrollo.",
    "No omitir conclusion final orientada a aplicacion juridica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "Estructurar productos segun ejes: problema, conceptos/normas/doctrina, producto, analisis propio, conclusion transferible."
  ],
  "quality_gates": [
    "Revisar que la salida sea JSON parseable antes de aplicar memoria aguas abajo.",
    "Verificar integridad academica: citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Detener propagacion si hay respuesta no estructurada o campos vacios criticos.",
    "Validar que el README no conserve placeholders ni rutas corruptas.",
    "Revisar que las reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol y formato letterpaper segun archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Actualizar Actividad X por el numero y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Completar figura docente (actualmente 'Nombre por definir') antes de entregar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de la actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Incluir datos minimos verificables: autor, titulo, anio, medio y nota de consulta.",
    "No agregar referencias sin evidencia documental.",
    "Usar la malla curricular local como fuente para ubicacion curricular.",
    "Agregar fuentes especificas solo cuando hayan sido consultadas o proporcionadas.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de estructura JSON.",
    "Aplicar normalizacion manual en ciclo 1 cuando la fuente sea provisional.",
    "Mantener estrategia lossless por union-dedupe en fusiones futuras.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Propagar a laterales solo reglas editoriales compartibles, no contenidos especificos de actividad.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar la referencia provisional de origen Codex.",
    "Confirmar nombre de figura docente en plantilla de reporte.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]",
    "Confirmar si el archivo de referencias debe llamarse referencias-derecho-administrativo-y-control o usar otra convencion local.",
    "Verificar si el anio de consulta del sitio institucional UnADM debe mantenerse como 2026.",
    "Confirmar si los tokens PowerShell sin expandir en README/programa son artefacto de generacion a corregir. [supuesto]"
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derecho-administrativo-y-control-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}