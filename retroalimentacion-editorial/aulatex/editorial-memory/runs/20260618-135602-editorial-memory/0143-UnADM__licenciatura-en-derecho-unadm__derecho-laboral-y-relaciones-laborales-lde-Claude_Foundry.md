```json
{
  "summary": [
    "Heredado: hubo salida no parseable en ciclo previo.",
    "Aplicar normalizacion manual antes de reutilizar memoria heredada.",
    "Destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Memoria consolidada por union-dedupe lossless sin recorte intencional.",
    "Asignatura destino: Derecho laboral y relaciones laborales, Licenciatura en Derecho UnADM.",
    "Materia destino validada: LDE-S7B1, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Existe antecedente de salidas no parseables desde Codex y GPT-Pro; normalizar antes de reutilizar.",
    "Conservar identidad UnADM y enfoque juridico-laboral en toda actividad.",
    "Mantener union-dedupe lossless sin eliminar reglas utiles previas.",
    "Corregir artefactos de plantilla en README y programa analitico antes de fijar canon.",
    "Heredado de institucion UnADM: salida sin JSON parseable desde Codex."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar asignatura: Derecho laboral y relaciones laborales.",
    "Usar codigo: LDE-S7B1.",
    "Usar licenciatura: Licenciatura en Derecho.",
    "Usar semestre 7 y bloque 1.",
    "Marcar como supuesto todo dato personal no confirmado del autor.",
    "Usar autor de plantilla solo si el alumno lo confirma.",
    "Supuesto: autor de plantilla es Martin Jonathan de la Cruz; confirmar por alumno.",
    "Marcar como provisional toda memoria heredada desde fuentes no parseables.",
    "Fuente provisional heredada: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional heredada: GPT-Pro desde Actividad 1 de Filosofia del Derecho.",
    "Fuente provisional heredada: Codex desde institucion UnADM."
  ],
  "structure_rules": [
    "Alinear cada entrega al flujo: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Conservar README de materia como punto de entrada canonico.",
    "Registrar nuevas reglas por union-dedupe sin eliminar reglas vigentes utiles.",
    "Organizar productos como reporte, presentacion, bibliografia local, programa analitico y carpeta de referencias.",
    "Corregir rutas o nombres mal renderizados antes de canonizar.",
    "Resolver marcadores PowerShell sin expandir ($(@{...}.Slug)) hacia el slug derecho-laboral-y-relaciones-laborales.",
    "Corregir entrada mal renderizada de reporte a reporte-derecho-laboral-y-relaciones-laborales.tex.",
    "Corregir entrada mal renderizada de referencias a referencias-derecho-laboral-y-relaciones-laborales/.",
    "Sustituir marcador de bibliografia por derecho-laboral-y-relaciones-laborales.bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico o social laboral.",
    "Sustentar postura academica propia con norma, doctrina o datos verificables.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Vincular conceptos laborales con aplicacion profesional comprobable.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de consolidar o propagar memoria.",
    "Verificar consistencia entre README, programa analitico y plantilla LaTeX.",
    "Confirmar trazabilidad de toda cita y ausencia de fuentes inventadas.",
    "Validar existencia de archivos y carpetas o marcarlos como supuestos.",
    "Detectar y corregir marcadores de plantilla sin expandir antes de fijar canon.",
    "Verificar cierre de entornos LaTeX truncados antes de compilar.",
    "Revisar respuesta no estructurada antes de aplicarla aguas abajo.",
    "Verificar que los metadatos coincidan con la materia destino.",
    "Revisar que el producto mantenga enfoque juridico-laboral."
  ],
  "latex_rules": [
    "Usar la plantilla .tex de la materia como base por actividad.",
    "Completar metadatos con datos reales de la actividad.",
    "Mantener compilacion en espanol y formato letterpaper.",
    "Conservar macros institucionales de universidad, curso, codigo y licenciatura.",
    "Completar el entorno authortable truncado antes de compilar.",
    "Validar cierre de entornos LaTeX antes de compilar.",
    "Evitar rutas o nombres derivados de plantillas no resueltas.",
    "No fijar autor personal sin confirmacion del alumno."
  ],
  "bibliography_rules": [
    "Centralizar fuentes en derecho-laboral-y-relaciones-laborales.bib.",
    "Conservar fuentes institucionales UnADM incluidas.",
    "Conservar claves base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar solo entradas BibTeX verificables y pertinentes a la actividad.",
    "Marcar como supuesto metadatos faltantes como fecha de consulta.",
    "Usar la malla curricular de Derecho como fuente institucional local cuando aplique.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Corregir referencias al marcador PowerShell de bibliografia antes de citar."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validar JSON y normalizacion.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Preservar reglas utiles previas aunque sean institucionales.",
    "Propagar solo mejoras verificables y compatibles con contexto juridico.",
    "Priorizar correccion de artefactos de plantilla en ciclo actual.",
    "Si se reutiliza memoria de ciclo 1, normalizar manualmente primero.",
    "No propagar reglas especificas de otra materia sin validar pertinencia laboral."
  ],
  "open_questions": [
    "Definir formato de cita juridica requerido por docente: APA, ISO 690 u otro.",
    "Confirmar si autor en plantilla es fijo institucional o variable por alumno.",
    "Verificar si existe rubrica oficial por actividad para convertirla en checklist.",
    "Confirmar nombres canonicos finales de reporte, presentacion y carpeta de referencias en README.",
    "Definir si LDE-S7B1 basta como codigo unico para todas las actividades.",
    "Confirmar si la bibliografia local requiere fecha de consulta actualizada por actividad."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derecho-laboral-y-relaciones-laborales-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```