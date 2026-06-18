# Memoria editorial AulaTeX

- Alcance: materia
- Etiqueta: derecho-de-la-empresa-y-emprendimiento-lde
- Ruta: UnADM/licenciatura-en-derecho-unadm/derecho-de-la-empresa-y-emprendimiento-lde
- Compresion: union-dedupe
- Sin regresion: si

## summary

- Base de destino inicializada con plantilla LaTeX y programa analitico de la materia.
- Se heredan alertas institucionales sobre salida no estructurada en ciclo 1.
- Aplicar normalizacion manual antes de propagar cambios aguas abajo.
- Salida sin JSON parseable desde Codex para UnADM.
- Materia local ubicada en semestre 6, bloque 2, tipo obligatoria y 8 creditos.
- Compresion aplicada por union-dedupe sin recorte.
- Origen actividad-1 de Filosofia del Derecho sin aporte estructurado verificable.
- Salida sin JSON parseable desde GPT-Pro para derecho-de-la-empresa-y-emprendimiento-lde
- README local presenta artefactos de salto en nombres de archivo y token Slug sin expandir.
- README local presenta artefactos de salto en nombres de archivo.
- README local presenta token Slug sin expandir.
- Programa analitico local presenta token Slug sin expandir.
- Reporte local parece truncado en la definicion de authortable.
- Se heredan alertas institucionales sobre salida no estructurada.
- Salida sin JSON parseable desde GPT-Pro para derecho-de-la-empresa-y-emprendimiento-lde.

## identity_rules

- Mantener identidad institucional UnADM en portada y metadatos.
- Usar nombre oficial de la materia: Derecho de la empresa y emprendimiento.
- Marcar como supuesto cualquier dato no confirmado por archivo local.
- Usar Licenciatura en Derecho como programa academico.
- Usar codigo local LDE-S6B2 cuando la plantilla lo requiera.
- Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.
- Usar autor de plantilla local solo si la actividad lo confirma.
- Autor de plantilla local confirmado: Martin Jonathan de la Cruz (supuesto, revisar por actividad).
- Fuente provisional: GPT-Pro desde Actividad 1
- Autor visible en plantilla local: Martin Jonathan de la Cruz; supuesto: confirmar por actividad.
- Fuente provisional: GPT-Pro desde Actividad 1.

## structure_rules

- Usar README de materia como punto de entrada canonico.
- Alinear cada entrega al esquema: problema, conceptos, producto, analisis propio, conclusion.
- Conservar correspondencia entre .tex, presentacion y .bib de la materia.
- Usar el programa analitico local para orientar productos academicos.
- Integrar evidencia, fundamento juridico y transferencia profesional.
- Verificar que nombres de archivos no conserven artefactos de generacion automatica.
- Resolver tokens de plantilla sin expandir en README y programa analitico (ej. $(@{...}.Slug)).
- Transformar planeacion semanal en reporte, presentacion y producto visual.
- Resolver tokens de plantilla sin expandir en README y programa analitico.

## activity_rules

- Cada actividad debe incluir conclusion juridica con criterio propio.
- Cada actividad debe incluir citas verificables y trazables a la bibliografia local.
- Agregar fuentes especificas de actividad al archivo .bib de la materia.
- Identificar el problema juridico o social que activa la actividad.
- Distinguir conceptos, normas, doctrina o datos pertinentes.
- Cerrar con postura academica propia y aplicacion practica.
- Transformar planeacion semanal en reporte, presentacion y producto visual.
- Incluir el producto solicitado por la planeacion.
- Incluir analisis propio y postura academica.
- Cerrar con conclusion juridica con criterio propio.
- Conectar la conclusion con aplicacion practica.
- Incluir citas verificables y trazables a la bibliografia local.

## quality_gates

- Validar JSON parseable antes de consolidar memoria.
- Revisar respuesta no estructurada antes de aplicar propagacion lateral o ascendente.
- No eliminar reglas utiles previas durante fusion por union-dedupe.
- Revisar respuesta no estructurada antes de aplicar aguas abajo.
- Aplicar normalizacion manual en ciclo 1 antes de reutilizar memoria.
- Verificar que los datos curriculares coincidan con la malla local.
- Corregir placeholders visibles antes de generar entregables.
- Verificar integridad sintactica de archivos .tex y cierre de entornos antes de compilar.
- Aplicar normalizacion manual en ciclo 2 antes de reutilizar memoria.
- Verificar que el README liste archivos reales y rutas existentes.
- No propagar datos locales no confirmados como reglas institucionales.

## latex_rules

- Conservar plantilla base de reporte con metadatos institucionales completos.
- Mantener consistencia de campos de curso y licenciatura en macros LaTeX.
- Verificar compilacion sin errores tras actualizar portada, secciones y referencias.
- Usar spanish, letterpaper y oneside salvo instruccion local distinta.
- Actualizar documenttitle y documentsubtitle por actividad.
- Mantener universitydepartment como Derecho de la empresa y emprendimiento.
- Validar que las rutas de imagen institucional existan antes de compilar.
- Reemplazar documenttitle generico de plantilla base por titulo de actividad concreto.
- Confirmar imagen departamentos/UnADM y configuracion height=1.57cm antes de compilar.
- Revisar que el archivo de reporte no quede truncado y que \end{tabular} cierre correctamente.
- Confirmar universitydepartmentimage como departamentos/UnADM antes de compilar.
- Confirmar universitydepartmentimagecfg como height=1.57cm antes de compilar.
- Revisar que el archivo de reporte no quede truncado.
- Revisar que \end{tabular} cierre correctamente.

## bibliography_rules

- No inventar fuentes; registrar solo fuentes verificables.
- Priorizar fuentes institucionales UnADM y documentos locales de malla curricular.
- Mantener claves BibTeX estables y sin duplicados.
- Conservar unadmSitioWeb y unadmMallaDerecho2024 como bibliografia base local.
- Registrar fuentes especificas en derecho-de-la-empresa-y-emprendimiento.bib.
- No citar fuentes no agregadas al .bib local.
- Indicar archivo local cuando la fuente provenga de assets-unadm.
- No inventar fuentes.
- Registrar solo fuentes verificables.
- Conservar unadmSitioWeb como bibliografia base local.
- Conservar unadmMallaDerecho2024 como bibliografia base local.

## propagation_hints

- Propagar estas reglas a nivel licenciatura en Derecho cuando no exista conflicto local.
- Propagar lateralmente a materias hermanas con misma pauta editorial de UnADM.
- En ciclo 1, exigir normalizacion manual previa por antecedente de salida no estructurada.
- Ciclo 1 necesita normalizacion manual si se reutiliza.
- Propagar alertas de placeholders y rutas generadas a materias con plantillas similares.
- No propagar datos curriculares especificos fuera de esta materia sin confirmacion local.
- Propagar alerta de tokens de plantilla sin expandir a materias con README generado.
- Propagar en ciclo 2 hacia arriba y laterales si no existe conflicto local.
- Propagar alerta de truncamiento LaTeX solo a plantillas con sintomas equivalentes.
- Exigir normalizacion manual previa por antecedente de salida no estructurada.
- Ciclo 2 necesita normalizacion manual si se reutiliza.

## open_questions

- Supuesto: la actividad origen no aporta reglas adicionales por falta de JSON estructurado.
- Confirmar si existe guia de citacion juridica especifica distinta a la plantilla general.
- Confirmar si el nombre de autor en plantilla debe parametrizarse por actividad.
- Confirmar si el README local debe corregir saltos o caracteres perdidos en nombres de archivos.
- Confirmar si el sitio UnADM debe conservar year 2026 como fecha de consulta o como anio bibliografico.
- Confirmar valor real del Slug en README y programa analitico tras expansion de tokens.
- Confirmar si el archivo de reporte esta incompleto en repositorio o solo en captura local.
- Confirmar cierre completo de \authortable en el reporte local.
