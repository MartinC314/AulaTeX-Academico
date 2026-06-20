{
  "summary": [
    "Memoria de materia consolidada con union-dedupe lossless y sin regresion.",
    "Destino canonico confirmado: UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde.",
    "Se conserva herencia institucional UnADM y trazabilidad de salidas no estructuradas previas.",
    "Se preservan mejoras verificables del contexto local: placeholders de automatizacion y literales corruptos en README/programa.",
    "Supuesto: no se recibio contenido tematico verificable de actividad-1 de Filosofia del Derecho para reglas disciplinares nuevas.",
    "Ciclo 17: consolidacion recursiva aplicada al destino canonico de la electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion academica.",
    "Usar tono juridico formal, claro y verificable.",
    "Conservar datos de asignatura: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No eliminar reglas heredadas; extender solo con evidencia verificable.",
    "Evitar renombrar la asignatura sin confirmacion oficial del nombre de la electiva.",
    "Conservar autor confirmado en plantilla: Martin Jonathan de la Cruz, matricula ES2611202040.",
    "Mantener codigo provisional LDE-S8B1 hasta confirmacion oficial distinta.",
    "Reconocer fuentes provisionales heredadas: Codex, GPT-Pro, Auto (model-router) y Claude Foundry desde actividad-1."
  ],
  "structure_rules": [
    "Mantener carpeta de materia como punto de entrada canonico.",
    "Conservar README, programa analitico, plantilla de reporte, plantilla de presentacion, bibliografia y carpeta de referencias.",
    "Usar el programa analitico como guia de reportes, presentaciones y productos visuales.",
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, analisis propio y conclusion.",
    "Alinear cada actividad al programa analitico de la materia.",
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
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas verificables.",
    "Confirmar que las rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular de Derecho respalde semestre, bloque y tipo.",
    "Corregir placeholders de automatizacion y literales corruptos en nombres de archivo antes de entrega.",
    "Marcar como pendiente todo dato no confirmado, en especial creditos y figura docente."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con opciones spanish, letterpaper, oneside.",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Conservar definiciones de curso y universidad sin renombrados inconsistentes.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio verificado.",
    "Conservar universitylocation Roma Norte, Ciudad de Mexico salvo cambio verificado.",
    "Completar campos pendientes de portada antes de entrega, en especial figura docente y creditos.",
    "No dejar creditos vacios cuando exista dato oficial.",
    "Evitar placeholders como $(@{...}.Slug) en archivos finales.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local."
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
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificacion de JSON parseable a nodos superiores.",
    "No propagar metadatos especificos de esta electiva a materias no equivalentes.",
    "Marcar ciclo 1 como normalizacion manual reutilizable cuando falte insumo tematico.",
    "Marcar ciclo 17 como consolidacion recursiva de memoria de materia.",
    "Supuesto: ciclo 17 requiere normalizacion manual si persiste falta de insumo tematico."
  ],
  "open_questions": [
    "Falta contenido fuente de actividad-1 de Filosofia del Derecho para extraer reglas especificas.",
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar codigo oficial de asignatura frente al provisional LDE-S8B1.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Corregir en README y programa los nombres con caracteres perdidos: reporte y referencias.",
    "Reemplazar en README/programa el placeholder $(@{...}.Slug) por electiva-semestre-8-bloque-1."
  ]
}