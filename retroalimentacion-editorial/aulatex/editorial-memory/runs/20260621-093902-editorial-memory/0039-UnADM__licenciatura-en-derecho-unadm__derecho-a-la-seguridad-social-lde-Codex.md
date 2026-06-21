{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas editoriales estables.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza patron reusable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin recorte.",
    "Se conserva gate critico: bloquear propagacion si no hay JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto pedido en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema juridico especifico de la actividad.",
    "Distinguir hechos, normas, conceptos y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que no haya regresion ni eliminacion de reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y editar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres/rutas de archivos y resolver tokens sin expandir antes de compilar [supuesto]."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; agregar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Distinguir bibliografia base de materia vs bibliografia especifica de actividad.",
    "Verificar que cada cita LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino.",
    "Propagar primero identidad, estructura reusable y gates de calidad.",
    "Mantener bandera historica: ciclo 1 requiere normalizacion manual si se reutiliza.",
    "Aplicar estrategia progresiva y conservadora: sumar, deduplicar, no recortar."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 sigue vigente oficialmente [supuesto].",
    "Confirmar si todos los archivos de Actividad-1 del README ya existen y son canon operable.",
    "Confirmar si hay rubrica oficial por actividad para ajustar profundidad argumentativa."
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
      "Resolver consignas con trazabilidad juridica verificable.",
      "Sostener todo desarrollo en problema, fundamento, evidencia, analisis y conclusion.",
      "Preservar memoria editorial por union-dedupe sin perdida."
    ],
    "reason_for_being": [
      "Convertir consignas en productos academicos utiles para practica juridica.",
      "Asegurar coherencia institucional, tecnica y bibliografica en toda entrega."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Integrar evidencia y contraste.",
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
          "justification": "La conclusion requiere fundamento legal verificable."
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
          "justification": "Preserva reglas utiles sin duplicados ni perdida."
        }
      ],
      "evidence": [
        "README de la materia define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo del destino.",
        "Archivo .bib local confirma base institucional y normativa verificable.",
        "Memoria previa exige normalizacion de salidas no parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 39: se transfirieron solo abstracciones estables desde actividad origen transversal.",
      "Ciclo 39: se preservaron reglas locales del destino sin mezclar contenido tematico de filosofia.",
      "Ciclo 39: se reforzaron gates de JSON, supuestos, trazabilidad y control bibliografico.",
      "Ciclo 39: consolidacion lossless aplicada por union-dedupe y sin regresion."
    ]
  }
}