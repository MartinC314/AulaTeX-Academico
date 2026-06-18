{
  "summary": [
    "Base institucional UnADM heredada con compresion union-dedupe y sin regresion.",
    "El destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "La materia se ubica en semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Existe antecedente de salida sin JSON parseable desde Codex para UnADM.",
    "El README local contiene nombres de archivos con artefactos de plantilla o caracteres faltantes."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar datos de la materia: Derecho financiero y bancario, clave LDE-S3B2, semestre 3, bloque 2.",
    "Conservar autoria real del alumno y matricula en la tabla de identificacion.",
    "Marcar como supuesto cualquier dato no confirmado del docente o grupo.",
    "Tratar Codex desde ingenieria en sistemas computacionales como fuente provisional heredada.",
    "Usar la Licenciatura en Derecho como facultad o programa academico del destino."
  ],
  "structure_rules": [
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Usar la carpeta de materia como punto de entrada canonico antes de crear actividades.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib de la materia.",
    "No eliminar reglas previas validas; solo agregar reglas nuevas verificables.",
    "Corregir en README nombres de archivos con caracteres faltantes o plantillas sin expandir.",
    "Mantener el programa analitico como guia editorial de reportes, presentaciones y productos visuales."
  ],
  "activity_rules": [
    "Iniciar cada actividad con un problema juridico o social delimitado.",
    "Sustentar con norma, doctrina o datos pertinentes al tema financiero y bancario.",
    "Cerrar con postura juridica propia y aplicable a la practica profesional.",
    "Evitar afirmaciones sin respaldo cuando la consigna pida evidencia.",
    "Adaptar el producto solicitado a la planeacion semanal disponible.",
    "Separar descripcion de conceptos, analisis propio y conclusion juridica."
  ],
  "quality_gates": [
    "Verificar que la salida sea JSON parseable antes de propagar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a archivos locales o memoria heredada.",
    "Bloquear propagacion si hay campos obligatorios vacios sin marcar supuesto.",
    "Validar que no existan duplicados semanticos antes de guardar memoria.",
    "Comprobar que toda mejora agregada tenga respaldo en contexto local o memoria heredada."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y formato letterpaper oneside salvo instruccion contraria.",
    "Conservar macros de identidad academica en el encabezado del .tex.",
    "Completar campos pendientes como Figura docente con dato real o etiqueta de supuesto.",
    "Evitar romper comandos y rutas de archivos en portada, tablas y referencias.",
    "Mantener titulo, subtitulo y materia sincronizados con la actividad real.",
    "Revisar que la tabla de identificacion compile sin celdas abiertas ni comandos incompletos."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en derecho-financiero-y-bancario.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Incluir fecha de consulta cuando la referencia sea web.",
    "Conservar la malla curricular local como fuente institucional de ubicacion curricular.",
    "Agregar entradas BibTeX solo cuando exista fuente verificable."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y deduplicadas.",
    "Mantener metodo de compresion union-dedupe con perdida cero.",
    "Ciclo 1: aplicar normalizacion manual si reaparece salida no estructurada.",
    "Etiquetar origen de reglas heredadas para auditoria de no regresion.",
    "Propagar a nivel materia las reglas generales de identidad, estructura y bibliografia.",
    "Propagar lateralmente solo reglas independientes de la asignatura especifica."
  ],
  "open_questions": [
    "Confirmar nombre de la figura docente para completar plantilla.",
    "Definir si existe formato obligatorio de citacion APA, IEEE u otro para esta materia.",
    "Validar si la localizacion institucional de portada debe mantenerse o actualizarse por lineamiento oficial.",
    "Confirmar si el grupo debe aparecer en la tabla de identificacion.",
    "Confirmar la planeacion semanal antes de crear actividades especificas.",
    "Verificar si los nombres de archivos del README deben corregirse manualmente o regenerarse."
  ]
}