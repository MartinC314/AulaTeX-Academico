{
  "summary": [
    "Heredado: hubo salida no parseable en ciclo previo.",
    "Aplicar normalizacion manual antes de reutilizar memoria heredada.",
    "Destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar datos de asignatura: Derecho laboral y relaciones laborales, LDE-S7B1, semestre 7, bloque 1.",
    "Marcar como supuesto cualquier dato personal no confirmado del autor."
  ],
  "structure_rules": [
    "Alinear cada entrega al esquema: problema, conceptos/normas, producto, analisis propio, conclusion transferible.",
    "Conservar README de materia como punto de entrada canonico.",
    "Registrar nuevas reglas por union-dedupe sin eliminar reglas vigentes utiles."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico o social laboral.",
    "Incluir postura academica propia sustentada en norma, doctrina o datos verificables.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar consistencia entre actividad, programa analitico y plantilla LaTeX.",
    "Confirmar que no se inventen fuentes y que toda cita sea trazable."
  ],
  "latex_rules": [
    "Usar la plantilla .tex de la materia como base de cada reporte.",
    "Completar metadatos del documento con datos reales de la actividad.",
    "Mantener compatibilidad con compilacion en espanol y formato letterpaper."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Conservar fuentes institucionales UnADM ya incluidas.",
    "Agregar solo entradas BibTeX verificables y relacionadas con la actividad.",
    "Marcar como supuesto cuando falte fecha de consulta u otro metadato."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo despues de validacion JSON.",
    "En ciclo 1, priorizar normalizacion manual de heredados no estructurados.",
    "Aplicar deduplicacion semantica por frase accionable corta."
  ],
  "open_questions": [
    "Definir formato de cita juridica requerido por docente (APA, ISO 690 u otro).",
    "Confirmar si la plantilla debe fijar autor institucional o variable por alumno.",
    "Verificar si existe rubrica oficial por actividad para convertirla en checklist."
  ]
}