{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y reglas locales de Derecho a la Seguridad Social sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se mantiene alerta institucional: no propagar salidas no parseables sin normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y estructura.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia destino como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Relacionar el desarrollo con seguridad social cuando corresponda al destino.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar rutas y nombres de archivo con tokens o caracteres corruptos antes de compilar.",
    "No copiar bloques LaTeX completos en memoria; guardar reglas reutilizables."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Agregar fuentes heredadas solo tras verificacion local [supuesto]."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico especifico de Filosofia del Derecho.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Propagar recursivamente solo despues de validar JSON y estructura."
  ],
  "open_questions": [
    "Confirmar si existe norma de citacion juridica especifica para esta materia [supuesto].",
    "Confirmar si las plantillas Actividad-1 del destino ya son canon operativo.",
    "Confirmar vigencia de cualquier fuente provisional heredada de nodos ajenos [supuesto].",
    "Confirmar si se exige rubrica formal por actividad para ajustar profundidad argumentativa.",
    "Confirmar si el codigo local LDE-S2B1 debe permanecer como metadato obligatorio [supuesto]."
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
      "Fundamento normativo verificable.",
      "Evidencia pertinente y citada.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para practica profesional.",
      "Preservar memoria editorial persistente con compresion lossless y sin regresion.",
      "Garantizar trazabilidad, calidad estructural y consistencia bibliografica."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Reglas reutilizables, no redaccion literal."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
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
        "Normalizacion estructurada"
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
          "justification": "El analisis exige una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica debe ser sustentada."
        },
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Permite consolidar sin perdida ni duplicados."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Da coherencia academica y profesional a los productos."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa y claves de cita.",
        "Memoria origen confirma gates de JSON parseable y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura y calidad.",
      "Se transfirieron solo abstracciones estables; se excluyo contenido tematico especifico de Filosofia.",
      "Se reforzo control de propagacion: JSON parseable + estructura minima.",
      "Se mantuvo bibliografia local del destino como canon y se marco herencia no verificada como [supuesto].",
      "Se preservo politica de no regresion y compresion lossless."
    ]
  }
}