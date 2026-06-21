{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral reutilizable desde actividad-1 sin copiar contenido especifico.",
    "Se preservan reglas institucionales UnADM, estructura editorial y compuertas de calidad ya validadas.",
    "Se refuerza deduplicacion lossless y normalizacion obligatoria antes de propagacion recursiva.",
    "Se mantiene caracter provisional de fuentes heredadas no verificadas localmente [supuesto].",
    "Se prioriza consistencia entre consigna local, desarrollo argumentativo y conclusion juridica propia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sostener integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y producto a la planeacion semanal o consigna docente.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre afirmaciones, evidencia y cierre."
  ],
  "activity_rules": [
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local.",
    "Usar fuentes de hermeneutica/argumentacion solo si la consigna lo exige [supuesto].",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar rutas y nombres canonicos antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho.",
    "Agregar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico y no reemplazo automatico [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir entre hermanos solo patrones reutilizables, no conclusiones ni redaccion literal.",
    "Mantener union-dedupe lossless para evitar regresiones.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas.",
    "Conservar registro historico de fuentes provisionales sin elevarlas a canon."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar estilo de citacion obligatorio institucional [supuesto: no definido].",
    "Confirmar nombre canonico final del archivo .bib de asignatura.",
    "Confirmar si actividad-2 requiere reporte, presentacion u otro formato."
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
        "Integridad academica y citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles.",
      "Asegurar fundamento juridico y trazabilidad editorial.",
      "Garantizar transferencia profesional del aprendizaje."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas",
        "Integridad academica",
        "Trazabilidad cita-bibliografia",
        "Ejes editoriales troncales",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, formato y finalidad comun."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo real de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad academica y cierre juridico.",
        "Programa analitico fija proposito y ejes de trabajo transferibles.",
        "Regla estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 55: union-dedupe de reglas repetidas sin recorte semantico.",
      "Ciclo 55: refuerzo lateral de patrones reutilizables desde actividad-1.",
      "Ciclo 55: se evita traslado de conclusiones especificas y bibliografia exclusiva.",
      "Ciclo 55: se mantienen supuestos abiertos donde falta consigna local."
    ]
  }
}