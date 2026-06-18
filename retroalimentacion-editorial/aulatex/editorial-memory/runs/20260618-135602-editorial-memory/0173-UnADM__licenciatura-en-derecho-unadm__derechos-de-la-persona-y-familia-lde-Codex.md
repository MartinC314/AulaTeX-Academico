{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Asignatura de Licenciatura en Derecho, semestre 3, bloque 1.",
    "Materia obligatoria seriada de 8 creditos segun malla curricular local.",
    "La carpeta local es punto de entrada canonico de la asignatura.",
    "Se conserva alerta institucional: hubo salida no JSON parseable en origen heredado.",
    "Se prioriza normalizacion manual previa cuando reaparezcan salidas no estructuradas.",
    "Plantilla de reporte local define alumno Martin Jonathan de la Cruz y matricula ES2611202040. [supuesto verificar vigencia]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, redaccion y metadatos.",
    "Usar nombre de asignatura exacto: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1.",
    "Conservar tipo curricular: obligatoria seriada.",
    "Conservar creditos: 8.",
    "Usar codigo de curso local LDE-S3B1 cuando aplique.",
    "Usar ubicacion institucional Roma Norte, Ciudad de Mexico en metadatos.",
    "Mantener figura docente como dato no confirmado hasta validacion. [supuesto]",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Tratar fuentes heredadas de otros programas como provisionales si reaparecen. [supuesto]"
  ],
  "structure_rules": [
    "Estructurar cada entrega en: problema, marco conceptual-normativo, analisis propio, conclusion juridica.",
    "Conservar coherencia con programa analitico local de la materia.",
    "Incluir trazabilidad entre consigna, desarrollo y cierre.",
    "Usar ejes locales: problema juridico o social, conceptos y normas, producto solicitado, analisis propio, conclusion transferible.",
    "Transformar planeacion semanal en reportes, presentaciones o productos visuales segun consigna.",
    "Mantener la carpeta de materia como punto de entrada canonico.",
    "Verificar consistencia entre nombres de archivo, slug y referencias antes de compilar.",
    "Corregir en README nombres corruptos de reporte y carpeta de referencias."
  ],
  "activity_rules": [
    "Adaptar reglas de actividad origen solo si son compatibles con materia destino. [supuesto]",
    "No trasladar contenido de Filosofia del Derecho sin validacion de pertinencia. [supuesto]",
    "Mantener conclusion con criterio juridico propio en toda actividad.",
    "Evitar texto generico; vincular argumentos al problema juridico planteado.",
    "Integrar fundamento juridico, evidencia y transferencia profesional.",
    "Registrar pendientes de consigna faltante en preguntas abiertas."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada intercambio de memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Detener propagacion si faltan datos minimos de actividad.",
    "Verificar que la consigna, rubrica y producto solicitado esten identificados.",
    "Confirmar integridad academica: sin afirmaciones sin sustento.",
    "Comprobar que cada afirmacion juridica relevante tenga respaldo verificable.",
    "Verificar que el .tex use el .bib local y no placeholders antes de compilar.",
    "Corregir placeholders de slug .bib en README y programa analitico antes de reutilizar plantilla."
  ],
  "latex_rules": [
    "Usar plantilla base de reporte de la materia como punto de partida.",
    "Conservar documentclass article en espanol y letterpaper salvo consigna distinta.",
    "Conservar opcion oneside salvo consigna distinta.",
    "Completar metadatos institucionales y academicos antes de redactar contenido.",
    "Usar titulo, subtitulo, asignatura y codigo local coherentes con la actividad.",
    "Actualizar documentsubtitle de Actividad X al numero real.",
    "Mantener espanol academico y consistencia terminologica juridica.",
    "Compilar sin errores y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar archivo local derechos-de-la-persona-y-familia.bib como fuente canonica.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a la actividad.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Reemplazar placeholders dinamicos de nombre .bib por slug canonico fijo."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de calidad.",
    "Aplicar compresion union-dedupe sin perdida y sin regresion.",
    "Mantener reglas institucionales estables como base comun.",
    "Etiquetar reglas heredadas provisionales hasta confirmacion en Derecho.",
    "No propagar reglas dependientes de consigna no confirmada.",
    "Si reaparece salida no JSON parseable, forzar normalizacion manual antes de propagar."
  ],
  "open_questions": [
    "Falta consigna especifica de actividad-1 de Filosofia del Derecho para mapear reglas exactas.",
    "Confirmar consigna especifica de la actividad destino en Derechos de la persona y familia.",
    "Confirmar si existe plantilla formal de presentacion obligatoria para esta materia.",
    "Confirmar datos de figura docente y criterios de evaluacion vigentes.",
    "Confirmar si el codigo LDE-S3B1 es requerido en todos los productos.",
    "Confirmar si los datos de alumno y matricula de la plantilla local siguen vigentes.",
    "Validar correccion definitiva de rutas y slugs corruptos en README local.",
    "Validar sustitucion definitiva del placeholder de .bib en README y programa analitico."
  ]
}