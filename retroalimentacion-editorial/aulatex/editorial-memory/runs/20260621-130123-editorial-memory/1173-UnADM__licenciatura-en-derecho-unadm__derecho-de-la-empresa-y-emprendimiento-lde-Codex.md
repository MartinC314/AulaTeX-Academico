{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless.",
    "Se transfiere solo marco editorial estable: identidad, estructura, calidad y trazabilidad.",
    "Se mantiene alerta por JSON no parseable en ciclos previos y normalizacion obligatoria.",
    "Se refuerza el flujo reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se confirma contexto local destino: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene control de tokens Slug sin expandir en README y programa analitico.",
    "Se mantiene alerta de posible truncamiento en reporte LaTeX local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial: Derecho de la empresa y emprendimiento.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado.",
    "Marcar como supuesto todo dato no visible en consigna o archivos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Identificar problema juridico o social de la actividad.",
    "Distinguir conceptos, normas, doctrina o datos pertinentes.",
    "Agregar fuentes especificas por actividad al .bib local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas en fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Corregir placeholders y tokens sin expandir antes de generar entregables.",
    "Verificar correspondencia entre producto entregado y consigna local."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener macros institucionales consistentes con materia destino.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) en nombres de archivo referenciados.",
    "Verificar cierre completo de entornos tabular y archivo no truncado."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes al tema local.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar fuentes no registradas en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables en nodos no equivalentes.",
    "No transferir contenido doctrinal especifico de Filosofia del Derecho al destino.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Exigir normalizacion manual en memorias con antecedente de salida no estructurada.",
    "Propagar alertas tecnicas de tokens y truncamiento solo a plantillas con sintomas equivalentes."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades de la materia destino.",
    "Confirmar guia de citacion juridica especifica de la materia destino.",
    "Confirmar si autor de plantilla se parametriza por actividad.",
    "Confirmar expansion final del Slug en README y programa analitico.",
    "Confirmar si year=2026 en unadmSitioWeb es anio bibliografico o fecha de consulta.",
    "Confirmar integridad completa de reporte-derecho-de-la-empresa-y-emprendimiento.tex."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Enfoque de transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Asegurar fundamento juridico y criterio propio en cada entrega.",
      "Sostener continuidad editorial institucional entre actividades y materia."
    ],
    "style_markers": [
      "Frases directas.",
      "Supuestos explicitados.",
      "Sin afirmaciones sin fuente.",
      "Cierre aplicado a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Marco normativo o doctrinal soporta postura propia.",
      "Coherencia entre pregunta guia y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
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
          "justification": "La conclusion requiere respaldo normativo y documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        },
        {
          "source": "Flujo problema-conclusion",
          "target": "Calidad argumentativa",
          "kind": "develops",
          "justification": "Ordena la construccion del criterio juridico."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "Archivo .bib local con claves institucionales.",
        "Historial de ciclos con alertas de salida no estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se preservan reglas validas sin regresion.",
      "Ciclo 8: se deduplican reglas repetidas en tono, estructura y calidad.",
      "Ciclo 8: se evita transferencia doctrinal especifica de nodo origen no equivalente.",
      "Ciclo 8: se refuerzan quality gates de parseo JSON y control de supuestos.",
      "Ciclo 8: se mantienen alertas tecnicas de Slug sin expandir y posible truncamiento LaTeX."
    ]
  }
}