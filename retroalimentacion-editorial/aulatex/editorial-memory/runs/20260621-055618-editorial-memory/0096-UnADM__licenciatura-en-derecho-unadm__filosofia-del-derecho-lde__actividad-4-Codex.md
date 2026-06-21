{
  "summary": [
    "Se consolida refuerzo lateral desde actividad hermana con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se mantiene regla de normalizacion estructurada y JSON parseable obligatorio.",
    "Se transfieren patrones reutilizables sin copiar conclusiones ni redaccion especifica.",
    "Supuesto: la consigna exacta de Actividad 4 no esta visible en fuentes locales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas meramente descriptivas.",
    "Confirmar que el producto corresponda a la consigna de Actividad 4.",
    "No asumir fuentes de semanas distintas sin validacion de pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) antes de cerrar nombres de archivo.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin validacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales estables sin perder especificidad local.",
    "Aplicar union-dedupe para compresion lossless y evitar regresiones.",
    "Transferir solo patrones reutilizables entre nodos hermanos.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del .bib ante token Slug no resuelto en README.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere bloque bib propio."
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
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto segun planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables con fundamento juridico y evidencia.",
      "Asegurar trazabilidad entre problema, fuentes, analisis y conclusion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales con logica juridica.",
      "Cita explicita en afirmaciones sustantivas.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Integridad academica",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta institucional exige consistencia de voz y forma."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen el orden minimo del desarrollo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe estar respaldada por evidencia verificable."
        }
      ],
      "evidence": [
        "Pauta editorial local: identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico local: cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables: gate de JSON estricto obligatorio."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con y sin acentos sin perder contenido valido.",
      "Se mantuvieron reglas nucleares de identidad, estructura, calidad y LaTeX.",
      "Se removio transferencia de contenido especifico no reutilizable de actividad hermana.",
      "Se conservaron supuestos abiertos donde no hay consigna local verificable."
    ]
  }
}