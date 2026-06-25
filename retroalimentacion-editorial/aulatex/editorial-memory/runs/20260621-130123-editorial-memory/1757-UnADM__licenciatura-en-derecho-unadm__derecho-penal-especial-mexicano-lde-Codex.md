{
  "summary": [
    "Se mantiene sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y cierre juridico propio.",
    "Se refuerza deduplicacion semantica lossless sin recorte de reglas utiles previas.",
    "Se confirma que solo se transfieren abstracciones editoriales, no contenido tematico de Filosofia del Derecho.",
    "Se mantiene control de calidad sobre JSON parseable, supuestos trazables y consistencia cita-bibliografia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir placeholders y nombres corruptos sin alterar slug canonico del destino."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de la actividad al .bib local antes de version final.",
    "No trasladar contenido disciplinar del origen sin evidencia verificable en el destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente insumos desestructurados antes de reutilizar.",
    "Confirmar estructura minima completa antes de aplicar aguas abajo.",
    "Validar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas del .bib.",
    "Compilar LaTeX sin errores criticos ni referencias rotas antes de salida final."
  ],
  "latex_rules": [
    "Mantener plantilla base en espanol y letterpaper.",
    "Completar metadatos del documento antes de entrega.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliografico canonico local.",
    "Corregir campo truncado Tipo/Creditos en authortable.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar solo fuentes realmente consultables y verificables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Registrar fecha de consulta en recursos web variables.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad institucional, estructura reusable y gates de calidad.",
    "Aplicar compresion por union-dedupe semantica sin perdida.",
    "Evitar transferir redaccion literal entre nodos transversales.",
    "Mantener bandera activa de normalizacion manual para herencias no estructuradas.",
    "Propagar correcciones de placeholders y campos truncados a materias laterales similares."
  ],
  "open_questions": [
    "Confirmar figura docente real en plantilla del destino.",
    "Confirmar si LDE-S2B2 queda fijo como codigo oficial de materia. [supuesto]",
    "Verificar cierre completo del campo Tipo/Creditos en .tex.",
    "Verificar que autor y matricula visibles correspondan al estudiante real.",
    "Confirmar consigna local de la proxima actividad para ajustar profundidad y formato.",
    "Confirmar si existen fuentes obligatorias adicionales de Derecho penal especial mexicano."
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
      "Problema juridico o social.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para la practica.",
      "Proteger coherencia institucional y calidad tecnica en todo flujo editorial LaTeX."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por bloques funcionales.",
      "Cierre con postura juridica propia.",
      "Supuestos marcados de forma explicita.",
      "Trazabilidad entre consigna, texto y bibliografia."
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
        "Sincronizacion transversal conservadora"
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
          "justification": "Evita reutilizar salidas no parseables y reduce errores aguas abajo."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena problema, fundamento, analisis y cierre."
        },
        {
          "source": "Integridad bibliografica",
          "target": "Validez academica",
          "kind": "depends_on",
          "justification": "Requiere citas verificables y correspondencia exacta con .bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "La transferencia es editorial transversal, no disciplinar literal."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "develops",
          "justification": "Unifica criterios sin romper contexto local del destino."
        }
      ],
      "evidence": [
        "README del destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico del destino define cinco ejes de trabajo.",
        ".bib local contiene base institucional verificable.",
        "Plantilla .tex mantiene campo truncado y figura docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se consolida union-dedupe sin regresion.",
      "Ciclo 22: se preservan reglas utiles previas y se eliminan duplicados literales.",
      "Ciclo 22: se refuerza gate de JSON parseable y normalizacion manual obligatoria.",
      "Ciclo 22: se mantiene veto a transferencia tematica no verificable desde origen transversal."
    ]
  }
}