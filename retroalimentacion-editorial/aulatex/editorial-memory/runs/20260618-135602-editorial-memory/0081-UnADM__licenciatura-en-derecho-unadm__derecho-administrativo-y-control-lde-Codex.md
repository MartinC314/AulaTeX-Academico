{
  "summary": [
    "Se consolida memoria base para la materia Derecho administrativo y control con compresion union-dedupe y sin regresion.",
    "Se preserva alerta institucional: validar respuestas no estructuradas antes de propagacion.",
    "Se alinea la materia con semestre 6, bloque 1, tipo obligatoria y creditos 8 segun malla local."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre de materia exacto: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Declarar cuando una regla provenga de fuente provisional. [supuesto]"
  ],
  "structure_rules": [
    "Organizar cada producto con: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Alinear entregables a la planeacion semanal y al programa analitico local.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib."
  ],
  "activity_rules": [
    "Cada actividad debe incluir postura academica propia y criterio juridico transferible.",
    "Vincular el tema de actividad con control administrativo y practica profesional.",
    "Explicitar el producto solicitado (reporte, presentacion o visual) antes del desarrollo.",
    "No omitir conclusion final orientada a aplicacion juridica."
  ],
  "quality_gates": [
    "Revisar que la salida sea JSON parseable antes de aplicar memoria aguas abajo.",
    "Verificar integridad academica: citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Detener propagacion si hay respuesta no estructurada o campos vacios criticos."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol y formato letterpaper segun archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real."
  ],
  "bibliography_rules": [
    "Registrar fuentes de la actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Incluir datos minimos verificables: autor, titulo, anio, medio y nota de consulta.",
    "No agregar referencias sin evidencia documental."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de estructura JSON.",
    "Aplicar normalizacion manual en ciclo 1 cuando la fuente sea provisional.",
    "Mantener estrategia lossless por union-dedupe en fusiones futuras.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]"
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar la referencia provisional de origen Codex.",
    "Confirmar nombre de figura docente en plantilla de reporte.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Corregir posibles artefactos de ruta/nombre en listado de estructura del README. [supuesto]"
  ]
}