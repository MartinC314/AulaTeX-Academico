{
  "summary": [
    "Se conserva estado previo y se mantiene compresion lossless por deduplicacion.",
    "Se consolida base editorial desde README y programa analitico de Etica y Moral juridica.",
    "Se preservan reglas utiles previas y se agregan mejoras verificables sin recorte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Alinear contenido con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar tono academico-juridico y cerrar con criterio propio.",
    "Tomar la carpeta de Etica y Moral juridica como punto de entrada canonico.",
    "[Supuesto] Actividad 6 pertenece formalmente a Etica y Moral juridica."
  ],
  "structure_rules": [
    "Estructurar cada producto con problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Ajustar estructura al producto solicitado por la planeacion semanal.",
    "Asegurar coherencia entre objetivo, desarrollo y cierre argumentativo.",
    "Mantener secciones reutilizables para reporte y presentacion."
  ],
  "activity_rules": [
    "Conservar integridad academica y trazabilidad de afirmaciones.",
    "Incluir postura argumentada, no solo resumen.",
    "Sustentar afirmaciones con fuentes declaradas y verificables.",
    "Traducir el contenido a aplicacion profesional juridica cuando proceda."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de cualquier propagacion.",
    "No propagar salidas no estructuradas sin normalizacion manual.",
    "Confirmar que no se eliminen reglas utiles previas en cada fusion.",
    "Verificar consistencia entre consigna de actividad, estructura y conclusion.",
    "Marcar explicitamente supuestos cuando falte dato formal."
  ],
  "latex_rules": [
    "Preparar contenido compatible con reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Usar secciones claras y estables para compilacion y reutilizacion.",
    "Evitar paquetes o comandos no justificados por la consigna.",
    "Mantener consistencia terminologica entre .tex, programa analitico y actividad."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de la actividad en etica-y-moral-juridica.bib.",
    "No inventar fuentes ni completar datos bibliograficos sin respaldo.",
    "Priorizar fuentes institucionales UnADM y bibliografia base de la asignatura.",
    "Deduplicar entradas equivalentes por clave canonica sin perder referencia cruzada.",
    "Marcar entradas incompletas para curacion editorial antes de citar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Conservar banderas de falla historicas como trazabilidad, no como regla operativa central.",
    "Reemplazar en ciclos futuros reglas provisionales por reglas verificadas de actividad 6.",
    "Aplicar union-dedupe lossless en cada ciclo de fusion.",
    "Si aparece conflicto, priorizar reglas locales verificadas del destino."
  ],
  "open_questions": [
    "Confirmar consigna exacta y formato de entrega de la Actividad 6.",
    "Definir plantilla LaTeX objetivo para Actividad 6: reporte, presentacion u otro.",
    "Establecer criterio formal de clave canonica para deduplicar .bib.",
    "Completar y validar campos faltantes en entradas .bib locales."
  ]
}