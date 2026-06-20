{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Asignatura de Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada de 8 creditos.",
    "La carpeta local es punto de entrada canonico de la asignatura.",
    "Memoria consolidada con compresion union-dedupe sin perdida y sin regresion.",
    "Se conserva alerta institucional por salidas no JSON parseable en memorias heredadas (Codex, GPT-Pro, Auto model-router y Claude Foundry).",
    "Se prioriza normalizacion manual antes de propagacion automatica cuando reaparezcan salidas no estructuradas.",
    "Plantilla local registra alumno Martin Jonathan de la Cruz y matricula ES2611202040. [supuesto verificar vigencia]",
    "Ciclo 13 de consolidacion en curso."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, redaccion y metadatos.",
    "Usar nombre de asignatura exacto: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1.",
    "Conservar tipo curricular: obligatoria seriada.",
    "Conservar creditos: 8.",
    "Usar codigo de curso local LDE-S3B1 cuando aplique.",
    "Usar ubicacion institucional Roma Norte, Ciudad de Mexico en metadatos.",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Mantener figura docente como dato no confirmado hasta validacion. [supuesto]",
    "Tratar fuentes heredadas de otros programas como provisionales si reaparecen (Codex desde ingenieria-en-sistemas-computacionales, Codex/GPT-Pro/Auto model-router/Claude Foundry desde Actividad 1). [supuesto]"
  ],
  "structure_rules": [
    "Estructurar cada entrega en problema, marco conceptual-normativo, analisis propio y conclusion juridica.",
    "Usar ejes locales: problema juridico o social, conceptos y normas, producto solicitado, analisis propio y conclusion transferible.",
    "Conservar coherencia con programa analitico local de la materia.",
    "Incluir trazabilidad entre consigna, desarrollo y cierre.",
    "Transformar planeacion semanal en reportes, presentaciones o productos visuales segun consigna.",
    "Mantener la carpeta de materia como punto de entrada canonico.",
    "Verificar que nombres de archivo, slug y referencias sean consistentes antes de compilar.",
    "Corregir en README nombres corruptos de reporte y carpeta de referencias.",
    "Corregir en README y programa analitico el placeholder dinamico del archivo .bib."
  ],
  "activity_rules": [
    "Adaptar reglas de actividad origen solo si son compatibles con materia destino. [supuesto]",
    "No trasladar contenido de Filosofia del Derecho sin validacion de pertinencia. [supuesto]",
    "Identificar producto solicitado antes de redactar.",
    "Vincular cada actividad con la planeacion o rubrica vigente cuando exista.",
    "Evitar texto generico; vincular argumentos al problema juridico planteado.",
    "Integrar fundamento juridico, evidencia y transferencia profesional.",
    "Mantener conclusion con criterio juridico propio en toda actividad.",
    "Registrar pendientes de consigna faltante en preguntas abiertas."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada intercambio de memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Detener propagacion si faltan datos minimos de actividad.",
    "No propagar reglas dependientes de actividad sin consigna confirmada.",
    "Verificar que consigna, rubrica y producto solicitado esten identificados.",
    "Confirmar integridad academica: sin afirmaciones sin sustento.",
    "Comprobar que cada afirmacion juridica relevante tenga respaldo verificable.",
    "Revisar nombres corruptos de reporte, referencias y archivo .bib en README local.",
    "Verificar que el .tex use el .bib local y no placeholders antes de compilar.",
    "Compilar sin errores y sin referencias rotas."
  ],
  "latex_rules": [
    "Usar plantilla base de reporte de la materia como punto de partida.",
    "Conservar documentclass article en espanol, letterpaper y oneside salvo consigna distinta.",
    "Completar metadatos institucionales y academicos antes de redactar contenido.",
    "Usar titulo, subtitulo, asignatura y codigo local coherentes con la actividad.",
    "Actualizar documentsubtitle de Actividad X al numero real de actividad.",
    "Mantener espanol academico y consistencia terminologica juridica.",
    "Usar el archivo bibliografico local derechos-de-la-persona-y-familia.bib.",
    "Evitar placeholders en nombres de archivos LaTeX, BibTeX y rutas.",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Mantener figura docente como Nombre por definir hasta confirmacion. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar archivo local derechos-de-la-persona-y-familia.bib como fuente canonica.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a la actividad.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Conservar malla curricular de Derecho como fuente curricular local.",
    "Reemplazar placeholders dinamicos de nombre .bib por slug canonico fijo."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de calidad.",
    "Mantener compresion union-dedupe sin perdida y sin regresion.",
    "Mantener reglas institucionales estables como base comun.",
    "Priorizar reglas institucionales UnADM sobre reglas de origen no juridicas.",
    "Propagar reglas de identidad, bibliografia y calidad si son comunes a UnADM.",
    "Propagar reglas de actividad solo con compatibilidad juridica confirmada.",
    "No propagar reglas dependientes de consigna no confirmada.",
    "Si reaparece salida no JSON parseable, forzar normalizacion manual antes de propagar.",
    "Aplicar normalizacion manual previa cuando reaparezcan salidas no estructuradas.",
    "Registrar origen y destino cuando se consolide memoria lateral.",
    "Ciclo 13 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Falta consigna especifica de actividad-1 de Filosofia del Derecho para mapear reglas exactas.",
    "Confirmar consigna especifica de la actividad destino en Derechos de la persona y familia.",
    "Confirmar si existe plantilla formal de presentacion obligatoria para esta materia.",
    "Confirmar datos de figura docente y criterios de evaluacion vigentes.",
    "Confirmar si el codigo LDE-S3B1 es requerido en todos los productos.",
    "Confirmar si los datos de alumno y matricula de la plantilla local siguen vigentes.",
    "Validar correccion definitiva de rutas y slugs corruptos en README local.",
    "Validar sustitucion definitiva del placeholder de .bib en README y programa analitico.",
    "Confirmar si el slug del .bib en README y programa analitico debe resolverse desde plantilla generadora. [supuesto]"
  ]
}