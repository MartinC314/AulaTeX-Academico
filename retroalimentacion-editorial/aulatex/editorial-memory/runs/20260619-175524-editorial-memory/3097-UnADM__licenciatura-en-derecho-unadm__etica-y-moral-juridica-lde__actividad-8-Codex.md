{
  "summary": [
    "Se preserva memoria valida previa de Actividad 8 sin eliminar reglas utiles.",
    "No hay evidencia parseable nueva desde Actividad 1 en este ciclo.",
    "Se mantiene fusion por union-dedupe con compresion lossless.",
    "Supuesto: el origen sigue sin salida estructurada util.",
    "Mejora verificable: se deduplican entradas repetidas de fuentes provisionales en reglas de identidad.",
    "Mejora verificable: se refuerza control de JSON parseable previo a propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en redaccion, enfoque academico y cierre juridico.",
    "Mantener referencia explicita a la asignatura Etica y Moral juridica en productos editoriales.",
    "Registrar la fuente de cada fusion con ruta origen y destino.",
    "Conservar etiquetas de fuente provisional cuando no exista evidencia estructurada valida.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: Auto (model-router) desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido y parseable.",
    "Usar el esquema canonico requerido sin omitir secciones.",
    "Aplicar compresion por union-dedupe sin recortar reglas utiles.",
    "Marcar explicitamente supuestos cuando falte evidencia.",
    "Conservar trazabilidad de cambios por ciclo en frases breves y verificables."
  ],
  "activity_rules": [
    "Alinear cada entrega al problema juridico o social de la actividad.",
    "Integrar conceptos, normas o doctrina pertinentes antes de concluir.",
    "Ajustar el producto al formato solicitado en la planeacion semanal.",
    "Incluir analisis propio y postura academica explicita.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Seguir los cinco ejes del programa analitico local como lista de verificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar ausencia de duplicados semanticos antes de guardar memoria.",
    "No eliminar reglas previas utiles durante la fusion.",
    "Revisar consistencia entre pauta editorial local y reglas de actividad.",
    "Aceptar solo mejoras verificables contra archivos locales o memoria previa."
  ],
  "latex_rules": [
    "Mantener compatibilidad con plantilla LaTeX de la asignatura.",
    "Evitar comandos no estandar sin justificacion academica.",
    "Asegurar que citas y referencias compilen sin errores.",
    "Mantener consistencia de nombres de archivos .tex y .bib segun slug de la materia."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables en .bib o material institucional.",
    "Agregar nuevas fuentes al archivo etica-y-moral-juridica.bib con metadatos minimos completos.",
    "Evitar claves BibTeX duplicadas para la misma obra cuando se edite.",
    "Citar en texto toda fuente listada que sustente afirmaciones clave.",
    "Marcar como pendiente la depuracion de duplicados historicos sin borrar trazabilidad.",
    "Supuesto: existe una entrada .bib truncada y debe validarse antes de editar o compilar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo bloques validados por JSON y esquema.",
    "Mantener bandera de normalizacion manual mientras persistan salidas no estructuradas.",
    "Priorizar consolidacion incremental: preservar, deduplicar, luego extender.",
    "Ciclo 5: sin insumo estructurado nuevo desde origen; mantener estado y esperar evidencia parseable.",
    "Ciclo 6 necesita normalizacion manual si se reutiliza.",
    "Ciclo 7 necesita normalizacion manual si se reutiliza.",
    "Ciclo 8 necesita normalizacion manual si se reutiliza.",
    "Ciclo 9 necesita normalizacion manual si se reutiliza.",
    "Ciclo 10 necesita normalizacion manual si se reutiliza.",
    "Ciclo 11 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar si existe contenido recuperable de Actividad 1 fuera de las bitacoras de error.",
    "Definir criterio local para resolver duplicados bibliograficos historicos en el .bib sin perder trazabilidad.",
    "Supuesto: la entrada de etica-y-moral-juridica.bib esta truncada en contexto local y requiere verificacion previa a edicion.",
    "Confirmar y corregir la entrada truncada en etica-y-moral-juridica.bib antes del siguiente ciclo."
  ]
}