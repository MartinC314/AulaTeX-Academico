{
  "summary": [
    "Materia destino: Derecho a la seguridad social, Licenciatura en Derecho UnADM.",
    "Carpeta destino configurada como punto de entrada canonico de la asignatura.",
    "Asignatura ubicada en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Productos orientados a problema, fundamento juridico, evidencia, analisis propio y conclusion transferible.",
    "Bibliografia local centralizada en derecho-a-la-seguridad-social.bib.",
    "Antecedente de salida sin JSON parseable desde GPT-Pro para derecho-a-la-seguridad-social-lde.",
    "Antecedente de salida sin JSON parseable desde Codex para UnADM.",
    "Persiste alerta institucional de ciclo 1; requiere normalizacion manual al reutilizar.",
    "La consolidacion aplica union-dedupe lossless sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre de materia: Derecho a la seguridad social.",
    "Usar datos curriculares oficiales: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local de curso cuando aplique: LDE-S2B1.",
    "Mantener adscripcion: Licenciatura en Derecho.",
    "Conservar trazabilidad de reglas heredadas provisionales con marca [supuesto].",
    "Registrar fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales [supuesto].",
    "Registrar fuente provisional heredada: GPT-Pro desde Actividad 1 [supuesto].",
    "No sobrescribir reglas validas previas; unir y deduplicar.",
    "No propagar datos personales de plantilla a laterales salvo requerimiento explicito [supuesto]."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Usar el programa analitico como guia editorial de productos.",
    "Alinear cada entrega a cinco ejes: problema, conceptos o norma, producto, analisis y conclusion.",
    "Transformar la planeacion semanal en productos con claridad y fundamento.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Registrar en memoria solo reglas accionables y verificables.",
    "Normalizar nombres de archivos con marcadores o caracteres corruptos antes de usarlos como canon.",
    "Usar archivos canonicos tras normalizacion: reporte, presentacion, bib, programa analitico y carpeta de referencias.",
    "Resolver marcadores de plantilla en nombres de archivo antes de compilar o citar rutas."
  ],
  "activity_rules": [
    "Definir desde el inicio el problema juridico o social de la actividad.",
    "Ajustar formato y alcance al producto solicitado por la planeacion semanal.",
    "Vincular el desarrollo con normas, doctrina, datos o fuentes pertinentes.",
    "Relacionar el contenido con Derecho a la seguridad social cuando corresponda.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Incluir postura academica propia con argumentacion clara.",
    "Evitar afirmaciones no sustentadas o marcarlas como [supuesto].",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Integrar evidencia verificable cuando el producto lo requiera."
  ],
  "quality_gates": [
    "Validar que toda salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Normalizar manualmente salidas no parseables de ciclo 1 cuando se reutilicen.",
    "Verificar coherencia entre objetivos de actividad y estructura final del documento.",
    "Confirmar que toda afirmacion relevante tenga soporte verificable o marca [supuesto].",
    "Comprobar que cada cita tenga entrada BibTeX en el .bib local.",
    "Comprobar que las fuentes citadas existan en el archivo .bib local.",
    "Verificar que no se eliminen reglas utiles previas.",
    "Confirmar que la compresion sea union-dedupe y no recorte.",
    "Resolver marcadores corruptos en README y programa analitico antes de usarlos como canon.",
    "Compilar archivos .tex despues de corregir rutas y nombres."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia.",
    "Personalizar solo campos variables de la actividad.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Mantener clase article salvo justificacion tecnica.",
    "Mantener idioma spanish y papel letterpaper si no hay instruccion contraria.",
    "Usar portada con alumno, matricula, figura docente, semestre, bloque, tipo y creditos cuando aplique.",
    "Conservar campo de figura docente como pendiente si el dato no esta disponible.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Corregir rutas y nombres corruptos antes de compilar.",
    "Usar coursecode LDE-S2B1 en la plantilla de esta materia.",
    "Conservar imagen institucional departamentos/UnADM si la ruta compila.",
    "Evitar cambios de clase o formato que rompan compatibilidad sin justificacion tecnica."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar entrada unadmSitioWeb si se cita el sitio institucional.",
    "Conservar entrada unadmMallaDerecho2024 si se cita la malla curricular.",
    "Agregar solo referencias especificas de actividad con datos completos y verificables.",
    "No inventar fuentes.",
    "Marcar fuentes faltantes como pendientes.",
    "Verificar correspondencia entre citas en LaTeX y entradas BibTeX.",
    "Usar la malla curricular local solo cuando se cite como fuente institucional.",
    "Reemplazar marcadores de slug por derecho-a-la-seguridad-social.bib antes de citar el archivo."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas en este ciclo.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Aplicar compresion lossless por union-dedupe sin regresion.",
    "Evitar regresion sobre identidad UnADM, estructura por ejes y control bibliografico.",
    "Propagar reglas curriculares solo a nodos de la misma materia.",
    "Propagar reglas generales de integridad, citas y JSON parseable a laterales compatibles.",
    "Propagar reglas LaTeX solo a plantillas compatibles [supuesto].",
    "No propagar datos personales a laterales salvo requerimiento explicito [supuesto].",
    "Tratar el origen Filosofia del Derecho Actividad 1 como lateral; no importar contenido disciplinar sin validacion [supuesto].",
    "Normalizar ciclo 1 antes de cualquier reutilizacion aguas abajo."
  ],
  "open_questions": [
    "Confirmar si la fuente provisional desde ingenieria sigue vigente para Derecho [supuesto].",
    "Definir nombre de figura docente en plantilla cuando el dato oficial exista.",
    "Confirmar norma de citacion requerida para la materia: APA, ISO, institucional o juridica mexicana [supuesto].",
    "Resolver y limpiar marcadores corruptos en README y programa analitico antes de usarlos como canon.",
    "Confirmar si el origen Filosofia del Derecho Actividad 1 aporta reglas especificas o solo reglas generales [supuesto].",
    "Confirmar si los datos personales de plantilla deben permanecer solo en nodo local [supuesto].",
    "Confirmar fuentes juridicas primarias requeridas para actividades especificas de seguridad social [supuesto]."
  ]
}