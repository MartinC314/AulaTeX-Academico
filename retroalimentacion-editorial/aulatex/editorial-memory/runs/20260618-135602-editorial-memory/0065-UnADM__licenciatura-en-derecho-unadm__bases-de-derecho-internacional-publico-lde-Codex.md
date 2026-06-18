{
  "summary": [
    "Materia destino con plantilla base, programa analitico y bib local ya definidos.",
    "Se conserva memoria institucional heredada sobre salida no parseable en ciclo previo.",
    "Supuesto: no hay reglas validas adicionales desde actividad origen por falta de contenido estructurado."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre oficial de la materia: Bases de derecho internacional publico.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Organizar cada entrega con problema, conceptos, analisis propio y conclusion juridica.",
    "Conservar separacion entre reporte, presentacion, programa analitico y bibliografia."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeacion semanal.",
    "Incluir postura academica propia sustentada en fuentes verificables.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar consistencia entre instrucciones de actividad y programa analitico.",
    "Bloquear afirmaciones sin respaldo documental o normativo."
  ],
  "latex_rules": [
    "Reutilizar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Completar metadatos de portada sin alterar identidad institucional.",
    "Mantener compatibilidad con estructura article en spanish y letterpaper."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; marcar faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas verificadas y no duplicadas.",
    "Mantener compresion union-dedupe con criterio lossless.",
    "Marcar como incidencia historica la salida no estructurada detectada en ciclo 1."
  ],
  "open_questions": [
    "Confirmar si existe memoria util adicional en actividad-1 para fusion posterior.",
    "Definir formato minimo de conclusion juridica por tipo de evidencia.",
    "Validar si se normaliza nomenclatura de archivos con caracteres acentuados."
  ]
}