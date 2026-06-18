{
  "summary": [
    "Base editorial de materia creada desde contexto local de Electiva S8 B1.",
    "Destino canonico: UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde.",
    "Memoria de materia consolidada con union-dedupe lossless sin eliminar reglas utiles.",
    "Se conserva herencia institucional UnADM.",
    "Se conservan antecedentes de salida sin JSON parseable desde Codex para UnADM y GPT-Pro para la electiva.",
    "Se integra memoria heredada institucional mediante union-dedupe lossless.",
    "Se incorporan mejoras verificables del contexto local: placeholders de automatizacion y literales corruptos en README/programa.",
    "Supuesto: no se recibio contenido tematico verificable de actividad-1 de Filosofia del Derecho para reglas disciplinares adicionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion academica.",
    "Usar tono juridico formal, claro y verificable.",
    "Conservar datos de asignatura: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Evitar renombrar la asignatura sin confirmacion oficial.",
    "Mantener codigo provisional LDE-S8B1 hasta confirmacion oficial distinta.",
    "Conservar autor confirmado en plantilla: Martin Jonathan de la Cruz, matricula ES2611202040.",
    "No eliminar reglas heredadas; extender solo con evidencia verificable.",
    "Reconocer fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Reconocer fuente provisional heredada: GPT-Pro desde actividad-1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar README, programa analitico, plantilla de reporte, plantilla de presentacion, bibliografia y carpeta de referencias.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, analisis propio, conclusion.",
    "Alinear cada actividad al programa analitico de la materia.",
    "Usar el programa analitico como guia de reportes, presentaciones y productos visuales.",
    "Incluir conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Declarar objetivo de la actividad al inicio del reporte.",
    "Vincular el producto solicitado con al menos un problema juridico o social.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Diferenciar resumen de fuentes y analisis propio del estudiante.",
    "Cerrar con postura academica sustentada.",
    "No trasladar contenido tematico de Filosofia del Derecho sin insumo verificable."
  ],
  "quality_gates": [
    "Verificar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas verificables.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular de Derecho respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado, en especial creditos y figura docente.",
    "Corregir placeholders de automatizacion y literales corruptos en nombres de archivo antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con opciones spanish, letterpaper, oneside.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar definiciones de curso y universidad sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio institucional verificado.",
    "Conservar universitylocation Roma Norte, Ciudad de Mexico salvo cambio verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar Figura docente solo con nombre confirmado.",
    "No dejar creditos vacios cuando exista dato oficial.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "Evitar placeholders de automatizacion como $(@{...}.Slug) en archivos finales."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "No inventar referencias; solo incluir fuentes consultadas y verificables.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Conservar entrada institucional del sitio web UnADM si fue consultada.",
    "Conservar entrada de malla curricular de Derecho como fuente local.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar.",
    "Usar claves BibTeX estables y descriptivas.",
    "Agregar referencias doctrinales, normativas o jurisprudenciales solo cuando la actividad las requiera."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales reglas validadas de calidad, estructura y trazabilidad.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificacion de JSON parseable a nodos superiores.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Registrar ciclo 1 como normalizacion manual reutilizable cuando falte insumo tematico.",
    "Marcar ciclo 2 como consolidacion de memoria de materia con contexto local.",
    "No propagar metadatos especificos de esta electiva a materias no equivalentes."
  ],
  "open_questions": [
    "Falta insumo tematico verificable de actividad-1 de Filosofia del Derecho para reglas especificas.",
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar codigo oficial de asignatura frente al provisional LDE-S8B1.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Corregir en README y programa los nombres con caracteres perdidos: reporte y referencias.",
    "Reemplazar en README/programa el placeholder $(@{...}.Slug) por electiva-semestre-8-bloque-1."
  ]
}