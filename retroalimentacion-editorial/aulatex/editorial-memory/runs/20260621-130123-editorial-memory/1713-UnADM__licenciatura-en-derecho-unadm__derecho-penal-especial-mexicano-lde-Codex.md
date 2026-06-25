{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y cierre juridico propio.",
    "No se transfiere contenido tematico de Filosofia del Derecho al destino por no equivalencia disciplinar.",
    "Se refuerza correccion de placeholders de slug y campos truncados en README, programa analitico y plantilla TeX.",
    "Se mantiene compresion lossless por union y deduplicacion sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
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
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir nombres corruptos y tokens sin resolver sin alterar el slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Vincular afirmaciones con normas, doctrina o datos verificables.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No trasladar redaccion ni contenido tematico del origen sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente todo insumo desestructurado antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marca de supuesto en cada afirmacion relevante.",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Compilar LaTeX sin errores criticos ni referencias rotas.",
    "Detectar y corregir placeholders y campos truncados antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y letterpaper.",
    "Completar metadatos documentales antes de salida final.",
    "Resolver token de slug a derecho-penal-especial-mexicano.bib en archivos de control.",
    "Completar campo truncado Tipo/Creditos en authortable.",
    "Evitar comandos o rutas con expresiones de plantilla sin resolver.",
    "Usar acentos y codificacion consistentes en .tex y .bib."
  ],
  "bibliography_rules": [
    "Usar derecho-penal-especial-mexicano.bib como fuente unica de referencias del entregable.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos faltantes.",
    "Agregar solo fuentes consultables y verificables por actividad.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir contenido disciplinar literal desde Filosofia del Derecho.",
    "Mantener bandera activa de normalizacion manual para ciclos con insumos no parseables.",
    "Propagar a laterales correcciones de placeholders, tokens y campos truncados."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantilla.",
    "Confirmar si LDE-S2B2 queda fijo como codigo oficial de materia. [supuesto]",
    "Confirmar que matricula visible corresponde al estudiante real. [supuesto]",
    "Verificar si existen actividades con formato distinto a reporte/presentacion.",
    "Confirmar fuentes penales obligatorias por actividad en planeacion local."
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
      "Conceptos y normas pertinentes.",
      "Producto alineado a consigna.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Estandarizar entregables con fundamento juridico, evidencia y aplicabilidad profesional.",
      "Asegurar continuidad editorial entre actividades sin perder contexto local."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Cierre con posicion juridica propia.",
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
        "Correccion de placeholders y campos truncados"
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
          "justification": "Exige citas verificables y correspondencia con .bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Transferencia limitada a abstracciones editoriales estables."
        },
        {
          "source": "Correccion de placeholders y campos truncados",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Reduce fallos de build y ambiguedad documental."
        }
      ],
      "evidence": [
        "README destino confirma semestre, bloque, tipo y creditos.",
        "Programa analitico destino fija cinco ejes de trabajo.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "README/programa/tex muestran token de slug sin resolver.",
        "Plantilla TeX presenta campo truncado Tipo/Creditos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 11: se reforzo transferencia transversal conservadora basada en abstracciones.",
      "Ciclo 11: se mantuvo bloqueo de propagacion para insumos no JSON parseables."
    ]
  }
}