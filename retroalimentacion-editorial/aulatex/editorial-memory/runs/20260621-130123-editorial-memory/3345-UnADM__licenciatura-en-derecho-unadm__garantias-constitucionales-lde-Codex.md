{
  "summary": [
    "Se consolida cerebro editorial minimo para Garantias constitucionales con sincronizacion transversal desde actividad no equivalente.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se mantiene estrategia conservadora: solo abstraer patrones editoriales, no contenido disciplinar de Filosofia del Derecho.",
    "Se refuerza compresion lossless por union-dedupe y sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
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
    "Evitar extrapolar fuentes de semanas o materias no confirmadas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion verificable.",
    "Resolver placeholders o tokens sin expandir en README, programa y rutas.",
    "Corregir truncamientos en portada y macros antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en garantias-constitucionales.bib.",
    "No inventar referencias; usar solo fuentes consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Agregar identificador, emisor y fecha en normas usadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales generales ya validadas.",
    "Evitar mover datos curriculares especificos fuera de su materia.",
    "Mantener alerta institucional sobre entradas no estructuradas.",
    "Aplicar normalizacion manual cuando la fuente llegue incompleta.",
    "Reforzar primero identidad, estructura, gates y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad en Garantias constitucionales.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar figura docente y fecha de entrega en plantilla.",
    "Confirmar estilo de citacion exigido [supuesto: APA o juridico institucional].",
    "Confirmar correccion total de truncamientos en README y portada LaTeX."
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
        "Entrada canonica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Garantias constitucionales.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Garantizar trazabilidad entre consigna, argumentacion, fuentes y cierre profesional."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Marcado explicito de supuestos.",
      "Separacion clara entre marco normativo y postura personal.",
      "Cierre con aplicacion juridica concreta."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado.",
      "Conclusion aplicable a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Consistencia cita-texto-bib"
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
          "justification": "La identidad institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se construye desde una pregunta o conflicto definido."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere sustento legal o doctrinal verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia confiable."
        }
      ],
      "evidence": [
        "README de la materia con pauta editorial y ubicacion curricular.",
        "Programa analitico con ejes de trabajo comunes.",
        "Archivo garantias-constitucionales.bib con base institucional.",
        "Reglas heredadas consolidadas por union-dedupe sin regresion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo totalidad util.",
      "Se bloquearon transferencias de contenido tematico no equivalente.",
      "Se reforzaron gates de parseabilidad, normalizacion y consistencia bibliografica.",
      "Se completo ADN editorial minimo del destino que estaba vacio."
    ]
  }
}