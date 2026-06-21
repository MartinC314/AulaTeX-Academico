{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicacion lossless y continuidad UnADM.",
    "Se preservan reglas troncales de Actividad 1: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza control de normalizacion: no propagar si no hay JSON parseable y estructura minima completa.",
    "Se mantiene separacion entre patrones reutilizables y contenido especifico no transferible entre hermanos.",
    "Supuesto: falta consigna y rubrica locales de Actividad 5; se conserva estructura base sin inventar contenido."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Conservar enfoque juridico-academico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local.",
    "No usar memorias de modelo como fuentes academicas citables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Distinguir afirmacion, evidencia e inferencia en bloques claros.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar el producto al enunciado real de Actividad 5 sin romper reglas de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones especificas de Actividad 1.",
    "No arrastrar bibliografia exclusiva de otro hermano sin confirmar pertinencia.",
    "Registrar supuesto operativo cuando falte alcance local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia entre producto entregable y consigna local de Actividad 5.",
    "Aplicar revision manual extra si hay historial de incidentes de parseo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en .tex.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas y nombres con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib solo fuentes realmente citadas en el texto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como potencialmente tematico de otra semana hasta confirmar pertinencia."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales y de calidad sin bajar especificidad local.",
    "Aplicar union y deduplicacion semantica; no recortar reglas utiles previas.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "Abrir preguntas cuando falten datos locales en lugar de inventar detalles."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rubrica de evaluacion de Actividad 5.",
    "Confirmar tipo de producto requerido: reporte, presentacion o recurso visual.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si la bibliografia de Interpretacion juridica (Semana 7) aplica a Actividad 5."
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
      "Problema juridico bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables con rigor juridico.",
      "Garantizar coherencia entre consigna, desarrollo y cierre.",
      "Sostener una memoria editorial estable y reutilizable."
    ],
    "style_markers": [
      "Encuadre inicial breve y funcional.",
      "Secciones con funcion argumentativa clara.",
      "Supuestos explicitados cuando falte informacion.",
      "Cierre con criterio propio y aplicacion profesional."
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
        "Consistencia cita-.bib",
        "Bibliografia base",
        "Bibliografia especifica de actividad"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, integridad y forma del entregable."
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
          "justification": "La conclusion juridica exige respaldo trazable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Bibliografia especifica de actividad",
          "target": "Bibliografia base",
          "kind": "contrasts",
          "justification": "La base orienta; la especifica responde a la consigna local."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico fija ejes: problema, conceptos, fuentes, analisis y cierre.",
        "Historial documenta riesgo de salidas no parseables y necesidad de gate estructural."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion semantica de reglas repetidas.",
      "Ciclo 18: refuerzo lateral de patrones transferibles desde hermano Actividad 1.",
      "Ciclo 18: preservacion de reglas utiles previas sin eliminacion regresiva.",
      "Ciclo 18: se evito copiar conclusiones o bibliografia exclusiva entre hermanos."
    ]
  }
}