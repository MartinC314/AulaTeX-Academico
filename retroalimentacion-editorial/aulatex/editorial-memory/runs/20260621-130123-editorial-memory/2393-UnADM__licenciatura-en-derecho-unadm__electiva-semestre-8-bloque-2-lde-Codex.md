{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura juridica reusable, calidad JSON y trazabilidad de fuentes.",
    "Se deduplican reglas sin recorte funcional y sin transferir contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerza control de supuestos y manejo de fuentes heredadas como provisionales hasta validacion local.",
    "Se mantiene correccion operativa de placeholders y nombres de archivo como riesgo transversal."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "Fijar autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Usar codigo de curso LDE-S8B2 en metadatos.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la consigna y planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Transformar planeacion semanal en reporte, presentacion o producto visual segun consigna."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal al producto concreto solicitado.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores sin confirmacion de consigna.",
    "No transferir contenido tematico especifico de otra materia sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Revisar manualmente herencias de ciclo 1 antes de reutilizacion.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Verificar correspondencia del producto con la consigna activa de la actividad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Completar metadatos de portada solo con datos confirmados; marcar faltantes como [supuesto].",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) a nombres literales.",
    "Corregir nombres de archivo truncados en listados y rutas antes de entrega."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM cuando corresponda.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener correspondencia estricta entre claves citadas y entradas .bib.",
    "Marcar como [supuesto] cualquier dato bibliografico pendiente de verificacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico local de actividad origen.",
    "Mantener compresion lossless por union-dedupe sin regresion de reglas utiles.",
    "Etiquetar como provisional toda herencia no verificada localmente.",
    "Aplicar estrategia progresiva: consolidar minimo estable y ampliar tras validacion."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino para metadatos finales.",
    "[supuesto] Confirmar figura docente para front matter.",
    "[supuesto] Confirmar si year=2026 y fecha de consulta del sitio UnADM deben actualizarse.",
    "[supuesto] Confirmar nombre oficial alterno de la electiva si existe.",
    "[supuesto] Confirmar politica local para reutilizar o segmentar .bib por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Control visible de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo LDE-S8B2.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y fuentes pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir consignas semanales en entregables juridicos claros, verificables y utiles para practica profesional.",
      "Sostener una memoria editorial estable, auditable y reutilizable entre nodos UnADM."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explicito.",
      "Secciones ordenadas.",
      "Postura propia respaldada.",
      "Cierre aplicable.",
      "Marcado [supuesto] cuando falte confirmacion."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion juridica -> evidencia verificable -> inferencia -> impacto practico.",
      "Evitar descripcion pura; priorizar juicio razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Correccion de placeholders"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar memoria no parseable y errores estructurales."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia entre afirmaciones y fuentes."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La aplicacion profesional depende del razonamiento del estudiante."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Separa datos confirmados de datos pendientes."
        },
        {
          "source": "Correccion de placeholders",
          "target": "Consistencia documental",
          "kind": "supports",
          "justification": "Reduce fallas operativas entre README, programa, .tex y .bib."
        }
      ],
      "evidence": [
        "README local y programa analitico de la materia destino.",
        "Regla heredada estable: bloquear salida no JSON parseable.",
        "Regla transversal estable: marcar [supuesto] datos no confirmados.",
        "Riesgo operativo observado: tokens $(@{...}.Slug) y nombres truncados."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa sin eliminar reglas utiles previas.",
      "Ciclo 5: se conserva herencia institucional de calidad y normalizacion.",
      "Ciclo 5: se agrega refuerzo transversal de estructura argumentativa reusable.",
      "Ciclo 5: se evita transferencia de contenido doctrinal especifico del nodo origen."
    ]
  }
}