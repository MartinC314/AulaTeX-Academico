{
  "summary": [
    "Memoria inicial creada para actividad-1 con reglas de compilacion y citacion del curso.",
    "Se conserva herencia institucional y se agrega normalizacion local verificable.",
    "Contrato de compilacion confirmado segun COMPILACION.md.",
    "Criterios de citacion con natbib y estructura academica minima fijados.",
    "Control de TEXINPUTS, BIBINPUTS y BSTINPUTS verificado.",
    "Salida sin JSON parseable desde Codex para UCNL [supuesto heredado]."
  ],
  "identity_rules": [
    "Mantener alcance UCNL y ruta exacta del destino.",
    "Usar etiqueta de curso: administracion-de-calidad-lad.",
    "Conservar regla heredada: fuente provisional Codex desde ingenieria-en-sistemas-computacionales [supuesto heredado].",
    "Registrar fuente local de referencia: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad/actividad-1.",
    "Codigo de curso: ADM-CAL; tetramestre 9."
  ],
  "structure_rules": [
    "Ejecutar compilacion desde la raiz del proyecto.",
    "Usar el script latexmk-build.ps1 con un unico argumento: ruta del .tex.",
    "No pasar \\input{template} como argumento al script.",
    "No pasar el .bib como argumento al script.",
    "Mantener salida PDF en la misma carpeta del .tex.",
    "Mantener auxiliares en .build/latex y .build/latex/aux.",
    "\\input{template} debe resolver a base/Plantilla-Informe/template.tex via TEXINPUTS.",
    "BibTeX debe ubicar administracion-de-calidad.bib via BIBINPUTS.",
    "El estilo atnumurl.bst debe resolverse via BSTINPUTS.",
    "TEXINPUTS y rutas se definen en .latexmkrc.",
    "Existen tres .tex en la carpeta: reporte, reporte-Actividad-1 y presentacion."
  ],
  "activity_rules": [
    "Mantener el formato del reporte de la materia al crear actividades nuevas.",
    "En reportes, declarar \\bibliography{administracion-de-calidad}.",
    "Toda clave citada debe existir en administracion-de-calidad.bib.",
    "No pegar instrucciones completas de planeacion dentro del producto final.",
    "Redactar con comprension propia y cumplimiento explicito de la actividad solicitada.",
    "Responder exactamente a la actividad solicitada en la planeacion.",
    "Usar la planeacion como lista de cumplimiento; no pegar instrucciones completas.",
    "Construir el producto academico solicitado dentro del documento cuando sea posible.",
    "Duplicar la plantilla maestra y renombrar por materia, semana y actividad.",
    "Actualizar documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universitydepartment.",
    "Identificar conceptos, elementos, criterios o categorias solicitados.",
    "Entregar en PDF con la nomenclatura indicada en el aula.",
    "Revisar bibliografia indicada, tomar notas y registrar citas antes de redactar."
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
    "Mantener interlineado 1.5 y estilo institucional indicado en plantilla.",
    "Incluir estructura academica minima: caratula, resumen breve, desarrollo, producto, conclusion, bibliografia.",
    "Compilar reporte de actividad con reporte-administracion-de-calidad-Actividad-1.tex.",
    "Usar fuente tipo Helvetica o equivalente visual a Arial.",
    "Usar formato APA 7 en cuerpo y referencias.",
    "Redaccion academica clara, coherente, cohesionada, formal y sin faltas.",
    "Ajustar variables coverwatermark... para apagar o cambiar la marca de agua institucional."
  ],
  "bibliography_rules": [
    "Usar archivo canonico: administracion-de-calidad.bib.",
    "Registrar en .bib todas las fuentes usadas por reportes y actividades de la carpeta.",
    "No inventar fuentes ni claves bibliograficas.",
    "Mantener consistencia exacta entre claves citadas y entradas existentes.",
    "Evitar duplicados de entradas en el .bib.",
    "Entrada disponible confirmada: unadm100TecnicasDidacticas2023."
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
  ],
  "sources": [
    "UCNL/licenciatura-en-administracion/administracion-de-calidad-lad/actividad-1"
  ],
  "locked_sections": [],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}