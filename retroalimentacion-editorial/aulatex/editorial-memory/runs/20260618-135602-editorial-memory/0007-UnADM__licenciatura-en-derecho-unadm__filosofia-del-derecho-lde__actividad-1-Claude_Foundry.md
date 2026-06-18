{
  "summary": [
    "Memoria de actividad consolidada para Filosofía del Derecho con identidad UnADM.",
    "Mantener normalización estructurada obligatoria antes de propagar.",
    "Ejes editoriales vigentes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Conservar alerta histórica de salidas no JSON parseable desde Codex para UnADM.",
    "Conservar alerta histórica de salida no JSON parseable desde GPT-Pro para Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna de actividad.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear la entrega al producto solicitado en la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas solo descriptivas o de resumen.",
    "No asumir que fuentes de semanas posteriores correspondan a actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto corresponda a la consigna de actividad 1.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo del README y programa analítico.",
    "Supuesto: archivo .bib canónico es filosofia-del-derecho.bib según token Slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 sobre interpretación jurídica.",
    "Conservar claves BibTeX originales del .bib tal como aparecen en el .tex."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "Ciclo 1 necesita normalización manual si se reutiliza."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si la actividad requiere reporte, presentación u otro formato principal.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico del archivo .bib de la asignatura.",
    "Confirmar si actividad 1 reutiliza el .bib de interpretación jurídica o requiere uno propio."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/filosofia-del-derecho-clean.bib"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}