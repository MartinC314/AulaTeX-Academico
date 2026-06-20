{
  "summary": [
    "Materia destino consolidada como punto de entrada canonico con identidad UnADM y enfoque juridico.",
    "Asignatura: Derecho a la seguridad social, Licenciatura en Derecho UnADM.",
    "Datos curriculares vigentes: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Productos alineados a cinco ejes: problema, conceptos o norma, producto, analisis y conclusion.",
    "Bibliografia local centralizada en derecho-a-la-seguridad-social.bib.",
    "Persisten antecedentes historicos de salida no parseable; requiere normalizacion manual al reutilizar.",
    "Se detectaron marcadores y caracteres corruptos en README y programa analitico; deben normalizarse antes de uso canonico.",
    "La consolidacion aplica compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre oficial de materia: Derecho a la seguridad social.",
    "Mantener adscripcion: Licenciatura en Derecho.",
    "Usar datos curriculares oficiales: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar coursecode LDE-S2B1 cuando aplique.",
    "No sobrescribir reglas validas previas; aplicar union y deduplicacion.",
    "Conservar trazabilidad de reglas heredadas provisionales con marca [supuesto].",
    "Registrar fuentes provisionales heredadas como historicas: Codex, GPT-Pro, Auto (model-router) y Claude Foundry desde actividad previa [supuesto].",
    "No propagar datos personales de plantilla a laterales salvo requerimiento explicito [supuesto]."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Usar el programa analitico como guia editorial de productos.",
    "Alinear cada entrega a cinco ejes: problema, conceptos o norma, producto, analisis y conclusion.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Transformar planeacion semanal en productos con claridad y fundamento juridico.",
    "Mantener consistencia entre reporte, presentacion y programa analitico.",
    "Usar archivos canonicos tras normalizacion: reporte, presentacion, bib, programa analitico y carpeta de referencias.",
    "Resolver marcadores de plantilla en rutas y nombres antes de compilar o citar.",
    "Normalizar nombres y rutas con marcadores o caracteres corruptos antes de usarlos como canon.",
    "Registrar en memoria solo reglas accionables y verificables."
  ],
  "activity_rules": [
    "Definir al inicio el problema juridico o social.",
    "Vincular el desarrollo con normas, doctrina, datos o fuentes pertinentes.",
    "Relacionar el contenido con Derecho a la seguridad social cuando corresponda.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Incluir postura academica propia con argumentacion clara.",
    "Integrar evidencia verificable cuando el producto lo requiera.",
    "Evitar afirmaciones no sustentadas o marcarlas como [supuesto].",
    "Ajustar formato y alcance al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Validar que toda salida sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Normalizar manualmente salidas no parseables de ciclos previos cuando se reutilicen.",
    "Verificar coherencia entre objetivos de actividad y estructura final.",
    "Confirmar que toda afirmacion relevante tenga soporte verificable o marca [supuesto].",
    "Comprobar que cada cita tenga entrada BibTeX en el .bib local.",
    "Resolver marcadores corruptos en README y programa analitico antes de usarlos como canon.",
    "Compilar archivos .tex despues de corregir rutas y nombres.",
    "Verificar que no se eliminen reglas utiles previas.",
    "Confirmar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte de la materia.",
    "Personalizar solo campos variables de la actividad.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Mantener clase article salvo justificacion tecnica.",
    "Mantener idioma spanish y papel letterpaper si no hay instruccion contraria.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Usar portada con alumno, matricula, figura docente, semestre, bloque, tipo y creditos cuando aplique.",
    "Usar coursecode LDE-S2B1 en la plantilla de esta materia.",
    "Conservar imagen institucional departamentos/UnADM si la ruta compila.",
    "Conservar campo de figura docente como pendiente si no existe dato oficial.",
    "Corregir rutas y nombres corruptos antes de compilar.",
    "Evitar cambios de formato que rompan compatibilidad sin justificacion tecnica."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar entradas unadmSitioWeb y unadmMallaDerecho2024 cuando se citen.",
    "Agregar solo referencias especificas de actividad con datos completos y verificables.",
    "Verificar correspondencia entre citas en LaTeX y entradas BibTeX.",
    "No inventar fuentes.",
    "Marcar fuentes faltantes como pendientes.",
    "Usar la malla curricular local solo cuando se cite como fuente institucional.",
    "Reemplazar marcadores de slug por derecho-a-la-seguridad-social.bib antes de citar el archivo."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas en este ciclo.",
    "Aplicar compresion union-dedupe lossless sin regresion.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable.",
    "Normalizar ciclos previos antes de cualquier reutilizacion aguas abajo.",
    "Propagar reglas curriculares solo a nodos de la misma materia.",
    "Propagar reglas generales de integridad, citas y JSON parseable a laterales compatibles.",
    "Propagar reglas LaTeX solo a plantillas compatibles [supuesto].",
    "No propagar datos personales a laterales salvo requerimiento explicito [supuesto].",
    "Tratar el origen Filosofia del Derecho Actividad 1 como lateral; no importar contenido disciplinar sin validacion [supuesto].",
    "Ciclo 15 hereda riesgo de parseo; validar JSON antes de propagar.",
    "Ciclo 15 requiere normalizacion manual si reutiliza salidas no parseables heredadas [supuesto]."
  ],
  "open_questions": [
    "Definir nombre oficial de figura docente para plantilla.",
    "Confirmar norma de citacion requerida: APA, ISO, institucional o juridica mexicana [supuesto].",
    "Confirmar si el origen Filosofia del Derecho Actividad 1 aporta reglas especificas o solo generales [supuesto].",
    "Confirmar si datos personales de plantilla deben permanecer solo en nodo local [supuesto].",
    "Confirmar fuentes juridicas primarias requeridas para actividades especificas de seguridad social [supuesto].",
    "Confirmar vigencia de fuentes provisionales heredadas desde ingenieria para contexto de Derecho [supuesto].",
    "Resolver y limpiar marcadores corruptos en README y programa analitico antes de usarlos como canon."
  ]
}