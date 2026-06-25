{
  "summary": [
    "Se consolida sincronizacion transversal con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM, estructura canonica y compresion union-dedupe lossless.",
    "Se refuerza gate de bloqueo por JSON no parseable y normalizacion previa obligatoria.",
    "Se mantiene contexto local verificado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Se agrega regla transversal: problema, marco conceptual-normativo, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre exacto de asignatura: Derecho de la contratacion internacional.",
    "Vincular toda entrega a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local verificada: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Mantener trazabilidad del origen heredado y su estado de verificacion.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, evidencia, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No eliminar reglas utiles previas; solo anexar mejoras verificables."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen descriptivo y postura argumentada propia.",
    "Vincular cada argumento con norma, doctrina, jurisprudencia o dato verificable.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Declarar limites del analisis cuando falten datos de consigna.",
    "No reutilizar automaticamente fuentes de otras materias o semanas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que toda afirmacion no respaldada quede marcada como supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local.",
    "Verificar que README, programa analitico y plantilla LaTeX sean consistentes."
  ],
  "latex_rules": [
    "Mantener clase article en espanol con letterpaper y oneside en plantilla actual.",
    "Conservar macros institucionales de curso, universidad y autor.",
    "Completar documenttitle y documentsubtitle segun actividad real.",
    "Evitar paquetes o comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con acentos correctos.",
    "Resolver placeholders tipo $(@{...}.Slug) antes de publicar rutas o nombres.",
    "Corregir nombres corruptos detectados en README (reporte/referencias) antes de reutilizar."
  ],
  "bibliography_rules": [
    "Usar derecho-de-la-contratacion-internacional.bib como repositorio canonico local.",
    "No inventar referencias; incluir solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar fuentes especificas por actividad y conservar claves BibTeX estables.",
    "Incluir metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o mutables.",
    "No citar fuentes heredadas si no fueron usadas en la actividad destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o referencias tematicas no pertinentes al destino.",
    "Conservar aviso historico de incidente JSON hasta confirmar resolucion en ciclo activo.",
    "Aplicar deduplicacion semantica por union, sin recorte destructivo."
  ],
  "open_questions": [
    "Supuesto: la incidencia de JSON no parseable historica sigue abierta; confirmar cierre.",
    "Confirmar formato uniforme de citas juridicas para norma, jurisprudencia y doctrina.",
    "Confirmar checklist minimo por tipo de actividad: reporte, presentacion y producto visual.",
    "Confirmar si README y programa deben sustituir definitivamente placeholders de Slug.",
    "Confirmar rubrica oficial de evaluacion para calibrar profundidad argumentativa."
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
        "Entrada canonica por carpeta de materia.",
        "Trazabilidad de herencia editorial entre ciclos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Derecho de la contratacion internacional."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos consistentes y verificables.",
      "Asegurar transferencia profesional del razonamiento juridico en cada entrega."
    ],
    "style_markers": [
      "Supuestos explicitos cuando falten datos.",
      "Separacion neta entre descripcion y postura propia.",
      "Cierre con criterio juridico transferible.",
      "Consistencia entre consigna, desarrollo y producto."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> evidencia -> analisis -> conclusion.",
      "Afirmacion juridica -> fuente verificable -> interpretacion propia.",
      "Consigna local -> producto alineado -> control final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Compresion lossless por deduplicacion",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica",
        "Trazabilidad de herencia"
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
          "justification": "Sin salida estructurada no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis se activa por una pregunta juridica concreta."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica",
          "kind": "supports",
          "justification": "La conclusion debe estar fundada en fuentes verificables."
        },
        {
          "source": "Compresion lossless por deduplicacion",
          "target": "Trazabilidad de herencia",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida de contexto."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Bib local: repositorio canonico de referencias verificables.",
        "Registro historico: incidente de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se deduplican reglas repetidas y se preserva contenido util sin recorte.",
      "Ciclo 19: se transfiere solo abstraccion estable desde actividad origen a materia destino.",
      "Ciclo 19: se refuerza gate JSON y normalizacion previa como condicion de propagacion.",
      "Ciclo 19: se mantiene separacion entre identidad institucional y contexto tematico local."
    ]
  }
}