# Memoria editorial AulaTeX

- Alcance: materia
- Etiqueta: administracion-de-calidad-lad
- Ruta: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad
- Compresion: union-dedupe
- Sin regresion: si
- Secciones fijadas: ninguna

## summary

- Materia ADM-CAL con plantilla maestra de reporte y actividad.
- Compilacion estandar con latexmk-build.ps1 desde raiz del proyecto.
- Bibliografia canonica de la materia en administracion-de-calidad.bib.
- Se hereda alerta institucional: salida previa no estructurada en ciclo 1.
- Salida sin JSON parseable desde Auto (model-router) para administracion-de-calidad-lad
- Targets conocidos: reporte, reporte-Actividad-1 y presentacion de la materia.

## identity_rules

- Usar identidad de materia: Administracion de calidad (ADM-CAL).
- Conservar ruta canonica: UCNL/licenciatura-en-administracion/administracion-de-calidad-lad.
- Mantener nombre base de bibliografia: administracion-de-calidad.bib.
- Fuente provisional: Auto (model-router) desde Actividad 1
- Mantener stems: ReportStem y PresentationStem = administracion-de-calidad.

## structure_rules

- Mantener formato de reporte de la materia para nuevas actividades.
- Incluir caratula, resumen breve, desarrollo, producto solicitado, conclusion y bibliografia.
- No pegar instrucciones completas de planeacion dentro del producto final.
- Usar la planeacion como lista de cumplimiento, no como contenido.
- Aplicar formato institucional: fuente tipo Helvetica/Arial e interlineado 1.5.

## activity_rules

- Responder exactamente a lo solicitado por la actividad de planeacion.
- Construir el producto academico solicitado dentro del documento cuando aplique.
- Redactar con comprension propia a partir de la bibliografia revisada.
- Duplicar y renombrar la plantilla por materia, semana y actividad.
- Actualizar metadatos: titulo, subtitulo, asignatura, codigo, departamento y docente.
- Entregar en PDF con la nomenclatura indicada en el aula.

## quality_gates

- Verificar que toda clave citada exista en administracion-de-calidad.bib.
- Validar compilacion correcta del .tex objetivo con script institucional.
- Revisar consistencia academica: claridad, coherencia, formalidad y ortografia.
- Revisar respuesta no estructurada heredada antes de propagar aguas abajo.
- Revisar respuesta no estructurada antes de aplicar aguas abajo.

## latex_rules

- Ejecutar compilacion siempre desde la raiz del proyecto.
- Usar .\\scripts\\latexmk-build.ps1 con la ruta del .tex como unico argumento obligatorio.
- No pasar \\input{template} como argumento; se resuelve por TEXINPUTS en .latexmkrc.
- En reportes, \\input{template} debe resolver a base/Plantilla-Informe/template.tex.
- No pasar .bib al script; declarar \\bibliography{administracion-de-calidad} en reportes.
- Permitir resolucion de atnumurl.bst mediante BSTINPUTS.
- Esperar PDF final junto al .tex y auxiliares en .build/latex y .build/latex/aux.
- Usar .\scripts\latexmk-build.ps1 con la ruta del .tex como unico argumento obligatorio.
- No pasar \input{template} como argumento; se resuelve por TEXINPUTS en .latexmkrc.
- En reportes, \input{template} debe resolver a base/Plantilla-Informe/template.tex.
- No pasar .bib al script; declarar \bibliography{administracion-de-calidad} en reportes.
- Resolver administracion-de-calidad.bib mediante BIBINPUTS.

## bibliography_rules

- Usar administracion-de-calidad.bib como archivo bibliografico canonico de la materia.
- Agregar en ese .bib las fuentes usadas por reportes y actividades de la carpeta.
- No inventar fuentes ni claves bibliograficas.
- Aplicar citas autor-anio con natbib: \\citep{clave} y \\citet{clave}.
- Supuesto: se busca estilo APA 7 en cuerpo y referencias segun comentarios de plantilla.
- Aplicar citas autor-anio con natbib: \citep{clave} y \citet{clave}.
- Fuente existente: unadm100TecnicasDidacticas2023 (referencia metodologica).

## propagation_hints

- Propagar estas reglas a actividades hermanas de la misma materia.
- Priorizar reglas de compilacion y bibliografia por su impacto transversal.
- Mantener compresion union-dedupe sin regresion ni recorte semantico.
- Ciclo 1: normalizacion manual recomendada si se detecta texto no estructurado heredado.
- Ciclo 1 necesita normalizacion manual si se reutiliza.

## open_questions

- Confirmar si el estilo bibliografico final exigido en entrega es exactamente APA 7.
- Confirmar si la marca de agua institucional en portada es obligatoria u opcional.
- Completar criterios truncados en el archivo de actividad 1 (texto fuente incompleto).
