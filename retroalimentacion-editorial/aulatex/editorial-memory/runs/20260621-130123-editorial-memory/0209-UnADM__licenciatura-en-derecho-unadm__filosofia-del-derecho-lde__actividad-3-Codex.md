{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reusable desde Actividad 1.",
    "Se preserva identidad UnADM y contexto curricular verificado.",
    "Se mantiene normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, analisis propio, conclusion juridica.",
    "Se aplica deduplicacion lossless sin eliminar reglas utiles previas.",
    "Se conservan supuestos abiertos donde falta consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex o GPT-Pro como antecedente provisional, no como fuente academica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Heredar patrones validos de actividad hermana sin copiar redaccion literal.",
    "No copiar conclusiones especificas ni bibliografia exclusiva de otro hermano.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o consigna de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar a nodos hermanos solo patrones generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar compresion por union y deduplicacion lossless en cada ciclo.",
    "Conservar bandera de riesgo cuando exista antecedente de salida no estructurada."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 3; confirmar producto exacto solicitado.",
    "Confirmar si el formato requerido es reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente a Actividad 3.",
    "Confirmar si la bibliografia depurada de Semana 7 aplica o no a Actividad 3."
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
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar continuidad editorial entre actividades sin perder especificidad local.",
      "Garantizar calidad tecnica y trazabilidad de fuentes en LaTeX."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmacion con evidencia y cierre interpretativo.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
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
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay trazabilidad confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de la delimitacion del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de argumentacion sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica y conclusion juridica con criterio propio.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion completa de reglas repetidas.",
      "Ciclo 9: transferencia lateral controlada de patrones reutilizables desde Actividad 1.",
      "Ciclo 9: sin inventar fuentes ni consigna local de Actividad 3.",
      "Ciclo 9: se mantienen reglas tecnicas LaTeX y calidad institucional sin regresion."
    ]
  }
}