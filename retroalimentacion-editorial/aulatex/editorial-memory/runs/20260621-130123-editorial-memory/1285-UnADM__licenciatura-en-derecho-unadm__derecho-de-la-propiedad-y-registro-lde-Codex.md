{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y ubicacion curricular local de la materia destino.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene politica de normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Supuesto: no existe consigna local de actividad especifica en este ciclo; se conserva cerebro minimo de materia."
  ],
  "identity_rules": [
    "Mantener identidad explicita UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de materia: Derecho de la propiedad y registro.",
    "Conservar programa: Licenciatura en Derecho.",
    "Registrar ubicacion curricular local: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar planeacion en reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Declarar objetivo puntual de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
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
    "Verificar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Conservar plantilla base .tex de la materia como punto de partida.",
    "Usar clase article con opciones spanish, letterpaper y oneside salvo instruccion distinta.",
    "Completar metadatos academicos obligatorios antes de compilar.",
    "Evitar placeholders sin resolver en portada y tabla de autor.",
    "Corregir tokens sin expandir en rutas y nombres de archivo del README y programa analitico.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar archivo local derecho-de-la-propiedad-y-registro.bib para fuentes de la materia.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; registrar solo fuentes consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar fuentes nuevas solo cuando correspondan a consigna confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no ambiguas.",
    "Transferir entre nodos transversales solo abstracciones editoriales estables.",
    "Evitar transferir redaccion literal o contenido tematico especifico de otra materia.",
    "Mantener compresion por union y deduplicacion sin regresion.",
    "Aplicar normalizacion manual cuando existan antecedentes no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar rubrica local de evaluacion por actividad en la materia destino.",
    "Confirmar si existe estilo de citacion juridica requerido por figura docente.",
    "Confirmar producto requerido por cada actividad (reporte, presentacion u otro).",
    "Confirmar sustitucion del placeholder de figura docente en plantilla .tex.",
    "Supuesto: falta consigna textual de actividad concreta para ajustar profundidad y formato."
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
      "Problema juridico claro.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Asegurar coherencia entre consigna, desarrollo y cierre juridico.",
      "Preservar calidad editorial institucional en cada entrega."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Sin placeholders al cierre."
    ],
    "argumentative_patterns": [
      "Del problema al marco conceptual.",
      "Del marco normativo a la evidencia.",
      "De la evidencia al analisis propio.",
      "Del analisis a conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
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
          "justification": "La identidad institucional exige forma y verificabilidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis debe responder al problema planteado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento juridico."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La estructura valida facilita control y auditoria editorial."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones no sustentadas."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "Archivo local derecho-de-la-propiedad-y-registro.bib.",
        "Regla institucional heredada: no propagar salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se deduplican reglas repetidas y se preserva contenido valido sin recorte semantico.",
      "Ciclo 14: se transfiere patron argumentativo estable desde actividad origen a materia destino.",
      "Ciclo 14: se evita importar contenido tematico especifico de Filosofia del Derecho por relacion transversal.",
      "Ciclo 14: se refuerza gate de JSON parseable y normalizacion previa a propagacion recursiva."
    ]
  }
}