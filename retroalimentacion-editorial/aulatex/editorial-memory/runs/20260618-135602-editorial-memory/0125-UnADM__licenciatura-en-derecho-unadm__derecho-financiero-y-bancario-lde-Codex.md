{
  "summary": [
    "Base institucional UnADM consolidada con compresion union-dedupe sin regresion.",
    "La materia exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Derecho financiero y bancario: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Se detectaron antecedentes de salida no parseable en JSON desde Codex y GPT-Pro.",
    "README y programa analitico muestran artefactos de plantilla en nombres de archivo.",
    "El reporte .tex mantiene titulo/subtitulo de plantilla y campos por completar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar datos de la materia: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Usar la Licenciatura en Derecho como programa academico.",
    "Conservar autoria real del alumno y matricula en la tabla de identificacion.",
    "Mantener autor Martin Jonathan de la Cruz y matricula ES2611202040 segun .tex local.",
    "Conservar localizacion Roma Norte, Ciudad de Mexico salvo lineamiento contrario.",
    "Marcar como supuesto cualquier dato no confirmado, especialmente figura docente o grupo.",
    "Tratar fuentes heredadas de motor como provisionales y auditables."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico antes de crear actividades.",
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib de la materia.",
    "No eliminar reglas validas previas; solo agregar mejoras verificables.",
    "Corregir artefactos de plantilla en README y programa analitico.",
    "Expandir el token de plantilla del .bib al slug literal derecho-financiero-y-bancario.bib."
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
    "Comprobar que cada mejora agregada sea verificable y sin fuentes inventadas."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instruccion contraria.",
    "Conservar macros de identidad academica en el encabezado del .tex.",
    "Reemplazar titulo y subtitulo de plantilla por los de la actividad real antes de entregar.",
    "Completar Figura docente con dato real o etiqueta explicita de supuesto.",
    "Mantener sincronizados titulo, subtitulo y materia entre portada y contenido.",
    "Evitar romper comandos y rutas en portada, tablas y referencias.",
    "Revisar que la tabla de identificacion compile sin celdas abiertas ni comandos incompletos."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliografico canonico de la materia.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Incluir fecha de consulta en referencias web.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y deduplicadas.",
    "Mantener metodo union-dedupe con compresion lossless.",
    "Propagar lateralmente solo reglas independientes de una actividad especifica.",
    "Etiquetar origen de reglas heredadas para auditoria de no regresion.",
    "Si reaparece salida no estructurada en ciclo 2, aplicar normalizacion manual como contingencia."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificacion.",
    "Definir formato obligatorio de citacion para la materia (supuesto: no definido aun).",
    "Validar si la localizacion de portada debe mantenerse o actualizarse por lineamiento oficial.",
    "Confirmar planeacion semanal vigente antes de generar actividades.",
    "Definir si los nombres de archivo con artefactos se corrigen manualmente o por regeneracion."
  ]
}