{
  "summary": [
    "Base institucional UnADM heredada y activa.",
    "Materia inicializada con base institucional UnADM y reglas locales verificables.",
    "Contexto local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Fuente curricular local confirmada: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Persisten incidencias tecnicas locales: salida no estructurada previa, rutas truncadas y placeholders sin resolver.",
    "Compresion aplicada por union-dedupe lossless.",
    "Origen de propagacion: Actividad 1 de Filosofia del derecho.",
    "Destino: Derecho de la responsabilidad civil y danos.",
    "La materia se inicializo sin memoria previa local.",
    "Antecedente institucional: salida sin JSON parseable desde Codex para UnADM.",
    "Antecedente local: salida sin JSON parseable desde GPT-Pro para esta materia.",
    "La memoria institucional heredada desde Codex es provisional.",
    "Ciclo de consolidacion: 2."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Usar contexto de Licenciatura en Derecho y materia de responsabilidad civil y danos.",
    "Usar enfoque de Derecho de la responsabilidad civil y danos.",
    "Marcar como supuesto cualquier dato no confirmado por guia oficial.",
    "Tratar memorias heredadas de Codex y GPT-Pro como fuentes provisionales.",
    "Fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "No cambiar la convencion local danos/daños sin confirmacion documental."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia local.",
    "Alinear cada producto a problema, conceptos o fuentes, analisis propio y conclusion juridica.",
    "Incluir ejes de trabajo del programa analitico cuando aplique.",
    "Corregir nombres truncados o plantillas interpoladas antes de usarlos como rutas finales.",
    "Usar el programa analitico local para orientar productos semanales.",
    "Respetar el producto solicitado por la planeacion de cada actividad."
  ],
  "activity_rules": [
    "Adaptar actividades heredadas de filosofia del derecho solo si son compatibles con responsabilidad civil y danos.",
    "No arrastrar contenido tematico de origen si no aplica al dano o a la responsabilidad civil.",
    "Formular un problema juridico o social que active la responsabilidad civil.",
    "Integrar conceptos, normas, doctrina o datos pertinentes segun la actividad.",
    "Separar fundamento juridico, evidencia y postura academica.",
    "Incluir transferencia a practica juridica en el cierre.",
    "Cerrar con criterio propio y conclusion juridica."
  ],
  "quality_gates": [
    "Validar que la salida sea JSON parseable antes de propagar.",
    "Revisar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Revisar consistencia con la pauta editorial de la materia.",
    "Verificar que toda afirmacion juridica tenga fuente o se marque como analisis propio.",
    "Aplicar control de no regresion sobre reglas utiles heredadas.",
    "Validar metadatos curriculares contra la malla local antes de citarlos.",
    "Detectar caracteres rotos, rutas truncadas y placeholders sin resolver en archivos locales.",
    "Validar compilacion LaTeX despues de completar la plantilla local."
  ],
  "latex_rules": [
    "Conservar plantilla LaTeX de la materia como base de reportes.",
    "Completar metadatos del documento por actividad sin cambiar identidad institucional.",
    "Usar titulo, subtitulo, asignatura, autor, universidad y departamento coherentes con la materia.",
    "Evitar caracteres rotos en rutas, nombres de archivo y comandos.",
    "Verificar que el archivo .bib local se llame derecho-de-la-responsabilidad-civil-y-danos.bib.",
    "Marcar como supuesto el codigo de curso LDE-S6B1 si no hay guia oficial que lo confirme.",
    "Supuesto: la plantilla .tex local esta truncada en authortable y debe completarse antes de compilar."
  ],
  "bibliography_rules": [
    "Agregar fuentes especificas de cada actividad en el .bib local de la materia.",
    "Conservar fuentes institucionales UnADM ya registradas.",
    "No inventar fuentes; si falta referencia, registrar pregunta abierta.",
    "Conservar la malla curricular de Derecho como fuente curricular local.",
    "Separar fuentes verificables de analisis propio.",
    "Entradas locales confirmadas: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas estables y no tematicas de una actividad puntual.",
    "Usar compresion por union-dedupe sin recorte semantico.",
    "Mantener alerta de normalizacion manual por antecedentes de salida no estructurada.",
    "Propagar control de rutas truncadas y placeholders como regla editorial general.",
    "No propagar el codigo LDE-S6B1 como oficial hasta confirmacion.",
    "No propagar detalles exclusivos de una actividad si no aplican a toda la materia.",
    "Ciclo 2 conserva reglas utiles de ciclos previos sin regresion."
  ],
  "open_questions": [
    "Confirmar si existe guia oficial de formato para actividades de esta materia.",
    "Confirmar convencion final de nombres de archivos con danos versus daños en todo el arbol.",
    "Confirmar si el codigo de curso LDE-S6B1 es oficial.",
    "Validar y corregir truncamientos en README: reporte y referencias.",
    "Resolver placeholder interpolado del nombre de archivo .bib en README y programa analitico.",
    "Completar la seccion authortable truncada en la plantilla .tex.",
    "Validar plantilla .tex por posible truncamiento local antes de reutilizar."
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