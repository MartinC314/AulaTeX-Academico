{
  "summary": [
    "Se conserva contingencia por falta de JSON parseable previo en el origen.",
    "Se mantiene normalizacion minima para propagacion segura y trazable.",
    "Se refuerza alineacion con pauta editorial local de la asignatura destino.",
    "No se detectan reglas nuevas verificables del origen en este ciclo. [Supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM y contexto de Licenciatura en Derecho.",
    "Mantener contexto de asignatura Etica y Moral juridica (semestre 1, bloque 2, obligatoria, 8 creditos).",
    "Etiquetar toda regla importada con origen y ciclo cuando aplique.",
    "Conservar trazabilidad de incidencias de parseo por modelo y actividad.",
    "Registrar fuente de cada consolidacion con ruta origen y destino."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido conforme al esquema requerido.",
    "Usar listas de frases cortas, accionables y sin duplicados.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Aplicar compresion lossless por deduplicacion, no por recorte.",
    "Marcar supuestos explicitamente con etiqueta [Supuesto]."
  ],
  "activity_rules": [
    "Alinear cada entrega a la pauta editorial local: problema, conceptos, analisis propio y conclusion juridica.",
    "Integrar fundamento juridico, evidencia y transferencia profesional en cada producto.",
    "Mantener integridad academica y citas verificables en cada actividad.",
    "Ajustar el producto solicitado a la planeacion semanal de la asignatura."
  ],
  "quality_gates": [
    "Validar parseo JSON antes de guardar memoria.",
    "Bloquear propagacion aguas abajo si la salida no cumple esquema.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Registrar incidencias de formato como resumen operativo.",
    "Verificar deduplicacion semantica sin perder reglas validas."
  ],
  "latex_rules": [
    "Mantener consistencia editorial entre reporte y presentacion de la asignatura.",
    "No agregar reglas LaTeX no verificadas por artefactos locales. [Supuesto]"
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables disponibles.",
    "Agregar fuentes especificas de actividad al archivo .bib de la asignatura cuando corresponda.",
    "Conservar trazabilidad entre citas en texto y entradas .bib.",
    "Revisar y deduplicar claves bibliograficas duplicadas sin perder informacion."
  ],
  "propagation_hints": [
    "Aplicar propagacion recursiva solo tras pasar compuerta de JSON valido.",
    "Normalizar incidencias repetidas en una sola regla general deduplicada.",
    "Conservar historial de ciclos sin multiplicar entradas equivalentes.",
    "Mantener estado de contingencia hasta recibir origen con contenido estructurado verificable."
  ],
  "open_questions": [
    "Confirmar si el origen ya dispone de JSON parseable util para extraer reglas academicas.",
    "Definir formato canonico unico para registro de errores de parseo por modelo.",
    "Definir criterio operativo para deduplicar entradas .bib duplicadas en la asignatura."
  ]
}