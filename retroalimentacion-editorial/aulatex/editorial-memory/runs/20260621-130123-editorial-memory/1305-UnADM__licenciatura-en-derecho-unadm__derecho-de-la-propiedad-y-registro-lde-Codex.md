{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad y materia con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y se refuerza normalizacion estructurada obligatoria antes de propagacion.",
    "Se mantienen ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita trasladar contenido tematico especifico de Filosofia del Derecho al dominio de Propiedad y Registro.",
    "Se corrigen duplicados por union-dedupe sin recorte de reglas utiles previas."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local LDE-S7B1 cuando corresponda.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar planeacion en reporte, presentacion u otro producto segun consigna.",
    "Verificar nombres de archivo del README antes de automatizar rutas.",
    "Resolver tokens no expandidos en rutas y nombres de archivo."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validacion de consigna.",
    "Verificar que el producto final corresponda a la actividad solicitada."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no existan placeholders sin resolver.",
    "Confirmar que la conclusion responda al problema planteado.",
    "Confirmar que las reglas propagadas sean verificables y no ambiguas."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Usar clase article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Actualizar documenttitle y documentsubtitle para cada actividad.",
    "Mantener coursename y coursecode locales consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir campos incompletos como Figura docente antes de entrega."
  ],
  "bibliography_rules": [
    "Usar archivo BibTeX local de la materia para fuentes especificas.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; usar solo obras consultables o archivos locales existentes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar fuentes especificas en derecho-de-la-propiedad-y-registro.bib.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico no transversal.",
    "Evitar regresiones respecto de reglas utiles previas.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "Supuesto: falta rubrica local detallada por actividad; confirmar criterio de evaluacion.",
    "Confirmar figura docente para sustituir placeholder en plantilla.",
    "Confirmar si cada actividad requiere reporte, presentacion u otro formato.",
    "Confirmar estilo de citacion juridica requerido por docente.",
    "Confirmar si hay fuentes obligatorias por semana en Propiedad y Registro."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho de la propiedad y registro.",
        "Codigo local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema juridico",
      "Marco conceptual y normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible",
      "Trazabilidad bibliografica"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia entre consigna, desarrollo argumentativo y cierre juridico.",
      "Preservar continuidad editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados explicitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre.",
      "Sin propagacion de salidas no parseables."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al analisis propio.",
      "Del analisis a la conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Trazabilidad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige formato y evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura parseable evita perdida y ambiguedad en propagacion."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere fundamento."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Citas consistentes con .bib sostienen verificabilidad."
        }
      ],
      "evidence": [
        "README de la materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-de-la-propiedad-y-registro.bib: claves institucionales existentes.",
        "Regla estable heredada: bloquear propagacion si salida no es JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 19: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 19: se mantiene politica de no propagar salidas no estructuradas.",
      "Ciclo 19: se refuerza compatibilidad entre estructura editorial y plantilla LaTeX local."
    ]
  }
}