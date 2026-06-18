{
  "summary": [
    "Base editorial de materia creada desde contexto local de Electiva S8 B1.",
    "Se conserva herencia institucional UnADM y control de calidad por salida no estructurada previa.",
    "Se integra memoria heredada institucional mediante union-dedupe lossless.",
    "Supuesto: no se recibio contenido especifico de actividad-1 de Filosofia del Derecho para reglas tematicas adicionales.",
    "Destino canonico: UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde.",
    "Salida sin JSON parseable previa desde Codex para UnADM registrada como antecedente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion academica.",
    "Usar tono juridico formal, claro y verificable.",
    "Conservar datos de asignatura: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No eliminar reglas heredadas; extender solo con evidencia local.",
    "Reconocer fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Evitar renombrar la asignatura si no existe confirmacion oficial del nombre de la electiva.",
    "Conservar autor confirmado en plantilla: Martin Jonathan de la Cruz, matricula ES2611202040.",
    "Mantener codigo de curso LDE-S8B1 mientras no exista codigo oficial distinto."
  ],
  "structure_rules": [
    "Organizar entregables con secuencia: problema, conceptos o fuentes, producto, analisis propio y conclusion.",
    "Alinear cada actividad al programa analitico de la materia.",
    "Incluir conclusion juridica transferible a la practica.",
    "Mantener carpeta de materia como punto de entrada canonico.",
    "Conservar README, programa analitico, plantilla de reporte, plantilla de presentacion, bibliografia y carpeta de referencias.",
    "Usar el programa analitico editorial como guia de reportes, presentaciones y productos visuales."
  ],
  "activity_rules": [
    "Declarar objetivo de la actividad al inicio del reporte.",
    "Vincular el producto solicitado con al menos un problema juridico o social.",
    "Diferenciar resumen de fuentes y analisis propio del estudiante.",
    "Cerrar con postura academica sustentada.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "No trasladar contenido tematico de Filosofia del Derecho sin insumo verificable."
  ],
  "quality_gates": [
    "Verificar que la salida sea JSON parseable antes de propagar.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas verificables.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Corregir literales de generador y caracteres corruptos en nombres de archivo antes de entrega.",
    "Confirmar que las rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular de Derecho respalde semestre, bloque y tipo de asignatura.",
    "Marcar como pendiente todo dato no confirmado, especialmente creditos y figura docente."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Completar campos pendientes de portada antes de entrega (docente, creditos si aplica).",
    "Conservar definiciones de curso y universidad sin renombrados inconsistentes.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio institucional verificado.",
    "Actualizar Figura docente solo con nombre confirmado.",
    "No dejar creditos vacios si el dato oficial esta disponible.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "Evitar placeholders de automatizacion como $(@{...}.Slug) en archivos finales.",
    "Mantener clase article spanish letterpaper oneside en la plantilla de reporte.",
    "Conservar universitylocation Roma Norte, Ciudad de Mexico salvo cambio verificado."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "No inventar referencias; solo incorporar fuentes consultadas y verificables.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Conservar entrada institucional del sitio web UnADM si fue consultada.",
    "Conservar entrada de malla curricular de Derecho como fuente local.",
    "Agregar referencias doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera.",
    "Usar claves BibTeX estables y descriptivas.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales reglas de calidad y estructura ya validadas.",
    "Marcar ciclo 1 como fase de normalizacion manual cuando falte insumo de actividad.",
    "Aplicar union-dedupe lossless para evitar duplicados semanticos.",
    "Propagar la regla de no inventar fuentes a materias laterales.",
    "Propagar la verificacion de JSON parseable a nodos superiores.",
    "No propagar metadatos especificos de Electiva S8 B1 a materias no equivalentes."
  ],
  "open_questions": [
    "Falta contenido fuente de actividad-1 de Filosofia del Derecho para extraer reglas especificas.",
    "Definir creditos oficiales de la electiva en metadatos de portada.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si existe uno distinto a Electiva Semestre 8 Bloque 1.",
    "Confirmar si presentacion-electiva-semestre-8-bloque-1.tex existe y comparte reglas de portada.",
    "Corregir en README los nombres de archivo con caracteres faltantes o placeholders (reporte, referencias).",
    "Confirmar codigo oficial de la asignatura frente al provisional LDE-S8B1."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}