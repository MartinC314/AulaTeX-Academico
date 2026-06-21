{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se mantiene validacion JSON estricta por antecedentes de salidas no parseables.",
    "Se evita transferir conclusiones o bibliografia exclusiva no verificada de un hermano a otro.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener tono formal academico UnADM.",
    "Alinear toda entrega a Licenciatura en Derecho y Filosofia del Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de otras semanas sin validar pertinencia.",
    "Confirmar primero formato requerido de Actividad 4 antes de fijar plantilla final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de propagacion recursiva."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Evitar comandos no estandar sin justificacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias.",
    "Verificar nombres reales de archivos antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4.",
    "Marcar como pendiente cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validacion estructural.",
    "Transferir solo patrones reutilizables de identidad, estructura y calidad.",
    "Evitar copia literal de redaccion o cierres especificos de Actividad 1.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Mantener union-dedupe para compresion lossless sin recorte."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y rubrica.",
    "Confirmar si Actividad 4 es reporte, presentacion u otro artefacto principal.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README.",
    "Confirmar si la bibliografia de interpretacion juridica (Semana 7) aplica a Actividad 4.",
    "Confirmar fuentes obligatorias docentes adicionales no visibles en contexto local."
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
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Asegurar trazabilidad entre problema, evidencia, analisis y conclusion.",
      "Sostener coherencia institucional en todas las actividades de la asignatura."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales claras.",
      "Citas explicitas por afirmacion relevante.",
      "Supuestos marcados cuando falten datos.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y normas aplicables.",
      "Contrastar fuentes.",
      "Fijar postura propia justificada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
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
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Relacion problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere respaldo comprobable."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes locales registran salidas no parseables y exigen gate JSON."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de tono, estructura y calidad.",
      "Se reforzo regla de no copiar contenido especifico entre hermanos.",
      "Se mantuvo compatibilidad con control de supuestos y fuentes provisionales.",
      "Se agrego control explicito sobre token Slug no resuelto en rutas bibliograficas."
    ]
  }
}