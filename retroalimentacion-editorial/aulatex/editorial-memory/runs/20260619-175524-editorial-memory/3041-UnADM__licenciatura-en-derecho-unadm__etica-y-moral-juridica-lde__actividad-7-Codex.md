{
  "summary": [
    "Se conserva memoria valida previa por falta de bloque JSON parseable del origen en este ciclo. [Supuesto]",
    "Se mantiene compresion lossless por union y deduplicacion semantica sin recorte.",
    "Se preserva contexto verificable de asignatura: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza validacion JSON estricta y esquema requerido antes de propagacion recursiva.",
    "Se deduplican reglas equivalentes sin eliminar reglas utiles.",
    "Se agrega control de consistencia con pauta editorial local y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en cada entrega.",
    "Usar enfoque de Licenciatura en Derecho con tono academico-juridico.",
    "Alinear la actividad con la asignatura Etica y Moral juridica del semestre 1, bloque 2.",
    "Conservar trazabilidad de fuente cuando el origen no sea parseable. [Supuesto]",
    "Registrar fuente provisional del ciclo cuando no exista JSON valido del origen. [Supuesto]"
  ],
  "structure_rules": [
    "Redactar con problema, conceptos, analisis propio y conclusion juridica.",
    "Integrar el producto solicitado por la planeacion semanal.",
    "Alinear estructura con la pauta editorial local de la asignatura.",
    "Preparar salida en JSON parseable antes de propagar memoria."
  ],
  "activity_rules": [
    "Incluir postura academica propia sustentada en fuentes verificables.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar afirmaciones sin respaldo documental.",
    "Mantener integridad academica en citas y referencias."
  ],
  "quality_gates": [
    "Validar JSON estricto y esquema requerido antes de guardar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar no eliminacion de reglas utiles previas.",
    "Aplicar propagacion recursiva solo si pasa compuertas de calidad.",
    "Marcar supuestos de forma explicita cuando falten datos parseables."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reporte, presentacion y .bib de la materia.",
    "Usar comandos y acentos consistentes para espanol en LaTeX.",
    "Evitar cambios de formato que rompan compilacion.",
    "Conservar consistencia entre archivos .tex y bibliografia local."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Deduplicar entradas bibliograficas equivalentes sin perder trazabilidad.",
    "Mantener una clave canonica y mapear aliases cuando existan duplicados de la misma obra. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar de forma recursiva solo tras validacion de esquema requerido.",
    "Priorizar union-dedupe para conservar memoria previa sin recorte.",
    "Si la entrada no es parseable, conservar estado y agregar nota de ciclo.",
    "Ejecutar normalizacion manual cuando persista salida no parseable.",
    "Ciclo 13 requiere normalizacion manual si la entrada no es parseable."
  ],
  "open_questions": [
    "Falta bloque parseable de reglas en el origen actividad-1 para extraer normas especificas.",
    "Definir criterio operativo final para duplicados .bib con claves distintas y metadatos iguales.",
    "Confirmar politica de alias bibliografico en citas LaTeX para no romper documentos existentes. [Supuesto]",
    "Confirmar si se corrige el .bib local truncado antes de nuevas propagaciones. [Supuesto]"
  ]
}