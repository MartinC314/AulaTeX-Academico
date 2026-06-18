{
  "summary": [
    "Memoria de actividad consolidada para Filosofía del Derecho con identidad UnADM.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Mantener normalización estructurada obligatoria antes de propagar.",
    "Ejes editoriales vigentes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Conservar alerta histórica de salidas no JSON parseable desde Codex para UnADM.",
    "Conservar alerta histórica de salida no JSON parseable desde GPT-Pro para Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho.",
    "Basar ubicación curricular en semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
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
    "No asumir que fuentes de semanas posteriores correspondan a actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
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
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 sobre interpretación jurídica."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclo 1 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 1.",
    "Confirmar producto exacto solicitado para actividad 1.",
    "Confirmar si la actividad requiere reporte, presentación u otro formato principal.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico del archivo .bib de la asignatura.",
    "Confirmar si actividad 1 reutiliza bibliografía existente o requiere .bib propio."
  ]
}