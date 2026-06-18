{
  "summary": [
    "Base editorial de materia creada desde contexto local de Electiva S8 B1.",
    "Se conserva herencia institucional y control de calidad por salida no estructurada previa.",
    "Supuesto: no se recibio contenido especifico de actividad-1 para reglas tematicas adicionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion academica.",
    "Usar tono juridico formal, claro y verificable.",
    "Conservar datos de asignatura: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No eliminar reglas heredadas; extender solo con evidencia local."
  ],
  "structure_rules": [
    "Organizar entregables con secuencia: problema, conceptos/fuentes, desarrollo del producto, analisis propio, conclusion.",
    "Alinear cada actividad al programa analitico de la materia.",
    "Incluir conclusion juridica transferible a la practica.",
    "Mantener carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Declarar objetivo de la actividad al inicio del reporte.",
    "Vincular el producto solicitado con al menos un problema juridico o social.",
    "Diferenciar resumen de fuentes y analisis propio del estudiante.",
    "Cerrar con postura academica sustentada."
  ],
  "quality_gates": [
    "Verificar que la salida sea JSON parseable antes de propagar.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas verificables.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Completar campos pendientes de portada antes de entrega (docente, creditos si aplica).",
    "Conservar definiciones de curso y universidad sin renombrados inconsistentes.",
    "Usar codificacion y paquetes compatibles con espanol academico."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "No inventar referencias; solo incorporar fuentes consultadas y verificables.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales reglas de calidad y estructura ya validadas.",
    "Marcar ciclo 1 como fase de normalizacion manual cuando falte insumo de actividad.",
    "Aplicar union-dedupe lossless para evitar duplicados semanticos."
  ],
  "open_questions": [
    "Falta contenido fuente de actividad-1 de Filosofia del Derecho para extraer reglas especificas.",
    "Definir creditos oficiales de la electiva en metadatos de portada.",
    "Confirmar nombre de figura docente para plantilla base."
  ]
}