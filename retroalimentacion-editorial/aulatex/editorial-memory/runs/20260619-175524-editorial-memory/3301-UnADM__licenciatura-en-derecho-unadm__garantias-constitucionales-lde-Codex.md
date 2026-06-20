{
  "summary": [
    "Materia destino con plantilla LaTeX, programa analitico y bibliografia local activos.",
    "Contexto local verificado: Garantias constitucionales, Licenciatura en Derecho, UnADM.",
    "Ubicacion curricular verificada: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Se mantiene alerta institucional por salidas no JSON parseables en ciclos previos.",
    "Origen ciclo 12 sin memoria de actividad parseable adicional; se mantiene base validada.",
    "Supuesto: reglas heredadas de Filosofia del derecho solo aplican como control editorial general."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos de materia destino: Garantias constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Registrar tipo Obligatoria y 8 creditos cuando aparezcan datos curriculares.",
    "Conservar coherencia con la Licenciatura en Derecho en todo producto.",
    "No trasladar contenido disciplinar de Filosofia del derecho sin validacion expresa.",
    "Marcar como provisional cualquier regla heredada no validada por la actividad fuente.",
    "Tratar fuentes heredadas desde Codex, GPT-Pro, Auto y Claude como provisionales."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega al esquema: problema, conceptos y fuentes, producto, analisis propio, conclusion transferible.",
    "Mantener separacion entre reporte, presentacion, programa analitico y referencias.",
    "Evitar cambios de nombres de archivo base salvo requerimiento explicito.",
    "Usar nombres locales verificados: reporte-garantias-constitucionales.tex, presentacion-garantias-constitucionales.tex y garantias-constitucionales.bib.",
    "Corregir referencias internas que conserven placeholders de generacion automatica.",
    "Preservar el programa analitico como guia editorial de la asignatura.",
    "Mantener carpeta referencias-garantias-constitucionales como deposito de fuentes locales.",
    "Corregir nombres truncados en README antes de usarlo como indice operativo."
  ],
  "activity_rules": [
    "Incluir un problema juridico o social claro desde la introduccion.",
    "Desarrollar analisis propio con postura academica explicita.",
    "Vincular cada afirmacion relevante con fuente verificable o norma identificable.",
    "Distinguir entre conceptos, normas, doctrina, datos y postura personal.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Validar formato JSON antes de propagar memoria aguas abajo.",
    "Bloquear propagacion automatica si la entrada no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Verificar congruencia entre metadatos de portada y datos curriculares de la materia.",
    "Verificar que no queden placeholders literales en rutas, nombres de archivo o bibliografia.",
    "Confirmar que toda cita usada tenga entrada bibliografica local.",
    "Confirmar que las fuentes institucionales correspondan a archivos o enlaces disponibles.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Revisar truncamientos visibles en README y plantilla LaTeX."
  ],
  "latex_rules": [
    "Conservar clase article en espanol, letterpaper y oneside segun plantilla.",
    "Completar campos de plantilla antes de entregar: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matricula, semestre, bloque, tipo y creditos correctos.",
    "Preservar coursecode como LDE-S2B1 salvo indicacion institucional distinta.",
    "Evitar comandos rotos o texto truncado en portada y metadatos.",
    "Verificar cierre completo de la macro authortable y de \\universityname en portada.",
    "Reparar truncamiento detectado cerca de la macro de portada antes de compilar.",
    "Mantener nombres y metadatos sin acentos solo si la plantilla lo requiere tecnicamente.",
    "No introducir paquetes nuevos sin necesidad editorial o tecnica verificable."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en garantias-constitucionales.bib.",
    "Mantener como base las entradas institucionales UnADM ya presentes.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias; usar solo fuentes consultadas y verificables.",
    "Usar claves BibTeX estables y descriptivas.",
    "Agregar normas juridicas con identificador, emisor y fecha cuando sean usadas.",
    "Incluir nota de consulta o procedencia cuando la fuente sea institucional o local.",
    "Corregir menciones al archivo bibliografico que usen placeholders generados."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas editoriales generales validadas.",
    "Propagar a materias laterales solo controles de identidad, estructura, calidad, LaTeX y bibliografia.",
    "Evitar propagar datos curriculares especificos fuera de Garantias constitucionales.",
    "No trasladar contenidos tematicos entre materias sin validacion de materia.",
    "Mantener alerta de JSON no parseable como regla institucional de control.",
    "Ciclo 1 al 12 requieren normalizacion manual si la fuente llega no estructurada."
  ],
  "open_questions": [
    "Falta confirmar memoria especifica parseable de la actividad origen para reglas disciplinares.",
    "Falta definir nombre de figura docente en plantilla destino.",
    "Falta verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Falta corregir nombres truncados de archivos en README.md.",
    "Falta reemplazar placeholder bibliografico en README.md y programa analitico.",
    "Falta confirmar si la fecha debe ser automatica con today o fija por entrega.",
    "Falta validar si se requiere formato APA, juridico mexicano u otro estilo de citacion."
  ]
}