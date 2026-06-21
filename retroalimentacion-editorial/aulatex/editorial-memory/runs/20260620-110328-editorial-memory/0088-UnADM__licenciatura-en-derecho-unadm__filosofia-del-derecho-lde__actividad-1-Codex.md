{
  "summary": [
    "Memoria local consolidada de Actividad 1 para Filosofía del Derecho con identidad UnADM.",
    "Normalización estructurada en JSON es obligatoria antes de cualquier propagación.",
    "Compresión lossless aplicada por unión y deduplicación sin recorte.",
    "Se preservan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se conserva control histórico de salidas no JSON parseable como puerta de calidad.",
    "README y programa analítico contienen tokens Slug sin expandir; deben resolverse.",
    "Supuesto: el .bib canónico esperado por Slug es filosofia-del-derecho.bib.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7 (interpretación jurídica) y no a Actividad 1.",
    "Se confirma artefacto principal local: reporte-filosofia-del-derecho-Actividad-1.tex.",
    "Se confirma contexto de Actividad Semana 2 con enfoque de mapa conceptual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna de Actividad 1.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Mantener claves BibTeX estables y originales.",
    "Conservar claves BibTeX del .bib tal como aparecen en el .tex.",
    "Supuesto: archivo .bib canónico esperado por Slug es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Conservar claves BibTeX del .bib tal como aparecen en el .tex.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica) y no a Actividad 1."
  ],
  "propagation_hints": [
    "Propagación local: aplicar cambios solo en la actividad actual.",
    "Propagar solo después de validar JSON y estructura.",
    "Propagar reglas generales cuando falte consigna textual.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Mantener validación estricta de parseo JSON antes de cualquier propagación.",
    "Ciclos previos con salidas no estructuradas requieren normalización manual si se reutilizan."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar producto exacto solicitado.",
    "Confirmar si el formato exigido final es reporte, presentación o mapa conceptual.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura.",
    "Confirmar si Actividad 1 reutiliza bibliografía existente o requiere .bib propio."
  ]
}