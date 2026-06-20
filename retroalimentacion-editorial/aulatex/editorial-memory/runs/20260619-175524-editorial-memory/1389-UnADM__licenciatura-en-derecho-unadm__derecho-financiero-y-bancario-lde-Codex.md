{
  "summary": [
    "Base institucional UnADM consolidada con compresion union-dedupe lossless y sin regresion.",
    "Derecho financiero y bancario pertenece a Licenciatura en Derecho: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "El destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Se detectaron antecedentes de salida no parseable en JSON desde Codex, GPT-Pro, Auto (model-router) y Claude Foundry.",
    "README y programa analitico contienen artefactos de plantilla en nombres de archivo.",
    "El token de plantilla del archivo .bib debe expandirse a derecho-financiero-y-bancario.bib.",
    "El reporte .tex mantiene titulo, subtitulo y campos de plantilla pendientes de personalizar.",
    "La bibliografia local conserva entradas base institucionales verificables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico del destino.",
    "Usar Derecho financiero y bancario como nombre de materia.",
    "Usar clave LDE-S3B2 para la materia.",
    "Usar semestre 3 y bloque 2.",
    "Usar tipo Obligatoria y 8 creditos.",
    "Conservar autor Martin Jonathan de la Cruz segun .tex local.",
    "Conservar matricula ES2611202040 segun .tex local.",
    "Conservar localizacion Roma Norte, Ciudad de Mexico salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado del docente o grupo.",
    "Tratar fuentes heredadas de motor como provisionales y auditables.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Fuente provisional: Auto (model-router) desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico antes de crear actividades.",
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib de la materia.",
    "Corregir artefactos de plantilla y caracteres faltantes en nombres de archivo del README.",
    "Expandir el token de plantilla del .bib al slug literal derecho-financiero-y-bancario.bib.",
    "No eliminar reglas previas validas; agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Iniciar cada actividad con un problema juridico o social delimitado.",
    "Sustentar con norma, doctrina o datos pertinentes al tema financiero y bancario.",
    "Separar descripcion conceptual, analisis propio y conclusion juridica.",
    "Cerrar con postura juridica propia aplicable a la practica profesional.",
    "Evitar afirmaciones sin respaldo cuando la consigna pida evidencia.",
    "Adaptar el producto solicitado a la planeacion semanal confirmada."
  ],
  "quality_gates": [
    "Verificar que toda salida de memoria sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear propagacion si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar deduplicacion semantica antes de guardar memoria.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Bloquear fuentes o metadatos bibliograficos inventados.",
    "Normalizar manualmente si reaparece salida no estructurada."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instruccion contraria.",
    "Conservar macros de identidad academica en el encabezado del .tex.",
    "Reemplazar titulo y subtitulo de plantilla por los de la actividad real antes de entregar.",
    "Mantener sincronizados titulo, subtitulo y materia entre portada y contenido.",
    "Completar Figura docente con dato real o etiqueta explicita de supuesto.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Revisar que la tabla de identificacion compile sin celdas abiertas ni comandos incompletos."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliografico canonico de la materia.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Registrar fuentes especificas de actividad en derecho-financiero-y-bancario.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Incluir fecha de consulta en referencias web."
  ],
  "propagation_hints": [
    "Propagar a nivel materia reglas generales de identidad, estructura y bibliografia.",
    "Propagar lateralmente solo reglas independientes de la asignatura o actividad especifica.",
    "Mantener metodo union-dedupe con compresion lossless.",
    "Etiquetar origen de reglas heredadas para auditoria de no regresion.",
    "Aplicar normalizacion manual si se reutiliza memoria de ciclos con salida no estructurada.",
    "Ciclo 18 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente para completar plantilla.",
    "Confirmar si el grupo debe aparecer en la tabla de identificacion.",
    "Definir formato obligatorio de citacion para la materia (APA, IEEE u otro); supuesto: no definido aun.",
    "Confirmar planeacion semanal vigente antes de generar actividades especificas.",
    "Verificar si los nombres de archivo del README deben corregirse manualmente o regenerarse.",
    "Confirmar numero real de actividad para sustituir Actividad X en el subtitulo del .tex.",
    "Validar si la localizacion de portada debe mantenerse o actualizarse por lineamiento oficial."
  ]
}