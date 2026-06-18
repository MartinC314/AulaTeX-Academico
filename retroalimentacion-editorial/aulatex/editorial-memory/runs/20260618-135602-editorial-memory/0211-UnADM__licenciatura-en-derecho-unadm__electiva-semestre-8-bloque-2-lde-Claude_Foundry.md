{
  "summary": [
    "Base institucional UnADM disponible, pero la herencia previa indica salida no JSON en origen historico.",
    "Aplicar normalizacion manual en ciclo 1 antes de propagar cambios derivados.",
    "La materia destino exige identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
    "Consolidar identidad UnADM para la materia Electiva Semestre 8 Bloque 2.",
    "Mantener enfoque de Licenciatura en Derecho con argumentacion juridica propia.",
    "Tratar la herencia Codex previa como provisional hasta revision manual.",
    "Usar compresion por union-dedupe sin recortar reglas utiles.",
    "El alumno confirmado es Martin Jonathan de la Cruz, matricula ES2611202040."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Conservar tono academico-juridico con postura propia sustentada.",
    "Identificar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] cualquier dato institucional no confirmado.",
    "Usar codigo de curso LDE-S8B2 en metadatos del reporte.",
    "Fijar autor y matricula confirmados en el front matter del reporte."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Organizar cada actividad en problema, conceptos/fuentes, producto, analisis propio y conclusion.",
    "Mantener consistencia entre README, programa analitico, reporte, presentacion y .bib local.",
    "Transformar la planeacion semanal en entregables concretos.",
    "Incluir un cierre argumentativo transferible a la practica juridica.",
    "Corregir rutas o nombres generados con placeholders antes de entrega.",
    "Resolver expresiones tipo $(@{...}.Slug) a nombres de archivo literales en README y programa.",
    "Restaurar primera letra de nombres de archivo truncados (eporte, eferencias) en listados."
  ],
  "activity_rules": [
    "Traducir la planeacion semanal a producto concreto solicitado por la actividad.",
    "Incluir analisis juridico propio, no solo resumen de fuentes.",
    "Cerrar cada actividad con conclusion aplicable a la practica juridica.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "No trasladar contenido especifico de Filosofia del Derecho sin fuente verificable."
  ],
  "quality_gates": [
    "Validar que toda salida sea JSON parseable antes de consolidar memoria.",
    "Revisar manualmente artefactos heredados de ciclo 1 antes de reutilizacion.",
    "Verificar trazabilidad entre afirmaciones y fuentes citadas.",
    "Confirmar que no existan placeholders visibles en README, .tex o .bib.",
    "Revisar respuesta no estructurada previa antes de aplicarla aguas abajo.",
    "Comprobar que los datos de portada coincidan con la materia destino.",
    "Verificar que no queden plantillas PowerShell sin evaluar en archivos finales.",
    "Confirmar nombres de archivo coherentes entre README, programa y carpeta real."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX base de la materia y sus metadatos institucionales.",
    "Completar campos pendientes del front matter antes de entrega final.",
    "Mantener compatibilidad de nombres de archivos entre .tex y recursos de la materia.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex como plantilla base del reporte.",
    "Actualizar titulo, subtitulo y actividad antes de compilar.",
    "Completar figura docente y creditos solo con datos confirmados.",
    "Corregir nombres de archivo mal renderizados en listados de estructura.",
    "Reemplazar Actividad X por el numero real de actividad antes de compilar.",
    "Completar campo Creditos en authortable cuando el dato este confirmado."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando correspondan.",
    "No inventar referencias; marcar [supuesto] cuando falte dato verificable.",
    "Conservar la malla curricular de Derecho como fuente institucional local.",
    "Agregar entradas BibTeX solo si existe dato bibliografico verificable.",
    "Mantener trazabilidad entre citas del texto y claves BibTeX.",
    "Reutilizar claves unadmSitioWeb y unadmMallaDerecho2024 como base institucional.",
    "Verificar fecha de consulta del sitio UnADM antes de entrega."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas validadas y sin ambiguedad.",
    "Etiquetar reglas heredadas de calidad como transversales de institucion UnADM.",
    "Mantener compresion por union-dedupe sin eliminar reglas utiles previas.",
    "Propagar reglas de integridad academica a materias UnADM compatibles.",
    "No propagar datos incompletos de creditos o figura docente.",
    "Usar ciclo 1 como etapa de normalizacion, no como evidencia definitiva.",
    "Propagar regla de resolver plantillas PowerShell como leccion transversal de generacion."
  ],
  "open_questions": [
    "[supuesto] Confirmar fuentes concretas de la actividad 1 de Filosofia del Derecho para reglas mas especificas.",
    "[supuesto] Definir creditos oficiales de la materia para completar metadatos.",
    "[supuesto] Confirmar nombre de figura docente para plantilla de reporte.",
    "[supuesto] Confirmar si la electiva tiene nombre oficial distinto a Electiva Semestre 8 Bloque 2.",
    "[supuesto] Verificar si el sitio institucional UnADM debe citarse con fecha de consulta actualizada.",
    "[supuesto] Confirmar si el ano 2026 del sitio UnADM en .bib es correcto o placeholder."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/electiva-semestre-8-bloque-2-lde"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}