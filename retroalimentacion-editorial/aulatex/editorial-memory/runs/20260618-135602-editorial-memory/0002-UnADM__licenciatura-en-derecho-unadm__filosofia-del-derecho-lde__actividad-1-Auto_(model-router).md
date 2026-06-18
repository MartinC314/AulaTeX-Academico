{
  "summary": [
    "Memoria base de actividad para Filosofía del Derecho con identidad UnADM.",
    "Conservar normalización estructurada antes de propagar reglas.",
    "Ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Aplicar compresión lossless por unión y deduplicación."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho.",
    "Basar ubicación curricular en semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar la fuente heredada Codex como provisional hasta verificarla."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado en la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores corresponden a actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar respuesta no estructurada antes de reutilizarla.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto corresponda a la consigna de actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a actividad 1.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo después de validar JSON y estructura.",
    "Reutilizar reglas de calidad institucional heredadas en ciclo 1.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 1.",
    "Confirmar producto exacto solicitado para actividad 1.",
    "Confirmar si la actividad requiere reporte, presentación u otro formato principal.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico del archivo .bib de la asignatura."
  ]
}