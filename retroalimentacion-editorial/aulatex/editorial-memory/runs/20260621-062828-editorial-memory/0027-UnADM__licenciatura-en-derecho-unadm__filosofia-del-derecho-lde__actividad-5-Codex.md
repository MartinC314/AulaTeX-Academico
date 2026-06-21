{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificable del README.",
    "Se refuerzan ejes editoriales troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar sin JSON parseable y estructura minima completa.",
    "Se conserva distincion entre bibliografia base de asignatura y bibliografia especifica por actividad.",
    "Supuesto: falta consigna local completa de Actividad 5; se mantiene plantilla argumentativa reusable."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda salida a UnADM, Licenciatura en Derecho, Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar encuadre curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias de modelos previos como insumo provisional, no como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmacion, evidencia e inferencia juridica.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear el entregable al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar contenido al enunciado real de Actividad 5 cuando se confirme.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones especificas de Actividad 1.",
    "No reutilizar bibliografia de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar contradicciones con identidad institucional y reglas vigentes.",
    "Aplicar revision manual extra si hay huella de incidentes de parseo previos."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Supuesto: .bib canonico esperado filosofia-del-derecho.bib; confirmar en contexto local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo obras realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de asignatura y bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; confirmar pertinencia para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir patrones reutilizables, no redaccion literal ni conclusiones cerradas.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union y deduplicacion semantica en cada ciclo.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos previos.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 5.",
    "Confirmar rubrica de evaluacion especifica de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del .bib de asignatura tras resolver token Slug.",
    "Confirmar si fuentes de Semana 7 aplican a Actividad 5.",
    "Confirmar fuentes obligatorias de la semana de Actividad 5."
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
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables academicos consistentes.",
      "Asegurar trazabilidad entre consigna, desarrollo, evidencia y cierre.",
      "Sostener continuidad editorial entre actividades hermanas sin copiar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales.",
      "Postura propia sustentada.",
      "Supuestos marcados cuando falten datos.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Transferencia a contexto profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-.bib",
        "Bibliografia base",
        "Bibliografia especifica por actividad"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, rigor y forma del entregable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere conflicto o pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia confiable."
        },
        {
          "source": "Bibliografia base",
          "target": "Bibliografia especifica por actividad",
          "kind": "contrasts",
          "justification": "La base orienta; la especifica responde a la consigna local."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El marco permite argumentacion juridica consistente."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de memoria: incidentes de salida no parseable requieren gate estructural.",
        "Contexto local: token Slug sin expandir en nombres de archivo; requiere confirmacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 27: deduplicacion semantica de reglas repetidas.",
      "Ciclo 27: preservadas reglas utiles previas sin recorte funcional.",
      "Ciclo 27: reforzada separacion entre patrones transferibles y contenido especifico de hermano.",
      "Ciclo 27: mantenida politica de supuestos explicitos ante falta de consigna local."
    ]
  }
}