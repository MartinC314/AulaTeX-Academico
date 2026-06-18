{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "La carpeta de materia es punto de entrada canonico.",
    "Se exige integridad academica, citas verificables y conclusion juridica propia.",
    "El programa analitico define cinco ejes: problema, marco conceptual-normativo, producto, analisis propio y cierre transferible.",
    "Existe antecedente institucional de salida no JSON parseable; mantener control de normalizacion en ciclo 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en todo entregable.",
    "Alinear contenido a Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico claro y profesional.",
    "Conservar trazabilidad de origen cuando la fuente sea provisional. [supuesto]"
  ],
  "structure_rules": [
    "Organizar cada producto con: planteamiento del problema, desarrollo, analisis propio y conclusion.",
    "Mapear el contenido a los cinco ejes del programa analitico.",
    "Asegurar coherencia entre README, programa analitico, .tex y .bib de la materia.",
    "Registrar bibliografia especifica de actividad en el .bib local de la asignatura."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la planeacion semanal.",
    "Incluir postura academica propia con sustento juridico.",
    "Cerrar con conclusion aplicable a la practica juridica.",
    "Verificar que toda afirmacion relevante tenga respaldo en fuente verificable."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Comprobar consistencia curricular y editorial con documentos locales de la materia.",
    "Controlar normalizacion manual en ciclo 1 cuando haya reutilizacion lateral o superior."
  ],
  "latex_rules": [
    "Usar plantilla .tex de la materia como base de reportes.",
    "Mantener metadatos del documento consistentes con nombre de asignatura y actividad.",
    "Conservar compatibilidad con configuracion en espanol y formato academico institucional.",
    "Evitar cambios destructivos en estructura canonica de archivos .tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos curriculares locales cuando apliquen.",
    "Agregar entradas BibTeX especificas de actividad en el archivo .bib de la materia.",
    "Mantener datos minimos de trazabilidad: autor institucional, titulo, anio, medio y nota de consulta."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas estables y no contextuales.",
    "Preservar compresion por union-dedupe sin perdida.",
    "No eliminar reglas utiles previas; solo ampliar con mejoras verificables.",
    "Marcar supuestos explicitamente cuando falte evidencia directa."
  ],
  "open_questions": [
    "Confirmar si la regla de 'Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales' sigue vigente para Derecho. [supuesto]",
    "Definir formato estandar de conclusion juridica (extension y criterios de evaluacion).",
    "Corregir nombres de archivos con caracteres anomalos en README para evitar errores de automatizacion.",
    "Validar si existe guia oficial de citacion juridica preferente para esta asignatura (APA, Chicago juridico u otra)."
  ]
}