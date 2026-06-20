{
  "summary": [
    "Se conserva estado previo por falta de reglas parseables del origen en este ciclo.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se agrega contexto verificable de asignatura para guiar futuras normalizaciones."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en cada entrega.",
    "Usar enfoque de Licenciatura en Derecho con tono academico-juridico.",
    "[Supuesto] Conservar trazabilidad de fuente cuando el origen no sea parseable."
  ],
  "structure_rules": [
    "Redactar productos con problema, conceptos, analisis propio y conclusion juridica.",
    "Alinear estructura con la pauta editorial local de la asignatura.",
    "Preparar salida en JSON parseable antes de propagar memoria."
  ],
  "activity_rules": [
    "Incluir postura academica propia sustentada en fuentes verificables.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar afirmaciones sin respaldo documental."
  ],
  "quality_gates": [
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar JSON estricto y esquema requerido antes de guardar.",
    "Confirmar no eliminacion de reglas utiles previas."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reportes y presentaciones .tex de la materia.",
    "Usar comandos y acentos consistentes para espanol en LaTeX.",
    "Evitar cambios de formato que rompan compilacion."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Deduplicar entradas bibliograficas equivalentes sin perder trazabilidad."
  ],
  "propagation_hints": [
    "Ciclo 1 requiere normalizacion manual si la entrada no es parseable.",
    "Propagar de forma recursiva solo tras pasar compuertas de calidad.",
    "Priorizar union-dedupe para conservar memoria previa sin recorte."
  ],
  "open_questions": [
    "Falta bloque parseable de reglas en el origen actividad-1 para extraer normas especificas.",
    "Definir criterio operativo para resolver duplicados en .bib con claves distintas y mismos metadatos."
  ]
}