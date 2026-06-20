{
  "summary": [
    "Memoria inicial creada para actividad-1 con reglas de compilacion y citacion del curso.",
    "Se conserva herencia institucional y se agrega normalizacion local verificable.",
    "Contrato de compilacion confirmado segun COMPILACION.md.",
    "Criterios de citacion con natbib y estructura academica minima fijados.",
    "Control de TEXINPUTS, BIBINPUTS y BSTINPUTS verificado."
  ],
  "identity_rules": [
    "Mantener alcance UCNL y ruta exacta del destino.",
    "Usar etiqueta de curso: administracion-de-calidad-lad.",
    "Conservar regla heredada: fuente provisional Codex desde ingenieria-en-sistemas-computacionales [supuesto heredado].",
    "Registrar fuente local de referencia: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad/actividad-1."
  ],
  "structure_rules": [
    "Ejecutar compilacion desde la raiz del proyecto.",
    "Usar el script latexmk-build.ps1 con un unico argumento: ruta del .tex.",
    "No pasar \\input{template} como argumento al script.",
    "\\input{template} debe resolver a base/Plantilla-Informe/template.tex via TEXINPUTS.",
    "No pasar el .bib como argumento al script.",
    "BibTeX debe ubicar administracion-de-calidad.bib via BIBINPUTS.",
    "El estilo atnumurl.bst debe resolverse via BSTINPUTS.",
    "Mantener salida PDF en la misma carpeta del .tex.",
    "Mantener auxiliares en .build/latex y .build/latex/aux."
  ],
  "activity_rules": [
    "Mantener el formato del reporte de la materia al crear actividades nuevas.",
    "Responder exactamente a la actividad solicitada en la planeacion.",
    "Usar la planeacion como lista de cumplimiento; no pegar instrucciones completas.",
    "Redactar con comprension propia y cumplimiento explicito.",
    "Construir el producto academico solicitado dentro del documento cuando sea posible.",
    "En reportes, declarar \\bibliography{administracion-de-calidad}.",
    "Toda clave citada debe existir en administracion-de-calidad.bib."
  ],
  "quality_gates": [
    "Validar que la respuesta sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar resolucion de template por TEXINPUTS.",
    "Verificar resolucion de .bib por BIBINPUTS.",
    "Verificar resolucion de atnumurl.bst por BSTINPUTS.",
    "Confirmar que no existan citas sin entrada BibTeX.",
    "Compilacion limpia sin errores ni advertencias de referencias o citas.",
    "Confirmar que el PDF final se genera en la carpeta de la actividad."
  ],
  "latex_rules": [
    "Usar natbib con citas autor-anio: \\citep{clave} y \\citet{clave}.",
    "Mantener interlineado 1.5 y estilo institucional indicado en la plantilla.",
    "Usar fuente tipo Helvetica o equivalente visual a Arial.",
    "Incluir estructura academica minima: caratula, resumen breve, desarrollo, producto, conclusion, bibliografia.",
    "Compilar el reporte de la actividad con reporte-administracion-de-calidad-Actividad-1.tex."
  ],
  "bibliography_rules": [
    "Usar archivo canonico: administracion-de-calidad.bib.",
    "Registrar en el .bib todas las fuentes usadas por reportes y actividades de esta carpeta.",
    "No inventar fuentes ni claves bibliograficas.",
    "Mantener consistencia exacta entre claves citadas y entradas existentes.",
    "Evitar duplicados de entradas en el .bib."
  ],
  "propagation_hints": [
    "Propagar en sentido ascendente solo reglas verificadas localmente.",
    "Conservar compresion union-dedupe sin eliminar reglas utiles previas.",
    "Ciclo 1 requiere normalizacion manual si se reutiliza en otros nodos.",
    "Mantener visible la referencia de fuente local al propagar."
  ],
  "open_questions": [
    "Confirmar si la plantilla maestra de Actividad-1 esta completa; el archivo visible parece truncado [supuesto].",
    "Confirmar guia definitiva de estilo APA 7 en salida final, dado uso de atnumurl.bst [supuesto].",
    "Confirmar si la regla heredada de fuente provisional sigue vigente para este curso [supuesto].",
    "Confirmar que la ruta base/Plantilla-Informe/template.tex coincide con TEXINPUTS activo [supuesto]."
  ]
}