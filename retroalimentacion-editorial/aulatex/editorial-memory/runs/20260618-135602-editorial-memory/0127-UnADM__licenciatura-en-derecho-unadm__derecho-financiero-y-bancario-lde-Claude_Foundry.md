{
  "summary": [
    "Base institucional UnADM consolidada con compresion union-dedupe sin regresion.",
    "El destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Derecho financiero y bancario pertenece a Licenciatura en Derecho: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Se detectaron antecedentes de salida no parseable en JSON desde Codex y GPT-Pro.",
    "El README local contiene artefactos de plantilla o caracteres faltantes en nombres de archivo.",
    "El programa analitico contiene un token de plantilla pendiente para el archivo .bib.",
    "El reporte .tex mantiene titulo, subtitulo y campos de plantilla pendientes de personalizar.",
    "La bibliografia local contiene entradas base UnADM y malla curricular de Derecho."
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
    "Marcar como supuesto cualquier dato no confirmado del docente.",
    "Marcar como supuesto cualquier dato no confirmado del grupo.",
    "Tratar GPT-Pro desde Actividad 1 como fuente provisional heredada.",
    "Tratar Codex desde ingenieria-en-sistemas-computacionales como fuente provisional heredada.",
    "Tratar fuentes heredadas de motor como provisionales y auditables."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico antes de crear actividades.",
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Corregir artefactos de plantilla y caracteres faltantes en nombres de archivo del README.",
    "Mantener el programa analitico como guia editorial de reportes, presentaciones y productos visuales.",
    "Expandir el token de plantilla del .bib al slug literal derecho-financiero-y-bancario.bib.",
    "No eliminar reglas validas previas; solo agregar mejoras verificables."
  ],
  "activity_rules": [
    "Iniciar cada actividad con un problema juridico o social delimitado.",
    "Sustentar con norma, doctrina o datos pertinentes al tema financiero y bancario.",
    "Separar descripcion conceptual, analisis propio y conclusion juridica.",
    "Cerrar con postura juridica propia aplicable a la practica profesional.",
    "Evitar afirmaciones sin respaldo cuando la consigna pida evidencia.",
    "Adaptar el producto a la planeacion semanal confirmada."
  ],
  "quality_gates": [
    "Verificar que toda salida de memoria sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear propagacion si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar deduplicacion semantica antes de guardar.",
    "Comprobar que cada mejora agregada sea verificable y sin fuentes inventadas.",
    "Bloquear fuentes o metadatos bibliograficos inventados.",
    "Normalizar manualmente si reaparece salida no estructurada."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instruccion contraria.",
    "Conservar macros de identidad academica en el encabezado del .tex.",
    "Reemplazar titulo de plantilla por el titulo de la actividad real antes de entregar.",
    "Reemplazar subtitulo de plantilla por el subtitulo de la actividad real antes de entregar.",
    "Completar Figura docente con dato real o etiqueta explicita de supuesto.",
    "Mantener sincronizados titulo, subtitulo y materia entre portada y contenido.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Revisar que la tabla de identificacion compile sin celdas abiertas ni comandos incompletos."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliografico canonico de la materia.",
    "Registrar fuentes especificas de actividad en derecho-financiero-y-bancario.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar la malla curricular local como fuente institucional de ubicacion curricular.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "Incluir fecha de consulta en referencias web.",
    "No inventar fuentes ni metadatos bibliograficos."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y deduplicadas.",
    "Propagar a nivel materia las reglas generales de identidad, estructura y bibliografia.",
    "Propagar lateralmente solo reglas independientes de la asignatura o actividad especifica.",
    "Mantener metodo de compresion union-dedupe con perdida cero.",
    "Etiquetar origen de reglas heredadas para auditoria de no regresion.",
    "Si reaparece salida no estructurada en ciclo 2, aplicar normalizacion manual como contingencia.",
    "Aplicar normalizacion manual si se reutiliza memoria de ciclo 1 con salida no estructurada."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente para completar plantilla.",
    "Definir formato obligatorio de citacion para la materia (APA, IEEE u otro); supuesto: no definido aun.",
    "Validar si la localizacion de portada debe mantenerse o actualizarse por lineamiento oficial.",
    "Confirmar si el grupo debe aparecer en la tabla de identificacion.",
    "Confirmar planeacion semanal vigente antes de generar actividades especificas.",
    "Definir si los nombres de archivo con artefactos se corrigen manualmente o por regeneracion.",
    "Confirmar numero real de actividad para sustituir Actividad X en el subtitulo del .tex."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derecho-financiero-y-bancario-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}