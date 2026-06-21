{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas editoriales estables.",
    "Se preserva identidad UnADM y contexto curricular local de Derecho a la Seguridad Social.",
    "Se refuerza patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se conserva gate critico: bloquear propagacion si salida no es JSON parseable.",
    "Se normaliza transferencia: abstraer reglas reutilizables y evitar arrastre tematico literal desde Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Delimitar problema y alcance desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, norma, doctrina y postura propia.",
    "Evitar entregas solo descriptivas; incluir argumentacion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en todos los .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar nombres de archivos y resolver tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativa juridica vigente verificable.",
    "Agregar solo referencias realmente consultables con metadatos minimos completos.",
    "No inventar fuentes; registrar faltantes como pendientes [supuesto].",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar correspondencia uno-a-uno entre cita LaTeX y entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener reglas locales de Seguridad Social como capa dominante del destino.",
    "Propagar recursivamente solo despues de validar JSON y estructura minima.",
    "Mantener bandera historica: ciclo 1 requirio normalizacion manual."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 debe figurar en todas las portadas [supuesto].",
    "Confirmar nombre oficial de figura docente para plantillas activas [supuesto].",
    "Verificar si existen consignas de Actividad 1 para ajustar artefacto inicial del destino.",
    "Confirmar vigencia de fuentes provisionales heredadas de nodos no juridicos [supuesto]."
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
      "Identidad institucional estable.",
      "Problema juridico delimitado.",
      "Marco normativo verificable.",
      "Evidencia trazable.",
      "Analisis propio argumentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar consignas en productos juridicos verificables y evaluables.",
      "Sostener continuidad editorial entre actividades, materia y propagacion transversal.",
      "Reducir riesgo de regresion mediante gates de calidad y trazabilidad."
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
      "Presentar evidencia verificable.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Propagacion transversal"
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
          "target": "Propagacion transversal",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Propagacion transversal",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicado."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige fundamento legal verificable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Propagacion transversal",
          "kind": "supports",
          "justification": "Asegura coherencia institucional entre nodos."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos base.",
        "Programa analitico local fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Memoria origen confirma gates de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: se refuerza transferencia de abstracciones estables y se evita arrastre tematico literal.",
      "Ciclo 10: se preservan reglas locales del destino y se integran gates transversales de calidad.",
      "Ciclo 10: se mantiene trazabilidad de supuestos y fuentes provisionales sin eliminar reglas utiles previas."
    ]
  }
}