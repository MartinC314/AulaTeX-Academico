{
  "summary": [
    "Se conserva identidad UnADM y enfoque juridico de la materia destino.",
    "Se mantiene normalizacion manual previa para herencias de ciclo 1.",
    "Se consolida compresion lossless por union-dedupe sin recortes.",
    "Se detectan placeholders y nombres truncados en README y programa analitico.",
    "Se mantiene exigencia de citas verificables y conclusion juridica propia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Conservar tono academico-juridico con postura propia sustentada.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Usar codigo de curso LDE-S8B2 en metadatos del reporte.",
    "Fijar autor Martin Jonathan de la Cruz y matricula ES2611202040 en front matter.",
    "Marcar como [supuesto] todo dato institucional no confirmado.",
    "Mantener fuente heredada como provisional hasta validacion manual."
  ],
  "structure_rules": [
    "Organizar cada actividad en problema, conceptos y fuentes, producto, analisis propio y conclusion.",
    "Mantener consistencia entre README, programa analitico, reporte, presentacion y archivo .bib local.",
    "Transformar la planeacion semanal en entregables concretos.",
    "Incluir cierre argumentativo transferible a la practica juridica.",
    "Corregir placeholders de plantillas en nombres de archivo y referencias.",
    "Resolver expresiones tipo $(@{...}.Slug) a nombres literales finales.",
    "Restaurar nombres truncados en estructura (reporte, referencias) antes de entrega."
  ],
  "activity_rules": [
    "Traducir la consigna semanal al producto concreto solicitado.",
    "Incluir analisis juridico propio y evitar solo resumen de fuentes.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "Cerrar cada actividad con conclusion aplicable a la practica juridica.",
    "No trasladar contenido especifico de otra materia sin fuente verificable."
  ],
  "quality_gates": [
    "Validar que toda salida de memoria sea JSON parseable.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizar.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar ausencia de placeholders visibles en README, .tex y .bib.",
    "Comprobar coherencia de datos de portada con la materia destino.",
    "Verificar que no queden plantillas PowerShell sin evaluar.",
    "Confirmar coherencia de nombres de archivo entre documentos y carpeta real.",
    "Revisar respuestas no estructuradas antes de propagarlas aguas abajo."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia con metadatos institucionales.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como base del reporte.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar.",
    "Reemplazar 'Actividad X' por el identificador real.",
    "Completar campos pendientes del front matter solo con datos confirmados.",
    "Mantener compatibilidad de nombres entre .tex y recursos asociados.",
    "Completar figura docente y creditos solo cuando exista confirmacion."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "No inventar referencias; marcar [supuesto] si falta dato verificable.",
    "Agregar entradas BibTeX solo con metadatos comprobables.",
    "Mantener trazabilidad entre citas en texto y claves BibTeX.",
    "Reutilizar claves base unadmSitioWeb y unadmMallaDerecho2024.",
    "Verificar y actualizar fecha de consulta del sitio UnADM antes de entrega.",
    "[supuesto] Validar si el year 2026 en unadmSitioWeb corresponde a consulta y no a publicacion."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y sin ambiguedad.",
    "Propagar reglas transversales de integridad academica en ecosistema UnADM.",
    "No propagar datos incompletos de creditos o figura docente.",
    "Mantener etiqueta de herencia provisional hasta revision manual.",
    "Propagar leccion transversal de corregir placeholders y nombres truncados.",
    "Aplicar union-dedupe para consolidar sin perdida de reglas utiles."
  ],
  "open_questions": [
    "[supuesto] Confirmar fuentes concretas de Actividad 1 de Filosofia del Derecho para extraer reglas especificas reutilizables.",
    "[supuesto] Confirmar creditos oficiales de Electiva Semestre 8 Bloque 2.",
    "[supuesto] Confirmar nombre oficial de figura docente para front matter.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc del sitio UnADM."
  ]
}