{
  "summary": [
    "Supuesto: la herencia institucional es valida y aplicable al destino.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Normalizar salidas no JSON antes de propagar.",
    "Preservar memoria editorial de UnADM, Derecho y la materia destino.",
    "Salida heredada desde Codex no fue JSON parseable.",
    "Herencia de alcance institucional UnADM aplicada en ciclo 1.",
    "Salida sin JSON parseable desde GPT-Pro para derecho-fiscal-y-tributario-lde.",
    "Ciclo 2: consolidar memoria sin regresion y sin recorte.",
    "Salida sin JSON parseable desde Codex para UnADM.",
    "Salida sin JSON parseable desde Codex para derecho-fiscal-y-tributario-lde.",
    "Salida sin JSON parseable desde Auto (model-router) para derecho-fiscal-y-tributario-lde.",
    "Salida sin JSON parseable desde Claude Foundry para derecho-fiscal-y-tributario-lde.",
    "Consolidacion ciclo 1 completada sin regresion y sin recorte.",
    "Ciclo 3: consolidar memoria sin regresion y sin recorte.",
    "Detectada evidencia local de README y programa analitico con rutas o slugs rotos que requieren normalizacion.",
    "Ciclo 4: consolidar memoria sin regresion y sin recorte.",
    "Detectada evidencia local de bloque LaTeX authortable truncado en el reporte.",
    "Ciclo 5: consolidar memoria sin regresion y con deduplicacion lossless."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en portada, tono y contexto.",
    "Usar datos de materia: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Marcar fuente como provisional cuando provenga de herencia no especifica de la materia.",
    "Usar clave de curso LDE-S6B1 cuando aplique.",
    "Fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Verificar datos personales y figura docente antes de entrega final.",
    "Autor base en plantilla: Martin Jonathan de la Cruz; matricula ES2611202040; verificar antes de compartir.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: Auto (model-router) desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1."
  ],
  "structure_rules": [
    "Usar README de la materia como punto de entrada canonico.",
    "Alinear cada entrega con ejes: problema, conceptos o normas, producto, analisis propio y conclusion.",
    "Mantener separacion entre reporte .tex, presentacion .tex y .bib local.",
    "Usar programa analitico como guia editorial de la materia.",
    "Mantener estructura local: reporte, presentacion, bibliografia, programa analitico y carpeta de referencias.",
    "Corregir nombres rotos en README antes de publicar.",
    "Corregir slug .bib dinamico sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Incluir problema juridico o social explicito al inicio.",
    "Incluir analisis propio con postura academica.",
    "Cerrar con conclusion juridica transferible a la practica.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Desarrollar el producto solicitado por la planeacion.",
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
    "Completar campos pendientes de plantilla antes de compilar.",
    "Mantener variables institucionales y de curso consistentes en el preambulo.",
    "Usar espanol y formato carta segun plantilla base.",
    "Actualizar titulo, subtitulo y actividad antes de cada entrega.",
    "Conservar portada institucional con UnADM y Licenciatura en Derecho.",
    "Sustituir placeholders generados por expresiones de plantilla.",
    "Reemplazar titulo y subtitulo base por los de la actividad real.",
    "Corregir bloque authortable truncado antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en derecho-fiscal-y-tributario.bib.",
    "Priorizar fuentes institucionales UnADM y documentos normativos verificables.",
    "No inventar referencias; marcar [fuente pendiente] cuando falte dato.",
    "Usar como base unadmSitioWeb y unadmMallaDerecho2024 cuando sean pertinentes.",
    "Citar la malla curricular local solo para datos curriculares.",
    "Agregar doctrina, legislacion o jurisprudencia solo si la actividad lo exige y la fuente es verificable."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo tras normalizacion JSON.",
    "Conservar regla de sin regresion en ciclos siguientes.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Propagar reglas generales de identidad UnADM a materias laterales.",
    "No propagar datos especificos de Derecho fiscal y tributario a materias no equivalentes.",
    "Mantener union-dedupe como metodo de compresion.",
    "En ciclo 2, priorizar mejoras verificables del contexto local antes de lateralizar.",
    "Ciclo 3 necesita normalizacion manual si se reutiliza.",
    "Ciclo 4 necesita normalizacion manual si se reutiliza.",
    "Ciclo 5 necesita normalizacion manual si se reutiliza.",
    "Ciclo 6 necesita normalizacion manual si se reutiliza.",
    "Ciclo 7 necesita normalizacion manual si se reutiliza.",
    "Ciclo 8 necesita normalizacion manual si se reutiliza.",
    "Ciclo 9 necesita normalizacion manual si se reutiliza.",
    "Ciclo 10 necesita normalizacion manual si se reutiliza.",
    "Ciclo 11 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Definir nombre de figura docente en plantilla.",
    "Confirmar si la fuente provisional de ingenieria sigue vigente para Derecho.",
    "Corregir rutas con caracteres anomalos en README: reporte y referencias.",
    "Confirmar si el autor y matricula deben permanecer en plantillas compartidas.",
    "Confirmar si se requiere bibliografia fiscal base adicional para la materia.",
    "Confirmar formato de citacion requerido por la asignatura.",
    "Resolver expresiones PowerShell sin expandir en README y programa analitico para el slug .bib.",
    "Supuesto: la entrada .bib local sera derecho-fiscal-y-tributario.bib en todas las actividades.",
    "Cerrar correctamente el bloque authortable y el documento LaTeX del reporte."
  ]
}