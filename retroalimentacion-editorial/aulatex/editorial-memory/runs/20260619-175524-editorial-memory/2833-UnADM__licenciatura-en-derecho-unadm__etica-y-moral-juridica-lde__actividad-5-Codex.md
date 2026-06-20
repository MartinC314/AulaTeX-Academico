{
  "summary": [
    "Se mantiene estado operativo: no hubo insumo parseable nuevo desde Actividad 1 en este ciclo.",
    "Se conserva trazabilidad recursiva entre origen y destino para ciclo 5.",
    "Se aplica compresion lossless por union y deduplicacion semantica sin recorte.",
    "Se normalizan incidencias de parseo con plantilla unica por ciclo.",
    "Supuesto: sin entrada parseable no se promueven reglas tematicas nuevas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM y Licenciatura en Derecho en cada entrega.",
    "Alinear la actividad a Etica y Moral juridica: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Registrar fuente de cada injerto de memoria con ruta origen y destino.",
    "Marcar como provisional toda regla derivada de salida no parseable.",
    "No promover reglas provisionales a canon sin validacion manual."
  ],
  "structure_rules": [
    "Responder siempre en JSON parseable y valido contra el esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar secciones existentes y agregar solo mejoras verificables.",
    "Aplicar compresion lossless por union y deduplicacion, sin recorte."
  ],
  "activity_rules": [
    "Alinear productos a la pauta editorial de la asignatura.",
    "Incluir problema, conceptos, analisis propio y conclusion juridica transferible.",
    "Mantener integridad academica y citas verificables en cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion aguas abajo si la salida no es JSON parseable.",
    "Revisar manualmente respuestas no estructuradas antes de consolidar memoria.",
    "Verificar que no se eliminen reglas utiles previas al fusionar.",
    "Validar ausencia de duplicados semanticos despues de fusionar."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reportes y presentaciones LaTeX de la asignatura.",
    "No introducir comandos o paquetes sin necesidad verificable."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos bibliograficos.",
    "Agregar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "Conservar trazabilidad entre citas en texto y entradas .bib.",
    "Supuesto: deduplicar claves bibliograficas duplicadas solo con validacion manual previa."
  ],
  "propagation_hints": [
    "Propagar solo reglas validadas y mantener incidencias como estado operativo.",
    "Usar plantilla unica por ciclo: si persiste fallo de parseo, marcar requiere normalizacion manual.",
    "Mantener trazabilidad recursiva entre actividad origen y destino en cada ciclo.",
    "Ciclo 5 requiere normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Falta contenido parseable de Actividad 1 para extraer reglas tematicas concretas.",
    "Confirmar si se desea bloqueo automatico tras N fallos consecutivos.",
    "Confirmar criterio operativo para depurar entradas .bib duplicadas sin perder trazabilidad."
  ]
}