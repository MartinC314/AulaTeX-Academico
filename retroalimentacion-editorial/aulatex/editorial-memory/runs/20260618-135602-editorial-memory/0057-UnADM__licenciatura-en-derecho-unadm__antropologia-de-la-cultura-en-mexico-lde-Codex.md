{
  "summary": [
    "Base institucional heredada detecta salida no JSON parseable en origen previo.",
    "Destino materia requiere identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
    "Se aplica consolidacion por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en portada y metadatos.",
    "Usar nombre de materia: Antropologia de la cultura en Mexico.",
    "Conservar adscripcion: Licenciatura en Derecho.",
    "Marcar fuente heredada como provisional hasta validar origen disciplinar."
  ],
  "structure_rules": [
    "Usar README de materia como punto de entrada canonico.",
    "Alinear entregables con ejes: problema, conceptos, producto, analisis, conclusion.",
    "Guardar fuentes de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Mantener separacion entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Definir problema juridico o social al inicio de cada actividad.",
    "Incluir analisis propio y postura academica explicita.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Verificar que cada afirmacion relevante tenga respaldo trazable."
  ],
  "quality_gates": [
    "Validar JSON parseable antes de propagar memoria aguas abajo.",
    "Revisar respuestas no estructuradas y normalizar manualmente en ciclo 1.",
    "No aceptar contenido sin estructura minima del esquema requerido.",
    "Comprobar consistencia entre metadatos de materia y documento final."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como referencia inicial.",
    "Mantener campos institucionales completos en encabezado LaTeX.",
    "Usar codificacion y configuracion en espanol coherentes con la plantilla.",
    "Evitar cambios de clase o formato sin necesidad academica."
  ],
  "bibliography_rules": [
    "No inventar fuentes; registrar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Agregar entradas BibTeX especificas por actividad en el .bib local.",
    "Incluir datos de consulta y notas de procedencia cuando corresponda."
  ],
  "propagation_hints": [
    "Propagar hacia arriba y laterales solo reglas ya validadas.",
    "Etiquetar como supuesto todo elemento heredado no confirmado en Derecho.",
    "Mantener metodo de compresion union-dedupe con preservacion total.",
    "Registrar incidencias de parseo como alerta reutilizable inter-materias."
  ],
  "open_questions": [
    "Supuesto: la regla heredada desde ingenieria aplica parcialmente en Derecho; confirmar alcance.",
    "Falta memoria especifica de actividad-1 de Filosofia del Derecho en formato estructurado.",
    "Confirmar estandar unico de citas (APA/otro) para toda la licenciatura.",
    "Validar si la ubicacion institucional en plantilla debe mantenerse fija o actualizarse."
  ]
}