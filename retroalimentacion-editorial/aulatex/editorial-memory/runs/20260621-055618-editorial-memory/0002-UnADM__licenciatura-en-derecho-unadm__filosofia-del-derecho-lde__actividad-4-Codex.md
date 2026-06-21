{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificable.",
    "Se refuerza validacion JSON estricta por antecedentes no parseables.",
    "Se transfieren solo patrones reutilizables desde Actividad 1.",
    "Supuesto: falta consigna local completa de Actividad 4."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Conservar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el producto final coincide con consigna de Actividad 4.",
    "Supuesto: no fijar tema especifico sin consigna visible."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto y consigna local."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres de archivo con caracteres danados o tokens sin resolver.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Agregar fuentes especificas de actividad en .bib de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base y bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin verificar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Evitar copiar conclusiones o bibliografia exclusiva entre hermanos.",
    "Mantener deduplicacion por union sin recorte semantico.",
    "Conservar banderas de normalizacion manual en ciclos con salida sucia.",
    "Propagar mejoras verificables a nodos laterales de la asignatura."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar formato requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre final del .bib canonico por token Slug no resuelto.",
    "Confirmar si reutiliza bibliografia existente o requiere .bib incremental."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
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
      "Transformar planeacion semanal en producto academico verificable.",
      "Asegurar coherencia entre identidad institucional, estructura y evidencia.",
      "Garantizar salida reutilizable y propagable sin degradacion."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales claras.",
      "Cita explicita por afirmacion relevante.",
      "Marcado de supuestos cuando falte dato local.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Delimitar conceptos y normas aplicables.",
      "Contrastar evidencia con postura propia.",
      "Resolver tension argumentativa.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato academico."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion segura."
        },
        {
          "source": "Relacion problema-evidencia-conclusion",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion se legitima por evidencia y analisis propio."
        }
      ],
      "evidence": [
        "Pauta editorial del README.",
        "Ejes de trabajo del programa analitico.",
        "Antecedentes de salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas por variantes ortograficas.",
      "Se preservaron gates de JSON y normalizacion manual.",
      "Se evitaron traslados de contenido especifico de Actividad 1.",
      "Se reforzo manejo de supuestos por falta de consigna local.",
      "Se mantuvo compatibilidad LaTeX-BibTeX sin inventar fuentes."
    ]
  }
}