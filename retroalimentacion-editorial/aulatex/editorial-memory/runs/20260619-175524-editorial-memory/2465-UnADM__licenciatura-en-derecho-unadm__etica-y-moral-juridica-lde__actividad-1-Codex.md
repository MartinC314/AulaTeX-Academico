{
  "summary": [
    "Se conserva estado de contingencia: no hubo JSON parseable previo en Actividad 1.",
    "Se agrega normalizacion minima para permitir propagacion segura sin perder trazabilidad.",
    "No hay reglas academicas transferibles verificables desde el origen en este ciclo. [Supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM y contexto de Licenciatura en Derecho.",
    "Etiquetar toda regla importada con origen y ciclo cuando aplique.",
    "Conservar trazabilidad de incidencias de parseo por modelo y actividad."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido conforme al esquema requerido.",
    "Usar listas de frases cortas, accionables y sin duplicados.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "activity_rules": [
    "Alinear cada entrega a la pauta editorial local: problema, conceptos, analisis propio y conclusion juridica.",
    "Mantener integridad academica y citas verificables en cada actividad."
  ],
  "quality_gates": [
    "Validar parseo JSON antes de guardar memoria.",
    "Bloquear propagacion aguas abajo si la salida no cumple esquema.",
    "Registrar incidencias de formato como resumen operativo."
  ],
  "latex_rules": [
    "Sin reglas LaTeX nuevas verificables en este ciclo. [Supuesto]"
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables disponibles.",
    "Agregar fuentes especificas de actividad al archivo .bib de la asignatura cuando corresponda."
  ],
  "propagation_hints": [
    "Normalizar incidencias repetidas en una sola regla general deduplicada.",
    "Aplicar propagacion recursiva solo tras pasar compuerta de JSON valido.",
    "Conservar historial de ciclos sin multiplicar entradas equivalentes."
  ],
  "open_questions": [
    "Confirmar si existe contenido estructurado util en el origen para extraer reglas de Actividad 1.",
    "Definir formato canonico de registro de errores de parseo por modelo."
  ]
}