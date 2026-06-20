{
  "summary": [
    "Se mantiene estado de contingencia por falta de JSON parseable verificable en el origen.",
    "Se conserva normalizacion minima para propagacion segura y trazable.",
    "Se aplica deduplicacion semantica lossless sin recorte.",
    "Se preserva alineacion con pauta editorial local de Etica y Moral juridica.",
    "No se detectan reglas nuevas verificables transferibles desde el origen en este ciclo. [Supuesto]"
  ],
  "identity_rules": [
    "Mantener identidad UnADM y contexto de Licenciatura en Derecho.",
    "Mantener contexto de asignatura Etica y Moral juridica: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Etiquetar toda regla importada con origen y ciclo cuando aplique.",
    "Registrar fuente de cada consolidacion con ruta origen y destino.",
    "Conservar trazabilidad de incidencias de parseo por modelo y actividad.",
    "Mantener fuente provisional por modelo cuando no exista JSON parseable verificable.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: Auto (model-router) desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido conforme al esquema requerido.",
    "Usar listas con frases cortas, accionables y sin duplicados.",
    "No eliminar reglas utiles previas; solo unir y deduplicar.",
    "Aplicar compresion lossless por deduplicacion, no por recorte.",
    "Marcar supuestos explicitamente con etiqueta [Supuesto]."
  ],
  "activity_rules": [
    "Alinear cada entrega a la pauta editorial local: problema, conceptos, analisis propio y conclusion juridica.",
    "Ajustar el producto solicitado a la planeacion semanal de la asignatura.",
    "Integrar fundamento juridico, evidencia y transferencia profesional en cada producto.",
    "Mantener integridad academica y citas verificables en cada actividad."
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
    "No agregar reglas LaTeX no verificadas por artefactos locales. [Supuesto]",
    "Sin reglas LaTeX nuevas verificables desde el origen en este ciclo. [Supuesto]"
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables disponibles.",
    "Conservar trazabilidad entre citas en texto y entradas .bib.",
    "Agregar fuentes especificas de actividad al archivo etica-y-moral-juridica.bib cuando corresponda.",
    "Revisar y deduplicar claves bibliograficas duplicadas sin perder informacion."
  ],
  "propagation_hints": [
    "Aplicar propagacion recursiva solo tras pasar compuerta de JSON valido.",
    "Mantener estado de contingencia hasta recibir origen con contenido estructurado verificable.",
    "Conservar historial de ciclos sin multiplicar entradas equivalentes.",
    "Normalizar incidencias repetidas en una sola regla general deduplicada.",
    "Usar normalizacion manual en ciclos con salida no parseable."
  ],
  "open_questions": [
    "Confirmar si existe contenido estructurado util en el origen para extraer reglas de Actividad 1.",
    "Definir formato canonico unico para registro de errores de parseo por modelo.",
    "Definir criterio operativo para deduplicar entradas .bib duplicadas en la asignatura."
  ]
}