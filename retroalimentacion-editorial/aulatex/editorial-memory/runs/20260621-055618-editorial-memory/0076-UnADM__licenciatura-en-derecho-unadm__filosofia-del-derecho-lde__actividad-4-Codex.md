{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 4 sin copiar contenido especifico.",
    "Se preservan reglas institucionales UnADM y ejes editoriales comunes de la asignatura.",
    "Se mantiene deduplicacion lossless con normalizacion de redaccion y acentos.",
    "Se refuerza validacion JSON estricta por antecedentes de salidas no parseables.",
    "Supuesto: la consigna puntual de Actividad 4 no esta visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el producto corresponda a la consigna de Actividad 4.",
    "No arrastrar conclusiones especificas de actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib puede no corresponder a Actividad 4; verificar aplicabilidad."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables de identidad, estructura, calidad y trazabilidad.",
    "No propagar redaccion literal ni bibliografia exclusiva entre hermanos.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas.",
    "Escalar mejoras verificables a nodos laterales de la misma asignatura."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios de evaluacion.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del .bib con slug resuelto.",
    "Confirmar si se usa .bib incremental o el .bib general de la asignatura."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
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
      "Transformar planeacion semanal en productos academicos con fundamento juridico.",
      "Asegurar trazabilidad entre consigna, argumento y conclusion.",
      "Preservar consistencia institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales y ordenadas.",
      "Postura personal sustentada.",
      "Supuestos marcados de forma explicita.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y normas.",
      "Contrastar evidencia.",
      "Desarrollar postura propia.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen secuencia de desarrollo y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida requiere respaldo verificable."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y criterio de conclusion juridica.",
        "Programa analitico fija cinco ejes reutilizables para todas las actividades.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 76: refuerzo lateral aplicado con transferencia de patrones reutilizables.",
      "Se deduplicaron variantes ortograficas y de acentuacion sin perdida de reglas.",
      "Se mantuvieron reglas utiles previas y se evitaron traslados de contenido especifico.",
      "Se reforzo control de supuestos por falta de consigna local visible."
    ]
  }
}