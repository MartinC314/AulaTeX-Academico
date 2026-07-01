{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, normalizacion estructurada y compresion union-dedupe sin perdida.",
    "Se transfiere solo abstraccion reusable: ejes editoriales, gates de calidad, disciplina bibliografica y patron argumentativo.",
    "Se evita traslado tematico literal de Filosofia del Derecho hacia Derecho penal especial mexicano.",
    "Se refuerza correccion local de placeholders, campos truncados y consistencia README-programa-TeX-bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear cada entregable al producto exigido por la planeacion semanal.",
    "Sincronizar coherencia entre README, programa analitico, plantilla TeX y .bib.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto y verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada propia; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar al .bib local solo fuentes especificas de la actividad con metadatos completos.",
    "No asumir que fuentes de otras semanas o materias aplican automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria aguas abajo.",
    "Normalizar manualmente cualquier insumo desestructurado heredado.",
    "Validar correspondencia 1:1 entre citas en texto y entradas en .bib.",
    "Detectar y corregir placeholders/tokens sin expandir antes de compilar.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla article en español y letterpaper salvo consigna contraria.",
    "Completar metadatos institucionales y academicos antes de version final.",
    "Corregir campo truncado Tipo/Creditos en authortable. [supuesto: pendiente actual]",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar nombre canónico de .bib: derecho-penal-especial-mexicano.bib.",
    "Evitar comandos o rutas no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar fuentes institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni completar datos sin verificacion.",
    "Registrar autor, titulo, año y fuente/editorial o URL en cada entrada.",
    "Registrar fecha de consulta cuando la fuente sea web o variable.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Transferir abstracciones estables; no transferir redaccion literal ni tematica ajena.",
    "Mantener bandera activa de normalizacion manual para insumos heredados no estructurados.",
    "Propagar correcciones de placeholders/campos truncados a nodos laterales similares.",
    "Evitar regresiones: nunca eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar figura docente real en plantilla TeX del destino.",
    "Confirmar si LDE-S2B2 queda fijo como regla global de materia. [supuesto: provisional]",
    "Verificar cierre completo del campo Tipo/Creditos truncado en reporte base.",
    "Confirmar consignas y rubricas de actividades para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias por semana en Derecho penal especial mexicano."
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
        "Semestre 2, bloque 2, obligatoria, 8 creditos.",
        "Respaldo curricular en malla institucional UnADM."
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
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia editorial entre contenido juridico y forma tecnica LaTeX.",
      "Preservar memoria institucional reusable sin contaminar disciplinas no equivalentes."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Marcado explicito de [supuesto] cuando falte evidencia local.",
      "Separacion clara entre dato verificado y dato provisional.",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Objetivo declarado -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Ejes editoriales de cinco pasos",
        "Integridad bibliografica 1:1",
        "Consistencia README-programa-TeX-bib",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales de cinco pasos",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordenan desarrollo y evitan resumen descriptivo."
        },
        {
          "source": "Integridad bibliografica 1:1",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Cada afirmacion queda trazable a evidencia."
        },
        {
          "source": "Consistencia README-programa-TeX-bib",
          "target": "Compilacion estable y entrega valida",
          "kind": "supports",
          "justification": "Reduce errores tecnicos y contradicciones editoriales."
        },
        {
          "source": "Conclusion juridica transferible",
          "target": "Pertinencia profesional",
          "kind": "develops",
          "justification": "Conecta aprendizaje con practica juridica."
        }
      ],
      "evidence": [
        "README local fija ubicacion curricular y pauta editorial.",
        "Programa analitico local define ejes de trabajo y proposito.",
        "Plantilla TeX local muestra pendiente en campo Tipo/Creditos. [supuesto: no corregido aun]",
        "Bib local contiene base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se mantiene union-dedupe lossless sin recorte.",
      "Ciclo 2: se preservan reglas previas utiles y se eliminan duplicados semanticos.",
      "Ciclo 2: se refuerza transferencia por abstraccion transversal, no por contenido tematico literal.",
      "Ciclo 2: se mantiene control de calidad estructural previo a toda propagacion."
    ]
  }
}