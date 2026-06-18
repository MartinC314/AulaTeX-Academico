```json
{
  "summary": [
    "Materia destino con plantilla LaTeX, programa analitico y bibliografia local activos.",
    "Contexto local verificado: Garantias constitucionales, Licenciatura en Derecho, UnADM.",
    "Ubicacion curricular verificada: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Se conserva alerta institucional: origen heredado no entrego JSON parseable.",
    "Supuesto: reglas heredadas se aplican como control editorial, no como contenido disciplinar.",
    "Supuesto: reglas de Filosofia del derecho solo se propagan si son editoriales generales.",
    "Origen ciclo 1: actividad-1 de Filosofia del derecho sin memoria especifica parseable disponible."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, encabezados y referencias institucionales.",
    "Usar datos de materia destino: Garantias constitucionales, LDE-S2B1, semestre 2, bloque 1.",
    "Conservar coherencia con la Licenciatura en Derecho en todo producto.",
    "Registrar tipo Obligatoria y 8 creditos cuando aparezcan datos curriculares.",
    "Marcar como provisional cualquier regla heredada no validada por la actividad fuente.",
    "Tratar la fuente institucional heredada desde Codex como provisional.",
    "No trasladar contenido disciplinar de Filosofia del derecho sin validacion expresa."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega al esquema: problema, conceptos y fuentes, producto, analisis propio, conclusion transferible.",
    "Mantener separacion entre reporte, presentacion, programa analitico y referencias.",
    "Evitar cambios de nombres de archivo base salvo requerimiento explicito.",
    "Usar nombres locales verificados: reporte-garantias-constitucionales.tex, presentacion-garantias-constitucionales.tex y garantias-constitucionales.bib.",
    "Corregir referencias internas que conserven placeholders de generacion automatica.",
    "Preservar el programa analitico como guia editorial de la asignatura.",
    "Mantener carpeta referencias-garantias-constitucionales como deposito de fuentes locales."
  ],
  "activity_rules": [
    "Incluir un problema juridico o social claro desde la introduccion.",
    "Desarrollar analisis propio con postura academica explicita.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Vincular cada afirmacion relevante con fuente verificable o norma identificable.",
    "Distinguir entre conceptos, normas, doctrina, datos y postura personal.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico."
  ],
  "quality_gates": [
    "Validar formato JSON antes de propagar memoria aguas abajo.",
    "Bloquear propagacion automatica si la entrada no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Verificar congruencia entre metadatos de portada y datos curriculares de la materia.",
    "Confirmar que toda cita usada tenga entrada bibliografica local.",
    "Compilar LaTeX antes de entregar productos finales.",
    "Revisar truncamientos visibles en README y plantilla LaTeX.",
    "Verificar que no queden placeholders literales en rutas, nombres de archivo o bibliografia.",
    "Confirmar que las fuentes institucionales correspondan a archivos o enlaces disponibles.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar clase article en espanol, letterpaper y oneside segun plantilla.",
    "Completar campos de plantilla antes de entregar: actividad, figura docente y fecha.",
    "Mantener tabla de autor con matricula, semestre, bloque, tipo y creditos correctos.",
    "Evitar comandos rotos o texto truncado en portada y metadatos.",
    "Preservar coursecode como LDE-S2B1 salvo indicacion institucional distinta.",
    "Reparar el truncamiento detectado cerca de la macro de portada antes de compilar.",
    "Mantener nombres y metadatos sin acentos solo si la plantilla lo requiere tecnicamente.",
    "No introducir paquetes nuevos sin necesidad editorial o tecnica verificable.",
    "Verificar cierre completo de la macro authortable y de \\universityname en portada."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en garantias-constitucionales.bib.",
    "Mantener como base las entradas institucionales UnADM ya presentes.",
    "No inventar referencias; usar solo fuentes consultadas y verificables.",
    "Incluir nota de consulta o procedencia cuando la fuente sea institucional o local.",
    "Corregir menciones al archivo bibliografico que usen placeholders generados.",
    "Usar claves BibTeX estables y descriptivas.",
    "Agregar normas juridicas con identificador, emisor y fecha cuando sean usadas.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas editoriales generales ya validadas.",
    "Etiquetar ciclo 1 con necesidad de normalizacion manual si hay herencia incompleta.",
    "Priorizar deduplicacion por union sin perder reglas utiles existentes.",
    "No trasladar contenidos tematicos de una actividad ajena sin validacion de materia.",
    "Mantener alerta de JSON no parseable como regla institucional de control.",
    "Propagar a materias laterales solo controles de identidad, estructura, calidad, LaTeX y bibliografia.",
    "Evitar propagar datos curriculares especificos fuera de Garantias constitucionales."
  ],
  "open_questions": [
    "Falta confirmar memoria especifica de la actividad origen para extraer reglas disciplinares validas.",
    "Falta definir nombre de figura docente en plantilla destino.",
    "Falta verificar y corregir truncamiento en reporte-garantias-constitucionales.tex.",
    "Falta corregir nombres truncados de archivos en README.md.",
    "Falta reemplazar el placeholder bibliografico en README.md y programa analitico.",
    "Falta confirmar si la fecha debe ser automatica con today o fija por entrega.",
    "Falta validar si se requiere formato APA, juridico mexicano u otro estilo de citacion."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/garantias-constitucionales-lde"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```