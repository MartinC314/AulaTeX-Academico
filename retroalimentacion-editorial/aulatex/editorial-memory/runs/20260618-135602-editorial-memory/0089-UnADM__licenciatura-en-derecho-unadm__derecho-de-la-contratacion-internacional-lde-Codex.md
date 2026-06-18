{
  "summary": [
    "Se hereda incidente institucional: salida no JSON parseable en ciclo previo.",
    "La materia exige identidad UnADM, citas verificables y conclusion juridica propia.",
    "Se mantiene compresion por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre de asignatura exacto: Derecho de la contratacion internacional.",
    "Marcar como supuesto cualquier dato no confirmado por planeacion oficial.",
    "Conservar trazabilidad de origen de reglas heredadas."
  ],
  "structure_rules": [
    "Alinear cada entrega al esquema: problema, conceptos/normas, producto, analisis propio, conclusion.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Agregar fuentes especificas de actividad al .bib local de la asignatura.",
    "No eliminar reglas previas utiles; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Incluir una conclusion juridica aplicable a practica profesional.",
    "Diferenciar con claridad resumen descriptivo y postura del autor.",
    "Vincular argumentos con norma, doctrina o evidencia verificable.",
    "Declarar limites del analisis cuando falten datos de la actividad."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar consistencia entre README, programa analitico y plantilla LaTeX.",
    "Confirmar que toda afirmacion normativa tenga respaldo en fuente citada.",
    "Bloquear propagacion si hay contenido no estructurado."
  ],
  "latex_rules": [
    "Mantener plantilla base article en espanol y formato letterpaper.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar titulos de actividad en \\documenttitle y \\documentsubtitle.",
    "Evitar cambios de clase o paquetes sin justificacion verificable."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia como repositorio principal.",
    "No inventar fuentes; registrar solo documentos consultables.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos aplicables.",
    "Incluir fecha de consulta cuando la fuente sea web o recurso mutable."
  ],
  "propagation_hints": [
    "Propagar a nodos superiores y laterales solo tras validacion JSON.",
    "Etiquetar herencia institucional como provisional hasta normalizacion completa.",
    "Aplicar deduplicacion semantica por regla, no por recorte textual."
  ],
  "open_questions": [
    "Supuesto: la incidencia de JSON no parseable sigue activa en este ciclo; confirmar.",
    "Falta definir formato uniforme de citas juridicas (norma, jurisprudencia, doctrina).",
    "Falta confirmar checklist minimo por tipo de actividad (reporte, presentacion, visual)."
  ]
}