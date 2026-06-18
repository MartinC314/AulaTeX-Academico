```json
{
  "summary": [
    "Heredado: hubo salida no parseable en ciclo previo.",
    "Aplicar normalizacion manual antes de reutilizar memoria heredada.",
    "Destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Memoria consolidada por union-dedupe sin recorte intencional.",
    "Asignatura destino: Derecho laboral y relaciones laborales, Licenciatura en Derecho UnADM.",
    "Ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Existe antecedente de salida no parseable desde Codex; normalizar antes de reutilizar heredados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar datos de asignatura: Derecho laboral y relaciones laborales, LDE-S7B1, semestre 7, bloque 1.",
    "Marcar como supuesto cualquier dato personal no confirmado del autor.",
    "Usar el autor de plantilla solo si esta confirmado.",
    "Marcar como provisional la memoria heredada desde Codex si se reutiliza.",
    "Supuesto: autor de plantilla es Martin Jonathan de la Cruz; confirmar por alumno."
  ],
  "structure_rules": [
    "Alinear cada entrega al esquema: problema, conceptos o normas, producto, analisis propio y conclusion transferible.",
    "Conservar README de materia como punto de entrada canonico.",
    "Registrar nuevas reglas por union-dedupe sin eliminar reglas vigentes utiles.",
    "Organizar productos como reporte, presentacion, bibliografia local, programa analitico y carpeta de referencias.",
    "Corregir rutas o nombres de archivo mal renderizados antes de usarlos como canon.",
    "Resolver plantillas PowerShell sin expandir ($(@{...}.Slug)) hacia el slug derecho-laboral-y-relaciones-laborales."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con un problema juridico o social laboral.",
    "Incluir postura academica propia sustentada en norma, doctrina o datos verificables.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Vincular conceptos laborales con aplicacion profesional verificable.",
    "No trasladar contenido de otra materia sin verificar pertinencia con Derecho laboral."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar consistencia entre actividad, programa analitico y plantilla LaTeX.",
    "Confirmar que no se inventen fuentes y que toda cita sea trazable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar que los metadatos coincidan con README, programa analitico y plantilla.",
    "Validar que nombres de archivos y carpetas existan o esten marcados como supuestos.",
    "Detectar marcadores de plantilla sin expandir antes de fijar canon de nombres."
  ],
  "latex_rules": [
    "Usar la plantilla .tex de la materia como base de cada reporte.",
    "Completar metadatos del documento con datos reales de la actividad.",
    "Mantener compatibilidad con compilacion en espanol y formato letterpaper.",
    "Conservar macros institucionales de universidad, curso, codigo y licenciatura.",
    "Validar cierre de entornos LaTeX antes de compilar.",
    "Evitar caracteres o rutas generadas por plantilla no resuelta en nombres de archivo.",
    "Completar el entorno authortable truncado en la plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Conservar fuentes institucionales UnADM ya incluidas.",
    "Agregar solo entradas BibTeX verificables y relacionadas con la actividad.",
    "Marcar como supuesto cuando falte fecha de consulta u otro metadato.",
    "Usar la malla curricular de Derecho como fuente institucional local cuando aplique.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Conservar claves base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo despues de validacion JSON.",
    "En ciclo 1, priorizar normalizacion manual de heredados no estructurados.",
    "Aplicar deduplicacion semantica por frase accionable corta.",
    "Preservar reglas utiles previas aunque provengan de memoria institucional.",
    "Propagar solo mejoras verificables hacia materias laterales."
  ],
  "open_questions": [
    "Definir formato de cita juridica requerido por docente: APA, ISO 690 u otro.",
    "Confirmar si la plantilla debe fijar autor institucional o variable por alumno.",
    "Verificar si existe rubrica oficial por actividad para convertirla en checklist.",
    "Confirmar nombres canonicos de reporte, presentacion y carpeta de referencias en README.",
    "Confirmar si el codigo LDE-S7B1 es suficiente para todas las actividades de la materia."
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