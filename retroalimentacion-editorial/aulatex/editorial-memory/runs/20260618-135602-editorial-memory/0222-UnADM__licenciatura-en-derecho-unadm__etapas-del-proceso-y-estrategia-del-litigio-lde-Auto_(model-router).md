{
  "summary": [
    "Materia destino con identidad UnADM y enfoque jurídico aplicado.",
    "Consolidación ciclo 2 desde Filosofía del Derecho Actividad 1 y memoria institucional heredada.",
    "Usar compresión por union-dedupe sin pérdida y sin regresión.",
    "Validar toda memoria como JSON parseable antes de propagar.",
    "La herencia institucional previa fue provisional y ya normalizada para uso operativo.",
    "La herencia previa incluyó salidas no estructuradas desde Codex y GPT-Pro.",
    "Existen nombres de archivo corruptos o con variables sin resolver en README y programa analítico. [supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar ubicación curricular: semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Usar tono académico-jurídico formal con postura propia sustentada.",
    "Conservar trazabilidad de origen editorial al consolidar memoria.",
    "Usar macros de portada: documenttitle, coursename, coursecode y universityname.",
    "Usar coursecode LDE-S5B2 mientras no exista corrección institucional. [supuesto]",
    "Mantener autor de plantilla Martin Jonathan de la Cruz salvo instrucción de actividad o docente. [supuesto]",
    "Registrar Codex y GPT-Pro como fuentes técnicas provisionales, no como autoridad académica."
  ],
  "structure_rules": [
    "Mantener README como entrada canónica de la asignatura.",
    "Usar el programa analítico como guía de ejes editoriales.",
    "Partir de un problema jurídico o social claro.",
    "Desarrollar conceptos, normas, doctrina o datos pertinentes.",
    "Adaptar la salida al producto pedido: reporte, presentación o visual.",
    "Incluir análisis propio antes del cierre.",
    "Cerrar con argumento transferible a la práctica profesional.",
    "Seguir cinco ejes: problema, conceptos, producto solicitado, análisis propio y conclusión transferible."
  ],
  "activity_rules": [
    "Verificar la instrucción específica de cada actividad antes de redactar.",
    "Rubricar cada entrega contra los ejes del programa analítico.",
    "Exigir conclusión jurídica con criterio propio en cada entrega.",
    "Integrar evidencia verificable y citas trazables en el cuerpo del trabajo.",
    "Agregar fuentes específicas de actividad al .bib local antes de la versión final.",
    "No citar fuentes que no se usen en el argumento.",
    "No reutilizar reglas laterales sin comprobar pertinencia jurídica.",
    "Relacionar etapas procesales y estrategia de litigio cuando la actividad lo requiera."
  ],
  "quality_gates": [
    "Validar JSON parseable en cualquier memoria antes de aplicar propagación.",
    "Comprobar union-dedupe sin eliminar reglas útiles previas.",
    "Revisar consistencia entre metadatos de materia y contenido entregado.",
    "Comprobar que cada afirmación factual tenga fuente o marca de supuesto.",
    "Confirmar ausencia de contradicciones con reglas heredadas de institución.",
    "Normalizar manualmente memorias heredadas si provienen de salida no parseable.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Revisar caracteres corruptos en README y plantilla antes de publicar. [supuesto]",
    "Validar que nombres de archivos en README no contengan variables sin resolver.",
    "Confirmar existencia real de archivos mencionados en README antes de enlazarlos.",
    "Compilar LaTeX antes de publicar entregables finales."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base de nuevas actividades.",
    "Usar reporte-etapas-del-proceso-y-estrategia-del-litigio.tex para reportes.",
    "Usar presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex para presentaciones si el archivo existe. [supuesto]",
    "Usar documentclass article con opciones spanish, letterpaper y oneside.",
    "Conservar macros institucionales de curso, universidad y asignatura.",
    "No eliminar campos de portada; completar faltantes según actividad.",
    "Conservar bloque authortable de la plantilla al adaptar portada.",
    "Mantener compatibilidad con español y formato letterpaper definido en plantilla.",
    "No confiar en nombres generados con variables sin resolver en README o Markdown.",
    "Usar nombres reales de archivos después de corregir rutas corruptas. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local.",
    "Conservar fuentes institucionales ya registradas: sitio UnADM y malla curricular Derecho 2024.",
    "Conservar claves BibTeX unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX específicas de actividad antes de citar.",
    "No inventar referencias; registrar solo fuentes consultadas y verificables.",
    "Incluir fecha de consulta cuando la fuente sea web o institucional dinámica.",
    "No citar bibliografía base si no fue usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales la validación de JSON parseable antes de fusionar memoria.",
    "Propagar arriba y laterales la regla de union-dedupe sin regresión.",
    "Propagar a materias vecinas de Derecho los cinco ejes editoriales del programa analítico.",
    "Propagar la restricción de no inventar fuentes.",
    "Propagar la revisión de respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Propagar la advertencia de normalización manual para memorias de ciclo 1.",
    "Propagar la revisión de variables sin resolver en READMEs generados.",
    "Propagar solo reglas generales; no propagar metadatos específicos de esta materia.",
    "Etiquetar como provisional cualquier fuente técnica heredada de modelos."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante.",
    "Confirmar estilo de citación jurídica requerido: APA, Chicago, ISO 690 u otro.",
    "Corregir nombres corruptos en README y validar rutas reales. [supuesto]",
    "Resolver variable sin compilar en nombres .bib dentro de README y programa analítico.",
    "Confirmar existencia operativa de presentacion-etapas-del-proceso-y-estrategia-del-litigio.tex. [supuesto]",
    "Confirmar código de curso correcto: README no lo declara pero plantilla usa LDE-S5B2. [supuesto]",
    "Confirmar si la fuente provisional Codex debe conservarse solo como bitácora técnica.",
    "Definir checklist mínimo por tipo de producto: reporte, presentación y material visual."
  ]
}