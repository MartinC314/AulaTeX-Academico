{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron comun reutilizable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva alerta de normalizacion manual para antecedentes no parseables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "No propagar datos personales de plantilla a nodos laterales [supuesto]."
  ],
  "structure_rules": [
    "Tomar README de materia como canon de estructura editorial local.",
    "Usar programa analitico como guia de proposito y ejes.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Mantener consistencia entre reporte, presentacion y actividad.",
    "Normalizar nombres de archivos con marcadores corruptos antes de usarlos como canon."
  ],
  "activity_rules": [
    "Delimitar el problema juridico o social al inicio.",
    "Vincular afirmaciones con norma, doctrina o dato verificable.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar formato al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales consistentes en archivos .tex.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas y nombres con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir en README o programa analitico antes de referenciar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda cita en LaTeX tenga clave BibTeX existente."
  ],
  "propagation_hints": [
    "Propagar a laterales y arriba solo reglas validadas y parseables.",
    "Transferir solo abstracciones editoriales estables entre materias no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de otra asignatura.",
    "Reutilizar gates institucionales de calidad y trazabilidad.",
    "Mantener bandera de riesgo para ciclos con salida no parseable.",
    "Aplicar compresion lossless por union-dedupe en cada ciclo."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria sigue vigente para este nodo [supuesto].",
    "Verificar si existen nuevos criterios jurisprudenciales obligatorios en planeaciones locales.",
    "Confirmar datos faltantes de plantilla (figura docente) cuando haya fuente oficial.",
    "Validar que los archivos de Actividad-1 del README existan fisicamente en el repositorio local."
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
      "Resolver consignas con base juridica verificable.",
      "Conectar problema, fundamento, evidencia, analisis y cierre.",
      "Sostener trazabilidad y consistencia tecnica del flujo editorial."
    ],
    "reason_for_being": [
      "Convertir planeaciones en productos academicos utiles, verificables y compilables.",
      "Preservar memoria editorial institucional sin perdida ni regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y conclusion.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
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
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La validez de la conclusion depende del fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion recursiva segura requiere estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "La integridad academica institucional exige trazabilidad de fuentes."
        }
      ],
      "evidence": [
        "README local define estructura canonica y control editorial.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Historial institucional mantiene gate de JSON parseable y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se reforzaron reglas transversales estables sin trasladar contenido tematico de Filosofia.",
      "Ciclo 19: se mantuvo union-dedupe lossless y no regresion.",
      "Ciclo 19: se preservaron gates criticos de parseo JSON, evidencia y consistencia bib."
    ]
  }
}