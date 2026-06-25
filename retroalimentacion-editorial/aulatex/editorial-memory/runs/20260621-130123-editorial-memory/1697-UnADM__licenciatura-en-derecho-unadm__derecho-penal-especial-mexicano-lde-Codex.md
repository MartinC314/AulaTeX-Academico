{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y cierre juridico propio.",
    "Se evita transferir contenido tematico de Filosofia del Derecho al destino penal sin evidencia local.",
    "Se refuerza control de calidad: JSON parseable, trazabilidad de supuestos y coherencia cita-bibliografia.",
    "Se mantiene compresion lossless por union-dedupe sin regresion."
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
    "Estructurar por secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir placeholders de slug y nombres corruptos sin cambiar slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Agregar fuentes especificas de la actividad al .bib local antes de version final.",
    "No asumir que bibliografia de otras semanas o materias aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Verificar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marca de supuesto en toda afirmacion relevante.",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Compilar LaTeX sin errores criticos ni referencias rotas.",
    "Detectar y corregir campos truncados y tokens sin resolver antes de entrega."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Conservar plantilla article y letterpaper salvo consigna contraria.",
    "Completar metadatos del documento antes de salida final.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir campo truncado Tipo/Creditos en authortable.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar fuentes institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Registrar fecha de consulta cuando aplique a recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y validadas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido disciplinar no verificable.",
    "Mantener bandera activa de normalizacion manual para insumos heredados no estructurados.",
    "Aplicar deduplicacion semantica sin perder reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar figura docente real en plantillas del destino.",
    "Confirmar si LDE-S2B2 queda fijo como codigo oficial en toda la materia. [supuesto]",
    "Confirmar consigna y rubrica de la primera actividad real de la materia destino.",
    "Verificar correccion completa de placeholders y caracteres anómalos en README/programa.",
    "Confirmar que matricula y datos de autor visibles siguen vigentes."
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
      "Producto segun planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y utiles para practica juridica.",
      "Asegurar continuidad editorial institucional entre actividades y formatos."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Cierre con posicion juridica propia.",
      "Marcado explicito de supuestos.",
      "Consistencia entre README, .tex y .bib."
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
          "justification": "Evita arrastre de salidas no parseables y reduce regresiones."
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
          "justification": "La trazabilidad de citas sostiene la calidad del entregable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "La transferencia es editorial, no tematica, por no equivalencia disciplinar."
        }
      ],
      "evidence": [
        "README del destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico del destino explicita cinco ejes de trabajo.",
        ".bib local contiene base institucional verificable.",
        "Plantilla .tex muestra placeholder y campo truncado pendientes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas del origen y destino.",
      "Ciclo 7: se mantiene regla historica de bloqueo por JSON no parseable.",
      "Ciclo 7: se refuerza no transferencia tematica entre nodos no equivalentes.",
      "Ciclo 7: se preserva ADN institucional UnADM y gates de integridad."
    ]
  }
}