{
  "summary": [
    "Se preserva historial de fallas de parseo JSON en Actividad 4.",
    "Se mantiene compresion union-dedupe lossless.",
    "No hay reglas nuevas transferibles desde origen por falta de JSON valido [supuesto].",
    "Se preservan reglas minimas verificables del contexto local de la asignatura.",
    "Se confirma encuadre institucional UnADM Derecho: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se confirma carpeta de asignatura como punto de entrada canonico.",
    "Se confirma estructura editorial: reporte, presentacion y archivo BibTeX.",
    "Se mantiene riesgo de integridad del .bib por entrada truncada detectada [supuesto].",
    "Se mantiene deteccion de duplicados bibliograficos equivalentes como tarea de depuracion."
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
    "Incluir cierre argumentativo transferible a la practica juridica.",
    "Asegurar coherencia entre actividad, reporte y presentacion cuando coexistan.",
    "Evitar secciones vacias en memoria persistente.",
    "Alinear estructura con ejes del programa analitico de la materia.",
    "Integrar el producto solicitado por la planeacion semanal dentro de la estructura base."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 al encuadre de Etica y Moral juridica.",
    "Explicar diferencia operativa entre etica, moral y norma juridica cuando aplique [supuesto].",
    "Sostener postura propia con fundamento academico verificable.",
    "Vincular el producto con un problema juridico o social concreto.",
    "Ajustar el producto al formato solicitado por la planeacion semanal [supuesto]."
  ],
  "quality_gates": [
    "Revisar respuesta no estructurada antes de aplicar aguas abajo.",
    "Rechazar salidas sin JSON parseable antes de fusionar memoria.",
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
    "Evitar comandos no estandar que rompan compilacion [supuesto].",
    "Sincronizar contenido entre reporte y presentacion cuando ambos existan."
  ],
  "bibliography_rules": [
    "Usar la bibliografia local de la asignatura como base inicial.",
    "No inventar fuentes ni metadatos bibliograficos.",
    "Depurar duplicados de entradas BibTeX equivalentes cuando se edite.",
    "Agregar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "Preferir una clave canonica por obra y mantener alias solo si hay dependencia tecnica [supuesto].",
    "Marcar entradas BibTeX truncadas o incompletas para correccion antes de citar [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas por JSON correcto.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Mantener nota de normalizacion manual mientras persistan salidas no parseables.",
    "Conservar historial de ciclos para auditoria editorial.",
    "Priorizar reglas del contexto local cuando el origen sea incompleto [supuesto].",
    "Ciclo 1 a 20 requiere normalizacion manual si se reutiliza.",
    "Ciclo 21 requiere normalizacion manual si se reutiliza [supuesto]."
  ],
  "open_questions": [
    "Falta JSON valido del origen Actividad 1 para transferencia completa.",
    "Se requiere confirmar rubrica exacta de la Actividad 4 para afinar reglas.",
    "Se requiere definir politica formal de deduplicacion BibTeX por clave canonica.",
    "Se debe confirmar plantilla LaTeX oficial de actividad en esta materia.",
    "Se debe completar y validar el archivo .bib local por posible truncamiento [supuesto]."
  ]
}