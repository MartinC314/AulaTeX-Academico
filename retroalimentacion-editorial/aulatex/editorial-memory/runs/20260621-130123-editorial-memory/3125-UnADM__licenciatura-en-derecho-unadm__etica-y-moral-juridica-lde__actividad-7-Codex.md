{
  "summary": [
    "Se realiza refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica con transferencia de patrones reutilizables.",
    "Se conserva compresion lossless por deduplicacion y sin eliminar reglas utiles previas.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene validacion JSON estricta y esquema completo antes de propagacion recursiva.",
    "Se preserva trazabilidad de supuestos y de fuentes provisionales no verificadas localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el tipo de entrega corresponda a la consigna de Actividad 7.",
    "No trasladar conclusiones especificas de otra asignatura; solo patrones de metodo."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura minima completa.",
    "Reutilizar reglas institucionales y de calidad comunes entre asignaturas del mismo bloque curricular.",
    "Aplicar analogia controlada: transferir metodo editorial, no contenido tematico especifico.",
    "Si falta consigna local, mantener estructura base y abrir preguntas en lugar de inventar datos.",
    "Mantener historial de ciclos con normalizacion manual cuando existan salidas no parseables."
  ],
  "open_questions": [
    "Confirmar consigna exacta y producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar politica local de manejo de claves BibTeX duplicadas para retrocompatibilidad. [Supuesto]",
    "Confirmar si se normalizaran tokens Slug en README/programa como parte del siguiente ciclo tecnico.",
    "Confirmar fuentes obligatorias de la semana correspondiente a Actividad 7."
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
        "Entrada canonica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Resolver un problema juridico o social con base conceptual y evidencia.",
      "Transformar planeacion semanal en producto academico evaluable.",
      "Sostener analisis propio y cierre juridico transferible."
    ],
    "reason_for_being": [
      "Conservar un nucleo editorial comun y verificable entre actividades laterales.",
      "Elevar consistencia metodologica sin forzar traslados tematicos indebidos.",
      "Garantizar trazabilidad, calidad formal y utilidad profesional del producto."
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
      "Exponer conceptos y marco normativo/doctrinal.",
      "Contrastar posturas con evidencia.",
      "Fijar postura propia.",
      "Concluir con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico o social",
        "Evidencia verificable",
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
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La pauta institucional exige integridad academica y citas comprobables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento juridico se construye a partir de una delimitacion inicial del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar del desarrollo argumentativo y la evidencia."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es base recurrente para argumentar en la asignatura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La validez del cierre depende del sustento documental."
        }
      ],
      "evidence": [
        "README de la asignatura: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito de realizacion y ejes de trabajo.",
        "Bibliografia local .bib: base disponible y necesidad de gestion cuidadosa de duplicados."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se refuerzan reglas nucleares transferibles sin copiar redaccion literal del nodo hermano.",
      "Ciclo 12: se mantiene regla de normalizacion estructurada previa a propagacion recursiva.",
      "Ciclo 12: se consolidan puertas de calidad y control explicito de supuestos.",
      "Ciclo 12: se preserva compatibilidad LaTeX/BibTeX y trazabilidad editorial."
    ]
  }
}