```json
{
  "summary": [
    "Consolidar memoria de Derecho administrativo y control con union-dedupe lossless y sin regresion.",
    "Preservar alerta institucional por salidas no JSON parseables desde Codex y GPT-Pro antes de propagar.",
    "Validar respuestas no estructuradas antes de cualquier propagacion.",
    "Alinear la materia con semestre 6, bloque 1, obligatoria y 8 creditos segun malla local.",
    "Reutilizar solo reglas editoriales generales desde Filosofia del derecho; no trasladar doctrina no verificada.",
    "Corregir artefactos locales de README y programa analitico en nombres de archivo y tokens sin expandir. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, metadatos y redaccion academica.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Declarar cuando una regla provenga de fuente provisional. [supuesto]",
    "Marcar como provisional cualquier regla originada en Codex desde ingenieria-en-sistemas-computacionales. [supuesto]",
    "Marcar como provisional cualquier regla originada en GPT-Pro desde Actividad 1. [supuesto]"
  ],
  "structure_rules": [
    "Organizar cada producto con: problema, conceptos/fuentes/normas/doctrina, producto solicitado, analisis propio y conclusion juridica transferible.",
    "Alinear entregables a la planeacion semanal y al programa analitico local.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener consistencia entre README, plantilla .tex y archivo .bib.",
    "Corregir artefactos de estructura en README antes de publicar indices.",
    "Nombrar archivos con slug derecho-administrativo-y-control cuando aplique.",
    "Resolver tokens PowerShell sin expandir en README y programa analitico (p.ej. $(@{...}.Slug)) por el slug literal derecho-administrativo-y-control. [supuesto]",
    "Corregir nombres de archivo con saltos de linea o caracteres espurios en README (reporte-, referencias-). [supuesto]",
    "Tratar tokens PowerShell sin expandir como artefactos de generacion. [supuesto]"
  ],
  "activity_rules": [
    "Cada actividad debe incluir postura academica propia y criterio juridico transferible.",
    "Vincular el tema con control administrativo y practica profesional.",
    "Explicitar el producto solicitado (reporte, presentacion o visual) antes del desarrollo.",
    "No omitir conclusion final orientada a aplicacion juridica.",
    "Separar reglas editoriales generales de contenidos sustantivos heredados de otras materias.",
    "Estructurar productos con ejes: problema, conceptos/normas/doctrina, producto, analisis propio y conclusion transferible."
  ],
  "quality_gates": [
    "Revisar que la salida sea JSON parseable antes de aplicar memoria aguas abajo.",
    "Verificar integridad academica con citas verificables y sin fuentes inventadas.",
    "Confirmar trazabilidad entre afirmaciones y bibliografia local.",
    "Detener propagacion si hay respuesta no estructurada o campos criticos vacios.",
    "Validar que README y programa no conserven placeholders ni rutas corruptas antes de publicar indices.",
    "Revisar que reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX en espanol y formato letterpaper segun archivo base.",
    "Completar metadatos institucionales y de curso antes de compilar.",
    "Conservar tabla de datos academicos del estudiante y docente en portada.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar Actividad X por numero y nombre real de la actividad.",
    "Mantener coursecode LDE-S6B1 salvo evidencia institucional distinta.",
    "Sustituir 'Nombre por definir' por el nombre oficial de la figura docente antes de entregar."
  ],
  "bibliography_rules": [
    "Registrar fuentes de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales.",
    "Incluir datos minimos verificables: autor, titulo, anio, medio y nota de consulta.",
    "No inventar fuentes ni agregar referencias sin evidencia documental.",
    "Usar la malla curricular local como fuente de ubicacion curricular.",
    "Agregar fuentes especificas solo si fueron consultadas o proporcionadas.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de estructura JSON.",
    "Aplicar normalizacion manual cuando la fuente sea provisional.",
    "Mantener estrategia lossless por union-dedupe en fusiones futuras.",
    "Marcar conflictos de nomenclatura entre rutas antes de consolidar. [supuesto]",
    "Propagar a laterales solo reglas editoriales compartibles, no contenido especifico de actividad.",
    "Preservar alerta institucional sobre respuestas no estructuradas en niveles superiores.",
    "Conservar antecedente de ciclo 1 con normalizacion manual si se reutiliza.",
    "En ciclo 2, revisar que la deduplicacion no elimine reglas utiles previas."
  ],
  "open_questions": [
    "Definir fuente definitiva para reemplazar referencias provisionales de Codex y GPT-Pro.",
    "Confirmar nombre oficial de la figura docente en plantilla de reporte.",
    "Validar si existe formato institucional obligatorio de citas para la Licenciatura en Derecho.",
    "Confirmar convencion final del archivo de referencias (referencias-derecho-administrativo-y-control u otra).",
    "Verificar si el anio de consulta del sitio institucional UnADM debe mantenerse en 2026.",
    "Confirmar si los tokens PowerShell sin expandir en README/programa son artefacto de generacion a corregir. [supuesto]",
    "Corregir posibles artefactos de ruta o nombre en listado de estructura del README. [supuesto]"
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derecho-administrativo-y-control-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}
```