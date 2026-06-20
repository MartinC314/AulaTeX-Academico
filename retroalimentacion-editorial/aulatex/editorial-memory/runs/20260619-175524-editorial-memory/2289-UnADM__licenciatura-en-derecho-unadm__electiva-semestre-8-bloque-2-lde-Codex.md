{
  "summary": [
    "Se conserva identidad UnADM y enfoque juridico de la materia destino.",
    "Ciclo 1 mantiene normalizacion manual obligatoria antes de reutilizar herencias.",
    "Compresion aplicable: union-dedupe lossless sin recortar reglas utiles.",
    "Persisten hallazgos locales de placeholders y nombres truncados en README y programa analitico.",
    "La materia exige integridad academica, citas verificables y conclusion juridica propia.",
    "El alumno confirmado es Martin Jonathan de la Cruz, matricula ES2611202040.",
    "No trasladar contenido especifico de Filosofia del Derecho sin fuente verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar codigo de curso LDE-S8B2 en metadatos.",
    "Fijar autor Martin Jonathan de la Cruz y matricula ES2611202040 en front matter.",
    "Conservar tono academico-juridico con postura propia sustentada.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato institucional no confirmado.",
    "Registrar fuentes heredadas como provisionales hasta validacion manual."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Organizar cada actividad en problema, conceptos y fuentes, producto, analisis propio y conclusion.",
    "Mantener consistencia entre README, programa analitico, reporte, presentacion y archivo .bib local.",
    "Transformar la planeacion semanal en entregables concretos.",
    "Incluir cierre argumentativo transferible a la practica juridica.",
    "Corregir placeholders en rutas, nombres de archivo y referencias antes de entrega.",
    "Resolver expresiones tipo $(@{...}.Slug) a nombres literales finales.",
    "Restaurar nombres truncados en estructura, como reporte y referencias.",
    "Confirmar que los listados coincidan con archivos y carpetas reales."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Incluir analisis juridico propio y evitar solo resumen de fuentes.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "Cerrar cada actividad con conclusion aplicable a la practica juridica.",
    "No trasladar contenido especifico de otra materia sin fuente verificable.",
    "Adecuar cualquier regla heredada al contexto de la electiva destino."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable antes de consolidar.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizarlos.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar ausencia de placeholders visibles en README, .tex y .bib.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar coherencia de nombres de archivo entre README, programa y carpeta real.",
    "Comprobar coherencia de datos de portada con la materia destino.",
    "Reemplazar valores genericos como Actividad X antes de entrega.",
    "Validar que figura docente y creditos no se completen sin confirmacion."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia con metadatos institucionales.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Reemplazar 'Actividad X' por el identificador real antes de compilar.",
    "Completar campos pendientes del front matter solo con datos confirmados.",
    "Completar figura docente solo cuando exista confirmacion.",
    "Completar creditos en authortable solo con dato oficial confirmado.",
    "Mantener compatibilidad de nombres entre .tex y recursos asociados."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "Reutilizar claves base unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Mantener trazabilidad entre citas en texto y claves BibTeX.",
    "No inventar referencias.",
    "Marcar como [supuesto] cualquier dato bibliografico no verificable.",
    "Verificar y actualizar fecha de consulta del sitio UnADM antes de entrega.",
    "[supuesto] Validar si el year 2026 en unadmSitioWeb corresponde a consulta y no a publicacion."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas y sin ambiguedad.",
    "Etiquetar reglas de calidad como transversales de institucion UnADM.",
    "Propagar reglas de integridad academica a materias UnADM compatibles.",
    "No propagar datos incompletos de creditos o figura docente.",
    "Mantener etiqueta de herencia provisional hasta revision manual.",
    "Usar ciclo 1 como etapa de normalizacion, no como evidencia definitiva.",
    "Propagar la regla de corregir placeholders y nombres truncados como leccion transversal.",
    "Propagar la regla de resolver plantillas PowerShell como leccion transversal de generacion.",
    "Aplicar union-dedupe para consolidar sin perdida de reglas utiles."
  ],
  "open_questions": [
    "[supuesto] Confirmar fuentes concretas de Actividad 1 de Filosofia del Derecho para extraer reglas especificas reutilizables.",
    "[supuesto] Confirmar creditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente para front matter y plantilla.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc del sitio UnADM.",
    "[supuesto] Confirmar si el year 2026 del sitio UnADM en .bib es correcto o placeholder."
  ]
}