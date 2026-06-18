```json
{
  "summary": [
    "Base editorial de materia creada desde contexto local de Electiva S8 B1.",
    "Se conserva herencia institucional UnADM y control de calidad por salida no estructurada previa.",
    "Se integra memoria heredada institucional mediante union-dedupe lossless.",
    "Destino canonico: UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-1-lde.",
    "Salida sin JSON parseable desde Codex para UnADM registrada como antecedente.",
    "Salida sin JSON parseable desde GPT-Pro para electiva-semestre-8-bloque-1-lde.",
    "Memoria de materia consolidada con union-dedupe lossless sin eliminar reglas utiles.",
    "Se incorporan mejoras verificables del contexto local: placeholders de automatizacion y literales corruptos en README/programa.",
    "Supuesto: actividad-1 de Filosofia del Derecho no aporta contenido tematico verificable para nuevas reglas disciplinares.",
    "Ciclo 2: consolidacion de memoria de materia con contexto local revisado."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y redaccion academica.",
    "Usar tono juridico formal, claro y verificable.",
    "Conservar datos de asignatura: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No eliminar reglas heredadas; extender solo con evidencia verificable.",
    "Evitar renombrar la asignatura sin confirmacion oficial del nombre de la electiva.",
    "Conservar autor confirmado en plantilla: Martin Jonathan de la Cruz, matricula ES2611202040.",
    "Mantener codigo provisional LDE-S8B1 hasta confirmacion oficial distinta.",
    "Fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional heredada: GPT-Pro desde actividad-1."
  ],
  "structure_rules": [
    "Organizar entregables en secuencia: problema, conceptos o fuentes, producto, analisis propio, conclusion.",
    "Alinear cada actividad al programa analitico de la materia.",
    "Incluir conclusion juridica transferible a la practica.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar README, programa analitico, plantilla de reporte, plantilla de presentacion, bibliografia y carpeta de referencias.",
    "Usar el programa analitico editorial como guia de reportes, presentaciones y productos visuales."
  ],
  "activity_rules": [
    "Declarar objetivo de la actividad al inicio del reporte.",
    "Vincular el producto solicitado con al menos un problema juridico o social.",
    "Diferenciar resumen de fuentes y analisis propio del estudiante.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Cerrar con postura academica sustentada.",
    "No trasladar contenido tematico de Filosofia del Derecho sin insumo verificable."
  ],
  "quality_gates": [
    "Verificar que la salida sea JSON parseable antes de propagar.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con citas verificables.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Corregir placeholders de automatizacion y literales corruptos en nombres de archivo antes de entrega.",
    "Confirmar que rutas locales citadas existan antes de usarlas como fuente.",
    "Revisar que la malla curricular de Derecho respalde semestre, bloque y tipo.",
    "Marcar como pendiente todo dato no confirmado, en especial creditos y figura docente."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes.",
    "Mantener clase article con opciones spanish, letterpaper, oneside.",
    "Completar campos pendientes de portada antes de entrega (docente, creditos si aplica).",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo cambio institucional verificado.",
    "Conservar universitylocation Roma Norte, Ciudad de Mexico salvo cambio verificado.",
    "Actualizar Figura docente solo con nombre confirmado.",
    "No dejar creditos vacios cuando exista dato oficial.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local.",
    "Evitar placeholders de automatizacion como $(@{...}.Slug) en archivos finales."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en electiva-semestre-8-bloque-1.bib.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "No inventar referencias; solo incorporar fuentes consultadas y verificables.",
    "Mantener notas de consulta y ruta de archivo cuando la fuente sea local.",
    "Conservar entradas institucionales existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar.",
    "Conservar entrada de malla curricular de Derecho como fuente local.",
    "Agregar doctrina, normativa o jurisprudencia solo cuando la actividad lo requiera.",
    "Usar claves BibTeX estables y descriptivas."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales reglas validadas de calidad, estructura y trazabilidad.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Propagar la regla de no inventar fuentes a nodos relacionados.",
    "Propagar la verificacion de JSON parseable a nodos superiores.",
    "No propagar metadatos especificos de esta electiva a materias no equivalentes.",
    "Registrar ciclo 1 como normalizacion manual reutilizable cuando falte insumo tematico.",
    "Marcar ciclo 2 como consolidacion de memoria de materia con contexto local."
  ],
  "open_questions": [
    "Falta insumo tematico verificable de actividad-1 de Filosofia del Derecho para reglas especificas.",
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la electiva si difiere del usado actualmente.",
    "Confirmar nombre de figura docente para plantilla base.",
    "Confirmar existencia y consistencia de presentacion-electiva-semestre-8-bloque-1.tex.",
    "Corregir en README y programa los nombres con caracteres perdidos: reporte y referencias.",
    "Reemplazar en README/programa el placeholder $(@{...}.Slug) por electiva-semestre-8-bloque-1.",
    "Confirmar codigo oficial de asignatura frente al provisional LDE-S8B1."
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
```