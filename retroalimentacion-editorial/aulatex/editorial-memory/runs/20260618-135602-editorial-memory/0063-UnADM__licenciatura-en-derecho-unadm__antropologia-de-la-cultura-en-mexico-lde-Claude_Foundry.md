{
  "summary": [
    "Base institucional heredada detecta salida no JSON parseable en origen previo.",
    "Destino materia requiere identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
    "Se aplica consolidacion por union-dedupe sin regresion.",
    "Destino: Antropologia de la cultura en Mexico, Licenciatura en Derecho, UnADM.",
    "La materia esta ubicada en semestre 4, bloque 2, tipo obligatoria, 8 creditos.",
    "Existe alerta heredada por salida no JSON parseable desde Codex en memoria UnADM.",
    "La fuente heredada desde ingenieria es provisional hasta validar pertinencia disciplinar.",
    "Origen ciclo actual: actividad-1 de Filosofia del Derecho, propagacion arriba-y-laterales.",
    "README, programa analitico y .bib local confirman estructura editorial de la materia.",
    "Salida sin JSON parseable desde GPT-Pro para antropologia-de-la-cultura-en-mexico-lde.",
    "Se conserva alerta de salidas no JSON parseables como incidencia reutilizable.",
    "Se confirma existencia del .bib local con entradas base institucionales.",
    "La memoria institucional heredada aporta una incidencia reutilizable de parseo.",
    "Ciclo 2 de consolidacion aplicado sobre la materia destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Conservar adscripcion: Licenciatura en Derecho.",
    "Marcar fuente heredada como provisional hasta validar origen disciplinar.",
    "Conservar ubicacion curricular: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar clave local LDE-S4B2 salvo indicacion institucional distinta.",
    "Marcar como supuesto todo elemento heredado no confirmado para Derecho.",
    "Marcar fuente heredada desde ingenieria-en-sistemas-computacionales como provisional.",
    "Mantener autor y matricula solo si coinciden con la actividad real.",
    "Marcar fuente provisional: Codex desde ingenieria-en-sistemas-computacionales.",
    "Marcar fuente provisional: GPT-Pro desde Actividad 1.",
    "Supuesto: la plantilla actual usa autor Martin Jonathan de la Cruz y matricula ES2611202040.",
    "No trasladar metadatos especificos de esta materia a materias distintas."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear entregables con ejes: problema, conceptos, producto, analisis y conclusion.",
    "Guardar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Mantener separacion entre reporte, presentacion y referencias.",
    "Usar programa analitico como guia editorial de productos.",
    "Usar reporte-antropologia-de-la-cultura-en-mexico.tex como plantilla base.",
    "Usar presentacion-antropologia-de-la-cultura-en-mexico.tex para productos expositivos cuando aplique.",
    "Conservar carpeta referencias-antropologia-de-la-cultura-en-mexico para insumos documentales.",
    "Corregir rutas o nombres generados con caracteres truncados antes de compilar.",
    "Resolver placeholders dinamicos tipo $(@{...}.Slug) a nombre literal del .bib antes de usar.",
    "Resolver $(@{...}.Slug) como antropologia-de-la-cultura-en-mexico antes de usar."
  ],
  "activity_rules": [
    "Definir problema juridico o social al inicio de cada actividad.",
    "Incluir analisis propio y postura academica explicita.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Verificar que cada afirmacion relevante tenga respaldo trazable.",
    "Integrar conceptos antropologicos, culturales, juridicos o sociales pertinentes.",
    "Relacionar el producto solicitado con la planeacion semanal.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar reducir el analisis cultural a afirmaciones juridicas sin puente argumentativo."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "No aceptar contenido sin estructura minima del esquema requerido.",
    "Comprobar consistencia entre metadatos de materia y documento final.",
    "Comprobar que semestre, bloque, tipo y creditos coincidan con la malla curricular local.",
    "Verificar que el archivo BibTeX local exista antes de citarlo.",
    "No citar fuentes ausentes en .bib o referencias locales.",
    "Verificar que las rutas del README no contengan placeholders o saltos corruptos.",
    "Revisar que portada, encabezados y bibliografia compilen sin errores.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar.",
    "Verificar que no queden placeholders sin resolver en README, programa analitico ni .tex.",
    "Registrar incidencias de parseo como alertas reutilizables."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Usar spanish, letterpaper y oneside salvo instruccion distinta.",
    "Evitar cambios de clase o formato sin necesidad academica.",
    "Mantener clase article salvo necesidad academica justificada.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename como Antropologia de la cultura en Mexico.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener universityname como Universidad Abierta y a Distancia de Mexico.",
    "Mantener coursecode LDE-S4B2 salvo indicacion institucional distinta.",
    "Conservar universityfaculty como Licenciatura en Derecho.",
    "Conservar universitydepartment como Antropologia de la cultura en Mexico.",
    "Conservar universitydepartmentimage como departamentos/UnADM salvo ajuste confirmado.",
    "Conservar universitylocation Roma Norte, Ciudad de Mexico como supuesto hasta confirmacion institucional."
  ],
  "bibliography_rules": [
    "No inventar fuentes; registrar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Agregar entradas BibTeX especificas por actividad en el .bib local.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda.",
    "Usar la malla curricular de Derecho como fuente de ubicacion curricular.",
    "Distinguir fuentes institucionales, doctrinales, normativas y datos empiricos.",
    "No citar una fuente que no exista en el .bib o en referencias locales.",
    "Registrar archivos locales con ruta verificable cuando se usen assets-unadm.",
    "Conservar entradas base unadmSitioWeb y unadmMallaDerecho2024 en el .bib local."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas ya validadas.",
    "Etiquetar como supuesto todo elemento heredado no confirmado en Derecho.",
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
    "Confirmar estandar unico de citas (APA/otro) para toda la licenciatura.",
    "Validar si la ubicacion institucional en plantilla debe mantenerse fija o actualizarse.",
    "Confirmar si la clave LDE-S4B2 es oficial o solo local.",
    "Confirmar si la conclusion juridica debe aparecer en todas las actividades antropologicas.",
    "Confirmar fuentes base oficiales de la asignatura distintas a la malla curricular.",
    "Confirmar si el .bib usa nombre literal o plantilla dinamica como nombre de archivo definitivo."
  ],
  "sources": [
    "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/actividad-1",
    "UnADM/licenciatura-en-derecho-unadm/antropologia-de-la-cultura-en-mexico-lde",
    "UnADM"
  ],
  "compression": {
    "method": "union-dedupe",
    "lossless": true
  },
  "schema_version": 1
}