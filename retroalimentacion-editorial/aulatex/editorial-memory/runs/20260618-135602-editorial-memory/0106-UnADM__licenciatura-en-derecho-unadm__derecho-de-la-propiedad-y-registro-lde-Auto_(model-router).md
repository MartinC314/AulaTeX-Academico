{
  "summary": [
    "Base institucional UnADM aplicable a la materia.",
    "Materia destino: Derecho de la propiedad y registro.",
    "Programa: Licenciatura en Derecho.",
    "Ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "La carpeta funciona como punto de entrada canonico de la asignatura.",
    "Se conserva enfoque de integridad academica, citas verificables y cierre juridico propio.",
    "Existe antecedente institucional con salida no JSON parseable; requiere normalizacion antes de reutilizarse.",
    "Supuesto: la actividad origen no aporta reglas parseables adicionales en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en portada y metadatos.",
    "Usar nombre de materia exacto: Derecho de la propiedad y registro.",
    "Conservar nivel y programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local cuando aplique: LDE-S7B1.",
    "Conservar a la UnADM como Universidad Abierta y a Distancia de Mexico.",
    "Marcar como provisional la regla heredada desde ingenieria-en-sistemas-computacionales si se reutiliza."
  ],
  "structure_rules": [
    "Alinear entregables con la estructura local: reporte, presentacion, bibliografia y referencias.",
    "Usar la carpeta de la materia como punto de entrada canonico.",
    "Transformar la planeacion semanal en productos academicos claros.",
    "Incluir problema juridico o social que activa la asignatura.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir producto solicitado por la planeacion.",
    "Incluir analisis propio y postura academica.",
    "Incluir conclusion transferible a la practica juridica.",
    "Mantener consistencia con semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Verificar nombres de archivos listados en README antes de automatizar rutas."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad antes del desarrollo.",
    "Relacionar contenido con propiedad y registro cuando aplique.",
    "Vincular cada actividad con el producto solicitado por la planeacion.",
    "Distinguir problema, fundamento, analisis y cierre argumentativo.",
    "Cerrar cada actividad con postura juridica propia y sustentada.",
    "Evitar afirmaciones juridicas sin fuente o razonamiento propio."
  ],
  "quality_gates": [
    "Validar formato estructurado antes de propagar a nodos aguas abajo.",
    "Revisar coherencia entre instrucciones de actividad y pauta editorial de la materia.",
    "Confirmar trazabilidad de citas y afirmaciones factuales.",
    "Revisar respuesta no estructurada heredada antes de aplicarla aguas abajo.",
    "Confirmar que no existan placeholders sin resolver.",
    "Confirmar que cada fuente citada exista en BibTeX o en repositorio local.",
    "Confirmar que la conclusion responda al problema planteado.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instruccion distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Mantener coursename como Derecho de la propiedad y registro.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode como LDE-S7B1 cuando corresponda.",
    "Evitar campos placeholder sin resolver en portada y tabla de autor.",
    "Corregir campos incompletos como Figura docente antes de entrega.",
    "Verificar compilacion despues de modificar portada, bibliografia o rutas."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia para fuentes especificas.",
    "Agregar fuentes especificas en derecho-de-la-propiedad-y-registro.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Conservar como fuente local la malla curricular de Derecho de UnADM.",
    "Conservar como fuente institucional el sitio web de UnADM si fue consultado.",
    "No inventar referencias.",
    "Registrar solo fuentes consultables o locales existentes.",
    "Incluir datos minimos de consulta o archivo local cuando aplique."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y no ambiguas.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia del origen.",
    "Mantener compresion union-dedupe sin eliminar reglas utiles previas.",
    "Aplicar ciclo 1 con normalizacion manual si se reutiliza memoria heredada.",
    "Propagar la identidad UnADM a materias laterales solo si comparten institucion.",
    "Propagar reglas curriculares solo dentro de la materia destino.",
    "No propagar datos locales de archivo si no existen en el nodo receptor."
  ],
  "open_questions": [
    "Falta insumo estructurado del origen actividad-1 para extraer reglas especificas.",
    "Definir si existe rubrica formal de evaluacion para esta materia.",
    "Confirmar estilo de citacion juridica requerido por docente en actividades.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Confirmar figura docente para sustituir el placeholder local.",
    "Confirmar si la actividad requiere reporte, presentacion u otro producto.",
    "Confirmar fuentes juridicas especificas de propiedad y registro para actividades futuras."
  ]
}