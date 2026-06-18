{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Consolidacion desde actividad origen y memoria institucional heredada.",
    "Usar compresion por union-dedupe sin perdida y sin regresion.",
    "Validar toda memoria como JSON parseable antes de propagar.",
    "La herencia institucional previa fue no estructurada y requiere normalizacion manual.",
    "Fuente institucional heredada marcada como provisional desde Codex e ingenieria-en-sistemas-computacionales.",
    "Ciclo 1 de consolidacion completado para esta materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial cuando se consolide memoria.",
    "Usar macros de portada: documenttitle, coursename, coursecode LDE-S5B2, universityname.",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo indicacion contraria. [supuesto]"
  ],
  "structure_rules": [
    "Partir de un problema juridico o social claro.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Incluir analisis propio antes del cierre.",
    "Cerrar con argumento transferible a la practica profesional.",
    "Adaptar la salida al producto pedido: reporte, presentacion o visual.",
    "Mantener README como entrada canonica de la asignatura.",
    "Usar el programa analitico como guia de ejes editoriales.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, analisis propio, conclusion transferible."
  ],
  "activity_rules": [
    "Verificar la instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analitico.",
    "Exigir conclusion juridica con criterio propio en cada entrega.",
    "Integrar evidencia verificable y citas trazables en el cuerpo del trabajo.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final.",
    "No reutilizar reglas laterales sin comprobar pertinencia juridica."
  ],
  "quality_gates": [
    "Validar JSON parseable en cualquier memoria antes de aplicar propagacion.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmacion factual tenga fuente o marca de supuesto.",
    "Confirmar ausencia de contradicciones con reglas heredadas de nivel institucion.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Normalizar manualmente memorias del ciclo 1 cuando provengan de salida no parseable.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos en README no contengan variables sin resolver."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "Mantener compatibilidad con espanol y formato letterpaper definido en plantilla.",
    "No eliminar campos de portada; completar los faltantes segun actividad.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si existe en carpeta. [supuesto]",
    "No confiar en nombres generados con variables sin resolver en README.",
    "Usar documentclass article con opciones spanish, letterpaper, oneside.",
    "Conservar bloque authortable de la plantilla al adaptar portada."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales ya registradas: sitio UnADM y malla curricular Derecho 2024.",
    "No inventar referencias; registrar solo fuentes consultadas y verificables.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinamica.",
    "Agregar entradas BibTeX especificas de actividad antes de citar.",
    "No citar bibliografia base si no fue usada en el argumento.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales reglas de validacion JSON y control de no regresion.",
    "Propagar a materias vecinas de Derecho los ejes: problema, fundamento, analisis propio y conclusion juridica.",
    "Marcar que la herencia inicial fue provisional y ya normalizada para ciclo 1.",
    "Propagar la advertencia de normalizacion manual para ciclo 1.",
    "Propagar la restriccion de no inventar fuentes.",
    "Propagar solo reglas generales; mantener metadatos especificos en la materia destino."
  ],
  "open_questions": [
    "Confirmar si el nombre de autor en plantilla es definitivo o variable por estudiante.",
    "Confirmar estilo de citacion juridica requerido: APA, Chicago, ISO 690 u otro.",
    "Revisar y corregir posibles caracteres corruptos en README y plantilla .tex. [supuesto]",
    "Definir checklist minimo por tipo de producto: reporte, presentacion y material visual.",
    "Corregir nombres corruptos en README y validar nombres reales de archivos. [supuesto]",
    "Confirmar existencia y plantilla de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como nota tecnica.",
    "Confirmar codigo de curso correcto: README no lo declara pero plantilla usa LDE-S5B2. [supuesto]"
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/etapas-del-proceso-y-estrategia-del-litigio-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}