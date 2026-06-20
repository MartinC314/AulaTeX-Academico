{
  "summary": [
    "Memoria consolidada para actividad-1 con contrato de compilacion, citacion y estructura academica.",
    "Se preserva herencia institucional UCNL y normalizacion local verificable.",
    "Contrato de compilacion confirmado segun COMPILACION.md.",
    "Control de TEXINPUTS, BIBINPUTS y BSTINPUTS verificado.",
    "Criterios de citacion con natbib y estructura academica minima fijados.",
    "Salida sin JSON parseable desde Codex para UCNL [supuesto heredado].",
    "Salida sin JSON parseable desde GPT-Pro para Actividad 1 [supuesto].",
    "Compresion aplicada por union-dedupe sin perdida.",
    "Propagacion ascendente en ciclo 2 con verificacion previa."
  ],
  "identity_rules": [
    "Mantener alcance UCNL y ruta exacta del destino.",
    "Usar etiqueta de curso: administracion-de-calidad-lad.",
    "Registrar fuente local: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad/actividad-1.",
    "Codigo de curso: ADM-CAL; tetramestre 9.",
    "Conservar fuente provisional Codex desde ingenieria-en-sistemas-computacionales [supuesto heredado].",
    "Conservar fuente provisional GPT-Pro desde Actividad 1 [supuesto]."
  ],
  "structure_rules": [
    "Ejecutar la compilacion desde la raiz del proyecto.",
    "Usar scripts/latexmk-build.ps1 con un unico argumento: ruta del .tex.",
    "Compilar: reporte-administracion-de-calidad.tex, reporte-administracion-de-calidad-Actividad-1.tex y presentacion-administracion-de-calidad.tex.",
    "No pasar \\input{template} como argumento al script.",
    "No pasar el .bib como argumento al script.",
    "Mantener el PDF final en la misma carpeta del .tex.",
    "Mantener auxiliares en .build/latex y .build/latex/aux.",
    "\\input{template} debe resolver a base/Plantilla-Informe/template.tex via TEXINPUTS.",
    "BibTeX debe ubicar administracion-de-calidad.bib via BIBINPUTS.",
    "El estilo atnumurl.bst debe resolverse via BSTINPUTS.",
    "Definir TEXINPUTS, BIBINPUTS y BSTINPUTS en .latexmkrc."
  ],
  "activity_rules": [
    "Mantener el formato del reporte de la materia al crear actividades nuevas.",
    "Responder exactamente a la actividad solicitada en la planeacion.",
    "Usar la planeacion como lista de cumplimiento; no pegar instrucciones completas.",
    "Revisar bibliografia indicada, tomar notas y registrar citas antes de redactar.",
    "Redactar con comprension propia y cumplimiento explicito.",
    "Construir el producto academico solicitado dentro del documento cuando sea posible.",
    "Duplicar la plantilla maestra y renombrar por materia, semana y actividad.",
    "Actualizar documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universitydepartment.",
    "En reportes, declarar \\bibliography{administracion-de-calidad}.",
    "Exigir que toda clave citada exista en administracion-de-calidad.bib.",
    "Entregar en PDF con la nomenclatura indicada en el aula."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar resolucion de template por TEXINPUTS hacia base/Plantilla-Informe/template.tex.",
    "Verificar resolucion del .bib por BIBINPUTS.",
    "Verificar resolucion de atnumurl.bst por BSTINPUTS.",
    "Confirmar que no existan citas sin entrada BibTeX.",
    "Exigir compilacion sin errores ni advertencias de citas o referencias.",
    "Confirmar que el PDF final se genere en la carpeta de la actividad.",
    "Confirmar existencia de los tres archivos de entrada .tex indicados.",
    "Confirmar que .latexmkrc defina TEXINPUTS, BIBINPUTS y BSTINPUTS."
  ],
  "latex_rules": [
    "Usar natbib con citas autor-anio: \\citep{clave} y \\citet{clave}.",
    "Mantener interlineado 1.5 y estilo institucional indicado en la plantilla.",
    "Usar fuente tipo Helvetica o equivalente visual a Arial.",
    "Incluir estructura academica minima: caratula, resumen breve, desarrollo, producto, conclusion y bibliografia.",
    "Compilar la actividad con reporte-administracion-de-calidad-Actividad-1.tex.",
    "Aplicar formato APA 7 en cuerpo y referencias [supuesto por plantilla].",
    "Redaccion academica clara, coherente, cohesionada, formal y sin faltas.",
    "Ajustar variables coverwatermark para gestionar la marca de agua institucional."
  ],
  "bibliography_rules": [
    "Usar archivo canonico: administracion-de-calidad.bib.",
    "Registrar en el .bib todas las fuentes usadas por reportes y actividades de esta carpeta.",
    "No inventar fuentes ni claves bibliograficas.",
    "Mantener consistencia exacta entre claves citadas y entradas existentes.",
    "Evitar duplicados de entradas en el .bib.",
    "Entrada confirmada disponible: unadm100TecnicasDidacticas2023.",
    "Agregar entradas faltantes al .bib antes de compilar."
  ],
  "propagation_hints": [
    "Propagar en sentido ascendente solo reglas verificadas localmente.",
    "Conservar compresion union-dedupe sin eliminar reglas utiles previas.",
    "Mantener visible la referencia de fuente local al propagar.",
    "Marcar y revisar supuestos antes de promover a niveles superiores.",
    "Ciclo 1 requiere normalizacion manual si se reutiliza [trazabilidad].",
    "Ciclo 2: normalizar y promover a nivel curso si supera los quality gates.",
    "Registrar cambios respecto al contrato de compilacion al propagar."
  ],
  "open_questions": [
    "Confirmar si la plantilla maestra de Actividad-1 esta completa; el archivo visible parece truncado [supuesto].",
    "Confirmar guia definitiva de estilo APA 7 en salida final, dado uso de atnumurl.bst [supuesto].",
    "Confirmar si la regla heredada de fuente provisional (Codex/GPT-Pro) sigue vigente para este curso [supuesto].",
    "Confirmar que base/Plantilla-Informe/template.tex coincide con TEXINPUTS activo en .latexmkrc [supuesto].",
    "Confirmar en el repositorio los nombres exactos de los tres .tex de entrada segun COMPILACION.md [supuesto].",
    "Confirmar que la plantilla habilita natbib con opciones autor-anio por defecto [supuesto]."
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