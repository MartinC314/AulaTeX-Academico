{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad de Filosofia del Derecho y materia de Seguridad Social.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin regresion.",
    "Se transfiere solo abstraccion estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no estructuradas sin normalizacion.",
    "Se refuerza compresion lossless por union-dedupe, nunca por recorte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, norma, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el contenido con seguridad social cuando aplique en el destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivo y resolver tokens sin expandir antes de compilar.",
    "Mantener metadatos institucionales consistentes en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normativa vigente verificable.",
    "Agregar solo referencias consultables y verificables.",
    "No inventar fuentes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas generales estables, no contenido tematico de Filosofia.",
    "Mantener reglas locales de Seguridad Social como prioridad contextual.",
    "Propagar solo despues de validar JSON y estructura.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin desplazar.",
    "Mantener bandera historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Evitar regresiones en identidad, calidad y trazabilidad."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia destino [supuesto].",
    "Confirmar si codigo local LDE-S2B1 sigue vigente en documentos oficiales [supuesto].",
    "Confirmar si la fuente provisional heredada de ingenieria debe retirarse del destino [supuesto].",
    "Confirmar rubricas especificas por actividad para ajustar profundidad argumentativa.",
    "Confirmar si todas las plantillas de Actividad 1 del README ya estan materializadas."
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
      "Evidencia trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para practica profesional.",
      "Preservar memoria editorial persistente con compresion lossless y sin regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Uso explicito de etiqueta [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Coherencia entre portada, metadatos, desarrollo y referencias."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia pertinente.",
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
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere base legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica debe sostenerse en fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y activos editoriales.",
        "Programa analitico destino fija proposito y ejes juridicos.",
        ".bib local destino confirma base institucional y normativa vigente.",
        "Memoria origen confirma gates de JSON, evidencia y conclusion transferible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 63: transferencia transversal conservadora aplicada sin mezclar contenido tematico no equivalente.",
      "Ciclo 63: se reforzaron gates de parseo JSON, trazabilidad y marca [supuesto].",
      "Ciclo 63: se consolidaron patrones argumentativos comunes entre nodos de Derecho.",
      "Ciclo 63: deduplicacion completa de reglas repetidas detectadas en origen y destino."
    ]
  }
}