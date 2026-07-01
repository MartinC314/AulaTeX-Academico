{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicacion lossless y sin recorte de reglas utiles.",
    "Se preserva ADN UnADM: identidad institucional, estructura argumentativa juridica y control de calidad formal.",
    "Se transfiere solo patron reutilizable desde Actividad 1: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de salida JSON parseable antes de propagacion recursiva.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque juridico-academico con claridad y precision.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmacion, evidencia e inferencia en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas troncales de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones especificas de Actividad 1.",
    "No reutilizar bibliografia exclusiva de otra semana sin confirmar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar revision manual extra por historial de incidentes de parseo.",
    "Rechazar relaciones de grafo con tipos fuera de: supports, contrasts, depends_on, develops."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib; verificar localmente antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como orientado a Semana 7 hasta confirmacion para Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura completa.",
    "Aplicar union y deduplicacion semantica sin eliminar reglas validas previas.",
    "Transferir solo patrones reutilizables; no copiar redaccion literal ni conclusiones de nodos hermanos.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos previos.",
    "Cuando falte consigna local, propagar plantilla base y preguntas abiertas en lugar de contenido inventado."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 5; confirmar producto exacto solicitado.",
    "Confirmar si Actividad 5 requiere reporte, presentacion o recurso visual.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 5.",
    "Confirmar nombre canonico final del .bib operativo de la asignatura."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Asegurar coherencia entre consigna, argumentacion y evidencia.",
      "Preservar continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y no ornamentales.",
      "Postura propia sustentada.",
      "Supuestos explicitados cuando falten datos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-.bib"
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
          "target": "Estructura argumentativa",
          "kind": "supports",
          "justification": "La pauta institucional define tono, integridad y forma del entregable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida necesita respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografia base",
          "target": "Bibliografia especifica de actividad",
          "kind": "develops",
          "justification": "La base orienta y la especifica ajusta a la consigna local."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica y conclusion juridica.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial de memoria: incidentes de parseo obligan gate de estructura."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando equivalencias utiles.",
      "Se removieron traslados literales de contenido especifico de Actividad 1.",
      "Se reforzo control de tipos de relacion del grafo para consistencia.",
      "Se mantuvo separacion entre bibliografia base y bibliografia por actividad."
    ]
  }
}