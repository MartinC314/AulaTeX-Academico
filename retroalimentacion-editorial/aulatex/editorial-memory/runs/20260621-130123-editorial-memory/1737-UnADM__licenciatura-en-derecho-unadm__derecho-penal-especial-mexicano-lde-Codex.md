{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes, normalizacion estructurada y cierre juridico propio.",
    "Se transfiere solo abstraccion reusable; no se transfiere contenido tematico de Filosofia del Derecho.",
    "Se refuerza control de calidad sobre JSON parseable, supuestos trazables y consistencia cita-bibliografia.",
    "Se mantiene compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: Licenciatura en Derecho, semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir placeholders y nombres corruptos sin alterar slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No trasladar doctrina o casos de Filosofia del Derecho sin evidencia local verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Confirmar estructura minima completa antes de aplicar aguas abajo.",
    "Validar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla article en español y letterpaper.",
    "Completar metadatos institucionales y academicos antes de salida final.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliografico canonico local.",
    "Corregir campo truncado Tipo/Creditos en authortable [supuesto: debe ser 'Obligatoria / 8'].",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar solo fuentes consultables y verificables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar abstracciones editoriales estables en nodos transversales.",
    "Evitar transferencia literal de redaccion o contenido disciplinar ajeno.",
    "Reforzar gates de calidad y grafo conceptual antes de nuevos saltos.",
    "Mantener bandera activa de normalizacion manual para herencias no estructuradas.",
    "Aplicar deduplicacion semantica sin recortar reglas utiles."
  ],
  "open_questions": [
    "Confirmar figura docente real en plantillas de la materia.",
    "Confirmar si LDE-S2B2 queda fijo como codigo canonico global de materia.",
    "Validar autor y matricula visibles contra datos institucionales.",
    "Confirmar que no quedan placeholders ni rutas con caracteres anómalos en README/programa.",
    "Definir consignas reales de actividades para activar reglas especificas por evidencia local."
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
      "Conceptos y norma aplicable.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Asegurar consistencia editorial entre consigna, desarrollo, evidencia y cierre."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo seccionado funcional.",
      "Cierre con posicion juridica propia.",
      "Marcado explicito de supuestos.",
      "Trazabilidad de fuentes."
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
          "justification": "Exige trazabilidad cita-bibliografia."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Se transfiere metodo editorial, no contenido tematico."
        },
        {
          "source": "Sincronizacion transversal conservadora",
          "target": "Estabilidad del nodo destino",
          "kind": "develops",
          "justification": "Refuerza ADN comun sin contaminar contexto disciplinar."
        }
      ],
      "evidence": [
        "README de destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo.",
        "Bib local contiene base institucional verificable.",
        "Plantilla TeX muestra token sin expandir y campo truncado a corregir."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicadas reglas repetidas y preservadas reglas utiles previas.",
      "Ciclo 17: reforzada politica de supuestos y fuentes provisionales.",
      "Ciclo 17: reforzados gates de JSON parseable, estructura minima y cita-bib 1:1.",
      "Ciclo 17: mantenida estrategia conservadora de no transferir contenido tematico entre nodos no equivalentes."
    ]
  }
}