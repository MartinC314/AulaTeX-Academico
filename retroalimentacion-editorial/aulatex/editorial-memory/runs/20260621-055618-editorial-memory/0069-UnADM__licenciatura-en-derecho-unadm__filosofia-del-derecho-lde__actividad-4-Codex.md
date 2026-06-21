{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales reutilizables.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta antes de propagar.",
    "Se mantiene regla de marcar supuestos cuando la consigna local no es visible.",
    "Se evita transferir conclusiones o bibliografia exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Aplicar los cinco ejes del programa analitico en cada entrega.",
    "Incluir problema, conceptos o normas, evidencia, analisis propio y conclusion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar formato exacto de Actividad 4 antes de fijar estructura final [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas.",
    "Verificar nombres reales de archivos cuando README tenga caracteres dañados o plantillas sin resolver [supuesto]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Agregar al .bib de asignatura solo fuentes realmente usadas por la actividad.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4 [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones reutilizables, no contenido especifico.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar union-dedupe para compresion lossless.",
    "Mantener banderas de normalizacion manual en ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro artefacto.",
    "Confirmar rubrica docente especifica para ajustar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de la asignatura tras resolver Slug.",
    "Confirmar si la bibliografia de interpretacion juridica aplica o no a Actividad 4."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables.",
      "Mantener coherencia entre identidad institucional, evidencia y argumentacion juridica."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Estructurar por secciones funcionales.",
      "Citar toda afirmacion sustantiva.",
      "Marcar supuestos de forma explicita.",
      "Cerrar con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Integrar evidencia verificable.",
      "Contrastar con analisis propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y trazabilidad",
        "Ejes editoriales de Filosofia del Derecho",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
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
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden argumentativo comun."
        },
        {
          "source": "Integridad academica y trazabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe derivar de evidencia verificable."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y conclusion juridica propia.",
        "Programa analitico define cinco ejes reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto.",
        "Token Slug sin resolver en README/programa requiere verificacion local [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: deduplicacion de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 69: refuerzo lateral de patrones comunes sin copiar redaccion especifica del hermano.",
      "Ciclo 69: conservadas reglas de supuestos, JSON estricto y trazabilidad bibliografica.",
      "Ciclo 69: se mantienen preguntas abiertas donde falta consigna local verificable."
    ]
  }
}