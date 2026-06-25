{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho y Derecho penal especial mexicano.",
    "Se preservan reglas estables: identidad UnADM, normalizacion estructurada, cinco ejes editoriales y cierre juridico propio.",
    "Se refuerza transferencia por abstracciones editoriales; no se transfiere contenido tematico filosofico al nodo penal sin evidencia local.",
    "Se mantiene compresion lossless por union y deduplicacion semantica sin regresion.",
    "Se integra control de placeholders y campos truncados detectados en README, programa analitico y plantilla TeX del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuentes locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega.",
    "Usar la carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir que bibliografia de otras materias o semanas aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Verificar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marca [supuesto] en cada afirmacion sensible.",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Compilar LaTeX sin errores criticos ni referencias rotas.",
    "Detectar y corregir placeholders o tokens sin resolver antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla article en español y letterpaper.",
    "Completar metadatos academicos antes de salida final.",
    "Corregir campo truncado Tipo/Creditos en authortable.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar nombre canonico del .bib local del destino.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar fuentes institucionales base verificables del destino.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar autor, titulo, año y fuente/editorial o URL como minimo.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal entre nodos no equivalentes.",
    "Mantener bandera de normalizacion manual para herencias no estructuradas (Codex/GPT-Pro).",
    "Propagar correcciones de placeholders y campos truncados a nodos laterales similares."
  ],
  "open_questions": [
    "[supuesto] Falta consigna puntual de actividades del destino; confirmar producto exacto por semana.",
    "Confirmar nombre real de figura docente para plantillas.",
    "Confirmar si LDE-S2B2 queda como codigo oficial fijo.",
    "Confirmar cierre correcto del campo Tipo/Creditos en plantilla TeX.",
    "Confirmar que autor y matricula visibles siguen vigentes."
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
      "Problema juridico o social",
      "Conceptos, normas y doctrina pertinentes",
      "Producto alineado a planeacion",
      "Analisis propio con postura",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener calidad argumentativa y trazabilidad de evidencia.",
      "Permitir propagacion segura entre nodos con minima friccion."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Cierre con posicion juridica propia.",
      "Marcado explicito de [supuesto] cuando falte evidencia."
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
        "Consistencia documental README-programa-.tex-.bib"
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
          "justification": "Evita reutilizar salidas no parseables y reduce regresiones."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena problema, evidencia, analisis y cierre juridico."
        },
        {
          "source": "Integridad bibliografica",
          "target": "Validez academica",
          "kind": "depends_on",
          "justification": "Exige trazabilidad entre citas y .bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Transferencia transversal limitada a reglas editoriales estables."
        },
        {
          "source": "Consistencia documental README-programa-.tex-.bib",
          "target": "Calidad de entrega",
          "kind": "develops",
          "justification": "Reduce errores de placeholders, slug y metadatos truncados."
        }
      ],
      "evidence": [
        "README de destino con ubicacion curricular y pauta editorial.",
        "Programa analitico del destino con cinco ejes de trabajo.",
        ".bib local con entradas institucionales base verificables.",
        "Plantilla .tex con campo truncado y figura docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion semantica aplicada sin perdida.",
      "Ciclo 12: reforzada regla de no transferir contenido tematico sin evidencia local.",
      "Ciclo 12: reforzados quality gates de JSON parseable y consistencia cita-bibliografia.",
      "Ciclo 12: incorporada correccion sistematica de tokens/slug y campos truncados."
    ]
  }
}