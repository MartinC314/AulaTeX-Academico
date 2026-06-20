{
  "summary": [
    "Memoria consolidada para actividad-1 con contrato de compilacion, citacion y estructura academica.",
    "Se preserva herencia institucional UCNL y normalizacion local verificable.",
    "Compresion aplicada por union-dedupe sin perdida.",
    "Persisten antecedentes de salida no JSON parseable como trazabilidad [supuesto heredado]."
  ],
  "identity_rules": [
    "Mantener alcance UCNL y ruta exacta del destino.",
    "Usar etiqueta de curso administracion-de-calidad-lad.",
    "Registrar fuente local: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad/actividad-1.",
    "Mantener codigo de curso ADM-CAL y tetramestre 9.",
    "Conservar fuente provisional Codex desde ingenieria-en-sistemas-computacionales [supuesto heredado].",
    "Conservar fuente provisional GPT-Pro desde Actividad 1 [supuesto]."
  ],
  "structure_rules": [
    "Ejecutar compilacion desde la raiz del proyecto.",
    "Usar scripts/latexmk-build.ps1 con un unico argumento: ruta del .tex.",
    "No pasar \\input{template} como argumento.",
    "No pasar el .bib como argumento.",
    "Mantener salida PDF en la misma carpeta del .tex.",
    "Mantener auxiliares en .build/latex y .build/latex/aux.",
    "Resolver \\input{template} por TEXINPUTS hacia base/Plantilla-Informe/template.tex.",
    "Resolver administracion-de-calidad.bib por BIBINPUTS.",
    "Resolver atnumurl.bst por BSTINPUTS.",
    "Definir TEXINPUTS, BIBINPUTS y BSTINPUTS en .latexmkrc.",
    "Reconocer tres .tex de trabajo en la carpeta: reporte, reporte-Actividad-1 y presentacion."
  ],
  "activity_rules": [
    "Mantener formato del reporte de la materia al crear actividades.",
    "Declarar \\bibliography{administracion-de-calidad} en reportes.",
    "Exigir que toda clave citada exista en administracion-de-calidad.bib.",
    "No pegar instrucciones completas de planeacion en el producto final.",
    "Usar la planeacion como lista de cumplimiento.",
    "Redactar con comprension propia y cumplimiento explicito de la actividad.",
    "Responder exactamente a lo solicitado en la actividad.",
    "Construir el producto academico solicitado dentro del documento cuando sea posible.",
    "Duplicar plantilla maestra y renombrar por materia, semana y actividad.",
    "Actualizar documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universitydepartment.",
    "Identificar conceptos, elementos, criterios o categorias solicitados.",
    "Entregar PDF con nomenclatura indicada en el aula.",
    "Revisar bibliografia indicada, tomar notas y registrar citas antes de redactar."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Verificar resolucion de template por TEXINPUTS.",
    "Verificar resolucion de .bib por BIBINPUTS.",
    "Verificar resolucion de atnumurl.bst por BSTINPUTS.",
    "Confirmar que no existan citas sin entrada BibTeX.",
    "Exigir compilacion sin errores ni advertencias de citas o referencias.",
    "Confirmar que el PDF final se genere en la carpeta de la actividad."
  ],
  "latex_rules": [
    "Usar natbib con \\citep{clave} y \\citet{clave}.",
    "Mantener interlineado 1.5 y estilo institucional de la plantilla.",
    "Usar fuente tipo Helvetica o equivalente visual a Arial.",
    "Mantener estructura minima: caratula, resumen breve, desarrollo, producto, conclusion y bibliografia.",
    "Compilar actividad con reporte-administracion-de-calidad-Actividad-1.tex.",
    "Aplicar formato APA 7 en cuerpo y referencias [supuesto por plantilla].",
    "Mantener redaccion academica clara, formal, coherente y sin faltas.",
    "Ajustar variables coverwatermark para gestionar marca de agua institucional."
  ],
  "bibliography_rules": [
    "Usar archivo canonico administracion-de-calidad.bib.",
    "Registrar en el .bib todas las fuentes usadas por reportes y actividades de la carpeta.",
    "No inventar fuentes ni claves bibliograficas.",
    "Mantener consistencia exacta entre claves citadas y entradas existentes.",
    "Evitar entradas duplicadas en el .bib.",
    "Entrada confirmada disponible: unadm100TecnicasDidacticas2023."
  ],
  "propagation_hints": [
    "Propagar en sentido ascendente solo reglas verificadas localmente.",
    "Mantener compresion union-dedupe y no eliminar reglas utiles previas.",
    "Conservar visible la referencia de fuente local en propagacion.",
    "Marcar y revisar supuestos antes de promover a niveles superiores.",
    "Mantener nota: ciclo 1 requiere normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si la plantilla maestra de Actividad-1 esta completa; el archivo visible parece truncado [supuesto].",
    "Confirmar compatibilidad final entre requisito APA 7 y uso de atnumurl.bst [supuesto].",
    "Confirmar vigencia de la regla heredada de fuente provisional Codex para este curso [supuesto].",
    "Confirmar que base/Plantilla-Informe/template.tex coincide con TEXINPUTS activo [supuesto]."
  ]
}