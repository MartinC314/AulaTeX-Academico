{
  "summary": [
    "Materia destino con identidad UnADM y enfoque juridico aplicado.",
    "Se conserva alerta institucional: hubo salida no JSON parseable en origen heredado.",
    "Se prioriza normalizacion manual en ciclo 1 antes de propagacion automatica."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en portada, redaccion y metadatos.",
    "Usar nombre de asignatura exacto: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1.",
    "Marcar como supuesto cualquier dato docente no confirmado."
  ],
  "structure_rules": [
    "Estructurar cada entrega en: problema, marco conceptual-normativo, analisis propio, conclusion juridica.",
    "Conservar coherencia con programa analitico local de la materia.",
    "Incluir trazabilidad entre consigna, desarrollo y cierre.",
    "Verificar que nombres de archivo y slug sean consistentes antes de compilar."
  ],
  "activity_rules": [
    "Adaptar reglas de actividad origen solo si son compatibles con materia destino. [supuesto]",
    "Mantener conclusion con criterio juridico propio en toda actividad.",
    "Evitar texto generico; vincular argumentos al problema juridico planteado.",
    "Registrar pendientes de consigna faltante en preguntas abiertas."
  ],
  "quality_gates": [
    "Validar JSON parseable en cada intercambio de memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Confirmar integridad academica: sin afirmaciones sin sustento.",
    "Detener propagacion si faltan datos minimos de actividad."
  ],
  "latex_rules": [
    "Usar plantilla base de reporte de la materia como punto de partida.",
    "Completar metadatos institucionales y academicos antes de redactar contenido.",
    "Mantener espanol academico y consistencia terminologica juridica.",
    "Compilar sin errores y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar archivo local derechos-de-la-persona-y-familia.bib como fuente canonica.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Agregar solo fuentes verificables y pertinentes a la actividad.",
    "No inventar referencias; marcar ausencias como pendiente."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo tras validacion de calidad.",
    "En ciclo 1, aplicar normalizacion manual previa a reutilizacion.",
    "Mantener compresion union-dedupe sin perdida y sin regresion.",
    "Etiquetar reglas heredadas provisionales hasta confirmacion en Derecho."
  ],
  "open_questions": [
    "Falta consigna especifica de actividad-1 de Filosofia del Derecho para mapear reglas exactas.",
    "Confirmar si existe plantilla formal de presentacion obligatoria para esta materia.",
    "Confirmar datos de figura docente y criterios de evaluacion vigentes.",
    "Revisar y corregir posibles rutas/slug corruptos en README local."
  ]
}