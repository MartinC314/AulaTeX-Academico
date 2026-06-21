{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta.",
    "Se transfieren solo patrones reutilizables desde Actividad 1.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Citar la malla curricular institucional para sustento de ubicacion.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia del producto con la consigna local de Actividad 4.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en el .bib.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de fijar rutas finales.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar al .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Registrar URL verificable en fuentes digitales.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin confirmar.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Mantener union-dedupe sin eliminar reglas utiles previas.",
    "Propagar a nodos hermano solo patrones generales reutilizables.",
    "Evitar copiar redaccion literal o bibliografia exclusiva entre hermanos.",
    "Preservar banderas de normalizacion manual para ciclos con salidas no estructuradas.",
    "Registrar mejoras verificables en cada ciclo para evitar regresion."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar si Actividad 4 reutiliza .bib existente o requiere .bib incremental.",
    "Confirmar nombre canonico final del .bib ante token README no resuelto."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico verificable.",
      "Sostener claridad juridica, evidencia y transferencia profesional.",
      "Mantener continuidad editorial entre actividades sin contaminar contenido especifico."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Separar estructura funcional por secciones.",
      "Citar evidencia de forma explicita.",
      "Marcar supuestos cuando falte dato local.",
      "Cerrar con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problematizar contexto inicial.",
      "Construir marco conceptual y normativo.",
      "Contrastar evidencia con analisis propio.",
      "Fijar postura justificada.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de la asignatura",
        "Integridad academica y trazabilidad",
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
          "target": "Tono formal y precision juridica",
          "kind": "supports",
          "justification": "La pauta editorial institucional define el registro de escritura."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales de la asignatura",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, fuentes, analisis y cierre."
        },
        {
          "source": "Integridad academica y trazabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion exige respaldo verificable y postura argumentada."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad academica y entrada canonica.",
        "Programa analitico fija cinco ejes reutilizables.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto.",
        "Supuesto: falta consigna local completa de Actividad 4."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas en identidad, estructura y calidad.",
      "Se mantuvieron reglas utiles previas sin recorte funcional.",
      "Se retiro transferencia de contenido especifico no reutilizable entre hermanos.",
      "Se reforzo control de supuestos por falta de consigna local."
    ]
  }
}