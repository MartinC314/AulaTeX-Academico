{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad origen y materia destino.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se transfieren solo abstracciones estables: identidad, estructura, calidad y trazabilidad.",
    "Se mantiene contexto curricular del destino como autoridad local verificada.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar codigo de curso LDE-S4B1 en metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "No mezclar metadatos curriculares del origen con el destino.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como procedencia provisional, no como identidad."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Distinguir reporte, presentacion y producto visual segun consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre README, programa analitico, .bib y plantillas .tex."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina, argumentos y criterio propio.",
    "Evitar extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Mantener auditoria de parseo JSON en propagacion recursiva."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local de la materia sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper y oneside.",
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en nombres de archivo antes de compilar.",
    "No alterar estructura base de portada sin instruccion editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Marcar referencias faltantes como pendientes.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Validar que todas las claves citadas existan en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo reglas generales verificadas entre nodos no equivalentes.",
    "Evitar traslado de contenido tematico especifico de Filosofia del Derecho al destino.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "Aplicar compresion por union-dedupe sin recorte semantico.",
    "No propagar supuestos como reglas definitivas.",
    "Si falta contexto local, mantener cerebro editorial minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar si publico debe normalizarse a publico o publico con acento en nombres editoriales. [supuesto]",
    "Confirmar reparacion definitiva de tokens $(@{...}.Slug) en README y programa analitico.",
    "Confirmar cierre correcto del entorno tabular en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar rubrica de evaluacion por actividad para ajustar profundidad argumentativa. [supuesto]",
    "Confirmar si existe formato institucional de conclusion juridica por tipo de evidencia. [supuesto]"
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Bases de derecho internacional publico."
      ]
    },
    "essence": [
      "Consigna como ancla del entregable.",
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica.",
      "Trazabilidad y verificabilidad documental.",
      "Transferencia profesional del cierre argumentativo."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos y verificables.",
      "Sostener consistencia editorial entre actividades y artefactos de la materia.",
      "Permitir propagacion recursiva segura sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no redundantes.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "La forma del producto depende del encargo semanal."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "Sin respaldo documental no hay cierre juridico solido."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Consistencia cita-bibliografia",
          "kind": "supports",
          "justification": "La estructura valida permite control de integridad editorial."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "La integridad academica materializa el estandar institucional."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El razonamiento ordenado habilita aplicacion profesional."
        }
      ],
      "evidence": [
        "README destino: ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bib local destino: claves institucionales base.",
        "Memoria origen: regla de normalizacion estructurada obligatoria.",
        "Memoria origen: ejes editoriales estables transferibles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 65: se refuerza transferencia transversal de reglas estables sin mover contenido tematico especifico.",
      "Ciclo 65: se conserva gate de bloqueo por JSON no parseable como control critico.",
      "Ciclo 65: se agrega correccion operativa de tokens Slug sin expandir en archivos de control.",
      "Ciclo 65: se mantiene estrategia progresiva y conservadora con deduplicacion lossless."
    ]
  }
}