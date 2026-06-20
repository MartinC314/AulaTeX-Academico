{
  "summary": [
    "Consolidar base editorial UnADM para la materia Derechos de autor.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Conservar README como entrada canonica de la asignatura.",
    "Preservar reglas utiles heredadas sin regresion.",
    "Registrar incidencias de salida no JSON parseable de fuentes heredadas previas.",
    "Marcar herencia previa no parseable como provisional hasta validacion local.",
    "Supuesto: la herencia desde filosofia-del-derecho-lde/actividad-1 sigue sin JSON parseable verificable.",
    "Origen ciclo 9: actividad-1 de filosofia-del-derecho-lde sin JSON parseable confirmado."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1 en documentos.",
    "Marcar fuentes heredadas no parseables como provisionales hasta validacion local.",
    "Fuente provisional: filosofia-del-derecho-lde/actividad-1 (sin JSON parseable).",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canonico de la asignatura.",
    "Usar programa-analitico como marco editorial.",
    "Organizar cada producto por problema, conceptos, producto, analisis y cierre.",
    "Mantener separacion entre reporte, presentacion y referencias.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Guardar bibliografia especifica en derechos-de-autor.bib.",
    "Sustituir marcadores literales $(@{...}.Slug) por derechos-de-autor.bib en README y programa analitico.",
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
    "Auditar README por marcadores de plantilla y caracteres extranos.",
    "No publicar con nombres corruptos de archivo.",
    "Validar localmente contenido heredado de ciclos previos antes de reutilizarlo.",
    "Mantener auditoria manual para contenido heredado de ciclos previos si se reutiliza."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo instruccion contraria.",
    "Declarar metadatos con macros antes de \\input{template}.",
    "Conservar tabla de autor con alumno, matricula y datos academicos completos en documentos locales.",
    "No propagar datos personales del alumno a otras materias.",
    "Nunca dejar \\usepackage sin argumento.",
    "Validar que los paquetes LaTeX queden en preambulo efectivo.",
    "Mover paquetes cargados despues de \\input{template} al preambulo correcto si la plantilla lo exige.",
    "Corregir \\usepackage truncado detectado al final del preambulo en reporte."
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
    "Propagar advertencias de herencia provisional solo como provisionales.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Ciclo 2 necesita normalizacion manual si se reutiliza.",
    "Ciclo 3 necesita normalizacion manual si se reutiliza.",
    "Ciclo 4 necesita normalizacion manual si se reutiliza.",
    "Ciclo 5 necesita normalizacion manual si se reutiliza.",
    "Ciclo 6 necesita normalizacion manual si se reutiliza.",
    "Ciclo 7 necesita normalizacion manual si se reutiliza.",
    "Ciclo 8 necesita normalizacion manual si se reutiliza.",
    "Ciclo 9 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si la clave de curso LDE-S5B1 es oficial en toda la suite.",
    "Definir nombre de figura docente para eliminar marcador pendiente.",
    "Validar si la ubicacion Roma Norte, Ciudad de Mexico debe mantenerse fija.",
    "Confirmar sustitucion definitiva de marcadores literales por derechos-de-autor.bib.",
    "Revisar y corregir errores de nombres de archivo en README.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template} en esta plantilla.",
    "Confirmar argumento correcto del \\usepackage truncado al final del preambulo en reporte.",
    "Confirmar si la herencia provisional (Codex, GPT-Pro, Auto, Claude) sigue vigente o debe retirarse tras validacion local."
  ]
}