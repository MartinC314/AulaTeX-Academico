{
  "summary": [
    "Base de destino inicializada con plantilla LaTeX y programa analitico de la materia.",
    "Se heredan alertas institucionales sobre salida no estructurada en ciclo 1.",
    "Aplicar normalizacion manual antes de propagar cambios aguas abajo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre oficial de la materia: Derecho de la empresa y emprendimiento.",
    "Marcar como supuesto cualquier dato no confirmado por archivo local."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear cada entrega al esquema: problema, conceptos, producto, analisis propio, conclusion.",
    "Conservar correspondencia entre .tex, presentacion y .bib de la materia."
  ],
  "activity_rules": [
    "Cada actividad debe incluir conclusion juridica con criterio propio.",
    "Cada actividad debe incluir citas verificables y trazables a la bibliografia local.",
    "Agregar fuentes especificas de actividad al archivo .bib de la materia."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de consolidar memoria.",
    "Revisar respuesta no estructurada antes de aplicar propagacion lateral o ascendente.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte con metadatos institucionales completos.",
    "Mantener consistencia de campos de curso y licenciatura en macros LaTeX.",
    "Verificar compilacion sin errores tras actualizar portada, secciones y referencias."
  ],
  "bibliography_rules": [
    "No inventar fuentes; registrar solo fuentes verificables.",
    "Priorizar fuentes institucionales UnADM y documentos locales de malla curricular.",
    "Mantener claves BibTeX estables y sin duplicados."
  ],
  "propagation_hints": [
    "Propagar estas reglas a nivel licenciatura en Derecho cuando no exista conflicto local.",
    "Propagar lateralmente a materias hermanas con misma pauta editorial de UnADM.",
    "En ciclo 1, exigir normalizacion manual previa por antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Supuesto: la actividad origen no aporta reglas adicionales por falta de JSON estructurado.",
    "Confirmar si existe guia de citacion juridica especifica distinta a la plantilla general.",
    "Confirmar si el nombre de autor en plantilla debe parametrizarse por actividad."
  ]
}