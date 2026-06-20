{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Consolidacion ciclo 7 desde Filosofia del Derecho Actividad 1 y memoria institucional heredada.",
    "Ciclos 1, 2, 3, 4, 5, 6 y 7 de consolidacion completados para esta materia destino.",
    "Aplicar compresion por union-dedupe sin perdida y sin regresion.",
    "Validar JSON parseable antes de cualquier propagacion.",
    "Salidas heredadas sin JSON parseable provienen de Codex, GPT-Pro, Auto y Claude Foundry; requieren validacion previa.",
    "La herencia no estructurada fue normalizada para uso operativo.",
    "Se detectan nombres y rutas con variables sin resolver en README y programa analitico. [supuesto]",
    "README muestra prefijos truncados en nombres de archivo (eporte, eferencias). [supuesto]",
    "Se detecta posible truncamiento de plantilla LaTeX en bloque authortable. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista correccion institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instruccion de actividad o docente. [supuesto]",
    "Registrar Codex, GPT-Pro, Auto y Claude Foundry como fuentes tecnicas provisionales, no como autoridad academica.",
    "Fuente provisional institucional: Codex desde ingenieria-en-sistemas-computacionales."
  ],
  "structure_rules": [
    "Mantener README como entrada canonica de la asignatura.",
    "Usar el programa analitico como guia editorial.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, analisis propio y conclusion transferible.",
    "Partir de un problema juridico o social claro.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes.",
    "Adaptar la salida al producto pedido: reporte, presentacion o visual.",
    "Incluir analisis propio antes del cierre.",
    "Cerrar con argumento transferible a la practica profesional."
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
    "Validar JSON parseable en toda memoria antes de aplicar propagacion.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Comprobar union-dedupe sin eliminar reglas utiles previas.",
    "Comprobar que cada afirmacion factual tenga fuente o marca de supuesto.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institucion.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Confirmar existencia real de archivos mencionados en README antes de enlazarlos.",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Revisar posibles caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Compilar LaTeX antes de publicar entregables finales.",
    "Normalizar manualmente memorias heredadas si provienen de salida no parseable."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar documentclass article con opciones spanish, letterpaper y oneside.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "Mantener compatibilidad con espanol y formato letterpaper definido en plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Reparar la plantilla si el bloque authortable quedo truncado antes de reutilizarla. [supuesto]",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si el archivo existe. [supuesto]",
    "No confiar en nombres generados con variables sin resolver en README o markdown.",
    "Usar nombres reales de archivos despues de corregir rutas corruptas. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Agregar entradas BibTeX especificas de actividad antes de citar.",
    "No inventar referencias; registrar solo fuentes consultadas y verificables.",
    "No citar bibliografia base si no fue usada en el argumento.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar fuentes institucionales ya registradas: sitio UnADM y malla curricular Derecho.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinamica."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales la validacion de JSON parseable antes de fusionar memoria.",
    "Propagar arriba y laterales la regla de union-dedupe sin regresion.",
    "Propagar la revision de respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Propagar la restriccion de no inventar fuentes.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales del programa analitico.",
    "Propagar la revision de variables sin resolver en READMEs generados.",
    "Propagar la advertencia de normalizacion manual para memorias heredadas no parseables.",
    "Propagar solo reglas generales; no propagar metadatos especificos de esta materia.",
    "Etiquetar como provisional cualquier fuente tecnica heredada de modelos.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza.",
    "Ciclo 2 necesita normalizacion manual si se reutiliza.",
    "Ciclo 3 necesita normalizacion manual si se reutiliza.",
    "Ciclo 4 necesita normalizacion manual si se reutiliza.",
    "Ciclo 5 necesita normalizacion manual si se reutiliza.",
    "Ciclo 6 necesita normalizacion manual si se reutiliza.",
    "Ciclo 7 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar estilo de citacion juridica requerido por la asignatura (APA, Chicago, ISO 690 u otro).",
    "Confirmar codigo de curso correcto: README no lo declara y plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Corregir nombres corruptos en README (reporte/referencias) y validar rutas reales. [supuesto]",
    "Resolver variable sin compilar en nombres .bib dentro de README y programa analitico. [supuesto]",
    "Verificar integridad del archivo reporte-etapas-del-proceso-y-estrategia-del-litigio.tex por posible truncamiento. [supuesto]",
    "Confirmar si Codex debe conservarse solo como bitacora tecnica provisional."
  ]
}