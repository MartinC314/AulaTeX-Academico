{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Consolidacion ciclo 2 desde Filosofia del Derecho Actividad 1 y memoria institucional heredada.",
    "Usar compresion por union-dedupe sin perdida y sin regresion.",
    "Validar toda memoria como JSON parseable antes de propagar.",
    "La herencia institucional previa fue no estructurada y ya normalizada para uso operativo.",
    "Salidas heredadas sin JSON parseable provienen de Codex y GPT-Pro; requieren validacion previa.",
    "Fuentes institucionales heredadas marcadas como provisionales desde Codex e ingenieria-en-sistemas-computacionales.",
    "Ciclos 1 y 2 de consolidacion completados para esta materia destino.",
    "Existen nombres de archivo corruptos o con variables sin resolver en README y programa analitico. [supuesto]",
    "README declara estructura con prefijos truncados (eporte, eferencias) por variables sin resolver. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Usar macros de portada: documenttitle, coursename, coursecode, universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista correccion institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instruccion de actividad o docente. [supuesto]",
    "Registrar Codex y GPT-Pro como fuentes tecnicas provisionales, no como autoridad academica.",
    "Registrar fuentes provisionales como nota tecnica y no como autoridad academica."
  ],
  "structure_rules": [
    "Mantener README como entrada canonica de la asignatura.",
    "Usar el programa analitico como guia de ejes editoriales.",
    "Partir de un problema juridico o social claro.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes al caso.",
    "Adaptar la salida al producto pedido: reporte, presentacion o visual.",
    "Incluir analisis propio antes del cierre.",
    "Cerrar con argumento transferible a la practica profesional.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, analisis propio y conclusion transferible."
  ],
  "activity_rules": [
    "Verificar la instruccion especifica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analitico.",
    "Exigir conclusion juridica con criterio propio en cada entrega.",
    "Integrar evidencia verificable y citas trazables en el cuerpo del trabajo.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final.",
    "No citar fuentes que no se usen en el argumento.",
    "No reutilizar reglas laterales sin comprobar pertinencia juridica.",
    "Relacionar etapas procesales y estrategia de litigio cuando la actividad lo requiera."
  ],
  "quality_gates": [
    "Validar JSON parseable en cualquier memoria antes de aplicar propagacion.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmacion factual tenga fuente o marca de supuesto.",
    "Confirmar ausencia de contradicciones con reglas heredadas de nivel institucion.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Normalizar manualmente memorias heredadas si provienen de salida no parseable.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Confirmar existencia real de archivos mencionados en README antes de enlazarlos.",
    "Compilar LaTeX antes de publicar entregables finales."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "Mantener compatibilidad con espanol y formato letterpaper definido en plantilla.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si el archivo existe. [supuesto]",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Usar nombres reales de archivos despues de corregir rutas corruptas. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar fuentes institucionales ya registradas: sitio UnADM y malla curricular Derecho 2024.",
    "No inventar referencias; registrar solo fuentes consultadas y verificables.",
    "Agregar entradas BibTeX especificas de actividad antes de citar.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinamica.",
    "No citar bibliografia base si no fue usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales la validacion de JSON parseable antes de fusionar memoria.",
    "Propagar arriba y laterales la regla de union-dedupe sin regresion.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales del programa analitico.",
    "Propagar a materias vecinas de Derecho los ejes: problema, fundamento, analisis propio y conclusion juridica.",
    "Propagar la restriccion de no inventar fuentes.",
    "Propagar la revision de respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Propagar la advertencia de normalizacion manual para memorias de ciclo 1.",
    "Propagar la revision de variables sin resolver en READMEs generados.",
    "Propagar solo reglas generales; no propagar metadatos especificos de esta materia.",
    "Etiquetar como provisional cualquier fuente tecnica heredada de modelos."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar estilo de citacion juridica requerido: APA, Chicago, ISO 690 u otro.",
    "Revisar y corregir posibles caracteres corruptos en README y plantilla .tex. [supuesto]",
    "Corregir nombres corruptos en README (reporte/referencias) y validar rutas reales. [supuesto]",
    "Resolver variable sin compilar en nombres .bib dentro de README y programa analitico.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Confirmar codigo de curso correcto: README no lo declara pero plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como bitacora tecnica.",
    "Definir checklist minimo por tipo de producto: reporte, presentacion y material visual."
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