{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de la asignatura.",
    "Se mantiene regla de normalizacion estructurada y bloqueo por JSON no parseable.",
    "Se deduplican reglas equivalentes por forma canonica sin perdida funcional.",
    "Se marcan como supuesto los datos no visibles de la consigna local de Actividad 4."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Vincular ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Marcar como supuesto todo dato no visible en la consigna."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la planeacion semanal y la consigna local.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, evidencia, analisis propio y conclusion juridica.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas desde actividad hermana.",
    "Adaptar la profundidad argumentativa a la rubrica local cuando exista."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar correspondencia entre producto entregable y consigna de Actividad 4.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar espanol con acentos y codificacion consistente en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Corregir nombres de archivo danados en README antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4.",
    "Agregar en el .bib de asignatura solo fuentes realmente usadas en el texto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas reutilizables y verificadas.",
    "Conservar mejoras institucionales sin reducir especificidad local.",
    "Aplicar union-dedupe canonica para evitar duplicados semanticos.",
    "No transferir redaccion literal ni bibliografia exclusiva entre hermanos.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas.",
    "Registrar cada refuerzo lateral en log de ADN editorial."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 4; confirmar producto exacto y extension.",
    "Confirmar rubrica de evaluacion especifica de Actividad 4.",
    "Confirmar si Actividad 4 exige reporte, presentacion u otro formato.",
    "Confirmar archivo .bib canonico final por token Slug sin resolver en README.",
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar trazabilidad entre problema, fuentes, analisis y cierre.",
      "Sostener calidad institucional en cada actividad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales con logica juridica.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar marco conceptual y normativo.",
      "Contrastar evidencia con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Coherencia problema-evidencia-conclusion"
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
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Coherencia problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe descansar en evidencia trazable."
        }
      ],
      "evidence": [
        "README define identidad, entrada canonica e integridad academica.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables justifican gate de JSON estricto.",
        "Supuesto: consigna local de Actividad 4 no visible en el contexto entregado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 37: se refuerza lateralmente estructura y calidad desde Actividad 1 a Actividad 4.",
      "Ciclo 37: se elimina duplicacion textual por canonizacion semantica sin recorte de reglas utiles.",
      "Ciclo 37: se preserva separacion entre patrones transferibles y contenido especifico no transferible.",
      "Ciclo 37: se mantienen preguntas abiertas donde faltan datos locales verificables."
    ]
  }
}