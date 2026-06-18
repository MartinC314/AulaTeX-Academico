{
  "summary": [
    "Materia destino consolidada como punto de entrada canonico con identidad UnADM y enfoque juridico.",
    "Materia destino: Derecho a la seguridad social, Licenciatura en Derecho UnADM.",
    "Asignatura ubicada en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Productos orientados a problema, fundamento juridico, evidencia, analisis propio y conclusion transferible.",
    "Bibliografia local centralizada en derecho-a-la-seguridad-social.bib.",
    "Persiste alerta institucional por salida no parseable en ciclo 1; requiere normalizacion manual al reutilizar.",
    "Antecedente de salida sin JSON parseable desde GPT-Pro para derecho-a-la-seguridad-social-lde.",
    "Antecedente de salida sin JSON parseable desde Codex para UnADM.",
    "La consolidacion aplica union-dedupe lossless sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre de materia: Derecho a la seguridad social.",
    "Mantener adscripcion: Licenciatura en Derecho.",
    "Usar datos curriculares oficiales: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local de curso cuando aplique: LDE-S2B1.",
    "No sobrescribir reglas validas previas; unir y deduplicar.",
    "Conservar trazabilidad de reglas heredadas provisionales con marca [supuesto].",
    "No propagar datos personales de plantilla a laterales salvo requerimiento explicito [supuesto].",
    "Registrar fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales [supuesto].",
    "Registrar fuente provisional heredada: GPT-Pro desde Actividad 1 [supuesto]."
  ],
  "structure_rules": [
    "Tomar el README de materia como canon de estructura editorial local.",
    "Alinear cada entrega a cinco ejes: problema, conceptos o norma, producto, analisis y conclusion.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Transformar la planeacion semanal en productos con claridad y fundamento.",
    "Usar el programa analitico como guia editorial de productos.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Usar archivos canonicos tras normalizacion: reporte, presentacion, bib, programa analitico y carpeta de referencias.",
    "Normalizar nombres de archivos con marcadores o caracteres corruptos antes de usarlos como canon.",
    "Resolver marcadores de plantilla en nombres de archivo antes de compilar o citar rutas.",
    "Registrar en memoria solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Definir desde el inicio el problema juridico o social de la actividad.",
    "Vincular el desarrollo con normas, doctrina, datos o fuentes pertinentes.",
    "Relacionar el contenido con Derecho a la seguridad social cuando corresponda.",
    "Incluir postura academica propia con argumentacion clara.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Integrar evidencia verificable cuando el producto lo requiera.",
    "Evitar afirmaciones no sustentadas o marcarlas como [supuesto].",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Ajustar formato y alcance al producto solicitado por la planeacion semanal."
  ],
  "quality_gates": [
    "Validar que toda salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Normalizar manualmente salidas no parseables de ciclo 1 cuando se reutilicen.",
    "Verificar coherencia entre objetivos de actividad y estructura final.",
    "Confirmar que toda afirmacion relevante tenga soporte verificable o marca [supuesto].",
    "Comprobar que cada cita tenga entrada BibTeX en el .bib local.",
    "Verificar que no se eliminen reglas utiles previas.",
    "Confirmar que la compresion aplicada sea union-dedupe y no recorte.",
    "Resolver marcadores corruptos en README y programa analitico antes de usarlos como canon.",
    "Compilar archivos .tex despues de corregir rutas y nombres."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia y personalizar solo campos variables.",
    "Mantener clase article salvo justificacion tecnica.",
    "Mantener idioma spanish y papel letterpaper si no hay instruccion contraria.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Usar coursecode LDE-S2B1 en la plantilla de esta materia.",
    "Usar portada con alumno, matricula, figura docente, semestre, bloque, tipo y creditos cuando aplique.",
    "Conservar campo de figura docente como pendiente si el dato no esta disponible.",
    "Conservar imagen institucional departamentos/UnADM si la ruta compila.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Corregir rutas y nombres corruptos antes de compilar.",
    "Evitar cambios de clase o formato que rompan compatibilidad sin justificacion tecnica."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Conservar entradas unadmSitioWeb y unadmMallaDerecho2024 cuando se citen.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo referencias especificas de actividad con datos completos y verificables.",
    "Usar la malla curricular local solo cuando se cite como fuente institucional.",
    "Verificar correspondencia entre citas en LaTeX y entradas BibTeX.",
    "Reemplazar marcadores de slug por derecho-a-la-seguridad-social.bib antes de citar el archivo.",
    "No inventar fuentes; marcar faltantes como pendientes."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas en este ciclo.",
    "Aplicar compresion union-dedupe lossless sin regresion.",
    "Evitar regresion sobre identidad UnADM, estructura por ejes y control bibliografico.",
    "Propagar reglas curriculares solo a nodos de la misma materia.",
    "Propagar reglas generales de integridad, citas y JSON parseable a laterales compatibles.",
    "Propagar reglas LaTeX solo a plantillas compatibles [supuesto].",
    "No propagar datos personales a laterales salvo requerimiento explicito [supuesto].",
    "Tratar el origen Filosofia del Derecho Actividad 1 como lateral; no importar contenido disciplinar sin validacion [supuesto].",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Normalizar ciclo 1 antes de cualquier reutilizacion aguas abajo."
  ],
  "open_questions": [
    "Confirmar vigencia de la fuente provisional heredada desde ingenieria para contexto de Derecho [supuesto].",
    "Definir nombre de figura docente en plantilla cuando el dato oficial exista.",
    "Confirmar norma de citacion requerida para la materia: APA, ISO, institucional o juridica mexicana [supuesto].",
    "Resolver y limpiar marcadores corruptos en README y programa analitico antes de usarlos como canon.",
    "Confirmar si el origen Filosofia del Derecho Actividad 1 aporta reglas especificas o solo reglas generales [supuesto].",
    "Confirmar si los datos personales de plantilla deben permanecer solo en nodo local [supuesto].",
    "Confirmar fuentes juridicas primarias requeridas para actividades especificas de seguridad social [supuesto]."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derecho-a-la-seguridad-social-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}