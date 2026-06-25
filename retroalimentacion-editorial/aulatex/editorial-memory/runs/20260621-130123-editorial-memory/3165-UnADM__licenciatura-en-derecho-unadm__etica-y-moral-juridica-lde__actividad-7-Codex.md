{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofia del Derecho a Etica y Moral juridica con deduplicacion lossless.",
    "Se preservan reglas validas previas del destino y se agregan solo patrones reutilizables verificados.",
    "Se consolidan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene validacion JSON estricta y normalizacion antes de propagacion recursiva.",
    "Se mantiene trazabilidad de supuestos cuando la consigna local no sea visible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sustentar ubicacion curricular con malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Preparar salida estructurada y parseable antes de propagar memoria."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar usar fuentes de otras semanas o materias sin validacion local.",
    "Confirmar que el entregable corresponda a la consigna de Actividad 7.",
    "Evitar afirmaciones sin respaldo o sin marca de [Supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar.",
    "Confirmar no eliminacion de reglas utiles previas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar propagacion recursiva solo tras pasar compuertas de calidad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas.",
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
    "Propagar lateral y recursivo solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables, no conclusiones ni redaccion literal.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Evitar regresiones sobre reglas de calidad ya consolidadas.",
    "Si faltan datos locales, propagar plantilla base y abrir preguntas.",
    "Registrar ciclo y fuente provisional cuando el origen futuro no sea parseable. [Supuesto]"
  ],
  "open_questions": [
    "Confirmar consigna exacta y formato de entrega de Actividad 7.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana para Etica y Moral juridica.",
    "Confirmar politica local de alias para claves BibTeX duplicadas.",
    "Confirmar si las claves duplicadas actuales deben mantenerse por retrocompatibilidad. [Supuesto]",
    "Confirmar cierre correcto de la entrada truncada en etica-y-moral-juridica.bib."
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
      "Transformar planeacion semanal en productos academicos rigurosos.",
      "Asegurar coherencia argumentativa y utilidad profesional.",
      "Preservar identidad UnADM con trazabilidad documental."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados.",
      "Cierre con aplicacion juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco aplicable.",
      "Contrastar posturas con evidencia.",
      "Tomar posicion propia justificada.",
      "Concluir con criterio transferible a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento se construye desde una delimitacion inicial clara."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es recurrente en la asignatura."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La argumentacion requiere fundamento doctrinal o normativo verificable."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bibliografia local: existencia de claves duplicadas y necesidad de politica de alias. [Supuesto]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se consolidan patrones reutilizables del nodo lateral sin copiar contenido especifico.",
      "Ciclo 22: se mantiene control de calidad JSON y no regresion de reglas utiles.",
      "Ciclo 22: se refuerza regla de supuestos explicitos ante datos no visibles."
    ]
  }
}