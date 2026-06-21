{
  "summary": [
    "Se refuerza memoria lateral de Actividad 4 con patrones reutilizables de Actividad 1.",
    "Se preserva identidad UnADM y marco curricular verificable sin copiar contenido especifico.",
    "Se consolida compresion lossless por deduplicacion y normalizacion estructurada obligatoria.",
    "Se mantiene gate estricto: sin JSON parseable no hay propagacion.",
    "Supuesto: la consigna local de Actividad 4 no esta visible; se conserva estructura base."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos con fuente institucional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir explicitamente problema, conceptos, evidencia y analisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar Actividad 4 a los ejes del programa analitico sin forzar fuentes de otra semana.",
    "Confirmar consigna especifica antes de fijar alcance tematico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar.",
    "Verificar nombres reales de archivos cuando README tenga caracteres danados."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si la consigna de Actividad 4 coincide tematicamente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones institucionales, estructurales y de calidad reutilizables.",
    "No transferir redaccion literal, conclusiones especificas ni bibliografia exclusiva de otro hermano.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar union-dedupe para compresion lossless sin recorte semantico."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios de evaluacion.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar si usa bibliografia propia o reutiliza parcialmente la existente.",
    "Confirmar nombre canonico final del archivo .bib derivado del Slug.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Semana 7; verificar aplicabilidad a Actividad 4."
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
      "Conceptos y marco normativo-doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar coherencia entre identidad institucional, estructura argumentativa y verificabilidad."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales separadas.",
      "Postura propia sustentada.",
      "Supuestos marcados cuando falte dato local.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y marco.",
      "Contrastar evidencia.",
      "Desarrollar analisis propio.",
      "Concluir con regla o implicacion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de la asignatura",
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
          "justification": "Sin estructura valida no hay transferencia segura."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, fuentes, analisis y cierre."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion requiere evidencia y argumentacion sustentada."
        },
        {
          "source": "filosofia-del-derecho-clean.bib",
          "target": "Actividad 4",
          "kind": "contrasts",
          "justification": "Supuesto de posible desajuste tematico por origen en Semana 7."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y entrada canonica.",
        "Programa analitico fija cinco ejes reutilizables.",
        "Historial reporta salidas no parseables; se mantiene gate JSON estricto.",
        "Regla de transferencia impide copiar contenido especifico entre hermanos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicacion integral de reglas repetidas en destino.",
      "Ciclo 22: refuerzo lateral de estructura y calidad desde Actividad 1 sin literalidad.",
      "Ciclo 22: se mantiene trazabilidad de supuestos por falta de consigna local visible.",
      "Ciclo 22: se conserva ADN institucional y control de propagacion segura."
    ]
  }
}