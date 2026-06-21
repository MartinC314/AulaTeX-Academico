{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicacion lossless.",
    "Se preserva identidad UnADM, ubicacion curricular y pauta editorial canonica.",
    "Se refuerza normalizacion JSON obligatoria antes de propagacion recursiva.",
    "Se mantienen ejes troncales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se transfieren solo patrones reutilizables desde Actividad 1, sin copiar conclusiones ni bibliografia exclusiva.",
    "Supuesto: falta consigna y rubrica local de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Alinear contenido con Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Mantener ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar enfoque juridico-academico con integridad academica y citas verificables.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmaciones, evidencia e inferencia juridica.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar bibliografia de otra semana sin confirmar pertinencia.",
    "Registrar supuesto operativo si hay duda de alcance."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar que el producto responda al problema y no solo resuma conceptos.",
    "Aplicar revision manual extra a memoria con incidentes previos de parseo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Validar nombre canonico real del .bib antes de compilar.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Agregar en .bib solo fuentes realmente citadas.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Confirmar pertinencia antes de reutilizar bibliografia de Semana 7 en Actividad 5."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe para compresion lossless; evitar recorte semantico.",
    "No propagar fuentes provisionales como bibliografia academica.",
    "Cuando falte consigna local, propagar plantilla estructural y preguntas abiertas.",
    "Evitar copiar redaccion literal, conclusiones especificas o bibliografia exclusiva entre hermanos."
  ],
  "open_questions": [
    "Supuesto: falta enunciado especifico de Actividad 5; confirmar consigna exacta.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar formato requerido: reporte, presentacion o recurso visual.",
    "Confirmar si Actividad 5 usa filosofia-del-derecho.bib o archivo especifico propio.",
    "Confirmar pertinencia de entradas de interpretacion juridica (Semana 7) para Actividad 5."
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
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico evaluable.",
      "Asegurar coherencia entre consigna, desarrollo y cierre juridico.",
      "Mantener trazabilidad editorial y tecnica para propagacion confiable."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales sin relleno.",
      "Afirmacion seguida de evidencia.",
      "Uso explicito de supuestos cuando falte informacion."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con aplicacion a practica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-.bib",
        "Bibliografia base",
        "Bibliografia especifica de actividad"
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
          "justification": "Define tono, forma y criterios minimos del entregable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia confiable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta la materia; la especifica responde a la consigna."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico: ejes problema-conceptos-fuentes-analisis-cierre.",
        "Historial: incidentes de salida no parseable obligan gate tecnico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 95: deduplicacion de reglas repetidas en tono, estructura y calidad.",
      "Ciclo 95: refuerzo lateral de gates JSON y consistencia cita-.bib.",
      "Ciclo 95: conservadas reglas utiles previas sin eliminacion.",
      "Ciclo 95: aislados elementos no transferibles (conclusiones/bibliografia exclusiva de hermano).",
      "Ciclo 95: mantenidas preguntas abiertas por falta de consigna local."
    ]
  }
}