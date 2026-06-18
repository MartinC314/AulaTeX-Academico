{
  "summary": [
    "Materia destino con base editorial verificable en README, programa analitico, plantilla LaTeX y .bib local.",
    "Se mantiene alerta historica: hubo salidas no JSON parseables en ciclos previos [supuesto: motor variable].",
    "Origen declarado: Filosofia del Derecho actividad 1, sin reglas nuevas verificables transferibles en este contexto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre oficial local: Historia del Derecho en Mexico.",
    "Conservar datos curriculares: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Marcar como supuesto toda fuente operativa no confirmada."
  ],
  "structure_rules": [
    "Tratar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega a cinco ejes: problema, conceptos y fuentes, producto, analisis propio, conclusion transferible.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Registrar fuentes especificas de actividad en historia-del-derecho-en-mexico.bib.",
    "Transformar planeacion semanal en reportes, presentaciones o productos visuales segun se solicite.",
    "No mezclar contenido de Filosofia del Derecho sin evidencia local verificable.",
    "Conservar subcarpeta referencias-historia-del-derecho-en-mexico para apoyo documental."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social concreto.",
    "Usar conceptos, normas, doctrina o datos pertinentes al problema.",
    "Desarrollar analisis propio con postura academica explicita.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Adaptar el formato al producto solicitado: reporte, presentacion o visual.",
    "Mantener integridad academica y citas verificables en cada actividad."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada ciclo de memoria.",
    "Revisar respuesta no estructurada antes de propagar aguas abajo.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Comprobar que toda afirmacion sustantiva tenga soporte verificable.",
    "Aplicar compresion union-dedupe sin recortar reglas utiles previas.",
    "Normalizar manualmente salidas de ciclo 1 antes de reutilizacion automatica.",
    "Revisar render de nombres de archivo en README antes de automatizar."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base editable para reportes.",
    "Usar presentacion-historia-del-derecho-en-mexico.tex para productos tipo presentacion.",
    "Conservar metadatos: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener campos institucionales; solo actualizar valores concretos por actividad.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "Mantener coursecode local LDE-S1B1 salvo confirmacion oficial contraria [supuesto]."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Conservar entradas institucionales de UnADM y malla curricular.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Corregir placeholders de Slug en README y programa antes de compilar o citar.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas editoriales transversales verificables.",
    "Propagar validacion JSON y normalizacion temprana a materias hermanas.",
    "Reutilizar la estructura de cinco ejes con ajuste tematico por asignatura.",
    "Mantener alerta de salidas no parseables en niveles superiores.",
    "No propagar datos curriculares especificos de esta materia a laterales."
  ],
  "open_questions": [
    "Confirmar fuente operativa definitiva para consolidacion de memoria.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local.",
    "Validar acentuacion oficial de Mexico/México segun lineamiento institucional.",
    "Corregir entradas con salto de linea anomalo en README (eporte, eferencias) [supuesto de render].",
    "Aportar contenido verificable de Filosofia del Derecho actividad 1 si se requiere fusion tematica."
  ]
}