{
  "summary": [
    "Se sincronizan reglas transversales estables desde actividad de Filosofia del Derecho hacia la materia de Seguridad Social.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin mezclar contenido tematico no equivalente.",
    "Se refuerza compresion lossless por union-dedupe y politica de no regresion.",
    "Se mantiene alerta institucional: toda salida no parseable requiere normalizacion manual previa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y trazabilidad.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, evidencia, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en marco conceptual-normativo, analisis y cierre.",
    "Ajustar formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar compresion lossless por union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener acentos y codificacion correcta en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver tokens no expandidos en README o programa analitico cuando aparezcan [supuesto]."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar nuevas fuentes solo con verificacion local y trazabilidad."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo reglas generales estables entre nodos no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual comun.",
    "Conservar reglas locales del destino como autoridad primaria.",
    "Mantener bandera de riesgo para ciclos con salidas no parseables."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia destino (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si existe rubrica oficial por actividad para ajustar profundidad argumentativa [supuesto].",
    "Confirmar si hay criterios locales de jurisprudencia obligatoria por unidad [supuesto].",
    "Verificar si persiste alguna fuente provisional heredada desde nodos no juridicos [supuesto]."
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
      "Problema juridico delimitado.",
      "Marco normativo y conceptual verificable.",
      "Evidencia y fuentes trazables.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables con valor academico y profesional.",
      "Preservar memoria editorial persistente sin perdida y sin regresion.",
      "Asegurar reutilizacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto] cuando falte evidencia local.",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay transferencia segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicados ni recorte."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige fundamento legal verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia transversal de entregas",
          "kind": "supports",
          "justification": "Homologa tono y criterios entre productos."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Regla persistente: normalizar salidas no parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se incorporan abstracciones estables desde nodo transversal no equivalente.",
      "Ciclo 20: se evita transferencia de contenido tematico especifico de Filosofia.",
      "Ciclo 20: se refuerzan gates de JSON, supuesto, citas y compresion lossless.",
      "Ciclo 20: se mantiene no regresion sobre identidad UnADM y estructura por ejes."
    ]
  }
}