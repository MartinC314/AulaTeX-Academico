{
  "summary": [
    "Sincronizacion transversal aplicada con deduplicacion semantica y sin recorte.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se transfiere del origen solo abstraccion reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables y heredados no normalizados.",
    "Se refuerza el destino con cerebro editorial minimo estable para materia no equivalente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y materia Derecho laboral y relaciones laborales.",
    "Usar contexto curricular verificado: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto con la planeacion semanal y la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Registrar reglas nuevas por union-dedupe sin eliminar reglas utiles previas."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral.",
    "Transformar la consigna en el tipo de producto solicitado: reporte, presentacion o visual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar o propagar.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto y metadatos."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener compilacion sin errores criticos ni referencias rotas.",
    "Conservar macros institucionales de curso y universidad.",
    "Completar metadatos reales de actividad antes de compilar.",
    "Resolver marcadores sin expandir tipo $(@{...}.Slug) en README, programa y rutas.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar solo referencias verificables y consultables.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Marcar como supuesto metadatos faltantes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico no homologable.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar normalizacion manual a memorias de ciclos con salida no parseable."
  ],
  "open_questions": [
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar formato de cita juridica exigido por docente (supuesto: no definido en archivos visibles).",
    "Confirmar si autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias.",
    "Confirmar si existe criterio local para jurisprudencia laboral en .bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion obligatoria de salidas no estructuradas.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas o doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Asegurar coherencia entre consigna, estructura, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados explicitamente.",
      "Trazabilidad de citas y fuentes.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar evidencia y doctrina.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion de salidas no parseables"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificacion de fuentes."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento juridico explicito."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica necesita respaldo comprobable."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar memoria defectuosa y mantiene consistencia editorial."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La propagacion solo procede con estructura valida."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Archivo .bib local: claves institucionales verificables.",
        "Supuesto: formato de cita docente no visible en fuentes locales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion aplicada sin perdida de reglas utiles.",
      "Ciclo 11: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 11: se consolida patron argumentativo transversal reusable.",
      "Ciclo 11: se mantiene politica de supuestos explicitos y fuentes provisionales.",
      "Ciclo 11: se corrige transferencia para nodos no equivalentes con abstracciones estables."
    ]
  }
}