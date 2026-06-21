{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de la asignatura.",
    "Se mantiene gate estricto de JSON parseable por antecedentes de salidas no estructuradas.",
    "Se transfieren patrones reutilizables de estructura, calidad, LaTeX y bibliografia sin copiar contenido especifico.",
    "Supuesto: la consigna puntual de Actividad 4 no esta visible de forma completa y requiere confirmacion local."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Mantener referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio en coherencia interna.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el producto corresponde a la consigna de Actividad 4.",
    "Supuesto: no reutilizar automaticamente fuentes de semanas distintas sin validar pertinencia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Revisar consistencia entre consigna local y reglas transferidas."
  ],
  "latex_rules": [
    "Mantener codificacion correcta en espanol para .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves bibliograficas en uso sin migracion completa.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas invalidas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra semana; validar uso en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales comunes y ajustar solo lo local de cada actividad.",
    "Evitar copiar redaccion literal, conclusiones o bibliografia exclusiva entre hermanos.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar union-dedupe para compresion lossless.",
    "Mantener bandera de normalizacion manual en ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver.",
    "Confirmar si Actividad 4 requiere .bib propio o reutiliza bibliografia existente.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
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
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar coherencia entre identidad institucional, rigor argumentativo y trazabilidad de fuentes."
    ],
    "style_markers": [
      "Definir objetivo antes de desarrollar.",
      "Estructura seccional estable y verificable.",
      "Explicitar supuestos cuando falten datos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Delimitar marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Concluir con implicacion juridica practica."
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
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal y precision juridica",
          "kind": "supports",
          "justification": "La pauta editorial exige consistencia institucional en toda actividad."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los cinco ejes ordenan apertura, desarrollo y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo y analisis, no solo descripcion."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, entrada canonica y exigencia de conclusion juridica propia.",
        "Programa analitico define proposito y cinco ejes de trabajo transferibles.",
        "Antecedentes de salidas no parseables justifican gate de JSON estricto.",
        "Token Slug sin resolver en README exige verificacion de nombres reales."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con equivalencia semantica.",
      "Se preservaron reglas utiles previas sin eliminar controles de calidad.",
      "Se reforzo transferencia lateral solo con patrones reutilizables.",
      "Se agrego alerta explicita sobre token Slug no resuelto en rutas y .bib.",
      "Se mantuvieron supuestos abiertos donde faltan datos de consigna local."
    ]
  }
}