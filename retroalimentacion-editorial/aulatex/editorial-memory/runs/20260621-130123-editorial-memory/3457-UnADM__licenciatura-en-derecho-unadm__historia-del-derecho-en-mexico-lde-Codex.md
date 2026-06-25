{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas del destino y se deduplican sin recorte.",
    "Se transfieren solo abstracciones estables: identidad UnADM, cinco ejes, control de calidad y trazabilidad.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables.",
    "Se evita migrar contenido tematico especifico de Filosofia del Derecho al destino no equivalente.",
    "Se refuerza cerebro editorial minimo de materia con vacios locales abiertos y marcados como supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de la materia: Historia del Derecho en Mexico [supuesto: acentuacion pendiente de validacion institucional].",
    "Conservar datos curriculares locales: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio, conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "No mezclar contenido tematico de otras materias sin evidencia local verificable."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar que el producto corresponda a la consigna de la actividad vigente.",
    "Adaptar salida a reporte, presentacion o producto visual segun consigna.",
    "No asumir fuentes de semanas o materias distintas sin verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizacion automatica.",
    "Aplicar compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar placeholders o tokens sin expandir antes de compilar o automatizar."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte y presentacion como base editable segun producto.",
    "Conservar metadatos institucionales clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores por actividad.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir nombres de archivo con render anomalo y resolver tokens tipo $(@{...}.Slug) antes de referenciar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local de la materia.",
    "Conservar entradas institucionales existentes de UnADM y malla curricular.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva en el destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales verificables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir redaccion literal o contenidos tematicos de materia no equivalente.",
    "Mantener alerta historica de salidas no parseables en nodos superiores y laterales.",
    "Aplicar estrategia progresiva: reforzar primero calidad y estructura, luego especializacion local.",
    "Si falta consigna local, conservar cerebro editorial minimo y abrir preguntas de contexto."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional: Mexico vs Mexico con acento en nombre de materia.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla [supuesto].",
    "Definir nombre oficial de figura docente para plantillas.",
    "Corregir en README y programa los tokens Slug no expandidos.",
    "Corregir entradas con render anomalo de archivos en README (eporte, eferencias) [supuesto].",
    "Confirmar rubricas y productos por actividad para ajustar profundidad argumentativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador en inferencias no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna transversal.",
      "Coherencia entre consigna, desarrollo y cierre.",
      "Evidencia verificable con trazabilidad.",
      "Postura propia con utilidad juridica practica.",
      "Control estricto de calidad estructural antes de propagar."
    ],
    "reason_for_being": [
      "Guiar productos academicos reutilizables sin perder identidad institucional.",
      "Convertir planeacion semanal en entregables claros, argumentados y verificables.",
      "Sostener memoria persistente sin regresiones y sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones funcionales y trazables.",
      "Marcado explicito de supuestos.",
      "Citas explicitas y verificables.",
      "Conclusion juridica con criterio propio."
    ],
    "argumentative_patterns": [
      "Problema y objetivo al inicio.",
      "Marco conceptual y normativo pertinente.",
      "Contraste de evidencia con postura propia.",
      "Cierre con implicacion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia consigna-producto",
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
          "justification": "La identidad exige evidencia verificable y formato institucional."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, fuentes, analisis y cierre."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de metadatos y fuentes consultables."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Coherencia consigna-producto",
          "kind": "develops",
          "justification": "Transfiere abstracciones estables sin contaminar contexto local."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y estructura canonica.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Regla persistente: bloquear salidas no JSON parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 7: transferencia transversal solo de abstracciones estables desde actividad origen.",
      "Ciclo 7: se preserva regla de no propagar contenido no estructurado.",
      "Ciclo 7: se mantiene vacio local tematico sin inventar fuentes ni consignas."
    ]
  }
}