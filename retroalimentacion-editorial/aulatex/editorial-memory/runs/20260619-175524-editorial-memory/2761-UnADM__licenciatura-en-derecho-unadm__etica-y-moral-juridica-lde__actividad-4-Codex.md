{
  "summary": [
    "Se conserva historial de fallas de parseo JSON en Actividad 4.",
    "Se mantiene compresion por union-dedupe sin perdida.",
    "No hay reglas transferibles nuevas desde origen por falta de JSON valido [supuesto].",
    "Se preservan reglas verificables del contexto local de la asignatura.",
    "Se confirma encuadre institucional: UnADM Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se confirma la carpeta de asignatura como punto de entrada canonico.",
    "Se confirma estructura editorial de productos: reporte, presentacion y archivo BibTeX de la materia.",
    "Se mantiene riesgo de integridad en .bib por entrada truncada detectada [supuesto].",
    "Se detectan duplicados bibliograficos equivalentes en el .bib local y se mantiene como tarea de depuracion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en cada entrega.",
    "Alinear contenido con Licenciatura en Derecho, semestre 1, bloque 2.",
    "Conservar trazabilidad de fuente y ciclo en cada propagacion.",
    "Etiquetar como provisional toda regla derivada de salidas no parseables.",
    "Usar la carpeta de la asignatura como punto de entrada canonico."
  ],
  "structure_rules": [
    "Usar estructura base: problema, conceptos/fuentes, analisis propio, conclusion juridica.",
    "Integrar el producto solicitado por la planeacion semanal dentro de la estructura base.",
    "Alinear estructura con ejes del programa analitico de la materia.",
    "Incluir cierre argumentativo transferible a la practica juridica.",
    "Asegurar coherencia entre actividad, reporte y presentacion cuando coexistan.",
    "Evitar secciones vacias en memoria persistente."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 al encuadre de Etica y Moral juridica.",
    "Vincular el producto con un problema juridico o social concreto.",
    "Sostener postura propia con fundamento academico verificable.",
    "Explicar diferencia operativa entre etica, moral y norma juridica cuando aplique [supuesto].",
    "Ajustar el producto al formato solicitado por la planeacion semanal [supuesto]."
  ],
  "quality_gates": [
    "Rechazar salidas sin JSON parseable antes de fusionar memoria.",
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Validar deduplicacion exacta para evitar perdida de reglas utiles.",
    "Marcar supuestos explicitamente cuando falten datos del origen.",
    "Verificar que toda afirmacion academica tenga respaldo en fuente citada.",
    "Verificar integridad sintactica del archivo .bib antes de citar [supuesto].",
    "Registrar y corregir entradas BibTeX truncadas antes de compilacion final [supuesto]."
  ],
  "latex_rules": [
    "Redactar entregables en LaTeX con estructura academica clara.",
    "Mantener compatibilidad con archivos canonicos de la materia.",
    "Usar citas y referencias con claves BibTeX existentes.",
    "Sincronizar contenido entre reporte y presentacion cuando ambos existan.",
    "Evitar comandos no estandar que rompan compilacion [supuesto]."
  ],
  "bibliography_rules": [
    "Usar la bibliografia local de la asignatura como base inicial.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Agregar nuevas fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "Depurar duplicados de entradas BibTeX equivalentes cuando se edite.",
    "Preferir una clave canonica por obra y mantener alias solo si hay dependencia tecnica [supuesto].",
    "Marcar entradas BibTeX truncadas o incompletas para correccion antes de citar [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas por JSON correcto.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Conservar historial de ciclos para auditoria editorial.",
    "Mantener nota de normalizacion manual mientras persistan salidas no parseables.",
    "Priorizar reglas del contexto local cuando el origen sea incompleto [supuesto].",
    "Ciclo 9 necesita normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Falta JSON valido del origen Actividad 1 para transferencia completa.",
    "Se requiere confirmar rubrica exacta de la Actividad 4 para afinar reglas.",
    "Se requiere definir politica formal de deduplicacion BibTeX (clave canonica).",
    "Se debe confirmar plantilla LaTeX oficial de actividad en esta materia.",
    "Se debe completar y validar el archivo .bib local por posible truncamiento [supuesto]."
  ]
}