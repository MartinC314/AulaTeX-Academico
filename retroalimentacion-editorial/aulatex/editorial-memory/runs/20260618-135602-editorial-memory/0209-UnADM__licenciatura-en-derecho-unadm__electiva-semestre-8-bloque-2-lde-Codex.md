{
  "summary": [
    "Base institucional UnADM disponible, pero la herencia previa indica salida no JSON en origen historico.",
    "Aplicar normalizacion manual en ciclo 1 antes de propagar cambios derivados.",
    "La materia destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Conservar tono academico-juridico con postura propia sustentada."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Organizar cada actividad en problema, conceptos/fuentes, producto, analisis propio y conclusion.",
    "Mantener consistencia entre README, programa analitico, reporte, presentacion y .bib local."
  ],
  "activity_rules": [
    "Traducir la planeacion semanal a producto concreto solicitado por la actividad.",
    "Incluir analisis juridico propio, no solo resumen de fuentes.",
    "Cerrar cada actividad con conclusion aplicable a la practica juridica."
  ],
  "quality_gates": [
    "Validar que toda salida sea JSON parseable antes de consolidar memoria.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizacion.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y sus metadatos institucionales.",
    "Completar campos pendientes del front matter antes de entrega final.",
    "Mantener compatibilidad de nombres de archivos entre .tex y recursos de la materia."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "No inventar referencias; marcar [supuesto] cuando falte dato verificable."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas y sin ambiguedad.",
    "Etiquetar reglas heredadas de calidad como transversales de institucion UnADM.",
    "Mantener compresion por union-dedupe sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "[supuesto] Confirmar fuentes concretas de la actividad 1 de Filosofia del Derecho para reglas mas especificas.",
    "[supuesto] Definir creditos oficiales de la materia para completar metadatos.",
    "[supuesto] Confirmar nombre de figura docente para plantilla de reporte."
  ]
}