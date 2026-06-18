{
  "summary": [
    "Supuesto: la herencia institucional es valida y aplicable al destino.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Normalizar salidas no JSON antes de propagar."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en portada, tono y contexto.",
    "Usar datos de materia: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Marcar fuente como provisional cuando provenga de herencia no especifica de la materia."
  ],
  "structure_rules": [
    "Usar README de la materia como punto de entrada canonico.",
    "Alinear cada entrega con ejes: problema, conceptos/normas, producto, analisis propio, conclusion.",
    "Mantener separacion entre reporte .tex, presentacion .tex y .bib local."
  ],
  "activity_rules": [
    "Incluir problema juridico o social explicito al inicio.",
    "Incluir analisis propio con postura academica.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de guardar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar consistencia entre metadatos de portada y programa analitico."
  ],
  "latex_rules": [
    "Completar campos pendientes de plantilla antes de compilar.",
    "Mantener variables institucionales y de curso consistentes en el preambulo.",
    "Usar espanol y formato carta segun plantilla base."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en derecho-fiscal-y-tributario.bib.",
    "Priorizar fuentes institucionales UnADM y documentos normativos verificables.",
    "No inventar referencias; marcar [fuente pendiente] cuando falte dato."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo tras normalizacion JSON.",
    "Conservar regla de sin regresion en ciclos siguientes.",
    "Ciclo 1: aplicar normalizacion manual si la entrada heredada es ambigua."
  ],
  "open_questions": [
    "Definir nombre de figura docente en plantilla.",
    "Confirmar si la fuente provisional de ingenieria sigue vigente para Derecho.",
    "Corregir rutas con caracteres anomalos en README (reporte/referencias)."
  ]
}