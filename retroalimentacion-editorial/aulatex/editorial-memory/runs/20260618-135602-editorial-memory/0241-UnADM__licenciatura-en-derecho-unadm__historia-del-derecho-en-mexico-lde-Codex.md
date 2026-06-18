{
  "summary": [
    "Materia con plantilla base LaTeX, programa analitico y .bib local disponibles.",
    "Se conserva alerta previa: hubo salida no JSON parseable en ciclo anterior.",
    "Se agrega memoria estructural verificable desde README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada, metadatos y redaccion.",
    "Usar nombre oficial de materia: Historia del Derecho en Mexico.",
    "Conservar datos curriculares: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Fuente provisional vigente: Codex para consolidacion de memoria [supuesto]."
  ],
  "structure_rules": [
    "Tratar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada entrega a los 5 ejes: problema, conceptos/fuentes, producto, analisis propio, conclusion transferible.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Registrar fuentes especificas de actividad en historia-del-derecho-en-mexico.bib."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social concreto.",
    "Desarrollar analisis propio con postura academica explicita.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Adaptar formato de salida al producto solicitado (reporte, presentacion o visual)."
  ],
  "quality_gates": [
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar JSON parseable en cada ciclo de memoria.",
    "Verificar consistencia entre datos curriculares y portada del documento.",
    "Comprobar que toda afirmacion sustantiva tenga soporte verificable."
  ],
  "latex_rules": [
    "Usar la plantilla reporte-historia-del-derecho-en-mexico.tex como base editable.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, coursename y coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y creditos.",
    "No eliminar campos institucionales; solo actualizar valores concretos por actividad."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Conservar entradas institucionales existentes de UnADM y malla curricular.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Incluir trazabilidad minima en notas de referencia (origen y fecha de consulta cuando aplique)."
  ],
  "propagation_hints": [
    "Propagar a nivel superior y lateral reglas de validacion JSON y normalizacion temprana.",
    "Reutilizar en materias hermanas la estructura de 5 ejes con ajuste tematico.",
    "Priorizar deduplicacion por union sin recorte de reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar si 'Fuente provisional: Codex' debe reemplazarse por fuente operativa definitiva.",
    "Definir nombre oficial de figura docente para plantillas de actividades.",
    "Verificar y corregir posibles errores de render en listado de archivos del README [supuesto]."
  ]
}