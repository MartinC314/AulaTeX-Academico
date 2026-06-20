{
  "summary": [
    "Materia destino con identidad UnADM y enfoque jurídico aplicado.",
    "La carpeta de materia es punto de entrada canónico.",
    "Asignatura de Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Se exige integridad académica, citas verificables y conclusión jurídica propia.",
    "El programa analítico define cinco ejes: problema, marco conceptual-normativo, producto, análisis propio y cierre transferible.",
    "La compresión editorial debe ser por unión y deduplicación sin pérdida.",
    "Existe antecedente de salida no JSON parseable; mantener control de normalización en ciclo 1.",
    "Detectados nombres/rutas con caracteres anómalos en README que requieren normalización."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Alinear contenido a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 créditos.",
    "Enfocar la asignatura en instrumentos y mecanismos de protección de los derechos humanos.",
    "Usar tono académico-jurídico claro y profesional.",
    "Conservar trazabilidad de origen cuando la fuente sea provisional. [supuesto]",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales. [supuesto]",
    "Fuente provisional: Codex desde Actividad 1. [supuesto]",
    "Fuente provisional: Auto (model-router) desde Actividad 1. [supuesto]"
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Organizar cada producto con planteamiento del problema, desarrollo, análisis propio y conclusión.",
    "Mapear el contenido a los cinco ejes del programa analítico.",
    "Asegurar coherencia entre README, programa analítico, archivos .tex y archivo .bib de la materia.",
    "Verificar que la estructura listada en README coincida con los archivos reales.",
    "Corregir nombres de archivos con caracteres anómalos antes de automatizar.",
    "Registrar bibliografía específica de actividad en el .bib local de la asignatura."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeación semanal.",
    "Distinguir problema jurídico o social, conceptos clave, producto solicitado y cierre argumentativo.",
    "Incluir postura académica propia con sustento jurídico.",
    "Vincular el análisis con normas, doctrina, datos o fuentes pertinentes.",
    "Cerrar con conclusión aplicable a la práctica jurídica.",
    "Verificar que toda afirmación relevante tenga respaldo en fuente verificable."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Comprobar consistencia curricular y editorial con documentos locales de la materia.",
    "Controlar normalización manual en ciclo 1 cuando haya reutilización lateral o superior.",
    "Confirmar que no se eliminen reglas útiles previas.",
    "Aplicar deduplicación sin recorte semántico.",
    "No incorporar fuentes no verificadas.",
    "Validar rutas y nombres reales de archivos antes de compilar o referenciar."
  ],
  "latex_rules": [
    "Usar plantilla .tex de la materia como base de reportes.",
    "Mantener metadatos del documento consistentes con nombre de asignatura y actividad.",
    "Actualizar título, subtítulo, materia y actividad antes de entregar.",
    "Conservar compatibilidad con configuración en español y formato académico institucional.",
    "Evitar cambios destructivos en estructura canónica de archivos .tex.",
    "Revisar que las rutas BibTeX apunten al archivo local real.",
    "No propagar marcadores de plantilla sin resolver."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Usar la malla curricular de Derecho solo como fuente curricular cuando corresponda.",
    "Diferenciar bibliografía base de bibliografía específica de actividad.",
    "Agregar entradas BibTeX específicas de actividad en el archivo .bib de la materia.",
    "Mantener datos mínimos de trazabilidad: autor institucional, título, año, medio y nota de consulta.",
    "Validar si la fuente citada respalda directamente la afirmación usada."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas estables y no contextuales.",
    "Preservar compresión por unión-dedupe sin pérdida.",
    "No eliminar reglas útiles previas; solo ampliar con mejoras verificables.",
    "Marcar supuestos explícitamente cuando falte evidencia directa.",
    "Mantener alerta de normalización en ciclo 1.",
    "Propagar la regla de JSON parseable a memorias UnADM relacionadas.",
    "Propagar la revisión de nombres anómalos solo donde existan archivos afectados.",
    "Ciclo 1 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si la regla de fuente provisional desde ingeniería-en-sistemas-computacionales sigue vigente para Derecho. [supuesto]",
    "Definir formato estándar de conclusión jurídica: extensión y criterios de evaluación.",
    "Validar si existe guía oficial de citación jurídica preferente para esta asignatura: APA, Chicago jurídico u otra.",
    "Confirmar la planeación semanal específica antes de crear actividades.",
    "Verificar si existen fuentes oficiales adicionales para instrumentos y mecanismos de protección de derechos humanos.",
    "Confirmar el nombre correcto de archivos con prefijos truncados en README (ej. 'eporte', 'eferencias')."
  ]
}