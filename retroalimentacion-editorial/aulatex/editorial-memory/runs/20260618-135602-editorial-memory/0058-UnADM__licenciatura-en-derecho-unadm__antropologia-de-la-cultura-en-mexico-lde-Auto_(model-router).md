{
  "summary": [
    "Consolidacion por union-dedupe lossless para la materia destino.",
    "Destino: Antropologia de la cultura en Mexico, Licenciatura en Derecho, UnADM.",
    "La materia esta ubicada en semestre 4, bloque 2, tipo obligatoria, 8 creditos.",
    "La pauta local exige identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
    "Existe alerta heredada por salida no JSON parseable desde Codex en memoria UnADM.",
    "La fuente heredada desde ingenieria es provisional hasta validar pertinencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Conservar adscripcion: Licenciatura en Derecho.",
    "Conservar ubicacion curricular: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar clave local LDE-S4B2 salvo indicacion institucional distinta.",
    "Marcar como supuesto todo elemento heredado no confirmado para Derecho.",
    "Marcar fuente heredada desde ingenieria como provisional."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Usar programa analitico como guia editorial de productos.",
    "Alinear entregables con ejes: problema, conceptos, producto, analisis, conclusion.",
    "Mantener separacion entre reporte, presentacion y referencias.",
    "Guardar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex para productos expositivos cuando aplique.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos documentales.",
    "Corregir rutas o nombres generados con caracteres truncados antes de compilar."
  ],
  "activity_rules": [
    "Definir problema juridico o social al inicio de cada actividad.",
    "Integrar conceptos antropologicos, culturales, juridicos o sociales pertinentes.",
    "Relacionar el producto solicitado con la planeacion semanal.",
    "Incluir analisis propio y postura academica explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar reducir el analisis cultural a afirmaciones juridicas sin puente argumentativo.",
    "Verificar que cada afirmacion relevante tenga respaldo trazable."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar respuestas no estructuradas y normalizar manualmente en ciclo 1.",
    "No aceptar contenido sin estructura minima del esquema requerido.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Comprobar que semestre, bloque, tipo y creditos coincidan con la malla curricular local.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "Verificar que las rutas del README no contengan placeholders o saltos corruptos.",
    "Revisar que portada, encabezados y bibliografia compilen sin errores.",
    "No propagar reglas provisionales como definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener clase article salvo necesidad academica justificada.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Usar configuracion en espanol coherente con la plantilla.",
    "Usar letterpaper y oneside si no hay instruccion distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename como Antropologia de la cultura en Mexico.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener universityname como Universidad Abierta y a Distancia de Mexico.",
    "Evitar cambios de clase o formato sin necesidad academica."
  ],
  "bibliography_rules": [
    "No inventar fuentes; registrar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Usar la malla curricular de Derecho como fuente de ubicacion curricular.",
    "Agregar entradas BibTeX especificas por actividad en el .bib local.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empiricos.",
    "No citar una fuente que no exista en el .bib o en referencias locales.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas ya validadas.",
    "Mantener metodo de compresion union-dedupe con preservacion total.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias.",
    "Ciclo 1 requiere normalizacion manual si se reutiliza memoria no estructurada.",
    "No eliminar reglas utiles previas durante consolidaciones futuras.",
    "Propagar identidad UnADM y criterios de integridad academica a materias laterales.",
    "Propagar como provisional cualquier regla heredada desde otra disciplina.",
    "No propagar metadatos especificos de esta materia a materias distintas."
  ],
  "open_questions": [
    "Supuesto: la regla heredada desde ingenieria aplica parcialmente en Derecho; confirmar alcance.",
    "Falta memoria especifica de actividad-1 de Filosofia del Derecho en formato estructurado.",
    "Confirmar estandar unico de citas para toda la licenciatura.",
    "Validar si la ubicacion institucional en plantilla debe mantenerse fija o actualizarse.",
    "Confirmar si la clave LDE-S4B2 es oficial o solo local.",
    "Confirmar si la conclusion juridica debe aparecer en todas las actividades antropologicas.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular."
  ]
}