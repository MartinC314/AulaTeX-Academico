{
  "summary": [
    "Se consolida memoria lateral para Actividad 5 con deduplicacion lossless y continuidad UnADM.",
    "Se preservan ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se transfieren solo patrones reutilizables desde Actividad 1; no se copian conclusiones ni bibliografia exclusiva.",
    "Se refuerza control de supuestos cuando falta consigna local de Actividad 5."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar enfoque juridico-academico con claridad, evidencia y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmacion, evidencia e inferencia juridica en bloques claros.",
    "Alinear cada seccion al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el entregable al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si hay duda de alcance y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Rechazar salidas no estructuradas antes de reutilizacion.",
    "Aplicar revision manual extra en memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Validar nombre canonico del .bib antes de compilar.",
    "Supuesto: .bib canonico esperado filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematico de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Conservar reglas utiles previas; agregar solo mejoras verificables.",
    "Aplicar union-dedupe para compresion lossless.",
    "No propagar bibliografia no verificada como academica.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica de Actividad 5.",
    "Confirmar si Actividad 5 requiere reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura.",
    "Confirmar si la bibliografia de Semana 7 es pertinente para Actividad 5."
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
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables argumentativos verificables.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusion juridica.",
      "Preservar continuidad editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve y funcional.",
      "Secciones no ornamentales.",
      "Postura propia sustentada.",
      "Uso explicito de supuestos.",
      "Control estricto de consistencia cita-.bib."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual o normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con transferencia a practica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-.bib",
        "Bibliografia base vs bibliografia especifica"
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
          "justification": "La pauta institucional define tono, forma y exigencia argumentativa."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis nace de una pregunta delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo correcto no hay transferencia confiable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta la asignatura; la especifica responde a la consigna local."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico fija ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial reporta incidentes de salida no parseable; se requiere gate estructural."
      ]
    },
    "reinforcement_log": [
      "Ciclo 97: deduplicacion completa de reglas repetidas y variantes acentuales.",
      "Ciclo 97: refuerzo lateral de patrones reutilizables desde Actividad 1 a Actividad 5.",
      "Ciclo 97: se preserva regla de no propagar sin JSON parseable.",
      "Ciclo 97: se mantiene separacion entre bibliografia base y bibliografia por actividad.",
      "Ciclo 97: se agregan preguntas abiertas por falta de consigna local, sin inventar contenido."
    ]
  }
}