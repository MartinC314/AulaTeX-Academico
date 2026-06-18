{
  "summary": [
    "Materia destino configurada como punto de entrada canonico con identidad UnADM y enfoque juridico.",
    "Se conserva alerta institucional: hubo salida no parseable en ciclo previo y requiere normalizacion manual.",
    "La asignatura exige productos con problema, fundamento, analisis propio y conclusion juridica transferible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales de la materia: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Conservar trazabilidad de origen cuando una regla sea provisional [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Alinear cada entrega a los cinco ejes: problema, conceptos/norma, producto, analisis, conclusion.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Registrar en memoria solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Definir desde el inicio el problema juridico o social de la actividad.",
    "Vincular el desarrollo con normas, doctrina o datos pertinentes al tema.",
    "Incluir postura academica propia con argumentacion clara.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Ajustar el formato al producto solicitado por la planeacion semanal."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas y normalizar manualmente cuando aplique.",
    "Verificar coherencia entre objetivos de actividad y estructura final del documento.",
    "Confirmar que toda afirmacion relevante tenga soporte verificable o marca de supuesto."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todo archivo .tex.",
    "Usar una estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Evitar cambios de clase o formato que rompan compatibilidad sin justificacion tecnica."
  ],
  "bibliography_rules": [
    "Usar el archivo .bib local de la materia como fuente bibliografica central.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo referencias especificas de actividad con datos completos y verificables.",
    "No inventar fuentes; marcar faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas ya validadas en este ciclo.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Aplicar compresion union-dedupe sin perdida y sin regresion."
  ],
  "open_questions": [
    "Confirmar si la regla de fuente provisional desde ingenieria sigue vigente para Derecho [supuesto].",
    "Definir nombre de figura docente en plantilla cuando se disponga del dato.",
    "Verificar si se requiere norma de citacion juridica especifica adicional (APA, ISO o institucional) [supuesto]."
  ]
}