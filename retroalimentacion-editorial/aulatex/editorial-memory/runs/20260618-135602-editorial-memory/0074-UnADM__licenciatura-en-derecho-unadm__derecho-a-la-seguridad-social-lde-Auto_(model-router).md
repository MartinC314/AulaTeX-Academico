{
  "summary": [
    "Materia destino: Derecho a la seguridad social, Licenciatura en Derecho UnADM.",
    "Carpeta configurada como punto de entrada canonico de la asignatura.",
    "Asignatura ubicada en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Productos orientados a problema, fundamento juridico, evidencia, analisis propio y conclusion transferible.",
    "Persiste alerta institucional por salida previa no parseable en ciclo 1.",
    "La consolidacion aplica union-dedupe sin perdida y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre de materia: Derecho a la seguridad social.",
    "Usar datos curriculares oficiales: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local de curso cuando aplique: LDE-S2B1.",
    "Conservar trazabilidad de reglas heredadas cuando sean provisionales.",
    "Registrar fuente provisional heredada desde ingenieria-en-sistemas-computacionales como [supuesto].",
    "No sobrescribir reglas validas previas; unir y deduplicar.",
    "No propagar datos personales de plantilla a laterales salvo que sean requeridos por el destino [supuesto]."
  ],
  "structure_rules": [
    "Tomar el README de materia como canon de estructura editorial local.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Alinear cada entrega a cinco ejes: problema, conceptos, producto, analisis y conclusion.",
    "Transformar la planeacion semanal en productos con claridad y fundamento.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Registrar en memoria solo reglas accionables y verificables.",
    "Normalizar nombres de archivos generados cuando aparezcan marcadores o caracteres corruptos."
  ],
  "activity_rules": [
    "Definir desde el inicio el problema juridico o social de la actividad.",
    "Vincular el desarrollo con normas, doctrina, datos o fuentes pertinentes.",
    "Relacionar el contenido con Derecho a la seguridad social cuando corresponda.",
    "Ajustar el formato al producto solicitado por la planeacion semanal.",
    "Incluir postura academica propia con argumentacion clara.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Evitar afirmaciones no sustentadas o marcarlas como [supuesto]."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Normalizar manualmente salidas no parseables del ciclo 1.",
    "Verificar coherencia entre objetivos de actividad y estructura final.",
    "Confirmar que toda afirmacion relevante tenga soporte verificable o marca de [supuesto].",
    "Comprobar que las fuentes citadas existan en el archivo .bib local.",
    "Verificar que no se eliminen reglas utiles previas.",
    "Confirmar que la compresion sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia.",
    "Personalizar solo campos variables de la actividad.",
    "Mantener clase article salvo justificacion tecnica.",
    "Mantener idioma spanish y papel letterpaper si no hay instruccion contraria.",
    "Mantener metadatos institucionales y de curso consistentes en todo archivo .tex.",
    "Usar portada con alumno, matricula, figura docente, semestre, bloque, tipo y creditos cuando aplique.",
    "Conservar campos de figura docente como pendiente si el dato no esta disponible.",
    "Evitar cambios de clase o formato que rompan compatibilidad sin justificacion tecnica.",
    "Corregir rutas o nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar entrada unadmSitioWeb si se cita el sitio institucional.",
    "Conservar entrada unadmMallaDerecho2024 si se cita la malla curricular.",
    "Agregar solo referencias especificas de actividad con datos completos y verificables.",
    "No inventar fuentes.",
    "Marcar fuentes faltantes como pendientes.",
    "Verificar que cada cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas en este ciclo.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Aplicar compresion union-dedupe sin perdida.",
    "Evitar regresion sobre identidad UnADM, estructura por ejes y control bibliografico.",
    "Propagar reglas curriculares solo a nodos de la misma materia.",
    "Propagar reglas generales de integridad, citas y JSON parseable a nodos laterales compatibles."
  ],
  "open_questions": [
    "Confirmar si la fuente provisional desde ingenieria sigue vigente para Derecho [supuesto].",
    "Definir nombre de figura docente en plantilla cuando se disponga del dato.",
    "Verificar si se requiere norma de citacion juridica especifica adicional [supuesto].",
    "Confirmar si la citacion debe ser APA, ISO, institucional o juridica mexicana [supuesto].",
    "Revisar marcadores corruptos en README antes de usarlos como lista canonica de archivos."
  ]
}