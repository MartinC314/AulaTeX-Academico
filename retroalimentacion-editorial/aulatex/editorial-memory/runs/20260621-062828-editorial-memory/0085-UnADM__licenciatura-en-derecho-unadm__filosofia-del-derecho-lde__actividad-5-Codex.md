{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicacion lossless.",
    "Se preserva identidad UnADM, estructura canonica y gates de calidad.",
    "Se transfieren patrones reutilizables desde Actividad 1 sin copiar contenido especifico.",
    "Se mantiene regla de normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se refuerza distincion entre bibliografia base y bibliografia especifica por actividad.",
    "Supuesto: falta consigna y rubrica local de Actividad 5; se mantiene plantilla editorial abierta."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear siempre con UnADM, Licenciatura en Derecho, Filosofia del Derecho.",
    "Conservar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales, no academicas."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir explicitamente afirmacion, evidencia e inferencia.",
    "Alinear el entregable al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones ni bibliografia exclusiva de actividades hermanas.",
    "Si falta alcance, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones clave.",
    "Validar consistencia entre citas en texto y .bib.",
    "Rechazar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Aplicar revision manual extra en memoria con historial de parseo fallido."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib, sujeto a verificacion local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Confirmar pertinencia antes de reutilizar bibliografia de Semana 7 en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir reglas generales reutilizables, no redaccion literal.",
    "Evitar regresiones: no eliminar reglas utiles previas.",
    "Aplicar union y deduplicacion como metodo de compresion lossless.",
    "Si faltan datos locales, propagar plantilla base y preguntas abiertas.",
    "Mantener bandera de riesgo historico por salidas no parseables en ciclos previos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica de evaluacion especifica de Actividad 5.",
    "Confirmar tipo de producto: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del .bib de asignatura.",
    "Confirmar si la bibliografia clean de Semana 7 aplica a Actividad 5."
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros y fundamentados.",
      "Sostener trazabilidad entre consigna, desarrollo, evidencia y conclusion.",
      "Garantizar continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales sin relleno.",
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
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bib"
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
          "justification": "La pauta institucional define tono, forma y estandar de integridad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
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
          "justification": "La transferencia segura exige estructura parseable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta el curso; la especifica responde a la consigna local."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad academica.",
        "Programa analitico fija ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial del nodo reporta incidentes de salida no parseable.",
        "Reglas de transferencia exigen no copiar conclusiones ni bibliografia exclusiva entre hermanos."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se preservaron reglas utiles previas de identidad, estructura, calidad y LaTeX.",
      "Se reforzo gate de JSON parseable como condicion de propagacion.",
      "Se mantuvo separacion entre patrones transferibles y contenido especifico de actividad hermana.",
      "Se agregaron supuestos explicitos donde faltan datos locales verificables."
    ]
  }
}