{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con union-dedupe lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate estricto de JSON parseable y normalizacion previa a propagacion.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; no se fijan contenidos tematicos cerrados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono formal academico.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el formato de entrega al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los ejes del programa analitico sin copiar redaccion de Actividad 1.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas como obligatorias para Actividad 4 sin confirmacion.",
    "Mantener trazabilidad entre consigna, producto y evidencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que el producto corresponda a la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo.",
    "Confirmar nombres reales de archivos con caracteres danados antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra actividad; validar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y argumentacion.",
    "Evitar mover conclusiones especificas o bibliografia exclusiva entre hermanos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe sin recorte semantico para compresion lossless."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar si el artefacto final es reporte, presentacion o producto visual.",
    "Confirmar rubrica docente especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README.",
    "Confirmar si Actividad 4 requiere bibliografia propia distinta de archivos existentes."
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
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y trazabilidad.",
      "Estandarizar calidad editorial sin perder adaptacion a cada actividad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Citas explicitas para cada afirmacion relevante.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y normas.",
      "Contrastar fuentes con analisis propio.",
      "Sostener postura justificada.",
      "Cerrar con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Integridad academica",
        "Ejes editoriales comunes",
        "Consigna local de actividad"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura parseable."
        },
        {
          "source": "Ejes editoriales comunes",
          "target": "Consigna local de actividad",
          "kind": "develops",
          "justification": "Los ejes guian la redaccion mientras se confirma la consigna especifica."
        }
      ],
      "evidence": [
        "README define identidad, entrada canonica e integridad academica.",
        "Programa analitico define proposito y cinco ejes reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicacion de reglas repetidas en tono, institucional y curricular.",
      "Ciclo 6: conservadas reglas utiles previas sin eliminar controles de calidad.",
      "Ciclo 6: reforzada transferencia lateral por patrones, sin copiar contenido especifico entre hermanos."
    ]
  }
}