{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con patrones reutilizables.",
    "Se preserva identidad UnADM, ubicacion curricular y pauta editorial verificable del nodo destino.",
    "Se consolida estructura canonica de actividad: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union y deduplicacion sin recorte de reglas utiles.",
    "Se mantiene bloqueo de propagacion cuando no exista JSON parseable y esquema completo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como sustento de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Integrar evidencia verificable en el desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el producto final al tipo de entrega solicitado en la planeacion semanal."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de otras semanas o materias sin validacion.",
    "Confirmar que el producto corresponde a la consigna de Actividad 7."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar propagacion recursiva solo si pasan todas las compuertas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas y nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar entradas equivalentes sin perder trazabilidad de claves existentes. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones del origen.",
    "Mantener normalizacion manual para ciclos con entradas no parseables.",
    "Evitar regresiones frente a reglas de calidad ya consolidadas.",
    "Si faltan datos locales, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta y tipo de producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente en Etica y Moral juridica.",
    "Confirmar politica local de alias para claves BibTeX duplicadas.",
    "Confirmar cierre correcto de la entrada truncada en etica-y-moral-juridica.bib. [Supuesto]"
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
        "Carpeta de asignatura como entrada canonica.",
        "Validacion estructural previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Actividad destino: Actividad 7."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Sostener trazabilidad editorial y bibliografica.",
      "Garantizar utilidad juridica profesional del cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y norma aplicable.",
      "Contrastar evidencia.",
      "Tomar postura propia.",
      "Concluir con criterio juridico transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Practica juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento parte del problema para construir postura."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida deriva del analisis y evidencia."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual sostiene la argumentacion de la materia."
        },
        {
          "source": "Moral",
          "target": "Practica juridica",
          "kind": "depends_on",
          "justification": "La valoracion moral condiciona decisiones de actuacion profesional."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bibliografia local .bib: base de fuentes y necesidad de control de duplicados."
      ]
    },
    "reinforcement_log": [
      "Se conservaron todas las reglas utiles previas del destino por union deduplicada.",
      "Se incorporaron patrones estructurales estables del origen sin copiar contenido especifico.",
      "Se reforzo control de supuestos y validacion JSON como compuertas obligatorias.",
      "Se mantuvo separacion entre bibliografia base y bibliografia por actividad."
    ]
  }
}