{
  "summary": [
    "Materia destino con plantilla LaTeX, programa analitico y bib local activos.",
    "Se conserva alerta institucional: origen previo no entrego JSON parseable.",
    "Supuesto: reglas heredadas se aplican como control de calidad, no como contenido disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos de materia destino: Garantias constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Conservar coherencia con Licenciatura en Derecho en todo producto.",
    "Marcar como provisional cualquier regla que provenga de memoria heredada no validada por actividad fuente."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega al esquema: problema, conceptos/fuentes, producto, analisis propio, conclusion transferible.",
    "Mantener separacion entre reporte, presentacion, programa analitico y referencias.",
    "Evitar cambios de nombres de archivo base salvo requerimiento explicito."
  ],
  "activity_rules": [
    "Incluir problema juridico o social claro desde la introduccion.",
    "Desarrollar analisis propio con postura academica explicita.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Vincular cada afirmacion relevante con fuente verificable o norma identificable."
  ],
  "quality_gates": [
    "Validar formato estructurado antes de propagar memoria aguas abajo.",
    "Bloquear propagacion automatica si la entrada no es JSON parseable.",
    "Verificar congruencia entre metadatos de portada y datos curriculares de la materia.",
    "Confirmar que toda cita usada tenga entrada bibliografica local."
  ],
  "latex_rules": [
    "Conservar clase article en espanol y formato letterpaper oneside segun plantilla.",
    "Completar campos de plantilla antes de entregar: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matricula, semestre/bloque y creditos correctos.",
    "Evitar comandos rotos o texto truncado en portada y metadatos."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en garantias-constitucionales.bib.",
    "Mantener como base las entradas institucionales UnADM ya presentes.",
    "No inventar referencias; usar solo fuentes consultadas y verificables.",
    "Incluir nota de consulta o procedencia cuando la fuente sea institucional o local."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas editoriales generales ya validadas.",
    "Etiquetar ciclo 1 con necesidad de normalizacion manual si hay herencia incompleta.",
    "Priorizar deduplicacion por union sin perder reglas utiles existentes.",
    "No trasladar contenidos tematicos de una actividad ajena sin validacion de materia."
  ],
  "open_questions": [
    "Falta confirmar memoria especifica de la actividad origen para extraer reglas disciplinares validas.",
    "Falta definir nombre de figura docente en plantilla destino.",
    "Falta verificar y corregir posible truncamiento en reporte-garantias-constitucionales.tex."
  ]
}