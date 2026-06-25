{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin regresion.",
    "Se refuerzan reglas editoriales estables y no se transfiere contenido disciplinar de Filosofia del Derecho.",
    "Se mantiene identidad UnADM y contexto curricular local de Garantias constitucionales.",
    "Se preserva gate critico: bloquear propagacion si no hay JSON parseable.",
    "Se confirma cerebro editorial minimo operativo para materia destino con vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada y metadatos.",
    "Usar contexto local verificado: Garantias constitucionales, Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir contenido disciplinar entre materias sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia.",
    "Corregir placeholders o truncamientos en README, programa y plantillas antes de reutilizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion automatica si la entrada no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y configuracion base de la plantilla local salvo justificacion verificable.",
    "Completar campos de portada: actividad, figura docente y fecha.",
    "Evitar comandos no estandar sin justificacion editorial o tecnica.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir truncamientos visibles en macros de portada antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM, normas y doctrina juridica verificable.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales ya validadas.",
    "No propagar datos curriculares locales fuera del nodo destino sin contexto.",
    "Mantener alerta institucional de riesgo por herencias no estructuradas.",
    "Etiquetar ciclos con necesidad de normalizacion manual cuando la fuente llegue no parseable.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual en saltos transversales."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna local de la primera actividad de Garantias constitucionales.",
    "Confirmar rubrica de evaluacion local para ajustar profundidad argumentativa.",
    "Confirmar figura docente y politica de fecha (fija o \\today).",
    "Confirmar estilo de citacion exigido (APA, juridico mexicano u otro).",
    "Confirmar correccion final de truncamientos en reporte y nombres en README."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada antes de propagar.",
        "Marcado explicito de supuestos.",
        "Separacion entre memoria local y herencia transversal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos.",
        "Coursecode local: LDE-S2B1."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable.",
      "Trazabilidad entre consigna, fuentes y producto."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos solidos y verificables.",
      "Estandarizar calidad editorial sin invadir contenido disciplinar no validado.",
      "Sostener continuidad institucional en propagacion transversal."
    ],
    "style_markers": [
      "Frases cortas y verificables.",
      "Separacion clara entre norma y opinion.",
      "Cierre con transferencia a practica juridica.",
      "Uso explicito de [Supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y norma aplicable.",
      "Argumentar con evidencia.",
      "Fijar postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia cita-texto-bib",
        "Propagacion transversal conservadora"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentacion solida."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica requiere sustento verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Solo salidas parseables permiten transferencia confiable."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "No transferencia disciplinar",
          "kind": "supports",
          "justification": "El salto entre nodos no equivalentes exige abstraer solo reglas estables."
        }
      ],
      "evidence": [
        "README de Garantias constitucionales con pauta editorial y ubicacion curricular.",
        "Programa analitico local con ejes de trabajo estables.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Memoria origen y destino con regla comun de JSON parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se deduplican reglas repetidas y se conserva contenido util sin recorte.",
      "Ciclo 12: se refuerzan gates criticos de parseabilidad JSON y consistencia cita-bib.",
      "Ciclo 12: se mantiene separacion entre abstraccion editorial y contenido disciplinar.",
      "Ciclo 12: se preserva identidad UnADM y contexto curricular local del destino."
    ]
  }
}