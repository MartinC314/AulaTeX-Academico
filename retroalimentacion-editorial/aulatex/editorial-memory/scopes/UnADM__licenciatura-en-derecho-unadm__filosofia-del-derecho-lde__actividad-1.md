# Memoria editorial AulaTeX

- Alcance: actividad
- Etiqueta: Actividad 1
- Ruta: UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde
- Compresion: union-dedupe
- Sin regresion: si

## summary

- Se crea memoria base de actividad para Filosofía del Derecho con identidad UnADM.
- Se conserva regla institucional de no propagar salidas no estructuradas sin normalización.
- Se fijan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.
- Memoria base de actividad para Filosofía del Derecho con identidad UnADM.
- Conservar normalización estructurada antes de propagar reglas.
- Ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.
- Aplicar compresión lossless por unión y deduplicación.
- Salida sin JSON parseable heredada desde Codex para UnADM; requiere normalización.
- Salida sin JSON parseable desde GPT-Pro para Actividad 1
- Memoria de actividad consolidada para Filosofía del Derecho con identidad UnADM.
- Se mantiene normalización estructurada obligatoria antes de propagar.
- Ejes editoriales vigentes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.
- Se confirma compresión lossless por unión y deduplicación.
- Se conserva alerta histórica de salidas no JSON parseable como control de calidad.
- Mantener normalización estructurada obligatoria antes de propagar.
- Conservar alerta histórica de salidas no JSON parseable desde Codex para UnADM.
- Conservar alerta histórica de salida no JSON parseable desde GPT-Pro para Actividad 1.

## identity_rules

- Mantener identidad institucional UnADM en tono y formato.
- Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.
- Usar la carpeta de asignatura como punto de entrada canónico.
- Marcar como supuesto cualquier dato no visible en la consigna de la actividad.
- Vincular la actividad a Licenciatura en Derecho.
- Basar ubicación curricular en semestre 1, bloque 2, obligatoria, 8 créditos.
- Marcar como supuesto cualquier dato no visible en la consigna.
- Tratar la fuente heredada Codex como provisional hasta verificarla.
- Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.
- Fuente provisional: GPT-Pro desde Actividad 1
- Marcar como supuesto cualquier dato no visible en la consigna de actividad.
- Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.
- Fuente provisional: Codex desde ingeniería-en-sistemas-computacionales.
- Fuente provisional: GPT-Pro desde Actividad 1.

## structure_rules

- Iniciar con encuadre breve del problema jurídico o social.
- Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.
- Cerrar con conclusión jurídica transferible a la práctica profesional.
- Alinear la entrega al producto solicitado en la planeación semanal.
- Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.
- Transformar la planeación en reporte, presentación o producto visual según consigna.

## activity_rules

- Definir objetivo puntual de la actividad antes del desarrollo.
- Sustentar afirmaciones con fuentes verificables y cita explícita.
- Incluir postura argumentada del estudiante, no solo resumen descriptivo.
- Verificar coherencia entre pregunta guía, desarrollo y conclusión.
- Incluir postura argumentada del estudiante.
- Evitar entregas solo descriptivas o de resumen.
- No asumir que fuentes de semanas posteriores corresponden a actividad 1.
- No asumir que fuentes de semanas posteriores correspondan a actividad 1.

## quality_gates

- Bloquear propagación si la salida no es JSON parseable.
- Revisar estructura mínima completa antes de aplicar aguas abajo.
- Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.
- Validar consistencia entre citas en texto y archivo .bib.
- Revisar respuesta no estructurada antes de reutilizarla.
- Verificar que el producto corresponda a la consigna de actividad 1.
- Revisar respuesta no estructurada antes de aplicar aguas abajo.
- Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.

## latex_rules

- Usar codificación y acentos correctos en español en .tex y .bib.
- Mantener claves BibTeX estables para evitar recompilaciones rotas.
- Evitar comandos no estándar sin justificación editorial.
- Compilar sin errores críticos y sin referencias rotas.
- Verificar nombres de archivos del README antes de referenciarlos.
- Corregir caracteres anómalos en rutas o nombres antes de compilar.
- Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo del README.
- Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo.
- Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo del README y programa analítico.
- Supuesto: archivo .bib canónico es filosofia-del-derecho.bib según token Slug del README.

## bibliography_rules

- Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.
- Registrar fuentes específicas de la actividad en el .bib de la asignatura.
- No inventar referencias; usar solo obras realmente consultables.
- Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.
- No inventar referencias.
- Usar solo obras realmente consultables.
- Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.
- No asumir que filosofia-del-derecho-clean.bib corresponde a actividad 1.
- Distinguir bibliografía base de bibliografía específica de actividad.
- Supuesto: filosofia-del-derecho-clean.bib referencia Semana 7 (interpretación jurídica), no actividad 1.
- Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.
- Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 (interpretación jurídica).
- Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 sobre interpretación jurídica.
- Conservar claves BibTeX originales del .bib tal como aparecen en el .tex.

## propagation_hints

- Propagar arriba y laterales solo después de validación de JSON y estructura.
- Reutilizar reglas de calidad institucional heredadas en ciclo 1.
- Aplicar normalización manual si se detecta salida no estructurada en nodos vecinos.
- Propagar arriba y laterales solo después de validar JSON y estructura.
- Evitar regresiones respecto de reglas útiles previas.
- Propagar solo reglas generales cuando falte consigna textual.
- Ciclo 1 necesita normalizacion manual si se reutiliza.
- Reutilizar reglas institucionales de calidad sin reducir especificidad local.
- Ciclo 1 necesita normalización manual si se reutiliza.
- Ciclo 2 necesita normalizacion manual si se reutiliza.

## open_questions

- Supuesto: falta consigna textual de 'actividad-1'; confirmar producto exacto solicitado.
- Confirmar si la actividad requiere reporte, presentación u otro formato principal.
- Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.
- Supuesto: falta consigna textual de actividad 1.
- Confirmar producto exacto solicitado para actividad 1.
- Confirmar rúbrica de evaluación específica.
- Confirmar fuentes obligatorias de la semana correspondiente.
- Confirmar nombre canónico del archivo .bib de la asignatura.
- Confirmar si actividad 1 reutiliza el .bib de interpretación jurídica o requiere uno propio.
- Supuesto: falta consigna textual de actividad 1; confirmar producto exacto solicitado.
- Confirmar si actividad 1 reutiliza bibliografía existente o requiere .bib propio.
