{
  "summary": [
    "Consolidar base editorial UnADM para la materia Derechos de autor.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Usar README como entrada canonica de la asignatura.",
    "Preservar reglas utiles heredadas sin regresion.",
    "Marcar herencia Codex como provisional hasta validacion local.",
    "Supuesto: herencia previa incluye salidas no JSON parseable y requiere validacion local."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1 en documentos.",
    "Marcar como provisional la fuente Codex heredada desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canonico de la asignatura.",
    "Usar programa-analitico como marco para problema, conceptos, producto, analisis y cierre.",
    "Mantener separacion entre reporte, presentacion y referencias de la materia.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Guardar bibliografia especifica en derechos-de-autor.bib.",
    "Corregir marcadores literales de plantilla en README y programa analitico.",
    "Sustituir $(@{...}.Slug) por derechos-de-autor.bib.",
    "Corregir nombres corruptos como eporte y eferencias antes de publicar."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Vincular conceptos con normas, doctrina o datos verificables.",
    "Cumplir formato solicitado por la planeacion semanal.",
    "Incluir analisis propio explicito.",
    "Evitar entregar solo resumen de fuentes.",
    "Cerrar con conclusion aplicable a la practica juridica.",
    "Agregar fuentes especificas por actividad al archivo BibTeX local."
  ],
  "quality_gates": [
    "Rechazar salidas no JSON parseable antes de propagar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Exigir citas verificables con correspondencia en .bib local.",
    "Detectar y corregir campos pendientes como Nombre por definir.",
    "Auditar README por caracteres extranos y marcadores de plantilla.",
    "Mantener normalizacion manual durante ciclo 1.",
    "Marcar herencia institucional provisional hasta confirmacion en Derecho."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo instruccion contraria.",
    "Declarar metadatos con macros antes de \\input{template}.",
    "Conservar tabla de autor con alumno, matricula y datos academicos completos.",
    "No propagar datos personales del alumno a otras materias.",
    "Validar que los paquetes LaTeX queden en preambulo efectivo.",
    "Evitar paquetes truncados o lineas incompletas en preambulo.",
    "Nunca dejar \\usepackage sin argumento.",
    "Mover paquetes cargados despues de \\input{template} al preambulo correcto si la plantilla lo exige.",
    "Corregir \\usepackage final sin argumento detectado en reporte."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo materiales institucionales o verificables.",
    "Registrar fuentes base UnADM incluidas en derechos-de-autor.bib.",
    "Conservar entrada local unadmSitioWeb si se cita.",
    "Conservar entrada local unadmMallaDerecho2024 si se cita.",
    "Agregar entradas BibTeX completas por actividad.",
    "Incluir fecha de consulta en fuentes web.",
    "Asegurar que toda cita en texto tenga entrada en .bib.",
    "Asegurar que toda entrada .bib usada corresponda con una cita o bibliografia requerida."
  ],
  "propagation_hints": [
    "Propagar hacia arriba reglas institucionales validadas en esta materia.",
    "Propagar lateralmente a materias LDE solo reglas genericas de calidad y estructura.",
    "No propagar datos personales del alumno a otras materias.",
    "No propagar marcadores pendientes ni nombres corruptos de archivo.",
    "Mantener bandera de normalizacion manual en ciclo 1.",
    "Propagar advertencia sobre herencia Codex solo como provisional.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Definir nombre de figura docente para eliminar marcador pendiente.",
    "Validar si Roma Norte, Ciudad de Mexico debe mantenerse fija.",
    "Confirmar sustitucion definitiva de marcadores literales por derechos-de-autor.bib.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template} en esta plantilla.",
    "Confirmar argumento correcto del \\usepackage truncado al final del preambulo en reporte.",
    "Confirmar si la fuente heredada Codex sigue vigente o debe retirarse tras validacion local."
  ]
}