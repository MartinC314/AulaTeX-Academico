{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Consolidacion ciclo 2 completada con compresion union-dedupe sin perdida.",
    "Se mantiene validacion JSON parseable antes de cualquier propagacion.",
    "La herencia institucional previa fue provisional y ya normalizada para uso operativo.",
    "Se detectan nombres de archivo corruptos o con variables sin resolver en README y programa analitico. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista correccion institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instruccion de actividad o docente. [supuesto]",
    "Registrar fuentes provisionales como nota tecnica y no como autoridad academica."
  ],
  "structure_rules": [
    "Partir de un problema juridico o social claro.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Adaptar la salida al producto pedido: reporte, presentacion o visual.",
    "Incluir analisis propio antes del cierre.",
    "Cerrar con argumento transferible a la practica profesional.",
    "Usar el programa analitico como guia de ejes editoriales.",
    "Mantener README como entrada canonica de la asignatura."
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
    "Validar JSON parseable en toda memoria antes de aplicar propagacion.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmacion factual tenga fuente o marca de supuesto.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institucion.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Normalizar manualmente memorias heredadas si provienen de salida no parseable.",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Revisar posibles caracteres corruptos en README y plantilla antes de publicar. [supuesto]"
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar documentclass article con opciones spanish, letterpaper, oneside.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si el archivo existe. [supuesto]",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "No confiar en nombres generados con variables sin resolver en README o markdown."
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX especificas de actividad antes de citar.",
    "No inventar referencias; registrar solo fuentes consultadas y verificables.",
    "No citar bibliografia base si no fue usada en el argumento.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinamica."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales la regla de validar JSON parseable antes de fusionar memoria.",
    "Propagar arriba y laterales la regla de union-dedupe sin regresion.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales del programa analitico.",
    "Propagar la restriccion de no inventar fuentes.",
    "Propagar solo reglas generales; no propagar metadatos especificos de esta materia.",
    "Etiquetar como provisional cualquier fuente tecnica heredada de modelos."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar estilo de citacion juridica requerido por la asignatura (APA, Chicago, ISO 690 u otro).",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README (reporte/referencias) y validar rutas reales. [supuesto]",
    "Resolver variable sin compilar en nombres .bib dentro de README y programa analitico.",
    "Confirmar si la fuente provisional Codex debe conservarse solo como bitacora tecnica."
  ]
}