{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Se conserva alerta institucional: hubo salida no JSON parseable en origen heredado.",
    "Se prioriza normalizacion manual en ciclo 1 antes de propagacion automatica.",
    "Asignatura de Licenciatura en Derecho, semestre 3, bloque 1.",
    "Materia obligatoria seriada de 8 creditos segun malla curricular local.",
    "La carpeta local es punto de entrada canonico de la asignatura.",
    "Plantilla de reporte local define alumno Martin Jonathan de la Cruz y matricula ES2611202040. [supuesto verificar vigencia]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, redaccion y metadatos.",
    "Usar nombre de asignatura exacto: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1.",
    "Marcar como supuesto cualquier dato docente no confirmado.",
    "Conservar tipo curricular: obligatoria seriada.",
    "Conservar creditos: 8.",
    "Usar codigo de curso local LDE-S3B1 cuando aplique.",
    "Tratar fuente Codex desde ingenieria-en-sistemas-computacionales como provisional si reaparece.",
    "Usar ubicacion institucional Roma Norte, Ciudad de Mexico en metadatos."
  ],
  "structure_rules": [
    "Estructurar cada entrega en: problema, marco conceptual-normativo, analisis propio, conclusion juridica.",
    "Conservar coherencia con programa analitico local de la materia.",
    "Incluir trazabilidad entre consigna, desarrollo y cierre.",
    "Verificar que nombres de archivo y slug sean consistentes antes de compilar.",
    "Usar ejes locales: problema juridico o social, conceptos y normas, producto solicitado, analisis propio, conclusion transferible.",
    "Transformar planeacion semanal en reportes, presentaciones o productos visuales segun consigna.",
    "Corregir rutas corruptas en README antes de reutilizar plantilla.",
    "Mantener la carpeta de materia como punto de entrada canonico.",
    "Corregir nombres de archivo con saltos de linea en README: reporte, referencias y carpeta de referencias."
  ],
  "activity_rules": [
    "Adaptar reglas de actividad origen solo si son compatibles con materia destino. [supuesto]",
    "Mantener conclusion con criterio juridico propio en toda actividad.",
    "Evitar texto generico; vincular argumentos al problema juridico planteado.",
    "Registrar pendientes de consigna faltante en preguntas abiertas.",
    "Integrar fundamento juridico, evidencia y transferencia profesional.",
    "No trasladar contenido de Filosofia del Derecho sin validacion de pertinencia. [supuesto]"
  ],
  "quality_gates": [
    "Validar JSON parseable en cada intercambio de memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar integridad academica: sin afirmaciones sin sustento.",
    "Detener propagacion si faltan datos minimos de actividad.",
    "Verificar que la consigna, rubrica y producto solicitado esten identificados.",
    "Comprobar que cada afirmacion juridica relevante tenga respaldo verificable.",
    "Revisar nombres corruptos: reporte, referencias y archivo .bib en README local.",
    "Verificar que el .tex use el .bib local y no un placeholder antes de compilar."
  ],
  "latex_rules": [
    "Usar plantilla base de reporte de la materia como punto de partida.",
    "Completar metadatos institucionales y academicos antes de redactar contenido.",
    "Mantener espanol academico y consistencia terminologica juridica.",
    "Compilar sin errores y sin referencias rotas.",
    "Conservar documentclass article en espanol y letterpaper salvo consigna distinta.",
    "Usar titulo, subtitulo, asignatura y codigo local coherentes con la actividad.",
    "Mantener figura docente como Nombre por definir hasta confirmacion.",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Conservar opcion oneside salvo consigna distinta.",
    "Actualizar documentsubtitle de Actividad X al numero de actividad real."
  ],
  "bibliography_rules": [
    "Usar archivo local derechos-de-la-persona-y-familia.bib como fuente canonica.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a la actividad.",
    "No inventar referencias; marcar ausencias como pendiente.",
    "Conservar malla curricular de Derecho como fuente curricular local.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "Corregir placeholder de nombre .bib en programa analitico si se reutiliza.",
    "Conservar entradas base: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de calidad.",
    "En ciclo 1, aplicar normalizacion manual previa a reutilizacion.",
    "Mantener compresion union-dedupe sin perdida y sin regresion.",
    "Etiquetar reglas heredadas provisionales hasta confirmacion en Derecho.",
    "No propagar reglas dependientes de actividad sin consigna confirmada.",
    "Priorizar reglas institucionales UnADM sobre reglas de origen no juridicas."
  ],
  "open_questions": [
    "Falta consigna especifica de actividad-1 de Filosofia del Derecho para mapear reglas exactas.",
    "Confirmar si existe plantilla formal de presentacion obligatoria para esta materia.",
    "Confirmar datos de figura docente y criterios de evaluacion vigentes.",
    "Revisar y corregir posibles rutas/slug corruptos en README local.",
    "Confirmar consigna especifica de la actividad destino en Derechos de la persona y familia.",
    "Confirmar si el codigo LDE-S3B1 es requerido en todos los productos.",
    "Confirmar si los datos de alumno y matricula de la plantilla local siguen vigentes.",
    "Confirmar si el slug del .bib en README y programa analitico debe resolverse desde plantilla generadora."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derechos-de-la-persona-y-familia-lde"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}