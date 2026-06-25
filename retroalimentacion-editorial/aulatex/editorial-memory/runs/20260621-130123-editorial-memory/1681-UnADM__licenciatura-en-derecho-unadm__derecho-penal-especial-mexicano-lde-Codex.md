{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables de identidad UnADM, estructura en cinco ejes y control de calidad.",
    "Se refuerza deduplicacion lossless por union semantica sin recorte de reglas utiles.",
    "Se mantiene veto a transferir contenido tematico de Filosofia del Derecho al dominio penal sin evidencia local.",
    "Se agrega prioridad de correccion de placeholders y campos truncados detectados en README, programa analitico y TeX."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna o fuentes locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Mantener consistencia de nombres de archivo y slug canonico de materia."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir fuentes de semanas posteriores sin validacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente insumos no estructurados antes de reutilizarlos.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Detectar y corregir placeholders, tokens sin expandir y campos truncados antes de compilar."
  ],
  "latex_rules": [
    "Usar espanol y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Completar campo truncado Tipo/Creditos en authortable del reporte base."
  ],
  "bibliography_rules": [
    "Usar derecho-penal-especial-mexicano.bib como fuente local unica del entregable.",
    "Conservar entradas institucionales base unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Transferir solo abstracciones editoriales estables entre materias distintas.",
    "Priorizar identidad institucional, estructura reusable y quality gates.",
    "No propagar redaccion literal ni contenido disciplinar sin evidencia local.",
    "Mantener bandera de normalizacion manual para ciclos con insumos heredados no parseables.",
    "Replicar en nodos laterales las correcciones de placeholders y nombres corruptos."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantillas del destino.",
    "Confirmar si LDE-S2B2 queda fijo como codigo oficial de materia. [supuesto]",
    "Confirmar consigna y rubrica de la primera actividad local para ajustar profundidad.",
    "Verificar si existen fuentes penales obligatorias no cargadas aun al .bib local.",
    "Validar cierre definitivo del campo Tipo/Creditos truncado en reporte base."
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
      "Conceptos, norma y doctrina pertinentes.",
      "Analisis propio con evidencia.",
      "Cierre juridico transferible.",
      "Sincronizacion documental y trazabilidad editorial."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia entre forma editorial y validez juridica.",
      "Sostener continuidad institucional entre actividades y materias."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por bloques funcionales.",
      "Postura propia sustentada.",
      "Marcado explicito de supuestos.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Consigna -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliografica",
        "Conclusion juridica transferible",
        "Correccion de placeholders editoriales"
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
          "justification": "Evita heredar salidas no parseables."
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
          "justification": "Exige citas verificables y .bib consistente."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "La transferencia es metodologica, no tematica."
        },
        {
          "source": "Correccion de placeholders editoriales",
          "target": "Consistencia de compilacion LaTeX",
          "kind": "supports",
          "justification": "Reduce fallas por tokens sin expandir y campos truncados."
        }
      ],
      "evidence": [
        "README de destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico de destino define cinco ejes de trabajo.",
        "derecho-penal-especial-mexicano.bib contiene base institucional verificable.",
        "Plantilla de reporte muestra campo truncado en Tipo/Creditos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 3: reforzada frontera entre transferencia editorial estable y contenido disciplinar no verificable.",
      "Ciclo 3: mantenido gate estricto de JSON parseable y normalizacion manual.",
      "Ciclo 3: incorporada prioridad de saneamiento de placeholders y truncamientos locales."
    ]
  }
}