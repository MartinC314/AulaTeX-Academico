{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas institucionales UnADM y normalizacion estructurada obligatoria.",
    "Se refuerza marco reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin recorte.",
    "Se conserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar al .bib local solo fuentes realmente consultables."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante la fusion.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Normalizar manualmente respuestas no estructuradas antes de propagar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con artefactos de salto antes de compilar.",
    "Actualizar documenttitle y documentsubtitle segun actividad.",
    "Verificar cierre de entornos truncados en el reporte local."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Registrar fuentes especificas de actividad en derecho-de-la-empresa-y-emprendimiento.bib.",
    "No citar fuentes ausentes en el .bib local.",
    "Mantener unadmSitioWeb y unadmMallaDerecho2024 como base local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o doctrina propia de otra materia.",
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener estrategia progresiva y conservadora sin regresiones."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividades especificas de la materia destino.",
    "Confirmar si documentauthor debe parametrizarse por actividad o mantenerse fijo.",
    "Confirmar valor final del Slug en README y programa analitico.",
    "Confirmar correccion de archivos listados con artefactos de salto.",
    "Confirmar politica bibliografica para year=2026 en unadmSitioWeb.",
    "Confirmar reparacion completa del .tex truncado en authortable."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico activador.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para practica juridica.",
      "Sostener calidad institucional en reportes y presentaciones de la materia."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo como soporte del criterio personal.",
      "Consistencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos",
        "Correspondencia README-.tex-.bib",
        "Tokens Slug sin expandir"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Evita mezclar hechos confirmados con inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Define tono, formato y trazabilidad comunes."
        },
        {
          "source": "Tokens Slug sin expandir",
          "target": "Correspondencia README-.tex-.bib",
          "kind": "contrasts",
          "justification": "Rompen consistencia documental y compilacion."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo .bib local con fuentes institucionales.",
        "Reglas heredadas de calidad JSON y normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion de reglas repetidas sin perdida semantica.",
      "Ciclo 7: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 7: conservadas alertas de JSON no parseable y normalizacion manual.",
      "Ciclo 7: reforzada separacion entre identidad editorial y contenido doctrinal especifico."
    ]
  }
}