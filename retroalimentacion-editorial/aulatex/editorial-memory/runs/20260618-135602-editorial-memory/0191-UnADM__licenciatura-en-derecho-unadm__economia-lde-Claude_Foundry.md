```json
{
  "summary": [
    "Materia destino: Economía LDE de UnADM, enfoque jurídico con evidencia, análisis propio y conclusión transferible.",
    "Ubicación curricular confirmada: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Fuente curricular local: malla-curricular-derecho-unadm.pdf en assets-unadm.",
    "Bibliografía local inicia con sitio institucional UnADM y malla curricular de Derecho.",
    "Origen de aprendizaje ciclo 1: actividad 1 de Filosofía del Derecho LDE.",
    "Compresión por unión-dedupe sin pérdida y sin regresión.",
    "Alerta heredada: salida no parseable desde GPT-Pro en ciclo 1 (economia-lde).",
    "Alerta heredada: salida no parseable desde Codex en alcance institucional UnADM.",
    "Normalización manual pendiente por salidas no parseables previas.",
    "README local define cinco archivos canónicos y pauta editorial de integridad académica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Usar contexto de Licenciatura en Derecho para Economía: semestre 3, bloque 2, obligatoria, 8 créditos.",
    "Conservar voz académica formal y enfoque jurídico aplicado.",
    "Marcar como supuesto cualquier dato no confirmado por planeación oficial.",
    "Tratar fuentes heredadas de modelos (GPT-Pro o Codex) como provisionales hasta validación editorial.",
    "Supuesto: las alertas GPT-Pro y Codex son controles de calidad, no fuentes académicas."
  ],
  "structure_rules": [
    "Organizar cada producto con problema, conceptos o datos, análisis propio y cierre argumentativo.",
    "Alinear contenido a los cinco ejes del programa analítico de Economía.",
    "Mantener la carpeta de materia como punto de entrada canónico.",
    "Agregar fuentes específicas de actividad en economia.bib.",
    "Usar reportes, presentaciones o productos visuales según planeación.",
    "Corregir artefactos visibles de plantilla en README y archivos de apoyo.",
    "Normalizar nombres visibles: reporte-economia.tex, presentacion-economia.tex, economia.bib y referencias-economia.",
    "Supuesto: README contiene placeholders sin expandir ($(@{...}.Slug)); resolver a economia.bib."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado (reporte, presentación o visual).",
    "Incluir conclusión jurídica con criterio propio en cada actividad.",
    "Verificar que el planteamiento responda a un problema jurídico o social concreto.",
    "No inventar hechos, normas ni referencias.",
    "Distinguir conceptos económicos, datos y argumentos jurídicos.",
    "Conectar la conclusión con práctica jurídica o impacto social."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes disponibles.",
    "Bloquear propagación si hay campos críticos vacíos sin marcar como supuesto.",
    "Verificar que las fuentes citadas existan en economia.bib o assets locales.",
    "Confirmar que metadatos de portada coincidan con README y plantilla base.",
    "Mantener alerta de parseo hasta cierre editorial documentado."
  ],
  "latex_rules": [
    "Conservar reporte-economia.tex como plantilla base de formato.",
    "Mantener metadatos académicos completos en portada (alumno, matrícula, figura docente, semestre, bloque, tipo, créditos).",
    "Usar estilo de citación authoryear consistente con setcitestyle definido.",
    "Evitar cambios de paquetes o clase sin justificación técnica verificable.",
    "Mantener español y papel carta salvo instrucción oficial distinta.",
    "Marcar figura docente pendiente como dato por definir.",
    "Conservar coursecode LDE-S3B2 coherente con semestre y bloque."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio local de referencias de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares oficiales.",
    "Registrar fecha de consulta cuando aplique a recursos web.",
    "No agregar fuentes no verificables o inexistentes.",
    "Agregar referencias específicas solo cuando se usen en el producto.",
    "Conservar unadmSitioWeb mientras su fecha de consulta sea verificable.",
    "Conservar unadmMallaDerecho2024 como referencia institucional local.",
    "No tratar salidas de modelos como bibliografía académica."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras normalización manual de ciclo 1.",
    "Aplicar unión-dedupe para evitar duplicados sin recorte.",
    "Conservar reglas heredadas válidas y anexar solo mejoras verificables.",
    "Propagar reglas generales de integridad académica a materias laterales.",
    "No propagar datos específicos de Economía como si fueran institucionales.",
    "Propagar incidencias de parseo como alerta persistente, no como contenido académico."
  ],
  "open_questions": [
    "Definir nombre de figura docente para metadatos de portada.",
    "Confirmar si existe guía formal de formato adicional para Economía en LDE.",
    "Validar si unadmSitioWeb requiere actualización anual de year y fecha de consulta.",
    "Confirmar si README debe registrar solo economia.bib como nombre canónico.",
    "Confirmar planeación oficial de actividades antes de crear fuentes específicas.",
    "Cerrar validación editorial de alertas GPT-Pro y Codex.",
    "Confirmar si los placeholders del README deben resolverse y regenerarse."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/economia-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```