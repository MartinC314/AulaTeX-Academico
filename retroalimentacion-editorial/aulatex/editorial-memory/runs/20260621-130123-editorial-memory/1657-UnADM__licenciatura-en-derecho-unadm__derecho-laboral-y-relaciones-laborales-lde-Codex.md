{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, normalizacion JSON y trazabilidad de fuentes.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, calidad y grafo conceptual.",
    "Se mantiene foco local de materia: Derecho laboral y relaciones laborales, semestre 7, bloque 1, 8 creditos.",
    "Se refuerza correccion de marcadores de plantilla sin expandir en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia destino.",
    "Usar contexto curricular verificado: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o plantilla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la planeacion semanal y consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Corregir rutas y nombres mal renderizados antes de canonizarlos."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Bloquear consolidacion o propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto y metadatos de plantilla."
  ],
  "latex_rules": [
    "Mantener compilacion en espanol y letterpaper.",
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y nombres de archivo.",
    "Completar entornos truncados de plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON, estructura y trazabilidad.",
    "Compartir entre nodos no equivalentes solo reglas editoriales estables.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Si un nodo vecino esta vacio, sembrar cerebro editorial minimo y dejar vacios locales abiertos."
  ],
  "open_questions": [
    "Supuesto: falta rubrica oficial por actividad en la materia destino.",
    "Confirmar formato de cita juridica exigido por docente.",
    "Confirmar si autor de plantilla es variable por alumno.",
    "Confirmar nombres canonicos finales tras corregir marcadores $(@{...}.Slug).",
    "Confirmar checklist de evaluacion local para convertir quality gates en control operativo."
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
        "Carpeta de materia como entrada canonica.",
        "Normalizacion obligatoria de salidas no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico laboral bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Garantizar coherencia entre consigna, estructura, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Frases precisas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin redaccion literal heredada entre materias.",
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
        "Normalizacion JSON",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "La identidad institucional exige trazabilidad y rigor de cita."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis pertinente depende de una delimitacion correcta del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento juridico verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura valida evita propagar errores editoriales."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La postura argumentativa mejora cuando se sustenta con evidencia trazable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo reutilizables.",
        "Bibliografia local: claves institucionales existentes y verificables.",
        "Antecedentes de salidas no parseables: regla de normalizacion reforzada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se mantiene union-dedupe lossless sin eliminar reglas utiles previas.",
      "Ciclo 19: se consolida patron transversal problema-conceptos-evidencia-analisis-conclusion.",
      "Ciclo 19: se refuerza gate estricto de JSON parseable antes de propagacion recursiva.",
      "Ciclo 19: se mantiene correccion de tokens de plantilla sin expandir como control tecnico-editorial."
    ]
  }
}