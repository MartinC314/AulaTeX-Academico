{
  "summary": [
    "Se mantiene identidad UnADM y enfoque juridico del destino.",
    "Se refuerza patron transversal estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se conserva normalizacion estructurada obligatoria antes de propagacion.",
    "Se mantiene compresion lossless por union-dedupe sin recorte ni regresion.",
    "Se preserva alerta institucional por salidas no parseables en ciclos previos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Vincular afirmaciones con normas, doctrina o datos verificables.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta en español en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres de archivos y rutas antes de compilar.",
    "Resolver tokens sin expandir en README o programa analitico antes de usarlos como canon."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar faltantes como pendientes o [supuesto].",
    "Agregar solo fuentes consultables y pertinentes a la actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino.",
    "Propagar reglas generales de identidad, calidad, JSON y trazabilidad.",
    "Mantener reglas curriculares especificas solo en nodos de la misma materia.",
    "Aplicar estrategia conservadora: unir, deduplicar y evitar regresiones.",
    "Si un nodo esta incompleto, crear cerebro editorial minimo y abrir vacios locales."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida por la materia [supuesto].",
    "Confirmar si codigo local LDE-S2B1 se usa oficialmente en entregas [supuesto].",
    "Confirmar vigencia de reglas provisionales heredadas de otros dominios [supuesto].",
    "Confirmar rubrica especifica por actividad para ajustar profundidad argumentativa.",
    "Confirmar uso obligatorio de plantillas de Actividad-1 ya listadas en README."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Resolver consignas en productos juridicos verificables.",
      "Sostener analisis con fundamento normativo y evidencia.",
      "Mantener cierre profesional transferible."
    ],
    "reason_for_being": [
      "Conservar un cerebro editorial persistente, estable y reutilizable.",
      "Garantizar calidad tecnica y academica en cada entrega.",
      "Permitir propagacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de reglas provisionales."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal pertinente.",
      "Contrastar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicacion ni perdida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Historial previo confirma necesidad de normalizacion por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 29: se refuerzan reglas transversales estables sin mezclar contenido literal del origen.",
      "Ciclo 29: se mantiene identidad y contexto curricular del destino como prioridad local.",
      "Ciclo 29: se consolidan gates de JSON, evidencia y deduplicacion lossless."
    ]
  }
}