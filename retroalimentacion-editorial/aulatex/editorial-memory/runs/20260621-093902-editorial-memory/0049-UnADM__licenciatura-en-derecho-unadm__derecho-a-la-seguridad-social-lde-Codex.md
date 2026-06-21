{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de Filosofia del Derecho y materia de Seguridad Social.",
    "Se preservan reglas estables de identidad UnADM, estructura por ejes y control de calidad parseable.",
    "Se mantiene compresion lossless por union-dedupe sin regresion ni recorte.",
    "Se evita transferir contenido tematico especifico de Filosofia; solo se transfieren abstracciones editoriales reutilizables.",
    "Se refuerza uso canonico de README, programa analitico y .bib local del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia editorial entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar cada producto con el campo de seguridad social cuando corresponda.",
    "No asumir fuentes de semanas o materias distintas sin validacion local [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin perdida."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivo cuando existan marcadores o tokens sin expandir.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar referencias; marcar faltantes como pendientes [supuesto].",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales ya validadas en JSON.",
    "En saltos transversales, transferir solo abstracciones editoriales estables.",
    "No propagar contenido doctrinal especifico de una materia a otra no equivalente.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos tempranos.",
    "Aplicar normalizacion manual cuando se detecte salida no estructurada.",
    "Preservar reglas utiles previas del destino y reforzar solo conexiones compatibles."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida por la materia (APA, ISO, juridica mexicana o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 debe aparecer en todas las plantillas [supuesto].",
    "Confirmar nombre oficial de figura docente para portada [supuesto].",
    "Confirmar si existe rubrica transversal institucional para actividades de la materia [supuesto].",
    "Confirmar si la alerta de fuente provisional heredada desde ingenieria sigue vigente para Derecho [supuesto]."
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
      "Fundamento normativo verificable.",
      "Evidencia y citas trazables.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util para practica profesional.",
      "Sostener continuidad editorial entre actividades sin perder contexto local de materia."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Uso explicito de etiqueta [supuesto] cuando falte verificacion.",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion profesional concreta."
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
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe",
        "Sincronizacion transversal conservadora"
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
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato de entregas",
          "kind": "supports",
          "justification": "Garantiza coherencia academica entre productos."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion inicial."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura depende de estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicar ni recortar."
        },
        {
          "source": "Sincronizacion transversal conservadora",
          "target": "Reglas locales de Seguridad Social",
          "kind": "develops",
          "justification": "Integra patrones comunes sin mezclar contenido tematico ajeno."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica y archivos base de trabajo.",
        "Programa analitico de destino define proposito y ejes juridicos.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Memoria origen confirma gates de JSON parseable y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura y calidad.",
      "Se preservaron reglas utiles previas del destino sin eliminacion.",
      "Se agrego patron transversal estable: problema-fundamento-evidencia-analisis-conclusion.",
      "Se excluyo transferencia de contenido doctrinal especifico de Filosofia por no equivalencia de nodo.",
      "Se reforzo control de trazabilidad con etiqueta [supuesto] y fuentes provisionales."
    ]
  }
}