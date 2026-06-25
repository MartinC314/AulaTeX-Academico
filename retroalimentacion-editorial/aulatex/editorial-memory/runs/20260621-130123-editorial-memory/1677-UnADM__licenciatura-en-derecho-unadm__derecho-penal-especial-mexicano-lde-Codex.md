{
  "summary": [
    "Se mantiene sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y cierre juridico propio.",
    "Se evita transferir contenido tematico de Filosofia del Derecho al destino penal sin evidencia local verificable.",
    "Se refuerzan correcciones locales verificables: placeholders de slug y campo truncado en plantilla TeX.",
    "Se conserva compresion lossless por union y deduplicacion sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en consigna o fuentes locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Vincular afirmaciones con normas, doctrina o datos pertinentes del ambito penal.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Agregar fuentes especificas de cada actividad al .bib local antes de version final.",
    "No trasladar contenido disciplinar de Filosofia del Derecho sin insumo verificable en el destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas del .bib.",
    "Verificar coherencia entre README, programa analitico y plantillas TeX.",
    "Detectar y corregir placeholders o tokens sin resolver antes de compilar.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Corregir campo truncado Tipo/Creditos en authortable.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico a derecho-penal-especial-mexicano.bib.",
    "Mantener nombres de archivos y slug canonico consistentes.",
    "Usar acentos y codificacion en espanol de forma estable en .tex y .bib."
  ],
  "bibliography_rules": [
    "Usar derecho-penal-especial-mexicano.bib como fuente unica de referencias del entregable local.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Registrar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Registrar fecha de consulta cuando aplique a recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables entre materias.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico no equivalente.",
    "Mantener bandera activa de normalizacion manual para insumos heredados no parseables.",
    "Propagar correcciones de placeholders y campos truncados a nodos laterales similares.",
    "Aplicar deduplicacion semantica sin recortar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantilla del destino.",
    "Verificar definitivamente autor y matricula visibles en archivos TeX. [supuesto]",
    "Confirmar si LDE-S2B2 se fija como codigo canonico global de la materia.",
    "Confirmar si cada actividad tendra .bib compartido o particionado por entrega.",
    "Validar que no queden rutas con caracteres anomales en README."
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos evaluables con rigor juridico.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusion.",
      "Sostener consistencia editorial en toda la materia."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Uso explicito de supuestos cuando falte dato.",
      "Cierre con posicion juridica propia.",
      "Consistencia entre .tex, .bib, README y programa analitico."
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
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "supports",
          "justification": "Evita heredar ruido no parseable entre nodos."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Ordena el desarrollo hasta un cierre aplicable."
        },
        {
          "source": "Integridad bibliografica",
          "target": "Validez academica",
          "kind": "depends_on",
          "justification": "Requiere citas verificables y .bib consistente."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Solo se transfieren reglas editoriales estables, no contenido tematico."
        }
      ],
      "evidence": [
        "README del destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico define cinco ejes de trabajo.",
        "Bib local contiene fuentes institucionales verificables.",
        "Plantilla TeX muestra campo truncado y requiere correccion verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 2: refuerzo de gates JSON parseable y normalizacion manual.",
      "Ciclo 2: consolidacion de transferencia transversal solo en abstracciones estables.",
      "Ciclo 2: adicion de correcciones locales verificables en placeholders y campo truncado."
    ]
  }
}