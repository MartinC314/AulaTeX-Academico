{
  "summary": [
    "Sincronizacion transversal completada con estrategia conservadora y sin regresion.",
    "Se conserva nucleo editorial estable: problema, conceptos-normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate critico: no propagar salidas no JSON parseable sin normalizacion previa.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza correccion operativa de placeholders y rutas corruptas en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada, metadatos y formato.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear entregas a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "No modificar datos de alumno o matricula sin verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Alinear el producto al formato solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Evitar trasladar contenido tematico de Filosofia del Derecho sin validar pertinencia local. [supuesto]",
    "Registrar vacios de consigna en preguntas abiertas.",
    "No asumir fuentes de semanas o materias distintas como obligatorias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar esquema minimo completo antes de guardar memoria.",
    "Exigir respaldo o marca [supuesto] en toda afirmacion no verificable.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Confirmar correspondencia entre consigna, rubrica y producto final."
  ],
  "latex_rules": [
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener espanol academico con acentos correctos en .tex y .bib.",
    "Conservar documentclass article, spanish, letterpaper, oneside salvo consigna distinta.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir placeholders de slug tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo corruptos en README (reporte y referencias) antes de reutilizar plantilla."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion de JSON y gates de calidad.",
    "Transferir solo abstracciones estables en saltos transversales entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual sobre contenido literal.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar como provisional cualquier regla heredada sin evidencia local."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica vigentes de la primera actividad local de la materia destino.",
    "Confirmar vigencia de datos de alumno, matricula y figura docente en plantilla. [supuesto]",
    "Confirmar si LDE-S3B1 es obligatorio en todos los productos.",
    "Validar sustitucion definitiva de placeholders de slug .bib en README y programa analitico.",
    "Confirmar si existe formato institucional obligatorio adicional para presentaciones."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica desde carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1.",
        "Obligatoria seriada, 8 creditos."
      ]
    },
    "essence": [
      "Resolver problemas juridicos con fundamento verificable.",
      "Integrar conceptos y normas con analisis propio.",
      "Cerrar con utilidad juridica practica y transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y evaluables.",
      "Sostener un estandar editorial comun entre actividades y materias.",
      "Preservar consistencia tecnica, argumentativa e institucional."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion explicita entre marco conceptual y postura propia.",
      "Etiquetado visible de [supuesto] cuando falte verificacion."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma, doctrina o fuente.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Integridad de evidencia y citas",
        "Normalizacion JSON",
        "Consistencia LaTeX y BibTeX",
        "Problema-conceptos-evidencia-analisis-conclusion"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y estandar de entrega."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Problema-conceptos-evidencia-analisis-conclusion",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Consistencia LaTeX y BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de trazabilidad."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Fortalece validez de analisis y conclusion."
        },
        {
          "source": "Problema-conceptos-evidencia-analisis-conclusion",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "Es el patron transversal reusable entre materias."
        }
      ],
      "evidence": [
        "README local de Derechos de la persona y familia.",
        "Programa analitico local de la materia.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla institucional heredada: no reutilizar salidas no estructuradas sin normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion completa de reglas repetidas sin recorte semantico.",
      "Ciclo 21: se transfiere solo abstraccion estable desde actividad origen a materia destino.",
      "Ciclo 21: se conserva alerta historica de JSON no parseable como gate permanente.",
      "Ciclo 21: se refuerza correccion de placeholders y rutas corruptas como requisito operativo."
    ]
  }
}