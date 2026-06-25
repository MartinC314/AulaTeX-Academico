{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se agregan mejoras verificables: bloqueo por JSON no parseable y normalizacion previa obligatoria.",
    "Se mantiene separacion entre abstracciones transferibles y contexto local de la materia destino.",
    "Supuesto: no hay consigna local de actividad especifica en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo local LDE-S7B1 cuando corresponda.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar la planeacion en reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el desarrollo con propiedad y registro cuando aplique.",
    "No asumir fuentes de semanas posteriores sin validacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna local."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener clase article con spanish, letterpaper y oneside salvo instruccion local distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Evitar placeholders sin resolver en portada y tabla de autor.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar nombres reales de archivos antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en derecho-de-la-propiedad-y-registro.bib.",
    "No inventar referencias.",
    "Usar solo obras consultables o archivos locales existentes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o datos hiperlocales no verificables.",
    "Mantener estrategia progresiva y conservadora sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar rubrica de evaluacion local por actividad.",
    "Confirmar si cada actividad exige reporte, presentacion u otro formato.",
    "Confirmar estilo de citacion juridica requerido por figura docente.",
    "Confirmar correccion definitiva de tokens corruptos en README/programa.",
    "Supuesto: falta consigna puntual de actividad para ajustar profundidad y producto."
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
        "Normalizacion estructurada obligatoria antes de propagacion.",
        "Sin propagacion de salidas no parseables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Materia: Derecho de la propiedad y registro.",
        "Codigo local: LDE-S7B1."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Fundamento conceptual y normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos y utiles para practica juridica.",
      "Sostener consistencia institucional y trazabilidad editorial en todo ciclo."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados explicitamente.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
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
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
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
          "justification": "La identidad institucional exige forma y evidencia verificable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder a una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere sustento normativo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La consistencia texto-.bib evita afirmaciones no verificables."
        }
      ],
      "evidence": [
        "README de la materia.",
        "Programa analitico de la materia.",
        "derecho-de-la-propiedad-y-registro.bib.",
        "Regla heredada institucional: revisar y normalizar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion completa de reglas repetidas.",
      "Ciclo 12: se conserva ADN editorial comun problema-conceptos-evidencia-analisis-conclusion.",
      "Ciclo 12: se refuerza gate critico de JSON parseable antes de propagacion.",
      "Ciclo 12: se evita traslado de contenido tematico especifico de Filosofia del Derecho no transversal."
    ]
  }
}