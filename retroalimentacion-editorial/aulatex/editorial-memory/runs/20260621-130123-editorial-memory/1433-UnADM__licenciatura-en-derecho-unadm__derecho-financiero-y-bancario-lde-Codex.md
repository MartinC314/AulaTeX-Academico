{
  "summary": [
    "Sincronizacion transversal consolidada con union-dedupe y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se mantiene enfoque lossless: deduplicar sin recortar reglas utiles.",
    "Se refuerza normalizacion obligatoria ante salidas no estructuradas.",
    "Se evita transferencia literal de contenido de Filosofia del Derecho al nodo de Derecho financiero y bancario."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares verificados del destino: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local.",
    "Conservar autoria y matricula locales mientras no exista correccion oficial."
  ],
  "structure_rules": [
    "Abrir con problema juridico o social delimitado.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos o marco normativo, analisis propio y cierre.",
    "Alinear el producto al formato pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar usar fuentes de otras semanas sin confirmacion de pertinencia.",
    "Separar descripcion conceptual de analisis y posicion propia."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Bloquear guardado si hay campos obligatorios vacios sin marca de supuesto.",
    "Validar deduplicacion semantica antes de persistir memoria."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Conservar claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens de plantilla sin expandir en README y programa analitico.",
    "Sincronizar titulo y subtitulo del reporte con actividad real antes de entrega.",
    "Completar campos de portada pendientes con dato real o etiqueta de supuesto."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y material juridico verificable.",
    "No inventar referencias ni metadatos.",
    "Registrar en .bib solo fuentes realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Incluir fecha de consulta en referencias web."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y deduplicadas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico especifico de otra materia.",
    "Aplicar normalizacion manual al reutilizar memorias de ciclos con salida no estructurada."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en portada. [supuesto]",
    "Confirmar formato obligatorio de citacion para la materia. [supuesto]",
    "Confirmar planeacion semanal vigente antes de generar actividades derivadas. [supuesto]",
    "Confirmar si la ubicacion de portada debe mantenerse por lineamiento institucional. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "No regresion de reglas utiles previas.",
        "Trazabilidad entre README, programa, .tex y .bib."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar consistencia editorial y tecnica en toda entrega."
    ],
    "style_markers": [
      "Frases directas y auditables.",
      "Supuestos marcados de forma explicita.",
      "Sin fuentes inventadas.",
      "Cierre juridico con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial breve.",
      "Delimitar marco conceptual o normativo.",
      "Desarrollar analisis propio soportado en evidencia.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Consistencia documental .tex-.bib-README-programa"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo comprobable."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia documental .tex-.bib-README-programa",
          "kind": "supports",
          "justification": "La identidad institucional exige coherencia formal y trazable."
        }
      ],
      "evidence": [
        "README local con pauta editorial canonica.",
        "Programa analitico con ejes de trabajo y proposito.",
        "Archivo .bib local con fuentes institucionales base.",
        "Historial de incidencias de salida no parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 7: reforzada regla de normalizacion previa a propagacion.",
      "Ciclo 7: transferidas solo abstracciones estables por relacion transversal.",
      "Ciclo 7: preservados huecos locales como preguntas abiertas con marca de supuesto."
    ]
  }
}