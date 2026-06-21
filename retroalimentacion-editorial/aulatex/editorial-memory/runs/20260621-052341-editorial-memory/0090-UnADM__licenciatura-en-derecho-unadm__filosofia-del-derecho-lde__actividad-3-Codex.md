{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 sin copiar conclusiones especificas.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analitico.",
    "Se mantiene regla critica: normalizar estructura y bloquear propagacion sin JSON parseable.",
    "Se refuerzan ejes recurrentes: problema, conceptos y fuentes, analisis propio y conclusion juridica.",
    "Se conserva deduplicacion lossless por union y sin regresion de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias Codex o GPT-Pro como antecedente editorial provisional, no como fuente academica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1.",
    "No copiar redaccion literal ni conclusiones especificas del nodo hermano.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, tema o formato de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar regla de no regresion: no eliminar reglas utiles previas.",
    "Distinguir evidencia academica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de cerrar entrega.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Usar archivo .tex de reporte o presentacion segun consigna confirmada."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en la actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de asignatura y bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib es tematico de Semana 7 y su uso en actividad-3 debe confirmarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos reglas institucionales, de estructura, calidad y trazabilidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Mantener bandera de riesgo cuando haya historial de salida no estructurada.",
    "Escalar preguntas abiertas cuando falte consigna local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato requerido: reporte, presentacion u otro.",
    "Confirmar tema real de actividad-3 y su semana correspondiente.",
    "Confirmar bibliografia obligatoria especifica de actividad-3.",
    "Confirmar archivo .tex principal canonico para actividad-3.",
    "Confirmar si aplica o no la bibliografia depurada de interpretacion juridica."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros y fundamentados.",
      "Asegurar evidencia verificable y argumentacion propia.",
      "Sostener continuidad editorial entre actividades sin perdida de reglas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Citas verificables en afirmaciones clave.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La pauta institucional exige criterio propio con rigor academico."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Bibliografia verificable",
          "kind": "depends_on",
          "justification": "La trazabilidad de citas y reglas requiere estructura parseable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad academica, citas verificables y conclusion juridica.",
        "Programa analitico define ejes de trabajo y proposito editorial.",
        "Historial de incidencias confirma necesidad de bloqueo sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 90: se consolidan reglas hermanas reutilizables sin copiar contenido especifico.",
      "Ciclo 90: se elimina duplicidad semantica y se preserva cobertura lossless.",
      "Ciclo 90: se refuerza politica de supuestos y no invencion de fuentes."
    ]
  }
}