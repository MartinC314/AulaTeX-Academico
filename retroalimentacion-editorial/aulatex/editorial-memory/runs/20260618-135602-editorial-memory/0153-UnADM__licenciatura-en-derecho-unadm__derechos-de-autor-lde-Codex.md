{
  "summary": [
    "Consolidar base editorial UnADM para la materia Derechos de autor.",
    "Mantener compresion por union-dedupe sin perdida.",
    "Marcar que la herencia previa viene de fuente provisional y requiere validacion local."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1 en documentos."
  ],
  "structure_rules": [
    "Conservar README como punto de entrada canonico de la asignatura.",
    "Usar programa-analitico como marco para problema, conceptos, producto, analisis y cierre.",
    "Guardar bibliografia especifica en derechos-de-autor.bib.",
    "Mantener separacion entre reporte, presentacion y referencias de la materia.",
    "Normalizar nombres de archivo con slug de la asignatura cuando aplique."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Vincular conceptos con normas, doctrina o datos verificables.",
    "Cumplir formato solicitado por la planeacion semanal.",
    "Incluir analisis propio explicito, no solo resumen de fuentes.",
    "Cerrar con conclusion aplicable a practica juridica."
  ],
  "quality_gates": [
    "Rechazar salidas no JSON parseable antes de propagar memoria.",
    "Verificar consistencia entre metadatos de portada y datos curriculares locales.",
    "Exigir citas verificables y correspondencia con .bib local.",
    "Detectar y corregir campos pendientes como 'Nombre por definir'.",
    "Marcar herencia institucional previa como provisional hasta confirmacion en Derecho."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y letterpaper salvo instruccion contraria.",
    "Declarar metadatos con macros de documento antes de \\input{template}.",
    "Conservar tabla de autor con alumno, matricula y datos academicos completos.",
    "Evitar paquetes truncados o lineas incompletas en preambulo.",
    "Usar tipografia sans serif de forma consistente si la plantilla la requiere."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales institucionales o verificables.",
    "Registrar fuentes base UnADM ya incluidas en derechos-de-autor.bib.",
    "Agregar nuevas entradas BibTeX completas por actividad.",
    "Incluir fecha de consulta cuando la fuente sea web.",
    "Asegurar que toda cita en texto tenga entrada en .bib y viceversa."
  ],
  "propagation_hints": [
    "Propagar hacia arriba reglas institucionales validadas en esta materia.",
    "Propagar lateralmente a materias LDE solo reglas genericas de calidad y estructura.",
    "No propagar datos personales del alumno a otras materias.",
    "Mantener bandera de normalizacion manual en ciclo 1 para contenido heredado."
  ],
  "open_questions": [
    "Confirmar si la clave de curso LDE-S5B1 es oficial en toda la suite.",
    "Definir nombre de figura docente para eliminar marcador pendiente.",
    "Validar si la ubicacion 'Roma Norte, Ciudad de Mexico' debe mantenerse fija.",
    "Revisar y corregir posibles errores de nombres de archivo en README (lineas con caracteres extranos).",
    "Confirmar si la fuente heredada 'Codex desde ingenieria' sigue vigente o debe retirarse tras validacion local."
  ]
}