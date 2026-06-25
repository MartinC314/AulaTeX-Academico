{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin regresion.",
    "Se preservan reglas estables de identidad, estructura, calidad, LaTeX y bibliografia.",
    "Se transfiere solo abstraccion editorial reusable; no se transfiere contenido disciplinar de Filosofia del Derecho.",
    "Se mantiene alerta institucional: bloquear propagacion cuando no haya JSON parseable.",
    "Se refuerza cerebro editorial minimo de materia destino con vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, Garantias constitucionales, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No transferir contenido disciplinar entre materias sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Evitar afirmaciones constitucionales sin fundamento normativo o bibliografico.",
    "No asumir que fuentes de otras semanas o materias aplican a la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagacion automatica si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar congruencia entre metadatos de portada y datos curriculares locales."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "No introducir paquetes no estandar sin necesidad verificable.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Corregir placeholders y tokens sin expandir en README, programa analitico y rutas.",
    "Reparar truncamientos en portada y macros antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar identificador, emisor y fecha cuando se cite normativa."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales ya validadas.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Evitar trasladar datos curriculares fuera de su materia.",
    "Mantener trazabilidad de reglas provisionales heredadas.",
    "Etiquetar ciclos con normalizacion manual cuando la fuente llegue no estructurada.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual."
  ],
  "open_questions": [
    "[Supuesto] Falta consigna local de la primera actividad en Garantias constitucionales.",
    "Confirmar nombre de figura docente en plantilla LaTeX.",
    "Confirmar correccion final de truncamientos en reporte-garantias-constitucionales.tex.",
    "Confirmar reemplazo total de placeholders de slug en README y programa analitico.",
    "Confirmar estilo de citacion exigido por la consigna local."
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
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Consistencia cita-texto-bib.",
      "Compresion lossless por deduplicacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para la practica juridica.",
      "Sostener calidad editorial estable entre nodos no equivalentes sin contaminar contenido disciplinar."
    ],
    "style_markers": [
      "Frases breves y verificables.",
      "Separacion clara entre marco normativo y postura personal.",
      "Cierre con aplicacion juridica concreta.",
      "Uso explicito de etiqueta [Supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio con evidencia.",
      "Conclusion aplicable."
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
          "justification": "El analisis requiere un conflicto definido."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe estar fundamentada."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay transferencia confiable."
        },
        {
          "source": "Consistencia cita-texto-bib",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo."
        }
      ],
      "evidence": [
        "README local con pauta editorial y ubicacion curricular.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Regla institucional heredada: no propagar salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion completada sin recorte semantico.",
      "Ciclo 8: se refuerzan quality gates de JSON y normalizacion.",
      "Ciclo 8: se conserva separacion entre abstraccion editorial y contenido disciplinar.",
      "Ciclo 8: se mantienen vacios locales como preguntas abiertas con etiqueta de supuesto."
    ]
  }
}