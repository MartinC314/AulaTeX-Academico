{
  "summary": [
    "Se refuerza actividad-2 con patrones reutilizables validados en actividad-1.",
    "Se mantiene compresion lossless por union y deduplicacion sin recorte.",
    "Se preserva identidad UnADM, ejes editoriales y control de calidad estructural.",
    "Se evita transferir conclusiones o bibliografia exclusiva del nodo hermano.",
    "Se mantiene caracter provisional de fuentes heredadas no verificadas localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre juridico.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la consigna docente disponible.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables y compatibles con el .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y nombres de archivo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y marco juridico verificable.",
    "Agregar fuentes especificas de actividad-2 en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Mantener metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico, no reemplazo automatico [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones generales reutilizables entre hermanos.",
    "Evitar copiar redaccion literal, conclusiones o bibliografia exclusiva del hermano.",
    "Mantener reglas utiles previas sin regresion.",
    "Aplicar normalizacion manual si reaparecen salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si el producto es reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica de actividad-2.",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug en README.",
    "Confirmar si existe estilo de citacion institucional obligatorio [supuesto: no confirmado]."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio.",
      "Evidencia verificable.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico con fundamento juridico.",
      "Asegurar trazabilidad entre afirmaciones, citas y bibliografia.",
      "Sostener continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales trazables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Normalizacion estructurada",
        "Trazabilidad cita-bibliografia",
        "Analisis propio"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, finalidad y criterios de entrega."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia confiable."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Regla consolidada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura total.",
      "Se reforzo transferencia lateral por patrones, no por contenido especifico.",
      "Se preservaron reglas historicas de normalizacion y calidad.",
      "Se agregaron supuestos explicitos donde faltan datos locales."
    ]
  }
}