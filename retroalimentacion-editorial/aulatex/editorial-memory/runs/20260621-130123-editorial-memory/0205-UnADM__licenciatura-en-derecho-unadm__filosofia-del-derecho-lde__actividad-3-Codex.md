{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 hacia actividad-3 sin copiar contenido especifico.",
    "Se preservan reglas institucionales, estructurales, de calidad y LaTeX con deduplicacion lossless.",
    "Se mantiene bloqueo de propagacion si no hay JSON parseable.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, analisis propio y conclusion juridica.",
    "Se mantiene politica de supuestos para datos no confirmados de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales no verificadas como antecedentes provisionales, no como fuentes academicas.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables entre actividades hermanas.",
    "No copiar redaccion literal ni conclusiones especificas de actividad-1.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o bibliografia obligatoria sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad verificada.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas en la actividad.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib puede ser tematico de Semana 7 y no necesariamente de actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos hermanos reglas generales de identidad, estructura y calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar union y deduplicacion lossless en cada ciclo.",
    "Mantener bandera de riesgo cuando existan incidencias historicas de parseo.",
    "Escalar preguntas abiertas cuando falte consigna local."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar bibliografia obligatoria de la semana de actividad-3.",
    "Confirmar si actividad-3 reutiliza bibliografia depurada de interpretacion juridica.",
    "Confirmar archivo .tex principal canonico para actividad-3."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Normalizacion estructurada obligatoria antes de propagar."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico verificable.",
      "Asegurar trazabilidad entre afirmaciones, evidencia y conclusion.",
      "Conservar identidad UnADM con utilidad profesional del cierre juridico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y orden logico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo consistente -> cierre transferible."
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
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta editorial institucional exige evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
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
        "README: identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico: ejes problema, conceptos, fuentes, analisis y cierre.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion integral sin perdida de reglas utiles.",
      "Ciclo 8: refuerzo lateral controlado de patrones, sin copiar contenido especifico entre hermanos.",
      "Ciclo 8: se conserva politica de supuestos y no invencion de fuentes."
    ]
  }
}