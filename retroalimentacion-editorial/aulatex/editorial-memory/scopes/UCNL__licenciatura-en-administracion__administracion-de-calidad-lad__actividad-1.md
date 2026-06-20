# Memoria editorial AulaTeX

- Alcance: actividad
- Etiqueta: Actividad 1
- Ruta: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad
- Compresion: union-dedupe
- Sin regresion: si
- Secciones fijadas: ninguna

## summary

- Memoria inicial creada para actividad-1 con reglas de compilacion y citacion del curso.
- Se conserva herencia institucional y se agrega normalizacion local verificable.
- Contrato de compilacion confirmado segun COMPILACION.md.
- Criterios de citacion con natbib y estructura academica minima fijados.
- Control de TEXINPUTS, BIBINPUTS y BSTINPUTS verificado.
- Salida sin JSON parseable desde Codex para UCNL [supuesto heredado].
- Salida sin JSON parseable desde GPT-Pro para Actividad 1
- Memoria consolidada para actividad-1 con contrato de compilacion, citacion y estructura academica.
- Se preserva herencia institucional UCNL y normalizacion local verificable.
- Compresion aplicada por union-dedupe sin perdida.
- Persisten antecedentes de salida no JSON parseable como trazabilidad [supuesto heredado].
- Salida sin JSON parseable desde GPT-Pro para Actividad 1 [supuesto].
- Propagacion ascendente en ciclo 2 con verificacion previa.

## identity_rules

- Mantener alcance UCNL y ruta exacta del destino.
- Usar etiqueta de curso: administracion-de-calidad-lad.
- Conservar regla heredada: fuente provisional Codex desde ingenieria-en-sistemas-computacionales [supuesto heredado].
- Registrar fuente local de referencia: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad/actividad-1.
- Codigo de curso: ADM-CAL; tetramestre 9.
- Fuente provisional: GPT-Pro desde Actividad 1
- Usar etiqueta de curso administracion-de-calidad-lad.
- Registrar fuente local: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad/actividad-1.
- Mantener codigo de curso ADM-CAL y tetramestre 9.
- Conservar fuente provisional Codex desde ingenieria-en-sistemas-computacionales [supuesto heredado].
- Conservar fuente provisional GPT-Pro desde Actividad 1 [supuesto].

## structure_rules

- Ejecutar compilacion desde la raiz del proyecto.
- Usar el script latexmk-build.ps1 con un unico argumento: ruta del .tex.
- No pasar \input{template} como argumento al script.
- No pasar el .bib como argumento al script.
- Mantener salida PDF en la misma carpeta del .tex.
- Mantener auxiliares en .build/latex y .build/latex/aux.
- \input{template} debe resolver a base/Plantilla-Informe/template.tex via TEXINPUTS.
- BibTeX debe ubicar administracion-de-calidad.bib via BIBINPUTS.
- El estilo atnumurl.bst debe resolverse via BSTINPUTS.
- TEXINPUTS y rutas se definen en .latexmkrc.
- Existen tres .tex en la carpeta: reporte, reporte-Actividad-1 y presentacion.
- Usar scripts/latexmk-build.ps1 con un unico argumento: ruta del .tex.
- No pasar \input{template} como argumento.
- No pasar el .bib como argumento.
- Resolver \input{template} por TEXINPUTS hacia base/Plantilla-Informe/template.tex.
- Resolver administracion-de-calidad.bib por BIBINPUTS.
- Resolver atnumurl.bst por BSTINPUTS.
- Definir TEXINPUTS, BIBINPUTS y BSTINPUTS en .latexmkrc.
- Reconocer tres .tex de trabajo en la carpeta: reporte, reporte-Actividad-1 y presentacion.
- Ejecutar la compilacion desde la raiz del proyecto.
- Compilar: reporte-administracion-de-calidad.tex, reporte-administracion-de-calidad-Actividad-1.tex y presentacion-administracion-de-calidad.tex.
- Mantener el PDF final en la misma carpeta del .tex.

## activity_rules

- Mantener el formato del reporte de la materia al crear actividades nuevas.
- En reportes, declarar \bibliography{administracion-de-calidad}.
- Toda clave citada debe existir en administracion-de-calidad.bib.
- No pegar instrucciones completas de planeacion dentro del producto final.
- Redactar con comprension propia y cumplimiento explicito de la actividad solicitada.
- Responder exactamente a la actividad solicitada en la planeacion.
- Usar la planeacion como lista de cumplimiento; no pegar instrucciones completas.
- Redactar con comprension propia y cumplimiento explicito.
- Construir el producto academico solicitado dentro del documento cuando sea posible.
- Duplicar la plantilla maestra y renombrar por materia, semana y actividad.
- Actualizar documenttitle, documentsubtitle, documentsubject, coursename, coursecode y universitydepartment.
- Identificar conceptos, elementos, criterios o categorias solicitados.
- Entregar en PDF con la nomenclatura indicada en el aula.
- Revisar bibliografia indicada, tomar notas y registrar citas antes de redactar.
- Mantener formato del reporte de la materia al crear actividades.
- Declarar \bibliography{administracion-de-calidad} en reportes.
- Exigir que toda clave citada exista en administracion-de-calidad.bib.
- No pegar instrucciones completas de planeacion en el producto final.
- Usar la planeacion como lista de cumplimiento.
- Redactar con comprension propia y cumplimiento explicito de la actividad.
- Responder exactamente a lo solicitado en la actividad.
- Duplicar plantilla maestra y renombrar por materia, semana y actividad.
- Entregar PDF con nomenclatura indicada en el aula.

## quality_gates

- Validar que la respuesta sea JSON parseable antes de propagar.
- Revisar respuesta no estructurada antes de aplicar aguas abajo.
- Verificar resolucion de template por TEXINPUTS.
- Verificar resolucion de .bib por BIBINPUTS.
- Verificar resolucion de atnumurl.bst por BSTINPUTS.
- Confirmar que no existan citas sin entrada BibTeX.
- Compilacion limpia sin errores ni advertencias de referencias o citas.
- Confirmar que el PDF final se genera en la carpeta de la actividad.
- Validar que la salida sea JSON parseable antes de propagar.
- Exigir compilacion sin errores ni advertencias de citas o referencias.
- Confirmar que el PDF final se genere en la carpeta de la actividad.
- Verificar resolucion de template por TEXINPUTS hacia base/Plantilla-Informe/template.tex.
- Verificar resolucion del .bib por BIBINPUTS.
- Confirmar existencia de los tres archivos de entrada .tex indicados.
- Confirmar que .latexmkrc defina TEXINPUTS, BIBINPUTS y BSTINPUTS.

## latex_rules

- Usar natbib con citas autor-anio: \citep{clave} y \citet{clave}.
- Mantener interlineado 1.5 y estilo institucional indicado en plantilla.
- Incluir estructura academica minima: caratula, resumen breve, desarrollo, producto, conclusion, bibliografia.
- Compilar reporte de actividad con el archivo reporte-administracion-de-calidad-Actividad-1.tex.
- Mantener interlineado 1.5 y estilo institucional indicado en la plantilla.
- Usar fuente tipo Helvetica o equivalente visual a Arial.
- Compilar el reporte de la actividad con reporte-administracion-de-calidad-Actividad-1.tex.
- Compilar reporte de actividad con reporte-administracion-de-calidad-Actividad-1.tex.
- Usar formato APA 7 en cuerpo y referencias.
- Redaccion academica clara, coherente, cohesionada, formal y sin faltas.
- Ajustar variables coverwatermark... para apagar o cambiar la marca de agua institucional.
- Usar natbib con \citep{clave} y \citet{clave}.
- Mantener interlineado 1.5 y estilo institucional de la plantilla.
- Mantener estructura minima: caratula, resumen breve, desarrollo, producto, conclusion y bibliografia.
- Compilar actividad con reporte-administracion-de-calidad-Actividad-1.tex.
- Aplicar formato APA 7 en cuerpo y referencias [supuesto por plantilla].
- Mantener redaccion academica clara, formal, coherente y sin faltas.
- Ajustar variables coverwatermark para gestionar marca de agua institucional.
- Incluir estructura academica minima: caratula, resumen breve, desarrollo, producto, conclusion y bibliografia.
- Compilar la actividad con reporte-administracion-de-calidad-Actividad-1.tex.
- Ajustar variables coverwatermark para gestionar la marca de agua institucional.
- Mantener redaccion academica clara, formal, coherente, cohesionada y sin faltas.

## bibliography_rules

- Usar archivo canonico: administracion-de-calidad.bib.
- Registrar en .bib todas las fuentes usadas por reportes y actividades de la carpeta.
- No inventar fuentes ni claves bibliograficas.
- Mantener consistencia entre claves citadas y entradas existentes.
- Registrar en el .bib todas las fuentes usadas por reportes y actividades de esta carpeta.
- Mantener consistencia exacta entre claves citadas y entradas existentes.
- Evitar duplicados de entradas en el .bib.
- Entrada disponible confirmada: unadm100TecnicasDidacticas2023.
- Usar archivo canonico administracion-de-calidad.bib.
- Registrar en el .bib todas las fuentes usadas por reportes y actividades de la carpeta.
- Evitar entradas duplicadas en el .bib.
- Entrada confirmada disponible: unadm100TecnicasDidacticas2023.
- Agregar entradas faltantes al .bib antes de compilar.

## propagation_hints

- Propagar en sentido ascendente solo reglas verificadas localmente.
- Conservar compresion union-dedupe sin eliminar reglas utiles previas.
- Ciclo 1 requiere normalizacion manual si se reutiliza en otros nodos.
- Mantener visible la referencia de fuente local al propagar.
- Ciclo 1 necesita normalizacion manual si se reutiliza.
- Mantener compresion union-dedupe y no eliminar reglas utiles previas.
- Conservar visible la referencia de fuente local en propagacion.
- Marcar y revisar supuestos antes de promover a niveles superiores.
- Mantener nota: ciclo 1 requiere normalizacion manual si se reutiliza.
- Ciclo 1 requiere normalizacion manual si se reutiliza [trazabilidad].
- Ciclo 2: normalizar y promover a nivel curso si supera los quality gates.
- Registrar cambios respecto al contrato de compilacion al propagar.
- Ciclo 2 necesita normalizacion manual si se reutiliza.

## open_questions

- Confirmar si la plantilla maestra de Actividad-1 esta completa; el archivo visible parece truncado [supuesto].
- Confirmar guia definitiva de estilo APA 7 en salida final, dado uso de atnumurl.bst [supuesto].
- Confirmar si la regla heredada de fuente provisional sigue vigente para este curso [supuesto].
- Confirmar que la ruta base/Plantilla-Informe/template.tex coincide con TEXINPUTS activo [supuesto].
- Confirmar compatibilidad final entre requisito APA 7 y uso de atnumurl.bst [supuesto].
- Confirmar vigencia de la regla heredada de fuente provisional Codex para este curso [supuesto].
- Confirmar que base/Plantilla-Informe/template.tex coincide con TEXINPUTS activo [supuesto].
- Confirmar si la regla heredada de fuente provisional (Codex/GPT-Pro) sigue vigente para este curso [supuesto].
- Confirmar que base/Plantilla-Informe/template.tex coincide con TEXINPUTS activo en .latexmkrc [supuesto].
- Confirmar en el repositorio los nombres exactos de los tres .tex de entrada segun COMPILACION.md [supuesto].
- Confirmar que la plantilla habilita natbib con opciones autor-anio por defecto [supuesto].
