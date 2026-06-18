{
  "summary": [
    "Consolidacion aplicada con union-dedupe lossless sin regresion.",
    "Se mantiene identidad UnADM y contexto de Derecho en la materia destino.",
    "Se conserva alerta de salidas no JSON parseables como incidencia reutilizable.",
    "README y programa analitico confirman pauta editorial con conclusion juridica.",
    "Se confirma existencia del .bib local con entradas base institucionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Conservar adscripcion: Licenciatura en Derecho.",
    "Conservar ubicacion curricular: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar clave local LDE-S4B2 salvo indicacion institucional distinta.",
    "Mantener autor y matricula solo si coinciden con la actividad real.",
    "Marcar como supuesto todo elemento heredado no confirmado disciplinarmente.",
    "Marcar fuentes heredadas desde ingenieria como provisionales."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear entregables con ejes: problema, conceptos, producto, analisis, conclusion.",
    "Mantener separacion entre reporte, presentacion y referencias.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex cuando aplique.",
    "Guardar fuentes en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos.",
    "Corregir rutas con caracteres truncados antes de compilar.",
    "Resolver placeholders dinamicos a nombres literales antes de uso."
  ],
  "activity_rules": [
    "Definir problema juridico o social al inicio.",
    "Integrar conceptos antropologicos, culturales y juridicos pertinentes.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Incluir analisis propio y postura academica explicita.",
    "Relacionar el producto con la planeacion semanal.",
    "Respaldar afirmaciones relevantes con fuente trazable.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar conclusiones juridicas sin puente argumentativo cultural."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "No aceptar contenido sin esquema minimo requerido.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Verificar semestre, bloque, tipo y creditos contra malla curricular local.",
    "Verificar existencia del .bib local antes de citar.",
    "No citar fuentes ausentes en .bib o referencias locales.",
    "Verificar que no queden placeholders sin resolver en README, programa o .tex.",
    "Revisar compilacion de portada, encabezados y bibliografia.",
    "No promover reglas provisionales a definitivas sin validacion."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex como referencia inicial.",
    "Mantener clase article salvo necesidad academica justificada.",
    "Usar spanish, letterpaper y oneside salvo instruccion distinta.",
    "Mantener campos institucionales completos en encabezado.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename como Antropologia de la cultura en Mexico.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener universityname como Universidad Abierta y a Distancia de Mexico.",
    "Mantener coursecode LDE-S4B2 salvo cambio institucional confirmado.",
    "Mantener universitylocation actual como supuesto hasta confirmacion institucional."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales.",
    "Agregar entradas BibTeX especificas por actividad en el .bib local.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Incluir fecha de consulta y procedencia cuando corresponda.",
    "Distinguir fuentes institucionales, doctrinales, normativas y empiricas.",
    "Registrar ruta verificable para archivos de assets-unadm usados."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas.",
    "Etiquetar incidencias de parseo como alertas reutilizables.",
    "Mantener compresion union-dedupe con preservacion total.",
    "No eliminar reglas utiles previas en consolidaciones futuras.",
    "Propagar identidad UnADM e integridad academica como base comun.",
    "No propagar metadatos especificos de esta materia a materias distintas.",
    "Mantener como provisionales reglas heredadas de otras disciplinas."
  ],
  "open_questions": [
    "Supuesto: alcance real de reglas heredadas desde ingenieria en contexto Derecho.",
    "Falta memoria estructurada especifica de actividad-1 de Filosofia del Derecho.",
    "Confirmar estandar unico de citas para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar si la conclusion juridica aplica a todas las actividades de la materia.",
    "Confirmar politica institucional sobre universitylocation en plantilla.",
    "Confirmar si el nombre final del .bib es literal y no dinamico."
  ]
}