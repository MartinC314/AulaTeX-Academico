{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y estructura canonica local de la materia destino.",
    "Se refuerza patron estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate critico: no propagar si la salida no es JSON parseable.",
    "Se evita transferir contenido tematico literal de Filosofia del Derecho al destino de Seguridad Social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Delimitar pregunta guia y verificar coherencia con conclusion.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen descriptivo.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar contenido con derecho a la seguridad social cuando aplique.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Confirmar compresion lossless por union-dedupe y sin regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar rutas y nombres con marcadores corruptos antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido doctrinal especifico de otra materia.",
    "Propagar primero identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener bandera historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin borrar reglas utiles.",
    "Si falta contexto local en subnodos, crear cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial o solo interno [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria sigue vigente en este nodo [supuesto].",
    "Confirmar datos faltantes de plantilla (figura docente) para metadatos finales.",
    "Confirmar criterios de evaluacion/rubrica por actividad para calibrar profundidad argumentativa."
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
      "Consistencia institucional y trazabilidad editorial.",
      "Producto academico verificable orientado a problema juridico.",
      "Fundamento normativo, evidencia y analisis propio.",
      "Cierre con utilidad juridica profesional.",
      "Persistencia de memoria por deduplicacion sin perdida."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos claros, verificables y evaluables.",
      "Asegurar continuidad editorial entre nodos sin mezclar dominios tematicos.",
      "Reducir errores de propagacion mediante gates tecnicos y de evidencia."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Coherencia entre objetivo, desarrollo y conclusion.",
      "Sin inventar fuentes ni citas."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer conceptos y marco normativo.",
      "Contrastar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo/doctrinal",
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
          "justification": "Sin delimitacion del problema no hay analisis pertinente."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentativa necesita respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La memoria solo se consolida de forma segura con estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Historial institucional registra salidas no parseables y exige normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 77: se deduplican reglas repetidas y se preserva contenido util previo.",
      "Ciclo 77: se transfiere patron editorial abstracto desde actividad de Filosofia sin arrastrar contenido tematico literal.",
      "Ciclo 77: se fortalecen gates de JSON, evidencia y consistencia bibtex.",
      "Ciclo 77: se mantiene enfoque conservador sin regresion de identidad UnADM."
    ]
  }
}