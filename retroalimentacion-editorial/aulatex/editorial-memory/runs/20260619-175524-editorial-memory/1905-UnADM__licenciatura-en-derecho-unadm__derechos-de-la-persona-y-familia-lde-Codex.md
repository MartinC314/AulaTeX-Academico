{
  "summary": [
    "Materia destino UnADM con enfoque juridico aplicado.",
    "Asignatura: Derechos de la persona y familia, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "La carpeta local es punto de entrada canonico.",
    "Se mantiene alerta por salidas no JSON parseable heredadas (Codex, GPT-Pro, Auto model-router y Claude Foundry).",
    "Se mantiene normalizacion manual previa cuando reaparezcan salidas no estructuradas.",
    "Consolidacion ciclo 15 completada con compresion union-dedupe sin perdida y sin regresion.",
    "Se detectan placeholders dinamicos y nombres corruptos en README/programa para correccion."
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
    "Conservar coherencia con programa analitico local de la materia.",
    "Incluir trazabilidad entre consigna, desarrollo y cierre.",
    "Usar ejes locales: problema juridico o social, conceptos y normas, producto solicitado, analisis propio, conclusion transferible.",
    "Transformar planeacion semanal en reporte, presentacion o producto visual segun consigna.",
    "Mantener la carpeta de materia como punto de entrada canonico.",
    "Verificar consistencia entre nombres de archivo, slug y referencias antes de compilar.",
    "Corregir en README nombres de archivo corruptos de reporte y carpeta de referencias.",
    "Corregir en README y programa analitico el placeholder dinamico del archivo .bib."
  ],
  "activity_rules": [
    "Adaptar reglas del origen solo si son compatibles con la materia destino. [supuesto]",
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Mantener conclusion con criterio juridico propio en cada actividad.",
    "Evitar texto generico y vincular argumentos al problema juridico.",
    "Integrar fundamento juridico, evidencia y transferencia profesional.",
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
    "Usar el archivo bibliografico local derechos-de-la-persona-y-familia.bib.",
    "Evitar placeholders en nombres de archivos LaTeX, BibTeX y rutas.",
    "Mantener figura docente como Nombre por definir hasta confirmacion. [supuesto]",
    "No modificar datos de alumno o matricula sin verificacion local."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como fuente canonica local.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a cada actividad.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Reemplazar placeholders dinamicos de nombre .bib por slug canonico fijo."
  ],
  "propagation_hints": [
    "Propagar solo despues de pasar quality gates.",
    "Aplicar compresion union-dedupe sin perdida y sin regresion.",
    "Mantener reglas institucionales estables como base comun.",
    "Propagar reglas institucionales, bibliograficas y de calidad comunes a UnADM.",
    "Propagar reglas de actividad solo con compatibilidad juridica confirmada.",
    "No propagar reglas dependientes de consigna no confirmada.",
    "Etiquetar reglas heredadas provisionales hasta validacion en Derecho.",
    "Registrar origen y destino en consolidaciones laterales.",
    "Si reaparece salida no JSON parseable, forzar normalizacion manual antes de propagar.",
    "Ciclo 15: mantener normalizacion manual previa si se reutiliza."
  ],
  "open_questions": [
    "Falta consigna especifica de actividad-1 de Filosofia del Derecho para mapear reglas exactas.",
    "Confirmar consigna especifica de la actividad destino en Derechos de la persona y familia.",
    "Confirmar si existe plantilla formal de presentacion obligatoria para esta materia.",
    "Confirmar datos vigentes de figura docente y criterios de evaluacion.",
    "Confirmar vigencia de nombre de alumno y matricula en plantilla. [supuesto]",
    "Confirmar si LDE-S3B1 debe aparecer en todos los productos.",
    "Validar correccion definitiva de nombres corruptos en README (reporte/referencias).",
    "Validar sustitucion definitiva del placeholder .bib en README y programa analitico."
  ]
}