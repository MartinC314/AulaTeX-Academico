{
  "summary": [
    "Supuesto: la herencia institucional es valida y aplicable al destino.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Normalizar salidas no JSON antes de propagar.",
    "Preservar memoria editorial de UnADM, Derecho y la materia destino.",
    "Salida sin JSON parseable desde Codex para UnADM.",
    "Herencia de alcance institucional UnADM aplicada en ciclo 1.",
    "Consolidacion ciclo 1 completada sin regresion y sin recorte."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en portada, tono y contexto.",
    "Usar datos de materia: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar clave de curso LDE-S6B1 cuando aplique.",
    "Marcar fuente como provisional cuando provenga de herencia no especifica de la materia.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Verificar datos personales y figura docente antes de entrega final.",
    "Autor base en plantilla: Martin Jonathan de la Cruz; matricula ES2611202040; verificar antes de compartir."
  ],
  "structure_rules": [
    "Usar README de la materia como punto de entrada canonico.",
    "Mantener estructura local: reporte, presentacion, bibliografia, programa analitico y carpeta de referencias.",
    "Alinear cada entrega con ejes: problema, conceptos o normas, producto, analisis propio y conclusion.",
    "Corregir nombres rotos en README antes de publicar.",
    "Corregir slug .bib dinamico sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Incluir problema juridico o social explicito al inicio.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Desarrollar el producto solicitado por la planeacion.",
    "Incluir analisis propio con postura academica.",
    "Cerrar con conclusion juridica transferible a la practica.",
    "Vincular argumentos fiscales y tributarios con aplicacion profesional."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de guardar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar consistencia entre metadatos de portada y programa analitico.",
    "Confirmar semestre, bloque, tipo y creditos contra la malla curricular local.",
    "Revisar que no existan placeholders sin resolver en README, .tex o .bib.",
    "Comprobar que toda cita usada tenga entrada bibliografica verificable.",
    "Verificar integridad de .tex para compilacion y cierre de entornos truncados.",
    "Corregir rutas con caracteres anomalos antes de publicar."
  ],
  "latex_rules": [
    "Usar espanol y formato carta segun plantilla base.",
    "Conservar portada institucional con UnADM y Licenciatura en Derecho.",
    "Mantener variables institucionales y de curso consistentes en el preambulo.",
    "Actualizar titulo, subtitulo y actividad antes de cada entrega.",
    "Completar campos pendientes de plantilla antes de compilar.",
    "Sustituir placeholders generados por expresiones de plantilla.",
    "Corregir bloque authortable truncado antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en derecho-fiscal-y-tributario.bib.",
    "Priorizar fuentes institucionales UnADM y documentos normativos verificables.",
    "Usar como base unadmSitioWeb y unadmMallaDerecho2024 cuando sean pertinentes.",
    "Citar la malla curricular local solo para datos curriculares.",
    "No inventar referencias; marcar [fuente pendiente] cuando falte dato.",
    "Agregar doctrina, legislacion o jurisprudencia solo si la actividad lo exige y la fuente es verificable."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo tras normalizacion JSON.",
    "Mantener union-dedupe como metodo de compresion.",
    "Conservar regla de sin regresion en ciclos siguientes.",
    "Ciclo 1: aplicar normalizacion manual si la entrada heredada es ambigua.",
    "Propagar reglas generales de identidad UnADM a materias laterales.",
    "No propagar datos especificos de Derecho fiscal y tributario a materias no equivalentes."
  ],
  "open_questions": [
    "Definir nombre de figura docente en plantilla.",
    "Confirmar si la fuente provisional de ingenieria sigue vigente para Derecho.",
    "Confirmar si el autor y matricula deben permanecer en plantillas compartidas.",
    "Confirmar formato de citacion requerido por la asignatura.",
    "Confirmar si se requiere bibliografia fiscal base adicional para la materia.",
    "Resolver expresiones PowerShell sin expandir en README y programa analitico para el slug .bib.",
    "Corregir rutas con caracteres anomalos en README: reporte y referencias.",
    "Supuesto: la entrada .bib local sera derecho-fiscal-y-tributario.bib en todas las actividades."
  ]
}