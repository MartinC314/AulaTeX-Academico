{
  "summary": [
    "Se consolida sincronizacion transversal ciclo 4 con estrategia progresiva y conservadora.",
    "Se preservan reglas utiles previas sin regresion y con union-dedupe lossless.",
    "Se transfieren solo abstracciones estables desde actividad origen a materia destino.",
    "Se refuerzan identidad UnADM, cinco ejes editoriales, validacion estructural y trazabilidad.",
    "Se mantiene separacion entre fuentes provisionales y autoridad academica verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Conservar trazabilidad del origen editorial en cada fusion de memoria.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar fuentes provisionales como nota tecnica, no como autoridad academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeacion semanal.",
    "Aplicar cinco ejes: problema, conceptos, producto solicitado, analisis propio, conclusion transferible.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "activity_rules": [
    "Verificar la instruccion especifica de cada actividad antes de redactar.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar cada afirmacion con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante en cada entrega.",
    "Comprobar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de la version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la memoria no es JSON parseable.",
    "Validar estructura minima completa antes de fusionar aguas abajo.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que toda afirmacion factual tenga fuente o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar cualquier salida no estructurada antes de reutilizar.",
    "Verificar correspondencia entre producto entregable y consigna de actividad."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local de la materia como base.",
    "Conservar macros institucionales de portada y metadatos.",
    "Mantener compatibilidad con espanol y letterpaper definidos en plantilla.",
    "No eliminar campos de portada; completar faltantes segun actividad.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y documentos de apoyo.",
    "Corregir nombres de archivo corruptos antes de referenciarlos. [supuesto]"
  ],
  "bibliography_rules": [
    "Usar etapas-del-proceso-y-estrategia-del-litigio.bib como repositorio local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web o institucionales dinamicas.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar bibliografia base si no fue usada en el argumento."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables en nodos no equivalentes.",
    "No propagar redaccion literal de actividades; propagar patrones y gates.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual.",
    "Mantener metadatos locales en cada materia y evitar sobrescritura transversal.",
    "Aplicar normalizacion manual cuando reaparezcan salidas no parseables de ciclos iniciales."
  ],
  "open_questions": [
    "Confirmar si documentauthor debe ser fijo de plantilla o variable por estudiante. [supuesto]",
    "Confirmar estilo de citacion juridica requerido por la asignatura.",
    "Confirmar si el coursecode LDE-S5B2 es definitivo institucionalmente. [supuesto]",
    "Confirmar checklist minimo por tipo de producto: reporte, presentacion, visual.",
    "Confirmar correccion de rutas con caracteres corruptos en README. [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro, verificable y argumentativo."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etapas del proceso y estrategia del litigio."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos trazables, fundamentados y aplicables.",
      "Mantener consistencia editorial institucional en toda la materia.",
      "Asegurar calidad tecnica y argumentativa antes de propagar memoria."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Bloques argumentativos visibles.",
      "Citas trazables.",
      "Cierre juridico aplicable.",
      "Etiquetado explicito de [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Cinco ejes editoriales",
        "JSON parseable",
        "Normalizacion estructurada",
        "Union-dedupe sin regresion",
        "Conclusion juridica transferible",
        "Integridad academica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige verificabilidad y trazabilidad."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La estructura por ejes conduce al cierre aplicable."
        },
        {
          "source": "JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay normalizacion confiable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Union-dedupe sin regresion",
          "kind": "supports",
          "justification": "La deduplicacion lossless requiere estructura consistente."
        }
      ],
      "evidence": [
        "README local de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico local con cinco ejes de trabajo.",
        "Bib local con fuentes institucionales UnADM.",
        "Plantilla .tex local con metadatos institucionales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion semantica completada sin eliminar reglas utiles previas.",
      "Ciclo 4: reforzada transferencia transversal por abstracciones estables.",
      "Ciclo 4: reforzados gates de JSON parseable, estructura minima y no regresion.",
      "Ciclo 4: mantenida separacion entre fuentes provisionales y fuentes academicas verificadas."
    ]
  }
}