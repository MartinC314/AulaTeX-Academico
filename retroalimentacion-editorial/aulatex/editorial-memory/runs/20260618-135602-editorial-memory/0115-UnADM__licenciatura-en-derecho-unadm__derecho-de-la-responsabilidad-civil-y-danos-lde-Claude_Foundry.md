{
  "summary": [
    "Base institucional UnADM heredada y activa.",
    "Materia inicializada con base institucional UnADM y reglas locales verificables.",
    "Contexto local confirma Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "La memoria institucional heredada desde Codex es provisional.",
    "Se conserva alerta de salida no estructurada en ciclo 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Usar contexto de Licenciatura en Derecho.",
    "Usar enfoque de Derecho de la responsabilidad civil y danos.",
    "Marcar como supuesto cualquier dato no confirmado por guia oficial.",
    "Tratar la memoria institucional Codex heredada como fuente provisional."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Alinear cada producto a problema, conceptos o fuentes, analisis propio y conclusion juridica.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia local.",
    "Incluir ejes de trabajo del programa analitico cuando aplique.",
    "Corregir nombres truncados o plantillas interpoladas antes de usarlos como rutas finales."
  ],
  "activity_rules": [
    "Adaptar actividades heredadas de filosofia del derecho solo si son compatibles con responsabilidad civil y danos.",
    "No arrastrar contenido tematico de origen si no aplica al dano o la responsabilidad civil.",
    "Formular un problema juridico o social que active la responsabilidad civil.",
    "Integrar conceptos, normas, doctrina o datos pertinentes segun la actividad.",
    "Incluir transferencia a practica juridica en el cierre."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar consistencia con la pauta editorial de la materia.",
    "Verificar que toda afirmacion juridica tenga fuente o se marque como analisis propio.",
    "Aplicar control de no regresion sobre reglas utiles heredadas.",
    "Revisar respuestas no estructuradas antes de aplicarlas aguas abajo.",
    "Validar metadatos curriculares contra la malla local antes de citarlos.",
    "Detectar caracteres rotos, rutas truncadas y placeholders sin resolver en archivos locales."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX de la materia como base de reportes.",
    "Completar metadatos del documento por actividad sin cambiar identidad institucional.",
    "Usar titulo, subtitulo, asignatura, autor, universidad y departamento coherentes con la materia.",
    "Evitar caracteres rotos en rutas, nombres de archivo y comandos.",
    "Verificar que el archivo .bib local se llame derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Marcar como supuesto el codigo de curso LDE-S6B1 si no hay guia oficial que lo confirme.",
    "Supuesto: la plantilla .tex local termina truncada en authortable y debe completarse antes de compilar."
  ],
  "bibliography_rules": [
    "Agregar fuentes especificas de cada actividad en el .bib local de la materia.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "Conservar la malla curricular de Derecho como fuente curricular local.",
    "Separar fuentes verificables de analisis propio.",
    "No inventar fuentes; si falta referencia, registrar pregunta abierta.",
    "Entradas locales confirmadas: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas estables y no tematicas de una actividad puntual.",
    "En ciclo 1, aplicar normalizacion manual por antecedente de salida no estructurada.",
    "Usar compresion por union-dedupe sin recorte semantico.",
    "Propagar la alerta sobre rutas truncadas solo como control editorial general.",
    "No propagar detalles exclusivos de una actividad si no aplican a toda la materia."
  ],
  "open_questions": [
    "Confirmar si existe guia oficial de formato para actividades de esta materia.",
    "Confirmar convencion final de nombres de archivos con danos versus daños en todo el arbol.",
    "Validar plantilla .tex por posible truncamiento local antes de reutilizar.",
    "Confirmar si el codigo de curso LDE-S6B1 es oficial.",
    "Corregir en README los nombres truncados de reporte y referencias.",
    "Resolver el placeholder interpolado del nombre de archivo .bib en documentos locales (README y programa analitico)."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/derecho-de-la-responsabilidad-civil-y-danos-lde"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}