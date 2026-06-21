{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables y sin mezclar contenido tematico.",
    "Se preserva identidad UnADM y estructura canonica local de Derecho a la Seguridad Social.",
    "Se refuerza patron reusable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva alerta institucional: bloquear y normalizar salidas no parseables antes de propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia destino como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; incluir postura argumentada.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver marcadores o tokens sin expandir en README y programa analitico antes de usarlos como canon."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Agregar al .bib solo fuentes especificas de actividad con metadatos minimos completos.",
    "Conservar trazabilidad entre clave BibTeX y cita en texto.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables para nodos transversales.",
    "No transferir redaccion literal ni contenidos tematicos propios de Filosofia del Derecho.",
    "Propagar gates de calidad, identidad institucional y disciplina de citacion como nucleo comun.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Aplicar normalizacion manual cuando reaparezca salida no estructurada de ciclos previos."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local de curso LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar datos faltantes de figura docente para portada [supuesto].",
    "Confirmar si cada actividad requiere .tex dedicado o reutiliza plantilla base [supuesto]."
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
      "Identidad institucional consistente.",
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia y citas trazables.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para la practica.",
      "Preservar memoria editorial persistente sin perdida por deduplicacion.",
      "Habilitar sincronizacion transversal segura entre nodos."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
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
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin salida estructurada no hay reutilizacion confiable."
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
          "justification": "El analisis exige una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia transversal de entregables",
          "kind": "supports",
          "justification": "Uniforma tono, formato y criterios de calidad."
        }
      ],
      "evidence": [
        "README de la materia destino define estructura canonica y archivos base.",
        "Programa analitico del destino define proposito y ejes juridicos.",
        "derecho-a-la-seguridad-social.bib confirma base normativa local verificable.",
        "Memoria origen aporta patron estable de argumentacion academica transferible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 91: se reforzo ADN transversal sin transferir contenido tematico de filosofia.",
      "Ciclo 91: se consolidaron gates de calidad estructural y trazabilidad bibliografica.",
      "Ciclo 91: se mantuvo estrategia conservadora de no regresion y union-dedupe."
    ]
  }
}