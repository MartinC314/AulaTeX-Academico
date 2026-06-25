{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se refuerza normalizacion obligatoria antes de propagacion recursiva.",
    "Se mantiene separacion estricta entre abstracciones editoriales y contenido disciplinar.",
    "Supuesto: el origen aporta patrones validos de actividad, no criterios tematicos para Garantias constitucionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir contenido disciplinar entre materias sin validacion expresa."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion, programa analitico y bibliografia."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar correspondencia exacta entre producto entregable y consigna de actividad.",
    "No asumir fuentes de otras semanas o materias sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver placeholders o tokens sin expandir en README, programa analitico y rutas.",
    "Verificar cierre completo de macros de portada antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad entre cita en texto, entrada BibTeX y evidencia documental."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales ya validadas.",
    "Evitar trasladar redaccion literal o contenido tematico entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener alerta institucional de riesgo cuando haya antecedentes no parseables.",
    "Si un nodo destino carece de contexto local, crear cerebro minimo y abrir vacios como preguntas.",
    "Etiquetar ciclos con necesidad de normalizacion manual cuando la fuente llegue incompleta."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad en Garantias constitucionales.",
    "Confirmar figura docente y politica de fecha en portada.",
    "Confirmar estilo de citacion requerido por la materia.",
    "Confirmar correccion total de truncamientos en README y plantilla LaTeX.",
    "Supuesto: la herencia desde Filosofia del Derecho se limita a patrones editoriales transferibles."
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
        "Marcado explicito de supuestos."
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
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Consistencia cita-texto-bib."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos evaluables con rigor juridico.",
      "Asegurar trazabilidad entre consigna, evidencia y conclusion.",
      "Sostener una memoria editorial reutilizable sin contaminar contenido disciplinar."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Separacion entre marco normativo y postura personal.",
      "Cierre con aplicacion juridica concreta.",
      "Supuestos etiquetados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo explicito.",
      "Desarrollo por conceptos y normas.",
      "Analisis propio con soporte.",
      "Cierre transferible a practica profesional."
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
        "Compresion lossless por union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
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
          "justification": "La conclusion juridica debe estar sustentada."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia confiable."
        },
        {
          "source": "Compresion lossless por union-dedupe",
          "target": "Sin regresion editorial",
          "kind": "supports",
          "justification": "La deduplicacion conserva reglas utiles sin recorte."
        }
      ],
      "evidence": [
        "README de la materia con pauta editorial y ubicacion curricular.",
        "Programa analitico con ejes de trabajo comunes.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Reglas heredadas consolidadas por union-dedupe."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 4: se mantiene frontera entre transferencia editorial y contenido disciplinar.",
      "Ciclo 4: se consolidan patrones argumentativos comunes de actividad.",
      "Ciclo 4: se preservan reglas LaTeX y bibliografia con foco en estabilidad y trazabilidad."
    ]
  }
}