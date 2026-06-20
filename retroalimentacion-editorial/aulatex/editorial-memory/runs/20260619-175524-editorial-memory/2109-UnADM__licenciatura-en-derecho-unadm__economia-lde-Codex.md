{
  "summary": [
    "Materia destino: Economia LDE de UnADM con enfoque juridico, evidencia, analisis propio y conclusion transferible.",
    "Ubicacion curricular confirmada: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Fuente curricular local: malla-curricular-derecho-unadm.pdf en assets-unadm.",
    "Bibliografia base local: unadmSitioWeb y unadmMallaDerecho2024 en economia.bib.",
    "README local define cinco archivos canonicos y presenta placeholders o artefactos de plantilla por resolver.",
    "Persisten alertas heredadas de salida no parseable (GPT-Pro, Codex, Auto, Claude Foundry) en economia-lde y alcance institucional.",
    "Normalizacion manual pendiente para ciclos y salidas afectados por alertas de parseo.",
    "Compresion aplicada: union-dedupe lossless, sin regresion.",
    "Supuesto: alertas de parseo pertenecen a control de calidad editorial y no a contenido disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar contexto de Licenciatura en Derecho para Economia: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Conservar voz academica formal y enfoque juridico aplicado.",
    "Marcar como supuesto todo dato no confirmado por planeacion oficial.",
    "Tratar salidas de modelos (GPT-Pro, Codex, Auto, Claude Foundry) como fuentes provisionales de control editorial, no academicas.",
    "Supuesto: las alertas de parseo pertenecen a control de calidad editorial y no a contenido disciplinar."
  ],
  "structure_rules": [
    "Organizar productos con problema, conceptos o datos, analisis propio y cierre argumentativo.",
    "Alinear contenido a los cinco ejes del programa analitico de Economia.",
    "Mantener carpeta de materia como punto de entrada canonico.",
    "Usar reporte, presentacion o producto visual segun planeacion.",
    "Agregar fuentes especificas de actividad en economia.bib solo si se usan.",
    "Normalizar nombres visibles: reporte-economia.tex, presentacion-economia.tex, economia.bib, referencias-economia.",
    "Corregir artefactos de plantilla en README y programa analitico.",
    "Resolver placeholders tipo $(@{...}.Slug) a economia.bib.",
    "Supuesto: los saltos rotos en README (eporte o eferencias) provienen de plantilla y deben corregirse."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado (reporte, presentacion o visual).",
    "Incluir conclusion juridica con criterio propio en cada actividad.",
    "Verificar que el planteamiento responda a un problema juridico o social concreto.",
    "Distinguir conceptos economicos, datos y argumentos juridicos.",
    "Conectar la conclusion con practica juridica o impacto social.",
    "No inventar hechos, normas ni referencias."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes disponibles.",
    "Verificar que las fuentes citadas existan en economia.bib o assets locales.",
    "Confirmar que metadatos de portada coincidan con README y plantilla base.",
    "Bloquear propagacion si hay campos criticos vacios sin marcar como supuesto.",
    "Mantener alerta de parseo hasta cierre editorial documentado."
  ],
  "latex_rules": [
    "Conservar reporte-economia.tex como plantilla base de formato.",
    "Mantener metadatos academicos completos en portada (alumno, matricula, figura docente, semestre, bloque, tipo, creditos).",
    "Conservar coursecode LDE-S3B2 coherente con semestre y bloque.",
    "Marcar figura docente como pendiente cuando no este confirmada.",
    "Usar estilo de citacion authoryear consistente con setcitestyle.",
    "Mantener espanol y papel carta salvo instruccion oficial distinta.",
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
    "Propagar reglas generales de integridad academica a materias laterales.",
    "No propagar datos especificos de Economia como si fueran institucionales.",
    "Propagar incidencias de parseo como alerta persistente, no como contenido academico.",
    "Mantener bandera de normalizacion manual en ciclos con salida no parseable reutilizada.",
    "Ciclo 22: mantener bandera de normalizacion manual si se reutiliza salida afectada por parseo."
  ],
  "open_questions": [
    "Definir nombre de figura docente para metadatos de portada.",
    "Confirmar si existe guia formal de formato adicional para Economia en LDE.",
    "Confirmar si README debe registrar solo economia.bib como nombre canonico.",
    "Confirmar resolucion y regeneracion de placeholders en README y programa analitico.",
    "Validar si unadmSitioWeb requiere actualizacion anual de year y fecha de consulta.",
    "Cerrar validacion editorial de alertas de parseo heredadas."
  ]
}