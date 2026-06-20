{
  "summary": [
    "Consolidacion aplicada con union-dedupe lossless y sin regresion.",
    "Destino confirmado: Antropologia de la cultura en Mexico, Licenciatura en Derecho, UnADM.",
    "Ubicacion curricular confirmada: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "README y programa analitico confirman pauta editorial con conclusion juridica.",
    "Existe .bib local con entradas base institucionales verificables.",
    "Se conserva alerta reutilizable por salidas no JSON parseables en memoria heredada.",
    "Ciclo 1 de propagacion requiere normalizacion manual de memoria no estructurada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Conservar adscripcion: Licenciatura en Derecho.",
    "Conservar ubicacion curricular: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar clave local LDE-S4B2 salvo indicacion institucional distinta.",
    "Mantener autor y matricula solo si coinciden con la actividad real.",
    "Marcar como supuesto todo elemento heredado no confirmado disciplinarmente.",
    "Marcar fuentes heredadas desde ingenieria como provisionales.",
    "No trasladar metadatos especificos de esta materia a materias distintas."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Usar programa analitico como guia editorial de productos.",
    "Alinear entregables con ejes: problema, conceptos, producto, analisis y conclusion.",
    "Mantener separacion entre reporte, presentacion y referencias.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex para productos expositivos cuando aplique.",
    "Guardar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos documentales.",
    "Corregir rutas o nombres con caracteres truncados antes de compilar.",
    "Resolver placeholders dinamicos tipo $(@{...}.Slug) a nombres literales antes de usar."
  ],
  "activity_rules": [
    "Definir problema juridico o social al inicio de cada actividad.",
    "Integrar conceptos antropologicos, culturales, juridicos o sociales pertinentes.",
    "Relacionar el producto solicitado con la planeacion semanal.",
    "Incluir analisis propio y postura academica explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Respaldar cada afirmacion relevante con fuente trazable.",
    "Evitar conclusiones juridicas sin puente argumentativo cultural.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "No aceptar contenido sin esquema minimo requerido.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Verificar semestre, bloque, tipo y creditos contra malla curricular local.",
    "Verificar existencia del .bib local antes de citar.",
    "No citar fuentes ausentes en .bib o referencias locales.",
    "Verificar que rutas del README no contengan placeholders o saltos corruptos.",
    "Verificar que no queden placeholders sin resolver en README, programa analitico ni .tex.",
    "Revisar compilacion de portada, encabezados y bibliografia.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar.",
    "Registrar incidencias de parseo como alertas reutilizables."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener clase article salvo necesidad academica justificada.",
    "Usar spanish, letterpaper y oneside salvo instruccion distinta.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename como Antropologia de la cultura en Mexico.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener universityname como Universidad Abierta y a Distancia de Mexico.",
    "Mantener coursecode LDE-S4B2 salvo cambio institucional confirmado.",
    "Conservar universityfaculty como Licenciatura en Derecho.",
    "Conservar universitydepartment como Antropologia de la cultura en Mexico.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo ajuste confirmado.",
    "Conservar universitylocation como supuesto hasta confirmacion institucional."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Agregar entradas BibTeX especificas por actividad en el .bib local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024 en el .bib local.",
    "Incluir fecha de consulta y procedencia cuando corresponda.",
    "Distinguir fuentes institucionales, doctrinales, normativas y empiricas.",
    "No citar una fuente que no exista en el .bib o en referencias locales.",
    "Registrar ruta verificable para archivos de assets-unadm usados."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas ya validadas.",
    "Propagar identidad UnADM e integridad academica como base comun.",
    "Mantener metodo de compresion union-dedupe con preservacion total.",
    "No eliminar reglas utiles previas durante consolidaciones futuras.",
    "Etiquetar como supuesto todo elemento heredado no confirmado en Derecho.",
    "Mantener como provisionales reglas heredadas de otras disciplinas.",
    "No propagar metadatos especificos de esta materia a materias distintas.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Ciclo 1 necesita normalizacion manual si se reutiliza memoria no estructurada."
  ],
  "open_questions": [
    "Falta memoria estructurada especifica de actividad-1 de Filosofia del Derecho.",
    "Supuesto: alcance real de reglas heredadas desde ingenieria en contexto Derecho.",
    "Confirmar si LDE-S4B2 es clave oficial o solo local.",
    "Confirmar estandar unico de citas para la licenciatura.",
    "Confirmar si la conclusion juridica aplica a todas las actividades antropologicas.",
    "Confirmar politica institucional sobre universitylocation en plantilla.",
    "Confirmar si el nombre final del .bib es literal y no dinamico."
  ]
}