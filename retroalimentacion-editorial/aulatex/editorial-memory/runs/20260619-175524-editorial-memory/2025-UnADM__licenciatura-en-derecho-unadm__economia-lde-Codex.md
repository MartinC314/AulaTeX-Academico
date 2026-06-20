{
  "summary": [
    "Materia destino: Economía LDE de UnADM.",
    "Ubicación curricular confirmada: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "La materia usa enfoque jurídico con evidencia, análisis propio y conclusión transferible.",
    "Origen de aprendizaje ciclo 1: actividad 1 de Filosofía del Derecho LDE.",
    "Bibliografía base local: unadmSitioWeb y unadmMallaDerecho2024 en economia.bib.",
    "README local define cinco archivos canónicos y pauta editorial de integridad académica.",
    "Se detectaron salidas no parseables previas (GPT-Pro, Codex, Auto, Claude Foundry) para economia-lde.",
    "Normalización manual pendiente en ciclo 1 por alertas de parseo.",
    "Se conserva compresión por unión-dedupe sin pérdida y sin regresión."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar contexto de Licenciatura en Derecho para Economía: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Conservar voz académica formal y enfoque jurídico aplicado.",
    "Marcar como supuesto cualquier dato no confirmado por planeación oficial.",
    "Tratar salidas de modelos (GPT-Pro, Codex, Auto, Claude Foundry) como fuentes provisionales de control, no académicas.",
    "Supuesto: las alertas de parseo son control de calidad editorial y no contenido disciplinar."
  ],
  "structure_rules": [
    "Organizar cada producto con problema, conceptos o datos, análisis propio y cierre argumentativo.",
    "Alinear contenido a los cinco ejes del programa analítico de Economía.",
    "Mantener la carpeta de materia como punto de entrada canónico.",
    "Usar reportes, presentaciones o productos visuales según planeación.",
    "Agregar fuentes específicas de actividad en economia.bib solo si se usan.",
    "Corregir artefactos de plantilla en README y programa analítico.",
    "Normalizar nombres visibles: reporte-economia.tex, presentacion-economia.tex, economia.bib y referencias-economia.",
    "Supuesto: placeholders tipo $(@{...}.Slug) deben resolverse a economia.bib."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado (reporte, presentación o visual).",
    "Verificar que el planteamiento responda a un problema jurídico o social concreto.",
    "Distinguir conceptos económicos, datos y argumentos jurídicos.",
    "Incluir conclusión jurídica con criterio propio en cada actividad.",
    "Conectar la conclusión con práctica jurídica o impacto social.",
    "No inventar hechos, normas ni referencias."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Mantener alerta de parseo hasta cierre editorial documentado.",
    "Confirmar trazabilidad entre afirmaciones y fuentes disponibles.",
    "Bloquear propagación si hay campos críticos vacíos sin marcar como supuesto.",
    "Verificar que las fuentes citadas existan en economia.bib o assets locales.",
    "Confirmar que metadatos de portada coincidan con README y plantilla base."
  ],
  "latex_rules": [
    "Conservar reporte-economia.tex como plantilla base de formato.",
    "Mantener metadatos académicos completos en portada.",
    "Incluir alumno, matrícula, figura docente, semestre, bloque, tipo y créditos.",
    "Conservar coursecode LDE-S3B2 coherente con semestre y bloque.",
    "Usar estilo de citación authoryear consistente con setcitestyle definido.",
    "Mantener español y papel carta salvo instrucción oficial distinta.",
    "Evitar cambios de clase o paquetes sin justificación técnica verificable.",
    "Marcar figura docente como pendiente cuando no esté confirmada."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio local de referencias de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares oficiales.",
    "Conservar unadmSitioWeb mientras su fecha de consulta sea verificable.",
    "Conservar unadmMallaDerecho2024 como referencia institucional local.",
    "Registrar fecha de consulta cuando aplique a recursos web.",
    "Agregar referencias específicas solo cuando se usen en el producto.",
    "No agregar fuentes no verificables o inexistentes.",
    "No tratar salidas de modelos como bibliografía académica."
  ],
  "propagation_hints": [
    "Aplicar estrategia unión-dedupe para evitar duplicados sin recorte.",
    "Conservar reglas heredadas válidas y anexar solo mejoras verificables.",
    "Propagar incidencias de parseo como alerta persistente, no como contenido académico.",
    "Propagar arriba y laterales solo tras normalización manual de ciclo 1.",
    "Propagar reglas generales de integridad académica a materias laterales.",
    "No propagar datos específicos de Economía como si fueran institucionales.",
    "Ciclo 1 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Definir nombre de figura docente para metadatos de portada.",
    "Confirmar si existe guía formal de formato adicional para Economía en LDE.",
    "Validar si unadmSitioWeb requiere actualización anual de year y fecha de consulta.",
    "Confirmar si README debe registrar solo economia.bib como nombre canónico.",
    "Confirmar planeación oficial de actividades antes de crear fuentes específicas.",
    "Confirmar si los placeholders del README y programa analítico deben resolverse y regenerarse.",
    "Cerrar validación editorial de alertas de parseo heredadas."
  ]
}