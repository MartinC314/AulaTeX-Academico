{
  "summary": [
    "Base institucional UnADM consolidada con compresion union-dedupe y sin regresion.",
    "El destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Derecho financiero y bancario pertenece a Licenciatura en Derecho, semestre 3, bloque 2, obligatoria, 8 creditos.",
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
    "Tratar Codex desde ingenieria en sistemas computacionales como fuente provisional heredada.",
    "Tratar GPT-Pro desde Actividad 1 como fuente provisional heredada.",
    "Tratar fuentes heredadas de motor como provisionales y auditables."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Mantener el programa analitico como guia editorial de reportes, presentaciones y productos visuales.",
    "Corregir artefactos de plantilla en README y programa analitico.",
    "Corregir nombres de archivos con caracteres faltantes en README.",
    "Expandir el token de plantilla del .bib al slug literal derecho-financiero-y-bancario.bib.",
    "No eliminar reglas previas validas.",
    "Agregar solo mejoras verificables."
  ],
  "activity_rules": [
    "Iniciar cada actividad con un problema juridico o social delimitado.",
    "Sustentar con norma, doctrina o datos pertinentes al tema financiero y bancario.",
    "Separar descripcion conceptual, analisis propio y conclusion juridica.",
    "Adaptar el producto a la planeacion semanal confirmada.",
    "Evitar afirmaciones sin respaldo cuando la consigna pida evidencia.",
    "Cerrar con postura juridica propia aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Verificar que toda salida de memoria sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear propagacion si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar deduplicacion semantica antes de guardar.",
    "Comprobar que cada mejora agregada sea verificable.",
    "Bloquear fuentes o metadatos bibliograficos inventados.",
    "Normalizar manualmente si reaparece salida no estructurada."
  ],
  "latex_rules": [
    "Mantener documentclass article en spanish, letterpaper, oneside salvo instruccion contraria.",
    "Conservar macros de identidad academica en el encabezado del .tex.",
    "Reemplazar titulo de plantilla por el titulo de la actividad real antes de entregar.",
    "Reemplazar subtitulo de plantilla por el subtitulo de la actividad real antes de entregar.",
    "Mantener sincronizados titulo, subtitulo y materia entre portada y contenido.",
    "Completar Figura docente con dato real o etiqueta explicita de supuesto.",
    "Revisar que la tabla de identificacion compile sin celdas abiertas ni comandos incompletos.",
    "Evitar romper comandos y rutas en portada, tablas y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo bibliografico canonico de la materia.",
    "Registrar fuentes especificas de actividad en derecho-financiero-y-bancario.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Conservar la malla curricular local como fuente institucional de ubicacion curricular.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo con fuente verificable.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Incluir fecha de consulta en referencias web."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y deduplicadas.",
    "Mantener metodo union-dedupe con compresion lossless.",
    "Etiquetar origen de reglas heredadas para auditoria de no regresion.",
    "Propagar a nivel materia las reglas generales de identidad, estructura y bibliografia.",
    "Propagar lateralmente solo reglas independientes de una actividad especifica.",
    "Aplicar normalizacion manual si se reutiliza memoria de ciclo 1 con salida no estructurada.",
    "Si reaparece salida no estructurada en ciclo 2, aplicar normalizacion manual como contingencia."
  ],
  "open_questions": [
    "Confirmar nombre real de la figura docente.",
    "Confirmar si el grupo debe aparecer en la tabla de identificacion.",
    "Definir formato obligatorio de citacion para la materia; supuesto: no definido aun.",
    "Validar si la localizacion de portada debe mantenerse o actualizarse por lineamiento oficial.",
    "Confirmar planeacion semanal vigente antes de generar actividades.",
    "Definir si los nombres de archivo con artefactos se corrigen manualmente o por regeneracion.",
    "Confirmar numero real de actividad para sustituir Actividad X en el subtitulo del .tex."
  ]
}