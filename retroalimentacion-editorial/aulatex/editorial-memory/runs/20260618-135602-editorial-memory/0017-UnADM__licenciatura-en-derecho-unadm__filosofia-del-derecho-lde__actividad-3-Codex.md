{
  "summary": [
    "Base heredada indica salida no JSON parseable en ciclo previo.",
    "Se requiere normalizacion manual antes de propagar automaticamente.",
    "La materia exige identidad UnADM, integridad academica, citas verificables y cierre juridico propio."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda actividad.",
    "Alinear contenido con Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2.",
    "Marcar como supuesto cualquier dato no confirmado por fuentes locales."
  ],
  "structure_rules": [
    "Usar estructura minima: problema, conceptos/fuentes, analisis propio, conclusion juridica transferible.",
    "Ajustar el producto al tipo solicitado por la planeacion semanal.",
    "Conservar consistencia con README y programa analitico de la asignatura."
  ],
  "activity_rules": [
    "Para actividad-3, heredar reglas validas de actividad-1 sin eliminar ninguna util.",
    "Registrar diferencias especificas de la actividad como supuestos hasta confirmar guia oficial.",
    "Incluir postura academica propia sustentada en fuentes verificables."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de guardar memoria.",
    "Revisar respuestas no estructuradas antes de aplicar propagacion aguas abajo.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Aplicar no regresion: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre claves BibTeX y citas en .tex.",
    "No renombrar claves bibliograficas ya usadas en documentos.",
    "Usar acentos y nombres propios correctos en metadatos BibTeX."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y normativas/jurisprudenciales verificables.",
    "Agregar en .bib solo entradas realmente citadas por la actividad.",
    "Mantener URLs verificables cuando existan."
  ],
  "propagation_hints": [
    "Propagar arriba-y-laterales solo despues de normalizacion manual en ciclo 1.",
    "Usar compresion union-dedupe lossless para consolidar memoria.",
    "Conservar bandera de riesgo por antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Falta confirmar consigna exacta de actividad-3.",
    "Falta confirmar formato de entrega requerido en actividad-3 (reporte, presentacion u otro).",
    "Falta confirmar bibliografia obligatoria especifica de actividad-3."
  ]
}