{
  "summary": [
    "Consolidar base editorial UnADM para Derechos de autor.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Usar README como entrada canonica de la asignatura.",
    "Marcar herencia Codex como provisional hasta validacion local.",
    "Preservar reglas utiles heredadas sin regresion."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar datos curriculares locales: semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1.",
    "Marcar como provisional la fuente Codex heredada desde ingenieria."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canonico.",
    "Usar programa-analitico como marco editorial.",
    "Organizar cada producto por problema, conceptos, producto, analisis y cierre.",
    "Mantener separacion entre reporte, presentacion y referencias.",
    "Guardar bibliografia especifica en derechos-de-autor.bib.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Corregir marcadores literales de plantilla en README y programa analitico.",
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
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Exigir citas verificables con correspondencia en .bib local.",
    "Detectar y corregir campos pendientes como Nombre por definir.",
    "Auditar README por caracteres extranos y marcadores de plantilla.",
    "Marcar herencia institucional previa como provisional hasta confirmacion en Derecho.",
    "Mantener normalizacion manual durante ciclo 1."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo instruccion contraria.",
    "Declarar metadatos con macros antes de \\input{template}.",
    "Conservar tabla de autor con alumno, matricula y datos academicos completos.",
    "No propagar datos personales del alumno a otras materias.",
    "Evitar paquetes truncados o lineas incompletas en preambulo.",
    "Nunca dejar \\usepackage sin argumento.",
    "Usar tipografia sans serif de forma consistente si la plantilla la requiere.",
    "Validar que los paquetes LaTeX queden en preambulo efectivo."
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
    "No propagar datos personales del alumno.",
    "No propagar marcadores pendientes ni nombres corruptos de archivo.",
    "Mantener bandera de normalizacion manual en ciclo 1.",
    "Propagar advertencia sobre herencia Codex solo como provisional."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Definir nombre de figura docente.",
    "Validar si Roma Norte, Ciudad de Mexico debe mantenerse fija.",
    "Confirmar sustitucion definitiva de marcadores literales por derechos-de-autor.bib.",
    "Confirmar si la fuente heredada Codex desde ingenieria sigue vigente.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template} en esta plantilla."
  ]
}