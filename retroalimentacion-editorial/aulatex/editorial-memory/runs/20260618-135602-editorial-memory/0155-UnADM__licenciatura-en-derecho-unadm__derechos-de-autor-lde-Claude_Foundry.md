```json
{
  "summary": [
    "Consolidar base editorial UnADM para la materia Derechos de autor.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Usar README como entrada canonica de la asignatura.",
    "Marcar herencia Codex como provisional hasta validacion local.",
    "Preservar reglas utiles heredadas sin regresion.",
    "Supuesto: herencia previa proviene de fuente provisional sin JSON parseable y requiere validacion local."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar datos curriculares locales: semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1 en documentos.",
    "Marcar como provisional la fuente Codex heredada desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canonico de la asignatura.",
    "Usar programa-analitico como marco para problema, conceptos, producto, analisis y cierre.",
    "Guardar bibliografia especifica en derechos-de-autor.bib.",
    "Mantener separacion entre reporte, presentacion y referencias de la materia.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Corregir marcadores literales de plantilla en README y programa analitico.",
    "Corregir nombres corruptos como eporte y eferencias antes de publicar.",
    "Sustituir expresiones literales $(@{...}.Slug) por derechos-de-autor.bib en README y programa analitico."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Vincular conceptos con normas, doctrina o datos verificables.",
    "Cumplir formato solicitado por la planeacion semanal.",
    "Incluir analisis propio explicito, no solo resumen de fuentes.",
    "Cerrar con conclusion aplicable a la practica juridica.",
    "Agregar fuentes especificas por actividad al archivo BibTeX local."
  ],
  "quality_gates": [
    "Rechazar salidas no JSON parseable antes de propagar memoria.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Exigir citas verificables con correspondencia en .bib local.",
    "Detectar y corregir campos pendientes como Nombre por definir.",
    "Auditar README por caracteres extranos y marcadores de plantilla.",
    "Mantener normalizacion manual durante ciclo 1.",
    "Marcar herencia institucional previa como provisional hasta confirmacion en Derecho."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo instruccion contraria.",
    "Declarar metadatos con macros antes de \\input{template}.",
    "Conservar tabla de autor con alumno, matricula y datos academicos completos.",
    "Evitar paquetes truncados o lineas incompletas en preambulo.",
    "Usar tipografia sans serif de forma consistente si la plantilla la requiere.",
    "Nunca dejar \\usepackage sin argumento.",
    "Validar que los paquetes LaTeX queden en preambulo efectivo.",
    "No propagar datos personales del alumno a otras materias.",
    "Corregir \\usepackage final sin argumento detectado al cierre del preambulo en reporte."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales institucionales o verificables.",
    "Registrar fuentes base UnADM ya incluidas en derechos-de-autor.bib.",
    "Conservar entrada local unadmSitioWeb si se cita.",
    "Conservar entrada local unadmMallaDerecho2024 si se cita.",
    "Agregar entradas BibTeX completas por actividad.",
    "Incluir fecha de consulta en fuentes web.",
    "Asegurar que toda cita en texto tenga entrada en .bib y viceversa.",
    "Asegurar que toda entrada .bib usada corresponda con una cita o bibliografia requerida."
  ],
  "propagation_hints": [
    "Propagar hacia arriba reglas institucionales validadas en esta materia.",
    "Propagar lateralmente a materias LDE solo reglas genericas de calidad y estructura.",
    "No propagar datos personales del alumno a otras materias.",
    "No propagar marcadores pendientes ni nombres corruptos de archivo.",
    "Mantener bandera de normalizacion manual en ciclo 1 para contenido heredado.",
    "Propagar advertencia sobre herencia Codex solo como provisional."
  ],
  "open_questions": [
    "Confirmar si la clave de curso LDE-S5B1 es oficial en toda la suite.",
    "Definir nombre de figura docente para eliminar marcador pendiente.",
    "Validar si Roma Norte, Ciudad de Mexico debe mantenerse fija.",
    "Revisar y corregir errores de nombres de archivo en README (lineas con caracteres extranos).",
    "Confirmar sustitucion definitiva de marcadores literales por derechos-de-autor.bib.",
    "Confirmar si la fuente heredada Codex desde ingenieria sigue vigente o debe retirarse tras validacion local.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template} en esta plantilla.",
    "Confirmar argumento correcto del \\usepackage truncado al final del preambulo en reporte."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derechos-de-autor-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```