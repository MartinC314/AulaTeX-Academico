{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless por union.",
    "Se preserva identidad UnADM y marco curricular verificable de Filosofia del Derecho.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate estricto: no propagar salidas no estructuradas ni JSON no parseable.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; se conserva estructura base sin inventar contenido."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Vincular la actividad a Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear forma de entrega al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes exclusivas de otra actividad sin confirmar pertinencia.",
    "Confirmar primero si Actividad 4 exige reporte, presentacion u otro formato.",
    "Integrar evidencia solo cuando exista respaldo documental local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo.",
    "Validar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia final del producto con consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si la consigna de Actividad 4 coincide tematicamente.",
    "Conservar trazabilidad entre cita en texto y entrada bibliografica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales reutilizables.",
    "No transferir redaccion literal ni conclusiones especificas de actividad hermana.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe para evitar duplicados semanticos.",
    "Mantener banderas de normalizacion manual en ciclos con antecedentes no parseables.",
    "Escalar solo despues de validar JSON, estructura y consistencia bibliografica."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar producto solicitado, extension y rubrica de evaluacion.",
    "Confirmar nombre canonico final del .bib ante token Slug no resuelto en README.",
    "Confirmar si bibliografia de interpretacion juridica (Semana 7) aplica a Actividad 4.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica en carpeta de asignatura",
        "Normalizacion obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Filosofia del Derecho",
        "Semestre 1, bloque 2",
        "Asignatura obligatoria de 8 creditos"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y marco normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica aplicable"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos",
      "Asegurar trazabilidad entre fuentes, argumentos y conclusion",
      "Preservar consistencia editorial institucional entre actividades hermanas"
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones funcionales con logica juridica",
      "Cita explicita para cada afirmacion sustantiva",
      "Marcado de supuestos cuando falten datos locales"
    ],
    "argumentative_patterns": [
      "Plantear problema",
      "Exponer conceptos y normas pertinentes",
      "Contrastar evidencia con analisis propio",
      "Fijar postura razonada",
      "Concluir con transferencia profesional"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Relacion problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo completo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        }
      ],
      "evidence": [
        "Pauta editorial del README",
        "Ejes de trabajo del programa analitico",
        "Antecedentes de salidas no parseables en ciclos previos",
        "Token Slug sin resolver detectado en contexto local"
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes con variantes ortograficas.",
      "Se mantuvieron reglas de calidad y normalizacion como nucleo no negociable.",
      "Se evito transferencia de contenido especifico de Actividad 1.",
      "Se incorporaron solo patrones reutilizables para refuerzo lateral en Actividad 4."
    ]
  }
}