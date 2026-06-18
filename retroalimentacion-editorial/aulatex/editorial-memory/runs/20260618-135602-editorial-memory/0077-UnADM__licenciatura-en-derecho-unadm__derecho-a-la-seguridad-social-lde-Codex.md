{
  "summary": [
    "Materia destino consolidada como punto de entrada canonico con identidad UnADM y enfoque juridico.",
    "Asignatura ubicada en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Productos orientados a problema, fundamento juridico, evidencia, analisis propio y conclusion transferible.",
    "Persiste alerta institucional por salida no parseable en ciclo 1; requiere normalizacion manual al reutilizar.",
    "Se aplica compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre de materia: Derecho a la seguridad social.",
    "Usar datos curriculares oficiales: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local de curso cuando aplique: LDE-S2B1.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Conservar trazabilidad de reglas heredadas provisionales con marca [supuesto].",
    "No propagar datos personales de plantilla a laterales salvo requerimiento explicito [supuesto].",
    "Registrar fuente provisional heredada como referencia historica: Codex/GPT-Pro desde actividad previa [supuesto]."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Alinear cada entrega a cinco ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Transformar la planeacion semanal en productos con claridad y fundamento.",
    "Registrar en memoria solo reglas accionables y verificables.",
    "Normalizar nombres de archivos con marcadores o caracteres corruptos antes de usar como canon."
  ],
  "activity_rules": [
    "Definir desde el inicio el problema juridico o social de la actividad.",
    "Vincular el desarrollo con normas, doctrina, datos o fuentes pertinentes.",
    "Relacionar el contenido con Derecho a la seguridad social cuando corresponda.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Incluir postura academica propia con argumentacion clara.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Ajustar formato y alcance al producto solicitado por la planeacion semanal.",
    "Evitar afirmaciones no sustentadas o marcarlas como [supuesto]."
  ],
  "quality_gates": [
    "Validar que toda salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Normalizar manualmente salidas no parseables de ciclo 1 cuando se reutilicen.",
    "Verificar coherencia entre objetivos de actividad y estructura final del documento.",
    "Confirmar que toda afirmacion relevante tenga soporte verificable o marca [supuesto].",
    "Comprobar que cada cita tenga entrada BibTeX en el .bib local.",
    "Verificar que no se eliminen reglas utiles previas.",
    "Confirmar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia.",
    "Personalizar solo campos variables de la actividad.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Mantener clase article salvo justificacion tecnica.",
    "Mantener idioma spanish y papel letterpaper si no hay instruccion contraria.",
    "Usar portada con alumno, matricula, figura docente, semestre, bloque, tipo y creditos cuando aplique.",
    "Conservar campo de figura docente como pendiente si el dato no esta disponible.",
    "Corregir rutas y nombres corruptos antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar entradas unadmSitioWeb y unadmMallaDerecho2024 cuando se citen.",
    "Agregar solo referencias especificas de actividad con datos completos y verificables.",
    "No inventar fuentes.",
    "Marcar fuentes faltantes como pendientes.",
    "Verificar correspondencia entre citas en LaTeX y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas en este ciclo.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Aplicar compresion lossless por union-dedupe sin regresion.",
    "Propagar reglas curriculares solo a nodos de la misma materia.",
    "Propagar reglas generales de integridad, citas y JSON parseable a laterales compatibles."
  ],
  "open_questions": [
    "Confirmar vigencia de la fuente provisional heredada desde ingenieria para contexto de Derecho [supuesto].",
    "Definir nombre de figura docente en plantilla cuando el dato oficial exista.",
    "Confirmar norma de citacion requerida para la materia: APA, ISO, institucional o juridica mexicana [supuesto].",
    "Resolver y limpiar marcadores corruptos en README y programa analitico antes de usarlos como canon."
  ]
}