{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de reglas estables.",
    "Se preserva identidad UnADM y contexto curricular del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial comun: problema, fundamento, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se aplica compresion lossless por union-dedupe y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a la practica profesional.",
    "Relacionar el contenido con derecho a la seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Usar codificacion correcta para espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas, tokens sin expandir y nombres corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normatividad verificable.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y estables.",
    "No transferir redaccion literal ni conceptos tematicos exclusivos de Filosofia del Derecho.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual base.",
    "Mantener bandera de riesgo historico por salidas no parseables de ciclos previos.",
    "Aplicar union-dedupe sin recorte en cada ciclo."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar rubrica oficial por actividad para ajustar profundidad argumentativa [supuesto].",
    "Confirmar datos faltantes de portada (figura docente) cuando exista fuente oficial.",
    "Confirmar si toda actividad requiere artefacto dual reporte/presentacion o solo uno [supuesto]."
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
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia pertinente y trazable.",
      "Analisis propio no descriptivo.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables y utiles para practica profesional.",
      "Asegurar consistencia editorial entre actividades, formatos y ciclos de memoria."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura sustentada.",
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
          "justification": "El analisis exige una pregunta juridica delimitada."
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
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicacion."
        }
      ],
      "evidence": [
        "README destino define estructura canonica de artefactos.",
        "Programa analitico destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Historial institucional reporta salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se refuerza transferencia transversal conservadora de reglas estables.",
      "Ciclo 16: se preservan reglas utiles previas del destino sin eliminacion.",
      "Ciclo 16: se evita traslado de contenido tematico no equivalente desde Filosofia del Derecho.",
      "Ciclo 16: se consolida ADN minimo reconstruible con foco en identidad, estructura, calidad y trazabilidad."
    ]
  }
}