{
  "summary": [
    "Sincronizacion transversal consolidada entre nodos no equivalentes con enfoque conservador.",
    "Se preserva identidad UnADM y estructura canonica local de Derecho a la Seguridad Social.",
    "Se refuerzan reglas estables transferibles: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin recorte y sin regresion.",
    "Permanece alerta institucional por antecedentes de salida no parseable en ciclos previos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, evidencia, analisis, conclusion.",
    "Separar desarrollo en bloques verificables: marco conceptual, marco normativo, analisis propio, cierre.",
    "Mantener consistencia entre reporte, presentacion y actividad.",
    "Ajustar formato final al producto solicitado por planeacion semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema juridico al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar estructura minima completa antes de propagar recursivamente.",
    "Confirmar correspondencia entre consigna, desarrollo y producto final.",
    "Validar que toda afirmacion tenga respaldo o marca [supuesto].",
    "Comprobar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Conservar plantilla base local y personalizar solo campos variables.",
    "Mantener codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivo con marcadores corruptos antes de usarlos como canon.",
    "No copiar bloques LaTeX completos al propagar memoria."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada clave citada exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Conservar reglas locales de Seguridad Social como capa primaria del destino.",
    "Aplicar estrategia progresiva y conservadora: sumar mejoras verificables sin eliminar reglas previas."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o interno [supuesto].",
    "Verificar vigencia de fuentes provisionales heredadas desde otros dominios [supuesto].",
    "Confirmar rubrica de evaluacion por actividad para calibrar profundidad argumentativa.",
    "Confirmar uso obligatorio de plantillas Actividad-1 en reporte y presentacion."
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
      "Resolver consignas con estructura juridica verificable.",
      "Unir fundamento normativo y analisis propio.",
      "Convertir aprendizaje en conclusion aplicable."
    ],
    "reason_for_being": [
      "Preservar un cerebro editorial persistente, trazable y reusable.",
      "Asegurar calidad formal, juridica y tecnica en cada entrega."
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
          "justification": "Sin problema delimitado no hay argumentacion util."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica debe sostenerse en fuentes."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo juridico.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Memoria previa registra necesidad de normalizacion en salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se reforzo patron transversal de cinco ejes sin mezclar tematicas de filosofia.",
      "Ciclo 12: se preservaron reglas locales de Seguridad Social como capa primaria.",
      "Ciclo 12: se mantuvieron gates criticos de JSON parseable y trazabilidad de supuestos.",
      "Ciclo 12: deduplicacion aplicada sin perdida semantica ni eliminacion de reglas utiles."
    ]
  }
}