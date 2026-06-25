{
  "summary": [
    "Se consolida transferencia lateral reutilizable desde Filosofia del Derecho hacia Etica y Moral juridica sin copiar contenido especifico.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless en formato JSON.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene validacion estructural estricta antes de propagacion recursiva.",
    "Se incorpora control explicito de supuestos cuando falte consigna local verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sustentar ubicacion curricular con malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la planeacion semanal de la actividad.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Confirmar que el tipo de entrega corresponde a la consigna de Actividad 7.",
    "No asumir fuentes de otras semanas o materias sin validacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas y nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener clave canonica y alias solo si no rompe retrocompatibilidad. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y metodo.",
    "Evitar copiar conclusiones especificas o bibliografia exclusiva entre materias hermanas.",
    "Aplicar normalizacion manual si un nodo vecino entrega salida no estructurada.",
    "Evitar regresiones respecto de reglas utiles previamente consolidadas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta y producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar politica local de alias BibTeX para duplicados existentes.",
    "Confirmar si el .bib local esta completo o truncado antes de normalizar duplicados. [Supuesto]"
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
        "Carpeta de asignatura como entrada canonica.",
        "Validacion estructural previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y utiles para la practica juridica.",
      "Preservar trazabilidad editorial y calidad tecnica en cada ciclo de memoria."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar posturas con evidencia.",
      "Fijar postura del estudiante.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
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
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El argumento se construye desde la delimitacion del caso o dilema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende del razonamiento y evidencia previos."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es base transversal en la asignatura."
        },
        {
          "source": "Moral",
          "target": "Practica juridica",
          "kind": "depends_on",
          "justification": "La valoracion moral orienta criterios de actuacion profesional."
        }
      ],
      "evidence": [
        "README de la asignatura confirma identidad institucional y ubicacion curricular.",
        "Programa analitico define ejes de trabajo y proposito editorial.",
        "Archivo .bib local confirma base bibliografica y necesidad de control de duplicados."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se refuerza transferencia lateral de patrones editoriales comunes sin arrastre de contenido especifico.",
      "Ciclo 10: se mantiene regla de no propagar salidas no parseables.",
      "Ciclo 10: se preserva compresion lossless por union y deduplicacion."
    ]
  }
}