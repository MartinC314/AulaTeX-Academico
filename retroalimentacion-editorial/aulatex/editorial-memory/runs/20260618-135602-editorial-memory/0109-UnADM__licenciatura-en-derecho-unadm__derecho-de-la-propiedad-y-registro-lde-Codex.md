{
  "summary": [
    "Base institucional UnADM verificada y aplicable a la materia.",
    "Materia destino: Derecho de la propiedad y registro.",
    "Programa: Licenciatura en Derecho.",
    "Ubicacion curricular verificada: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "La carpeta funciona como punto de entrada canonico de la asignatura.",
    "Existe antecedente institucional con salida no JSON parseable; requiere normalizacion antes de reutilizarse.",
    "Salida no JSON parseable reportada en ciclos previos (Codex y GPT-Pro).",
    "Supuesto: la actividad origen no aporta reglas nuevas parseables en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en portada y metadatos.",
    "Usar nombre de materia exacto: Derecho de la propiedad y registro.",
    "Conservar nivel y programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local cuando aplique: LDE-S7B1.",
    "Conservar a la UnADM como Universidad Abierta y a Distancia de Mexico.",
    "Registrar ubicacion institucional: Roma Norte, Ciudad de Mexico.",
    "Marcar como provisional toda regla heredada desde otro programa academico."
  ],
  "structure_rules": [
    "Alinear entregables con la estructura local: reporte, presentacion, bibliografia y referencias.",
    "Incluir problema juridico o social que activa la asignatura.",
    "Incluir conceptos, normas, doctrina o datos pertinentes.",
    "Incluir producto solicitado por la planeacion.",
    "Incluir analisis propio y postura academica.",
    "Incluir conclusion transferible a la practica juridica.",
    "Usar la carpeta de la materia como punto de entrada canonico.",
    "Verificar nombres de archivos listados en README antes de automatizar rutas.",
    "Supuesto: README contiene tokens corruptos; usar slug derecho-de-la-propiedad-y-registro para resolver rutas."
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
    "Confirmar que no existan placeholders sin resolver.",
    "Confirmar que cada fuente citada exista en BibTeX o en repositorio local.",
    "Confirmar que la conclusion responda al problema planteado.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas.",
    "Revisar toda respuesta no estructurada heredada antes de aplicarla aguas abajo."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instruccion distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Mantener coursename como Derecho de la propiedad y registro.",
    "Mantener documentsubject como Licenciatura en Derecho.",
    "Mantener coursecode como LDE-S7B1 cuando corresponda.",
    "Mantener autor por defecto Martin Jonathan de la Cruz salvo instruccion distinta.",
    "Conservar matricula del alumno ES2611202040 en tabla de autor.",
    "Mantener universitydepartmentimage departamentos/UnADM con height 1.57cm.",
    "Corregir campos incompletos como Figura docente antes de entrega.",
    "Verificar compilacion despues de modificar portada, bibliografia o rutas.",
    "Evitar campos placeholder sin resolver en portada y tabla de autor."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia para fuentes especificas.",
    "Agregar fuentes especificas en derecho-de-la-propiedad-y-registro.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; registrar solo fuentes consultables o locales existentes.",
    "Incluir datos minimos de consulta o archivo local cuando aplique.",
    "Usar clave unadmSitioWeb para el sitio institucional consultado.",
    "Usar clave unadmMallaDerecho2024 para la malla curricular local."
  ],
  "propagation_hints": [
    "Propagar arriba y laterales solo reglas validadas y no ambiguas.",
    "Mantener compresion union-dedupe sin eliminar reglas utiles previas.",
    "Marcar como supuesto cualquier regla no confirmada por evidencia del origen.",
    "Aplicar normalizacion manual a salidas no JSON antes de reutilizarlas.",
    "Propagar la identidad UnADM a nodos laterales solo si comparten institucion.",
    "Propagar reglas curriculares solo dentro de la materia destino.",
    "No propagar datos locales de archivo si no existen en el nodo receptor."
  ],
  "open_questions": [
    "Falta insumo estructurado del origen actividad-1 para extraer reglas especificas.",
    "Confirmar si existe rubrica formal de evaluacion para esta materia.",
    "Confirmar estilo de citacion juridica requerido por la figura docente.",
    "Confirmar si la salida no JSON heredada ya fue normalizada en otro ciclo.",
    "Confirmar figura docente para sustituir el placeholder local.",
    "Confirmar si cada actividad requiere reporte, presentacion u otro producto.",
    "Confirmar fuentes juridicas especificas de propiedad y registro para actividades futuras.",
    "Confirmar nombres de archivo reales del README ante tokens corruptos detectados."
  ]
}