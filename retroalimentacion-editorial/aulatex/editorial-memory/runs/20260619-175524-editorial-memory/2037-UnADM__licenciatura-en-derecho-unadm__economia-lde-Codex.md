{
  "summary": [
    "Materia destino: Economia LDE de UnADM con enfoque juridico, evidencia, analisis propio y conclusion transferible.",
    "Ubicacion curricular confirmada: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Origen de aprendizaje: actividad 1 de Filosofia del Derecho LDE.",
    "Bibliografia base local: unadmSitioWeb y unadmMallaDerecho2024 en economia.bib.",
    "Fuente curricular local: malla-curricular-derecho-unadm.pdf en assets-unadm.",
    "Persisten alertas heredadas de salida no parseable (GPT-Pro, Codex, Auto, Claude Foundry) para economia-lde.",
    "Normalizacion manual pendiente en ciclos afectados por alertas de parseo.",
    "Base local usa cinco archivos canonicos y requiere resolver placeholders visibles en README y programa analitico.",
    "Compresion aplicada: union-dedupe lossless, sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar contexto de Licenciatura en Derecho para Economia: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Conservar voz academica formal y enfoque juridico aplicado.",
    "Marcar como supuesto todo dato no confirmado por planeacion oficial.",
    "Tratar salidas de modelos (GPT-Pro, Codex, Auto, Claude Foundry) como fuentes provisionales de control editorial, no academicas.",
    "Supuesto: las alertas de parseo pertenecen a control de calidad y no a contenido disciplinar."
  ],
  "structure_rules": [
    "Organizar cada producto con problema, conceptos o datos, analisis propio y cierre argumentativo.",
    "Alinear contenido a los cinco ejes del programa analitico de Economia.",
    "Mantener la carpeta de materia como punto de entrada canonico.",
    "Usar reporte, presentacion o producto visual segun planeacion.",
    "Normalizar nombres visibles: reporte-economia.tex, presentacion-economia.tex, economia.bib y referencias-economia.",
    "Agregar fuentes especificas de actividad en economia.bib solo si se usan.",
    "Corregir artefactos de plantilla en README y programa analitico.",
    "Supuesto: placeholders tipo $(@{...}.Slug) deben resolverse a economia.bib."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado (reporte, presentacion o visual).",
    "Verificar que el planteamiento responda a un problema juridico o social concreto.",
    "Distinguir conceptos economicos, datos y argumentos juridicos.",
    "Incluir conclusion juridica con criterio propio en cada actividad.",
    "Conectar la conclusion con practica juridica o impacto social.",
    "No inventar hechos, normas ni referencias."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes disponibles.",
    "Verificar que las fuentes citadas existan en economia.bib o assets locales.",
    "Bloquear propagacion si hay campos criticos vacios sin marcar como supuesto.",
    "Confirmar que metadatos de portada coincidan con README y plantilla base.",
    "Mantener alerta de parseo hasta cierre editorial documentado."
  ],
  "latex_rules": [
    "Conservar reporte-economia.tex como plantilla base de formato.",
    "Mantener metadatos academicos completos en portada (alumno, matricula, figura docente, semestre, bloque, tipo, creditos).",
    "Conservar coursecode LDE-S3B2 coherente con semestre y bloque.",
    "Marcar figura docente como pendiente cuando no este confirmada.",
    "Mantener espanol y papel carta salvo instruccion oficial distinta.",
    "Usar estilo de citacion authoryear consistente con setcitestyle.",
    "Evitar cambios de clase o paquetes sin justificacion tecnica verificable."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio local de referencias de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares oficiales.",
    "Conservar unadmSitioWeb mientras su fecha de consulta sea verificable.",
    "Conservar unadmMallaDerecho2024 como referencia institucional local.",
    "Registrar fecha de consulta cuando aplique a recursos web.",
    "Agregar referencias especificas solo cuando se usen en el producto.",
    "No agregar fuentes no verificables o inexistentes.",
    "No tratar salidas de modelos como bibliografia academica."
  ],
  "propagation_hints": [
    "Aplicar union-dedupe para compresion lossless sin recorte.",
    "Conservar reglas heredadas validas y agregar solo mejoras verificables.",
    "Propagar arriba y laterales solo tras normalizacion manual del ciclo afectado.",
    "Propagar incidencias de parseo como alerta persistente, no como contenido academico.",
    "No propagar datos especificos de Economia como si fueran institucionales.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Ciclo 2: mantener bandera de normalizacion manual si se reutiliza salida no parseable.",
    "Ciclo 3 necesita normalizacion manual si se reutiliza.",
    "Ciclo 4 necesita normalizacion manual si se reutiliza.",
    "Ciclo 5 necesita normalizacion manual si se reutiliza.",
    "Ciclo 6 necesita normalizacion manual si se reutiliza.",
    "Ciclo 7 necesita normalizacion manual si se reutiliza.",
    "Ciclo 8 necesita normalizacion manual si se reutiliza.",
    "Ciclo 9 necesita normalizacion manual si se reutiliza.",
    "Ciclo 10 necesita normalizacion manual si se reutiliza.",
    "Ciclo 11 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Definir nombre de figura docente para metadatos de portada.",
    "Confirmar si existe guia formal de formato adicional para Economia en LDE.",
    "Validar si unadmSitioWeb requiere actualizacion anual de year y fecha de consulta.",
    "Confirmar si README debe registrar solo economia.bib como nombre canonico.",
    "Confirmar planeacion oficial de actividades antes de crear fuentes especificas.",
    "Confirmar resolucion y regeneracion de placeholders en README y programa analitico.",
    "Cerrar validacion editorial de alertas de parseo heredadas.",
    "Supuesto: la referencia heredada de Codex aplica solo como alerta de calidad y no como fuente academica."
  ]
}