{
  "summary": [
    "Memoria inicial creada para actividad-1 con reglas de compilacion y citacion del curso.",
    "Se conserva herencia institucional y se agrega normalizacion local verificable."
  ],
  "identity_rules": [
    "Mantener alcance UCNL y ruta exacta del destino.",
    "Usar etiqueta de curso: administracion-de-calidad-lad.",
    "Conservar regla heredada: fuente provisional Codex desde ingenieria-en-sistemas-computacionales [supuesto heredado]."
  ],
  "structure_rules": [
    "Ejecutar compilacion desde la raiz del proyecto.",
    "Usar el script latexmk-build.ps1 con un unico argumento: ruta del .tex.",
    "No pasar \\input{template} como argumento al script.",
    "No pasar el .bib como argumento al script.",
    "Mantener salida PDF en la misma carpeta del .tex.",
    "Mantener auxiliares en .build/latex y .build/latex/aux."
  ],
  "activity_rules": [
    "Mantener el formato del reporte de la materia al crear actividades nuevas.",
    "En reportes, declarar \\bibliography{administracion-de-calidad}.",
    "Toda clave citada debe existir en administracion-de-calidad.bib.",
    "No pegar instrucciones completas de planeacion dentro del producto final.",
    "Redactar con comprension propia y cumplimiento explicito de la actividad solicitada."
  ],
  "quality_gates": [
    "Validar que la respuesta sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar resolucion de template por TEXINPUTS.",
    "Verificar resolucion de .bib por BIBINPUTS.",
    "Verificar resolucion de atnumurl.bst por BSTINPUTS.",
    "Confirmar que no existan citas sin entrada BibTeX."
  ],
  "latex_rules": [
    "Usar natbib con citas autor-anio: \\citep{clave} y \\citet{clave}.",
    "Mantener interlineado 1.5 y estilo institucional indicado en plantilla.",
    "Incluir estructura academica minima: caratula, resumen breve, desarrollo, producto, conclusion, bibliografia.",
    "Compilar reporte de actividad con el archivo reporte-administracion-de-calidad-Actividad-1.tex."
  ],
  "bibliography_rules": [
    "Usar archivo canonico: administracion-de-calidad.bib.",
    "Registrar en .bib todas las fuentes usadas por reportes y actividades de la carpeta.",
    "No inventar fuentes ni claves bibliograficas.",
    "Mantener consistencia entre claves citadas y entradas existentes."
  ],
  "propagation_hints": [
    "Propagar en sentido ascendente solo reglas verificadas localmente.",
    "Conservar compresion union-dedupe sin eliminar reglas utiles previas.",
    "Ciclo 1 requiere normalizacion manual si se reutiliza en otros nodos."
  ],
  "open_questions": [
    "Confirmar si la plantilla maestra de Actividad-1 esta completa; el archivo visible parece truncado [supuesto].",
    "Confirmar guia definitiva de estilo APA 7 en salida final, dado uso de atnumurl.bst [supuesto].",
    "Confirmar si la regla heredada de fuente provisional sigue vigente para este curso [supuesto]."
  ]
}