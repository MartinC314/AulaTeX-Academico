{
  "summary": [
    "Memoria de materia consolidada con union-dedupe lossless y sin regresion.",
    "Destino canonico confirmado: UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde.",
    "Se conserva herencia institucional UnADM y trazabilidad de salidas no estructuradas previas.",
    "Se preservan mejoras verificables del contexto local: placeholders de automatizacion y literales corruptos en README/programa.",
    "Ciclo 12: consolidacion recursiva aplicada al destino canonico.",
    "Supuesto: actividad-1 de Filosofia del Derecho no aporta contenido tematico verificable adicional."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion academica.",
    "Usar tono juridico formal, claro y verificable.",
    "Conservar datos de asignatura: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Conservar autor confirmado en plantilla: Martin Jonathan de la Cruz, matricula ES2611202040.",
    "Mantener codigo provisional LDE-S8B1 hasta confirmacion oficial distinta.",
    "Evitar renombrar la asignatura sin confirmacion oficial del nombre de la electiva.",
    "No eliminar reglas heredadas; extender solo con evidencia verificable.",
    "Reconocer fuentes provisionales heredadas: Codex, GPT-Pro, Auto (model-router) y Claude Foundry desde actividad-1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar README, programa analitico, plantilla de reporte, plantilla de presentacion, bibliografia y carpeta de referencias.",
    "Usar el programa analitico como guia de reportes, presentaciones y productos visuales.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, analisis propio y conclusion.",
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
    "Corregir placeholders de automatizacion y literales corruptos en nombres de archivo antes de entrega.",
    "Marcar como pendiente todo dato no confirmado, en especial creditos y figura docente."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con opciones spanish, letterpaper, oneside.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Conservar definiciones de curso y universidad sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio verificado.",
    "Conservar universitylocation Roma Norte, Ciudad de Mexico salvo cambio verificado.",
    "Completar campos pendientes de portada antes de entrega.",
    "Actualizar figura docente solo con nombre confirmado.",
    "No dejar creditos vacios cuando exista dato oficial.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "Evitar placeholders como $(@{...}.Slug) en archivos finales."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "No inventar referencias; solo incluir fuentes consultadas y verificables.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Usar claves BibTeX estables y descriptivas.",
    "Conservar entradas institucionales existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar.",
    "Agregar doctrina, normativa o jurisprudencia solo cuando la actividad lo requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente reglas validadas de calidad, estructura y trazabilidad.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificacion de JSON parseable a nodos superiores.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "No propagar metadatos especificos de esta electiva a materias no equivalentes.",
    "Marcar ciclo 1 como normalizacion manual reutilizable cuando falte insumo tematico.",
    "Marcar ciclos reutilizados como normalizacion manual si persiste falta de insumo tematico.",
    "Marcar ciclo 12 como consolidacion recursiva de memoria de materia."
  ],
  "open_questions": [
    "Falta insumo tematico verificable de actividad-1 de Filosofia del Derecho para reglas especificas.",
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar codigo oficial de asignatura frente al provisional LDE-S8B1.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Corregir en README/programa el placeholder $(@{...}.Slug) por electiva-semestre-8-bloque-1.",
    "Corregir en README y programa los nombres con caracteres perdidos: reporte y referencias."
  ]
}