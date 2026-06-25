{
  "summary": [
    "Se sincroniza memoria transversal con union-dedupe sin perdida ni regresion.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se transfiere solo abstraccion estable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de JSON parseable y normalizacion previa a propagacion.",
    "Se evita mezclar contenido tematico de Filosofia del Derecho con Seguridad Social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; aplicar union-dedupe."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar cada actividad con el campo de seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que la compresion sea lossless por union-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Usar codificacion correcta para espanol en .tex y .bib.",
    "Mantener metadatos institucionales y de curso consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Resolver tokens sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y estables.",
    "No propagar contenido tematico especifico de Filosofia del Derecho al destino.",
    "Mantener alerta de riesgo por antecedentes de salida no parseable en ciclos previos.",
    "Aplicar estrategia progresiva y conservadora: reforzar primero identidad, estructura y gates.",
    "Preservar trazabilidad de reglas provisionales con etiqueta [supuesto]."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si el codigo local LDE-S2B1 debe figurar en todas las portadas [supuesto].",
    "Confirmar datos faltantes de figura docente para plantillas de actividad.",
    "Verificar si existen criterios de rubrica especificos por actividad en planeaciones locales."
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
      "Producto juridico verificable con problema, fundamento, evidencia, analisis y cierre.",
      "Transferencia transversal de patrones editoriales estables.",
      "Compresion lossless por deduplicacion."
    ],
    "reason_for_being": [
      "Garantizar coherencia editorial persistente entre nodos no equivalentes.",
      "Evitar regresiones y mantener calidad verificable en cada ciclo."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y conclusion."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia.",
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
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida exige fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica y artefactos base.",
        "Programa analitico define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Antecedentes de salida no parseable justifican gate de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se reforzo ADN transversal sin transferir redaccion literal del origen.",
      "Ciclo 18: se conservaron reglas utiles previas del destino y memoria heredada institucional.",
      "Ciclo 18: se depuraron duplicados semanticos por union-dedupe.",
      "Ciclo 18: se mantuvo abierto lo no verificable como [supuesto]."
    ]
  }
}