{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho y Derecho a la Seguridad Social.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, evidencia verificable y cierre juridico transferible.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se refuerza gate critico: bloquear propagacion si no hay JSON parseable.",
    "Se evita transferir contenido tematico literal de Filosofia; solo abstracciones editoriales reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre README, programa analitico, reporte y presentacion.",
    "Usar estructura minima verificable: portada, desarrollo, conclusion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente toda respuesta no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Conservar claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar nombres de archivo canonicos del README antes de referenciarlos.",
    "Corregir marcadores o tokens sin expandir en rutas y nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica local central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas en este ciclo.",
    "Compartir a laterales no equivalentes solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico local de otra materia.",
    "Preservar alerta historica: ciclos con salida no parseable requieren normalizacion manual.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 es oficial en todos los entregables [supuesto].",
    "Confirmar si figura docente debe permanecer como pendiente en plantillas base [supuesto].",
    "Confirmar vigencia de fuentes provisionales heredadas de otros dominios antes de reutilizar [supuesto]."
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
      "Marco normativo y doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio argumentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto juridico verificable y util profesionalmente.",
      "Garantizar continuidad editorial entre nodos sin perder identidad ni trazabilidad.",
      "Evitar regresiones mediante compresion lossless por union-dedupe."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
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
          "justification": "Sin estructura valida no hay reutilizacion confiable."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicado."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia transversal de entregables",
          "kind": "supports",
          "justification": "Unifica tono, formato y estandar academico entre nodos."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y archivos base.",
        "Programa analitico destino fija proposito y ejes de trabajo.",
        "derecho-a-la-seguridad-social.bib confirma base normativa e institucional.",
        "Historial institucional registra ciclos con salida no parseable y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 64: se refuerza gate JSON parseable como condicion de propagacion.",
      "Ciclo 64: se consolidan ejes editoriales comunes sin mezclar contenido tematico de Filosofia.",
      "Ciclo 64: se mantiene politica de no regresion y compresion lossless por union-dedupe.",
      "Ciclo 64: se preserva trazabilidad de supuestos y fuentes provisionales."
    ]
  }
}