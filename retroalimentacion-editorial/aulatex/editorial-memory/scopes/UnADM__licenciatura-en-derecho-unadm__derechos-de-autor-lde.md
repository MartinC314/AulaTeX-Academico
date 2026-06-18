# Memoria editorial AulaTeX

- Alcance: materia
- Etiqueta: derechos-de-autor-lde
- Ruta: UnADM/licenciatura-en-derecho-unadm/derechos-de-autor-lde
- Compresion: union-dedupe
- Sin regresion: si

## summary

- Consolidar base editorial UnADM para la materia Derechos de autor.
- Mantener compresion por union-dedupe sin perdida.
- Marcar que la herencia previa viene de fuente provisional y requiere validacion local.
- Consolidar base editorial UnADM para Derechos de autor.
- Usar README como entrada canonica de la asignatura.
- Marcar herencia Codex como provisional hasta validacion local.
- Preservar reglas utiles heredadas sin regresion.
- Supuesto: herencia previa proviene de fuente provisional sin JSON parseable y requiere validacion local.
- Salida sin JSON parseable desde GPT-Pro para derechos-de-autor-lde
- Supuesto: herencia previa incluye salidas no JSON parseable y requiere validacion local.
- Marcar herencia GPT-Pro como provisional hasta validacion local.
- Marcar herencia previa (Codex, GPT-Pro) como provisional hasta validacion local.
- Origen ciclo 2: actividad-1 de filosofia-del-derecho-lde sin JSON parseable confirmado.

## identity_rules

- Usar identidad institucional UnADM en portada y metadatos.
- Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.
- Mantener enfoque juridico con criterio propio en la conclusion.
- Supuesto: la materia conserva nomenclatura local LDE-S5B1 en documentos.
- Alinear entregables con Licenciatura en Derecho.
- Usar datos curriculares locales: semestre 5, bloque 1, obligatoria, 8 creditos.
- Supuesto: la materia conserva nomenclatura local LDE-S5B1.
- Marcar como provisional la fuente Codex heredada desde ingenieria.
- Marcar como provisional la fuente Codex heredada desde ingenieria-en-sistemas-computacionales.
- Fuente provisional: GPT-Pro desde Actividad 1
- Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.
- Fuente provisional: GPT-Pro desde Actividad 1.
- Fuente provisional: filosofia-del-derecho-lde/actividad-1 (sin JSON parseable).

## structure_rules

- Conservar README como punto de entrada canonico de la asignatura.
- Usar programa-analitico como marco para problema, conceptos, producto, analisis y cierre.
- Guardar bibliografia especifica en derechos-de-autor.bib.
- Mantener separacion entre reporte, presentacion y referencias de la materia.
- Normalizar nombres de archivo con slug de la asignatura cuando aplique.
- Conservar README como punto de entrada canonico.
- Usar programa-analitico como marco editorial.
- Organizar cada producto por problema, conceptos, producto, analisis y cierre.
- Mantener separacion entre reporte, presentacion y referencias.
- Normalizar nombres de archivo con slug derechos-de-autor.
- Corregir marcadores literales de plantilla en README y programa analitico.
- Corregir nombres corruptos como eporte y eferencias antes de publicar.
- Sustituir expresiones literales $(@{...}.Slug) por derechos-de-autor.bib en README y programa analitico.
- Sustituir $(@{...}.Slug) por derechos-de-autor.bib.
- Sustituir expresiones literales $(@{...}.Slug) por derechos-de-autor.bib.

## activity_rules

- Iniciar cada actividad con problema juridico o social delimitado.
- Vincular conceptos con normas, doctrina o datos verificables.
- Cumplir formato solicitado por la planeacion semanal.
- Incluir analisis propio explicito, no solo resumen de fuentes.
- Cerrar con conclusion aplicable a practica juridica.
- Incluir analisis propio explicito.
- Evitar entregar solo resumen de fuentes.
- Cerrar con conclusion aplicable a la practica juridica.
- Agregar fuentes especificas por actividad al archivo BibTeX local.

## quality_gates

- Rechazar salidas no JSON parseable antes de propagar memoria.
- Verificar consistencia entre metadatos de portada y datos curriculares locales.
- Exigir citas verificables y correspondencia con .bib local.
- Detectar y corregir campos pendientes como 'Nombre por definir'.
- Marcar herencia institucional previa como provisional hasta confirmacion en Derecho.
- Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.
- Verificar consistencia entre portada y datos curriculares locales.
- Exigir citas verificables con correspondencia en .bib local.
- Detectar y corregir campos pendientes como Nombre por definir.
- Auditar README por caracteres extranos y marcadores de plantilla.
- Mantener normalizacion manual durante ciclo 1.
- Revisar respuesta no estructurada antes de aplicar aguas abajo.
- Marcar herencia institucional provisional hasta confirmacion en Derecho.
- No publicar con nombres corruptos de archivo.
- Validar localmente contenido heredado de ciclo 1 antes de reutilizarlo.
- Validar localmente contenido heredado de ciclos previos antes de reutilizarlo.

## latex_rules

- Mantener plantilla article en espanol y letterpaper salvo instruccion contraria.
- Declarar metadatos con macros de documento antes de \input{template}.
- Conservar tabla de autor con alumno, matricula y datos academicos completos.
- Evitar paquetes truncados o lineas incompletas en preambulo.
- Usar tipografia sans serif de forma consistente si la plantilla la requiere.
- Mantener documentclass article en espanol y letterpaper salvo instruccion contraria.
- Declarar metadatos con macros antes de \input{template}.
- No propagar datos personales del alumno a otras materias.
- Nunca dejar \usepackage sin argumento.
- Validar que los paquetes LaTeX queden en preambulo efectivo.
- Corregir \usepackage final sin argumento detectado al cierre del preambulo en reporte.
- Mover paquetes cargados despues de \input{template} al preambulo correcto si la plantilla lo exige.
- Corregir \usepackage final sin argumento detectado en reporte.
- Conservar tabla de autor con alumno, matricula y datos academicos completos en documentos locales.

## bibliography_rules

- No inventar fuentes; usar solo materiales institucionales o verificables.
- Registrar fuentes base UnADM ya incluidas en derechos-de-autor.bib.
- Agregar nuevas entradas BibTeX completas por actividad.
- Incluir fecha de consulta cuando la fuente sea web.
- Asegurar que toda cita en texto tenga entrada en .bib y viceversa.
- No inventar fuentes.
- Usar solo materiales institucionales o verificables.
- Registrar fuentes base UnADM incluidas en derechos-de-autor.bib.
- Conservar entrada local unadmSitioWeb si se cita.
- Conservar entrada local unadmMallaDerecho2024 si se cita.
- Agregar entradas BibTeX completas por actividad.
- Incluir fecha de consulta en fuentes web.
- Asegurar que toda cita en texto tenga entrada en .bib.
- Asegurar que toda entrada .bib usada corresponda con una cita o bibliografia requerida.

## propagation_hints

- Propagar hacia arriba reglas institucionales validadas en esta materia.
- Propagar lateralmente a materias LDE solo reglas genericas de calidad y estructura.
- No propagar datos personales del alumno a otras materias.
- Mantener bandera de normalizacion manual en ciclo 1 para contenido heredado.
- No propagar datos personales del alumno.
- No propagar marcadores pendientes ni nombres corruptos de archivo.
- Mantener bandera de normalizacion manual en ciclo 1.
- Propagar advertencia sobre herencia Codex solo como provisional.
- Ciclo 1 necesita normalizacion manual si se reutiliza.
- Propagar advertencia sobre herencia GPT-Pro solo como provisional.
- Mantener auditoria manual para contenido heredado de ciclo 1 si se reutiliza.
- Propagar advertencia sobre herencia Codex y GPT-Pro solo como provisional.
- Mantener auditoria manual para contenido heredado de ciclos previos si se reutiliza.
- Ciclo 2 necesita normalizacion manual si se reutiliza.

## open_questions

- Confirmar si la clave de curso LDE-S5B1 es oficial en toda la suite.
- Definir nombre de figura docente para eliminar marcador pendiente.
- Validar si la ubicacion 'Roma Norte, Ciudad de Mexico' debe mantenerse fija.
- Revisar y corregir posibles errores de nombres de archivo en README (lineas con caracteres extranos).
- Confirmar si la fuente heredada 'Codex desde ingenieria' sigue vigente o debe retirarse tras validacion local.
- Confirmar si LDE-S5B1 es clave oficial en toda la suite.
- Definir nombre de figura docente.
- Validar si Roma Norte, Ciudad de Mexico debe mantenerse fija.
- Confirmar sustitucion definitiva de marcadores literales por derechos-de-autor.bib.
- Confirmar si la fuente heredada Codex desde ingenieria sigue vigente.
- Validar orden correcto entre paquetes LaTeX y \input{template} en esta plantilla.
- Revisar y corregir errores de nombres de archivo en README (lineas con caracteres extranos).
- Confirmar si la fuente heredada Codex desde ingenieria sigue vigente o debe retirarse tras validacion local.
- Confirmar argumento correcto del \usepackage truncado al final del preambulo en reporte.
- Confirmar si la fuente heredada Codex sigue vigente o debe retirarse tras validacion local.
- Revisar y corregir errores de nombres de archivo en README.
- Confirmar si la fuente heredada GPT-Pro desde Actividad 1 sigue vigente o debe retirarse tras validacion local.
