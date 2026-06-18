{
  "summary": [
    "Consolidar base editorial UnADM para Derechos de autor.",
    "Usar README como entrada canonica de la asignatura.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Preservar reglas utiles heredadas sin regresion.",
    "Marcar herencia Codex como provisional hasta validacion local.",
    "Marcar herencia GPT-Pro como provisional hasta validacion local.",
    "Supuesto: herencia previa incluye salidas no JSON parseable y requiere validacion local."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar datos curriculares locales: semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canonico.",
    "Usar programa-analitico como marco editorial.",
    "Organizar cada producto por problema, conceptos, producto, analisis y cierre.",
    "Mantener separacion entre reporte, presentacion y referencias.",
    "Guardar bibliografia especifica en derechos-de-autor.bib.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Corregir marcadores literales de plantilla en README y programa analitico.",
    "Corregir nombres corruptos como eporte y eferencias antes de publicar.",
    "Sustituir expresiones literales $(@{...}.Slug) por derechos-de-autor.bib."
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
    "No publicar con nombres corruptos de archivo.",
    "Marcar herencia institucional provisional hasta confirmacion en Derecho.",
    "Validar localmente contenido heredado de ciclo 1 antes de reutilizarlo."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo instruccion contraria.",
    "Declarar metadatos con macros antes de \\input{template}.",
    "Conservar tabla de autor con alumno, matricula y datos academicos completos en documentos locales.",
    "No propagar datos personales del alumno a otras materias.",
    "Usar tipografia sans serif de forma consistente si la plantilla la requiere.",
    "Evitar paquetes truncados o lineas incompletas en preambulo.",
    "Nunca dejar \\usepackage sin argumento.",
    "Validar que los paquetes LaTeX queden en preambulo efectivo.",
    "Corregir \\usepackage final sin argumento detectado en reporte.",
    "Mover paquetes cargados despues de \\input{template} al preambulo correcto si la plantilla lo exige."
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
    "Propagar advertencia sobre herencia Codex solo como provisional.",
    "Propagar advertencia sobre herencia GPT-Pro solo como provisional.",
    "Mantener auditoria manual para contenido heredado de ciclo 1 si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Definir nombre de figura docente.",
    "Validar si Roma Norte, Ciudad de Mexico debe mantenerse fija.",
    "Confirmar sustitucion definitiva de marcadores literales por derechos-de-autor.bib.",
    "Revisar y corregir errores de nombres de archivo en README.",
    "Confirmar si la fuente heredada Codex desde ingenieria sigue vigente o debe retirarse tras validacion local.",
    "Confirmar si la fuente heredada GPT-Pro desde Actividad 1 sigue vigente o debe retirarse tras validacion local.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template} en esta plantilla.",
    "Confirmar argumento correcto del \\usepackage truncado al final del preambulo en reporte."
  ]
}