{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preservan reglas utiles previas del nodo destino y del origen sin recorte.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, gates y grafo conceptual.",
    "Se mantiene obligatoria la normalizacion de salidas no parseables antes de reutilizar o propagar.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se conserva enfoque local del destino: Derecho laboral y relaciones laborales en UnADM."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia Derecho laboral y relaciones laborales.",
    "Usar contexto curricular verificado: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar como provisionales las fuentes heredadas no verificadas.",
    "Usar autor de plantilla solo si esta confirmado por el alumno. [supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la consigna y planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar la planeacion en reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en un conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada propia; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral.",
    "Marcar supuestos cuando falten datos de consigna o rubrica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre README, programa analitico y plantilla LaTeX.",
    "Detectar marcadores de plantilla sin expandir antes de canonizar nombres."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas o nombres mal renderizados antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y referencias.",
    "Completar entornos truncados de plantilla antes de compilar. [supuesto]"
  ],
  "bibliography_rules": [
    "Centralizar fuentes de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo entradas BibTeX consultables y pertinentes a la actividad.",
    "No inventar referencias, normas, doctrina ni jurisprudencia.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto metadatos faltantes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo reglas editoriales estables.",
    "Evitar transferencia de redaccion literal o contenido tematico de otra materia.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar formato de citacion juridica exigido por docente (APA, ISO 690 u otro).",
    "Confirmar si el autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias.",
    "Confirmar si el entorno authortable de la plantilla quedo completo. [supuesto]"
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
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas o doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Orientar productos academicos con claridad, fundamento juridico y transferencia profesional.",
      "Convertir planeacion semanal en entregables argumentativos verificables."
    ],
    "style_markers": [
      "Frases precisas y accionables.",
      "Supuestos marcados en forma explicita.",
      "Coherencia entre consigna, estructura y evidencia.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar evidencia.",
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
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida necesita fundamento juridico."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar errores estructurales y perdida de trazabilidad."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bibliografia local: claves institucionales verificables.",
        "Regla heredada estable: normalizar antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se consolida transferencia transversal estable desde actividad de otra materia sin copiar contenido tematico.",
      "Ciclo 20: se refuerza gate de JSON parseable y normalizacion previa como regla no negociable.",
      "Ciclo 20: se mantiene ADN argumentativo comun y foco local juridico-laboral del destino."
    ]
  }
}