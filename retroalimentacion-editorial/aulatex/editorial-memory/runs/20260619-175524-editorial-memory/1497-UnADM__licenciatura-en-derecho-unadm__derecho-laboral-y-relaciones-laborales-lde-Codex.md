{
  "summary": [
    "Materia destino confirmada: Derecho laboral y relaciones laborales de UnADM.",
    "Ubicacion curricular confirmada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Mantener identidad UnADM, enfoque juridico-laboral e integridad academica.",
    "Aplicar normalizacion manual por antecedentes de salidas no parseables.",
    "Consolidacion por union-dedupe lossless, sin recorte de reglas utiles.",
    "Corregir artefactos de plantilla en README, programa analitico y plantilla LaTeX antes de canonizar."
  ],
  "identity_rules": [
    "Mantener portada y metadatos con identidad institucional UnADM.",
    "Usar asignatura: Derecho laboral y relaciones laborales.",
    "Usar codigo: LDE-S7B1.",
    "Usar licenciatura: Licenciatura en Derecho.",
    "Usar semestre 7 y bloque 1 en metadatos.",
    "Marcar como supuesto todo dato personal no confirmado.",
    "No fijar autor personal sin confirmacion del alumno.",
    "Supuesto: autor de plantilla actual es Martin Jonathan de la Cruz; requiere confirmacion.",
    "Marcar como provisional memoria heredada desde fuentes no parseables."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, analisis propio, conclusion transferible.",
    "Organizar productos como reporte, presentacion, bibliografia local, programa analitico y carpeta de referencias.",
    "Corregir nombres o rutas mal renderizados antes de canonizar.",
    "Resolver marcadores PowerShell sin expandir hacia slug valido.",
    "Usar como nombres canonicos: reporte-derecho-laboral-y-relaciones-laborales.tex, presentacion-derecho-laboral-y-relaciones-laborales.tex, derecho-laboral-y-relaciones-laborales.bib, programa-analitico-derecho-laboral-y-relaciones-laborales.md, referencias-derecho-laboral-y-relaciones-laborales/."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema juridico o social laboral.",
    "Sustentar postura propia con norma, doctrina o datos verificables.",
    "Vincular conceptos laborales con aplicacion profesional verificable.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de consolidar o propagar memoria.",
    "Normalizar manualmente cualquier heredado no estructurado antes de reutilizar.",
    "Verificar consistencia entre README, programa analitico y plantilla LaTeX.",
    "Verificar que metadatos coincidan con la materia destino.",
    "Confirmar trazabilidad de toda cita.",
    "Confirmar ausencia de fuentes inventadas.",
    "Validar existencia de archivos y carpetas, o marcarlos como supuestos.",
    "Detectar y corregir marcadores de plantilla sin expandir.",
    "Verificar cierre de entornos LaTeX truncados antes de compilar.",
    "Revisar que el producto mantenga enfoque juridico-laboral."
  ],
  "latex_rules": [
    "Usar la plantilla .tex de la materia como base por actividad.",
    "Completar metadatos con datos reales de la actividad.",
    "Mantener compilacion en espanol y formato letterpaper.",
    "Conservar macros institucionales de universidad, curso, codigo y licenciatura.",
    "Completar el entorno authortable truncado antes de compilar.",
    "Evitar rutas o nombres derivados de plantillas no resueltas."
  ],
  "bibliography_rules": [
    "Centralizar fuentes en derecho-laboral-y-relaciones-laborales.bib.",
    "Conservar fuentes institucionales UnADM incluidas.",
    "Conservar claves base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar solo entradas BibTeX verificables y pertinentes a la actividad.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Marcar como supuesto metadatos faltantes, como fecha de consulta.",
    "Corregir referencias al marcador PowerShell de bibliografia antes de citar."
  ],
  "propagation_hints": [
    "Propagar solo despues de validar JSON y normalizacion manual.",
    "Aplicar deduplicacion semantica con frases cortas y accionables.",
    "Preservar reglas utiles previas aunque sean institucionales.",
    "Propagar solo mejoras verificables y compatibles con contexto juridico-laboral.",
    "No propagar reglas especificas de otra materia sin validar pertinencia.",
    "Ciclo 1 requiere normalizacion manual si se reutiliza memoria heredada."
  ],
  "open_questions": [
    "Confirmar formato de cita juridica exigido por docente: APA, ISO 690 u otro.",
    "Confirmar si el autor en plantilla es fijo institucional o variable por alumno.",
    "Verificar si existe rubrica oficial por actividad para convertirla en checklist.",
    "Confirmar si LDE-S7B1 basta como codigo unico en todas las actividades.",
    "Confirmar si la bibliografia local requiere fecha de consulta actualizada por actividad."
  ]
}