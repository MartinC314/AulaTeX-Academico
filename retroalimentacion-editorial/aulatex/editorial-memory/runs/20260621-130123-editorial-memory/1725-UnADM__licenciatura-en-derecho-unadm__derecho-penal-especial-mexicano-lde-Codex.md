{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de Filosofia del Derecho hacia materia de Derecho penal especial mexicano.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y cierre juridico propio.",
    "Se mantiene compresion lossless por union-dedupe sin recorte.",
    "Se refuerza bloqueo de propagacion ante JSON no parseable.",
    "Se confirma estrategia: transferir abstracciones editoriales, no contenido tematico de origen no equivalente.",
    "Se detectan placeholders y campos truncados locales; quedan como correccion prioritaria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar por bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir nombres corruptos y placeholders sin alterar el slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No trasladar contenido tematico de Filosofia del Derecho sin evidencia verificable local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente insumos desestructurados antes de reutilizar.",
    "Confirmar que cada afirmacion tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Compilar LaTeX sin errores criticos ni referencias rotas.",
    "Detectar y resolver placeholders o campos truncados antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y letterpaper.",
    "Usar acentos y codificacion consistentes en .tex y .bib.",
    "Completar metadatos documentales antes de version final.",
    "Evitar macros o rutas con tokens sin expandir.",
    "Resolver token $(@{...}.Slug) como derecho-penal-especial-mexicano.bib en README y programa analitico.",
    "Corregir campo truncado Tipo/Creditos en authortable.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "bibliography_rules": [
    "Usar derecho-penal-especial-mexicano.bib como fuente unica de referencias del entregable.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar fuentes especificas por actividad solo con datos verificables.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografia base institucional de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal y contenido disciplinar no homologable.",
    "Mantener bandera de normalizacion manual para herencias no estructuradas.",
    "Propagar a nodos laterales correcciones de placeholders, slugs y campos truncados.",
    "Evitar regresiones: conservar toda regla util previa."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantillas del destino.",
    "Confirmar si LDE-S2B2 queda como codigo oficial fijo de materia. [supuesto]",
    "Verificar si autor y matricula visibles son definitivos en todos los artefactos. [supuesto]",
    "Completar correccion de lineas corruptas en README (eporte/eferencias).",
    "Definir rubricas locales por actividad para ajustar profundidad argumentativa."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho penal especial mexicano.",
        "Semestre 2, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico concreto.",
      "Conceptos y norma aplicable.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes.",
      "Garantizar trazabilidad editorial y bibliografica en cada actividad.",
      "Sostener calidad institucional transversal entre nodos."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Inferencias juridicas explicitas.",
      "Cierre con posicion propia.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Consigna -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliografica",
        "Conclusion juridica transferible",
        "Consistencia inter-artefacto README-programa-.tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita reutilizar salidas no parseables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena problema, evidencia, analisis y cierre."
        },
        {
          "source": "Integridad bibliografica",
          "target": "Validez academica",
          "kind": "depends_on",
          "justification": "Exige citas verificables con correspondencia .bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Transferencia transversal limitada a reglas editoriales estables."
        },
        {
          "source": "Consistencia inter-artefacto README-programa-.tex-.bib",
          "target": "Calidad de entrega final",
          "kind": "develops",
          "justification": "Reduce errores de slug, placeholders y metadatos."
        }
      ],
      "evidence": [
        "README de destino con ubicacion curricular y pauta editorial.",
        "Programa analitico con cinco ejes de trabajo.",
        "Archivo .bib local con base institucional verificable.",
        "Plantilla .tex con campo truncado y figura docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se deduplican reglas repetidas sin perdida semantica.",
      "Ciclo 14: se preserva gate de JSON parseable como bloqueo duro.",
      "Ciclo 14: se refuerza no transferencia de contenido tematico entre nodos no equivalentes.",
      "Ciclo 14: se mantiene ADN de cinco ejes y cierre juridico propio.",
      "Ciclo 14: se prioriza correccion de placeholders y truncamientos locales."
    ]
  }
}