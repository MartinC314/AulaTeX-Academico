{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de Filosofia del Derecho hacia materia de Contratos y Obligaciones.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless sin recorte semantico.",
    "Se refuerza el nucleo transversal de cinco ejes: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se mantiene como regla dura la normalizacion de salidas no estructuradas antes de persistir o propagar.",
    "Se evita transferir contenido tematico de Filosofia del Derecho que no sea reusable en clave editorial."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares confirmados de la materia: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Conservar enfoque juridico aplicado a contratos y obligaciones.",
    "Usar codigo de curso LDE-S4B1 cuando la plantilla lo requiera.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Mantener trazabilidad entre objetivo, evidencia, argumento y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir bibliografia base y fuentes especificas de actividad."
  ],
  "activity_rules": [
    "Adaptar cada actividad al producto solicitado por la consigna vigente.",
    "Explicitar postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y cierre.",
    "No trasladar contenido de otras materias sin adecuacion disciplinar contractual.",
    "Marcar supuestos cuando falte instruccion especifica.",
    "Evitar asumir que fuentes de semanas posteriores aplican a actividades iniciales."
  ],
  "quality_gates": [
    "Bloquear persistencia o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Corregir placeholders tipo $(@{...}.Slug) en README y programa analitico antes de compilar.",
    "No degradar reglas utiles previas durante union-dedupe."
  ],
  "latex_rules": [
    "Usar plantilla base local de reporte o presentacion segun consigna.",
    "Mantener metadatos completos: curso, autor, universidad, ubicacion y subtitulo de actividad.",
    "Usar espanol academico claro y terminologia juridica precisa.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Usar derechos-de-los-contratos-y-obligaciones.bib como archivo canonico local."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Separar bibliografia base de bibliografia especifica por actividad.",
    "Conservar y reutilizar entradas base unadmSitioWeb y unadmMallaDerecho2024.",
    "Declarar [supuesto] si una referencia obligatoria no esta disponible."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables, no redaccion literal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual transversal.",
    "Excluir metadatos o contenido tematico especifico de Filosofia del Derecho en nodos no equivalentes.",
    "Aplicar compatibilidad disciplinar antes de propagacion lateral.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Si un nodo hijo esta vacio, inicializar cerebro minimo con identidad, estructura y gates."
  ],
  "open_questions": [
    "Confirmar guia formal de citacion obligatoria en la materia (APA, juridico mexicano u otra).",
    "Confirmar rubrica por actividad para calibrar profundidad argumentativa.",
    "Confirmar alcance normativo requerido por actividad: federal, local o mixto.",
    "Confirmar si presentacion comparte todos los metadatos del reporte.",
    "Confirmar si el autor por defecto debe mantenerse o variar por actividad [supuesto]."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de los contratos y obligaciones."
      ]
    },
    "essence": [
      "Modelo transversal de cinco ejes como esqueleto editorial estable.",
      "Normalizacion estructurada como requisito previo de memoria persistente.",
      "Analisis juridico propio con cierre profesional aplicable.",
      "Disciplina contractual como filtro de pertinencia tematica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y verificables.",
      "Asegurar coherencia entre problema, evidencia, argumento y conclusion.",
      "Preservar calidad institucional en todo salto transversal."
    ],
    "style_markers": [
      "Supuestos etiquetados como [supuesto].",
      "Secciones funcionales y auditables.",
      "Conclusion juridica operativa.",
      "Sin afirmaciones sin fuente o sin marca de supuesto."
    ],
    "argumentative_patterns": [
      "Plantear problema breve y delimitado.",
      "Definir objetivo y criterio de analisis.",
      "Sustentar con norma, doctrina o evidencia verificable.",
      "Desarrollar postura propia justificada.",
      "Cerrar con conclusion transferible a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "JSON parseable",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Trazabilidad cita-.bib",
        "Enfoque contractual"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "supports",
          "justification": "La persistencia confiable depende de salidas estructuradas."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis juridico propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta o conflicto delimitado."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge del razonamiento sustentado."
        },
        {
          "source": "Trazabilidad cita-.bib",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad bibliografica sostiene la calidad institucional."
        },
        {
          "source": "Enfoque contractual",
          "target": "Transferencia transversal",
          "kind": "contrasts",
          "justification": "Se transfieren reglas editoriales estables, no contenido filosofico especifico."
        }
      ],
      "evidence": [
        "README de materia confirma ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes transversales.",
        "Archivo .bib local confirma entradas base institucionales.",
        "Memoria origen confirma regla dura de normalizacion previa y JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 6: preservada regla de bloqueo por JSON no parseable.",
      "Ciclo 6: reforzada trazabilidad entre citas y .bib como gate transversal.",
      "Ciclo 6: conservada correccion tecnica de placeholders $(@{...}.Slug).",
      "Ciclo 6: excluida transferencia literal de contenidos tematicos no equivalentes."
    ]
  }
}