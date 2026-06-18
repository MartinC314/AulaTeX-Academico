{
  "summary": [
    "Consolidar identidad UnADM para Electiva Semestre 8 Bloque 2.",
    "Mantener enfoque de Licenciatura en Derecho con argumentación jurídica propia.",
    "Usar compresión lossless por unión-dedupe.",
    "El alumno confirmado es Martin Jonathan de la Cruz, matrícula ES2611202040.",
    "La materia exige integridad académica, citas verificables y conclusión jurídica propia.",
    "La herencia previa incluye salidas no JSON parseables desde Codex y GPT-Pro.",
    "Tratar herencias de ciclo 1 como provisionales hasta revisión manual.",
    "El contexto local contiene placeholders, nombres truncados y plantillas PowerShell sin resolver.",
    "No trasladar contenido específico de Filosofía del Derecho sin fuente verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redacción.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar código de curso LDE-S8B2 en metadatos.",
    "Fijar autor Martin Jonathan de la Cruz en front matter.",
    "Fijar matrícula ES2611202040 en front matter.",
    "Conservar tono académico-jurídico con postura propia sustentada.",
    "Marcar como [supuesto] cualquier dato institucional no confirmado.",
    "Registrar fuentes heredadas Codex y GPT-Pro como provisionales hasta validación manual."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Organizar cada actividad en problema, conceptos y fuentes, producto, análisis propio y conclusión.",
    "Mantener consistencia entre README, programa analítico, reporte, presentación y archivo .bib local.",
    "Transformar la planeación semanal en entregables concretos.",
    "Incluir cierre argumentativo transferible a la práctica jurídica.",
    "Corregir rutas y nombres generados con placeholders antes de entrega.",
    "Resolver expresiones tipo $(@{...}.Slug) a nombres literales finales.",
    "Restaurar nombres truncados en estructura, como reporte y referencias.",
    "Confirmar que los listados coincidan con archivos y carpetas reales."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Incluir análisis jurídico propio, no solo resumen de fuentes.",
    "Vincular conceptos, normas, doctrina o datos con el problema jurídico tratado.",
    "Cerrar cada actividad con conclusión aplicable a la práctica jurídica.",
    "Evitar contenido de otra materia sin fuente verificable.",
    "Adecuar cualquier regla heredada al contexto de la electiva destino."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable.",
    "Revisar respuestas no estructuradas antes de propagarlas aguas abajo.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizarlos.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar ausencia de placeholders visibles en README, .tex y .bib.",
    "Comprobar coherencia de datos de portada con la materia destino.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar coherencia de nombres de archivo entre README, programa y carpeta real.",
    "Reemplazar valores genéricos como Actividad X antes de entrega.",
    "Validar que figura docente y créditos no se completen sin confirmación."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia con metadatos institucionales.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar título, subtítulo y número real de actividad antes de compilar.",
    "Reemplazar 'Actividad X' por el identificador real.",
    "Completar campos pendientes del front matter solo con datos confirmados.",
    "Mantener compatibilidad de nombres entre .tex y recursos asociados.",
    "Completar figura docente solo cuando exista confirmación.",
    "Completar créditos en authortable solo con dato oficial confirmado.",
    "Corregir nombres de archivo mal renderizados en listados de estructura."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "No inventar referencias.",
    "Marcar como [supuesto] cualquier dato bibliográfico no verificable.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Mantener trazabilidad entre citas en texto y claves BibTeX.",
    "Reutilizar claves base unadmSitioWeb y unadmMallaDerecho2024.",
    "Verificar y actualizar fecha de consulta del sitio UnADM antes de entrega.",
    "[supuesto] Validar si el year 2026 en unadmSitioWeb corresponde a consulta y no a publicación."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas y sin ambigüedad.",
    "Etiquetar reglas de calidad como transversales de institución UnADM.",
    "Propagar reglas de integridad académica a materias UnADM compatibles.",
    "No propagar datos incompletos de créditos o figura docente.",
    "Usar ciclo 1 como etapa de normalización, no como evidencia definitiva.",
    "Mantener etiqueta de herencia provisional hasta revisión manual.",
    "Propagar la regla de corregir placeholders y nombres truncados como lección transversal.",
    "Propagar la regla de resolver plantillas PowerShell como lección transversal de generación.",
    "Aplicar unión-dedupe para consolidar sin pérdida de reglas útiles."
  ],
  "open_questions": [
    "[supuesto] Confirmar fuentes concretas de Actividad 1 de Filosofía del Derecho para extraer reglas específicas reutilizables.",
    "[supuesto] Definir créditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente para front matter.",
    "[supuesto] Confirmar si la electiva tiene nombre oficial distinto a Electiva Semestre 8 Bloque 2.",
    "[supuesto] Verificar si el sitio institucional UnADM debe citarse con fecha de consulta actualizada.",
    "[supuesto] Confirmar si el año 2026 del sitio UnADM en .bib es correcto o placeholder.",
    "[supuesto] Confirmar política institucional para year y fecha de consulta en @misc del sitio UnADM."
  ]
}