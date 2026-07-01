{
  "summary": [
    "Se mantiene identidad UnADM y foco juridico del destino.",
    "Se refuerza patron transversal estable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva regla critica: no propagar sin JSON parseable y normalizacion previa.",
    "Se preserva compresion lossless por union-dedupe sin recorte ni regresion.",
    "Se evita transferencia tematica literal de Filosofia del Derecho a Seguridad Social."
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
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Relacionar el contenido con derecho a la seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar recursivamente.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Resolver marcadores o tokens sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar en saltos no equivalentes: identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas locales del destino como capa superior de especificidad.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin reemplazar.",
    "Mantener alerta de normalizacion manual para artefactos heredados de ciclos con salidas no parseables [supuesto]."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si existe rubrica oficial por actividad para calibrar profundidad argumentativa [supuesto].",
    "Confirmar vigencia de reglas heredadas desde nodos no juridicos aun marcadas como provisionales [supuesto].",
    "Confirmar campos institucionales pendientes de plantilla (figura docente u otros) [supuesto]."
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
      "Estructura por ejes juridicos verificables.",
      "Argumentacion con postura propia sustentada.",
      "Trazabilidad de supuestos y fuentes provisionales.",
      "Compresion editorial lossless por deduplicacion."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util para practica profesional.",
      "Preservar memoria editorial persistente sin perder reglas validas previas.",
      "Habilitar sincronizacion transversal segura entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia verificable.",
      "Sostener postura propia argumentada.",
      "Concluir con criterio juridico transferible."
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
        "Normalizacion estructurada",
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
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "La postura gana solidez con respaldo trazable."
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
          "justification": "Conserva reglas utiles sin duplicados ni perdida."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica de artefactos.",
        "Programa analitico define proposito y ejes de trabajo de la materia.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Memoria de origen confirma gates de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se reforzo patron transversal comun sin mezclar contenido tematico de origen.",
      "Ciclo 2: se consolidaron gates de calidad como invariantes de propagacion.",
      "Ciclo 2: se mantuvo identidad local del destino como capa prioritaria.",
      "Ciclo 2: se deduplicaron reglas semanticamente equivalentes sin recorte."
    ]
  }
}