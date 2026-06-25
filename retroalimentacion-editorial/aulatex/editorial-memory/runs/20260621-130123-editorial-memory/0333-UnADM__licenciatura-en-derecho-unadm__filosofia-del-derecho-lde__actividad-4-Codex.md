{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y marco curricular de Filosofia del Derecho.",
    "Se mantienen ejes editoriales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se refuerza validacion JSON estricta por antecedentes de salida no parseable.",
    "Se mantiene regla de marcar como supuesto todo dato no visible en la consigna.",
    "Se evita transferir conclusiones especificas o bibliografia exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear toda entrega con UnADM y Licenciatura en Derecho.",
    "Mantener referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar como supuesto todo dato no confirmado localmente."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con citas verificables.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de otra semana aplica automaticamente.",
    "Confirmar consigna especifica de Actividad 4 antes de fijar contenido tematico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa antes de reutilizar memoria.",
    "Validar que cada afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar salidas no estructuradas heredadas.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar espanol correcto y acentos consistentes en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos si README trae plantilla sin resolver.",
    "Resolver tokens tipo $(@{...}.Slug) antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar fuentes ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra actividad; verificar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar normalizacion manual cuando un nodo vecino falle en estructura.",
    "Compartir gates de calidad institucional en nodos hermanos.",
    "Mantener trazabilidad de supuestos por ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar rubrica de evaluacion y extension requerida.",
    "Confirmar si el producto es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del archivo .bib con slug resuelto.",
    "Confirmar si se usa .bib incremental o uno unico de asignatura.",
    "Supuesto: falta validacion local de fuentes periodisticas ya citadas en el destino."
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
        "Normalizacion estructurada obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Filosofia del Derecho",
        "Semestre 1",
        "Bloque 2",
        "Obligatoria",
        "8 creditos"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y marco normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en entregables academicos trazables.",
      "Asegurar fundamento juridico y rigor argumentativo.",
      "Conectar aprendizaje teorico con aplicacion profesional."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones funcionales estables",
      "Cita explicita en afirmaciones sustantivas",
      "Marcado de supuestos cuando falte evidencia local",
      "Cierre con criterio juridico propio"
    ],
    "argumentative_patterns": [
      "Problema inicial",
      "Marco conceptual y normativo",
      "Contraste de fuentes",
      "Postura personal justificada",
      "Conclusion aplicable"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Validacion JSON",
        "Normalizacion estructurada",
        "Integridad academica",
        "Conclusion juridica propia"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato academico."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Conclusion juridica propia",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo hasta un cierre argumentado."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON",
          "kind": "depends_on",
          "justification": "La propagacion recursiva requiere estructura parseable."
        }
      ],
      "evidence": [
        "README fija identidad, integridad y conclusion juridica.",
        "Programa analitico fija cinco ejes reutilizables.",
        "Antecedentes de salida no parseable justifican gate JSON estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion de reglas repetidas en destino.",
      "Ciclo 18: refuerzo de gates JSON y estructura minima.",
      "Ciclo 18: preservacion de identidad curricular y tono institucional.",
      "Ciclo 18: no transferencia de contenido especifico de Actividad 1.",
      "Ciclo 18: se mantienen supuestos abiertos por falta de consigna local completa."
    ]
  }
}