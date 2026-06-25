{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de origen hacia materia destino.",
    "Se preservan reglas institucionales UnADM, normalizacion JSON y union-dedupe sin recorte.",
    "Se transfiere solo abstraccion estable: eje problema-conceptos-evidencia-analisis-conclusion.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar.",
    "Se mantiene alerta local por tokens Slug sin expandir y nombres de archivo con artefactos en README/programa.",
    "Supuesto: no hay consigna local de actividad especifica en destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de materia en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Ordenar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local.",
    "No asumir fuentes de semanas distintas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar manualmente salidas no estructuradas antes de propagacion recursiva."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir artefactos de nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas confiables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves ausentes en el .bib local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas abstractas y estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar contenido doctrinal especifico de una materia a otra sin equivalencia tematica.",
    "Mantener estrategia progresiva y conservadora para evitar regresiones.",
    "Aplicar propagacion recursiva solo tras validacion JSON y normalizacion."
  ],
  "open_questions": [
    "Confirmar guia de citacion juridica especifica de la materia destino.",
    "Confirmar si el autor visible de plantilla se parametriza por actividad.",
    "Confirmar expansion final del Slug en README y programa analitico.",
    "Confirmar si year=2026 en unadmSitioWeb es año bibliografico o de consulta.",
    "Supuesto: falta consigna puntual de actividad para ajustar profundidad y formato."
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
        "Integridad academica y trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia en semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Enfoque de transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico claro.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos consistentes.",
      "Sostener calidad editorial verificable entre actividades y formatos.",
      "Asegurar trazabilidad entre argumento, evidencia y conclusion."
    ],
    "style_markers": [
      "Frases directas.",
      "Supuestos marcados.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo/doctrinal como soporte del criterio personal.",
      "Coherencia estricta entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control de supuestos",
        "Integridad bibliografica"
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
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo trazable."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Unifica tono, formato y criterios de calidad."
        }
      ],
      "evidence": [
        "README local: ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bibliografia local: claves institucionales base verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 2: refuerzo de gates de JSON parseable y estructura minima.",
      "Ciclo 2: consolidacion del patron argumentativo reusable transversal.",
      "Ciclo 2: conservacion de alertas tecnicas de Slug y artefactos de archivo.",
      "Ciclo 2: exclusion explicita de transferencia doctrinal no equivalente."
    ]
  }
}