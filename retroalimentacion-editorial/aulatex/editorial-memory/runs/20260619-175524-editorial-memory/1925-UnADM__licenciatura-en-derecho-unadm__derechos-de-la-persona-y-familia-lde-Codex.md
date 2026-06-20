{
  "summary": [
    "Materia destino UnADM con enfoque juridico aplicado.",
    "Asignatura: Derechos de la persona y familia, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "La carpeta local es punto de entrada canonico de la asignatura.",
    "Memoria consolidada desde Filosofia del Derecho actividad 1 hacia Derechos de la persona y familia.",
    "Compresion union-dedupe sin perdida y sin regresion.",
    "Se mantiene alerta institucional por salidas no JSON parseable heredadas (Codex, GPT-Pro, Auto model-router y Claude Foundry).",
    "Se mantiene normalizacion manual previa cuando reaparezcan salidas no estructuradas.",
    "Se detectan placeholders dinamicos y nombres corruptos en README/programa para correccion.",
    "Consolidacion ciclo 20 completada con compresion union-dedupe sin perdida y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, redaccion y metadatos.",
    "Usar nombre exacto de asignatura: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1.",
    "Conservar tipo curricular: obligatoria seriada.",
    "Conservar creditos: 8.",
    "Usar codigo local LDE-S3B1 cuando aplique.",
    "Usar ubicacion institucional Roma Norte, Ciudad de Mexico en metadatos.",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Mantener figura docente como dato no confirmado hasta validacion. [supuesto]",
    "Tratar fuentes heredadas de otros programas/modelos como provisionales si reaparecen. [supuesto]"
  ],
  "structure_rules": [
    "Estructurar entregas en: problema, marco conceptual-normativo, analisis propio, conclusion juridica.",
    "Usar ejes locales: problema juridico o social, conceptos y normas, producto solicitado, analisis propio y conclusion transferible.",
    "Conservar coherencia con programa analitico local.",
    "Incluir trazabilidad entre consigna, desarrollo y cierre.",
    "Transformar planeacion semanal en reporte, presentacion o producto visual segun consigna.",
    "Mantener la carpeta de materia como punto de entrada canonico.",
    "Verificar consistencia entre nombres de archivo, slug y referencias antes de compilar.",
    "Corregir en README nombres corruptos de reporte y carpeta de referencias.",
    "Corregir en README y programa analitico el placeholder dinamico del archivo .bib."
  ],
  "activity_rules": [
    "Adaptar reglas del origen solo si son compatibles con la materia destino. [supuesto]",
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Integrar fundamento juridico, evidencia y transferencia profesional.",
    "Mantener conclusion con criterio juridico propio en cada actividad.",
    "Evitar texto generico y vincular argumentos al problema juridico.",
    "No trasladar contenido de Filosofia del Derecho sin validar pertinencia. [supuesto]",
    "Registrar pendientes cuando falte consigna."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada intercambio de memoria.",
    "Revisar toda salida no estructurada antes de aplicar aguas abajo.",
    "Detener propagacion si faltan datos minimos de actividad.",
    "No propagar reglas dependientes de actividad sin consigna confirmada.",
    "Verificar identificacion de consigna, rubrica y producto solicitado.",
    "Comprobar respaldo verificable para afirmaciones juridicas relevantes.",
    "Confirmar integridad academica: sin afirmaciones sin sustento.",
    "Corregir placeholders y nombres corruptos en README/programa antes de reutilizar plantilla.",
    "Verificar que el .tex use el .bib local canonico y no placeholders.",
    "Compilar sin errores y sin referencias rotas."
  ],
  "latex_rules": [
    "Usar plantilla base de reporte de la materia como punto de partida.",
    "Conservar documentclass article en spanish, letterpaper y oneside salvo consigna distinta.",
    "Completar metadatos institucionales y academicos antes de redactar.",
    "Usar titulo, subtitulo, asignatura y codigo local coherentes con la actividad.",
    "Actualizar documentsubtitle de Actividad X al numero real de actividad.",
    "Mantener espanol academico y terminologia juridica consistente.",
    "Mantener figura docente como Nombre por definir hasta confirmacion. [supuesto]",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Usar el archivo bibliografico local derechos-de-la-persona-y-familia.bib.",
    "Evitar placeholders en nombres de archivos LaTeX, BibTeX y rutas.",
    "Compilar sin errores y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como fuente canonica local.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar malla curricular de Derecho como fuente curricular local.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Agregar solo fuentes verificables y pertinentes a cada actividad.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Reemplazar placeholders dinamicos de nombre .bib por slug canonico fijo."
  ],
  "propagation_hints": [
    "Propagar solo despues de pasar quality gates.",
    "Mantener compresion union-dedupe sin perdida y sin regresion.",
    "Aplicar normalizacion manual previa cuando reaparezcan salidas no estructuradas.",
    "Si reaparece salida no JSON parseable, forzar normalizacion manual antes de propagar.",
    "Propagar reglas institucionales, bibliograficas y de calidad comunes a UnADM.",
    "Propagar reglas de actividad solo con compatibilidad juridica confirmada.",
    "No propagar reglas dependientes de consigna no confirmada.",
    "Etiquetar reglas heredadas provisionales hasta validacion en Derecho.",
    "Priorizar reglas institucionales UnADM sobre reglas de origen no juridicas.",
    "Registrar origen y destino en consolidaciones laterales.",
    "Ciclo 20: mantener normalizacion manual previa si se reutiliza."
  ],
  "open_questions": [
    "Falta consigna especifica de actividad-1 de Filosofia del Derecho para mapear reglas exactas.",
    "Confirmar consigna especifica de la actividad destino en Derechos de la persona y familia.",
    "Confirmar si existe plantilla formal de presentacion obligatoria para esta materia.",
    "Confirmar datos vigentes de figura docente y criterios de evaluacion. [supuesto]",
    "Confirmar vigencia de nombre de alumno y matricula en plantilla. [supuesto]",
    "Confirmar si LDE-S3B1 debe aparecer en todos los productos.",
    "Validar correccion definitiva de nombres corruptos en README (reporte/referencias).",
    "Validar sustitucion definitiva del placeholder .bib en README y programa analitico.",
    "Confirmar si el slug del .bib debe resolverse desde plantilla generadora o quedar fijo. [supuesto]"
  ]
}