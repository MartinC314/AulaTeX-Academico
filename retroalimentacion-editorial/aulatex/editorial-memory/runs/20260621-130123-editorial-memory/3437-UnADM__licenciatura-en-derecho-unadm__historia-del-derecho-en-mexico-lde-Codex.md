{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless por union.",
    "Se transfiere solo abstraccion estable: identidad UnADM, cinco ejes, normalizacion estructurada y control de calidad.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo de Historia del Derecho en Mexico.",
    "Se mantiene alerta operativa por antecedentes de salidas no JSON parseables.",
    "Se refuerza que toda inferencia no visible en consigna local se marque como supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de materia: Historia del Derecho en Mexico.",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Marcar como supuesto todo dato no visible en consigna o documento local."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio, conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado en planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "No mezclar contenido tematico de otra asignatura sin evidencia local verificable."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema concreto y alcance delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Adaptar salida al producto solicitado: reporte, presentacion o producto visual.",
    "No asumir que bibliografia de otra materia aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizacion aguas abajo.",
    "Normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar placeholders o tokens sin expandir antes de compilar o automatizar.",
    "Aplicar union-dedupe sin recortar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base para reportes.",
    "Usar presentacion-historia-del-derecho-en-mexico.tex para salidas tipo presentacion.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; actualizar solo valores concretos por actividad.",
    "Usar codificacion y acentos consistentes en espanol en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local.",
    "Conservar entradas institucionales UnADM y malla curricular.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Registrar en .bib las fuentes especificas por actividad.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales verificables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferir redaccion literal o contenidos tematicos no equivalentes.",
    "Mantener alerta historica de salidas no parseables en nodos superiores y laterales.",
    "Reutilizar marco de cinco ejes con ajuste tematico por asignatura.",
    "Preservar reglas locales del destino cuando no haya conflicto.",
    "Si falta contexto local, mantener cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial institucional de Mexico/México en nombre de materia.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar fuente operativa definitiva para trazabilidad de memoria [supuesto: Codex/GPT-Pro siguen provisionales].",
    "Corregir render anomalo en README para entradas de estructura (eporte/eferencias) [supuesto].",
    "Verificar si existen lineamientos locales adicionales para Historia del Derecho en Mexico no capturados aun."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin perder voz estudiantil."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular local: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna vertebral reusable.",
      "Coherencia entre consigna, desarrollo, evidencia y cierre juridico.",
      "Transferencia transversal por abstracciones estables, no por contenido tematico.",
      "Control de calidad tecnico y academico antes de toda propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Sostener identidad institucional y rigor juridico en toda entrega.",
      "Permitir propagacion recursiva segura con memoria estructurada."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual explicito.",
      "Bloques funcionales trazables.",
      "Citas explicitas y verificables.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Desarrollar conceptos y marco normativo/doctrinal pertinente.",
      "Contrastar evidencia con postura propia.",
      "Concluir con implicacion practica juridica transferible.",
      "Verificar correspondencia entre producto y consigna."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia entre consigna y producto",
        "Propagacion recursiva segura",
        "Supuesto explicitado"
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
          "justification": "La identidad exige formato institucional y citas verificables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, fuentes, analisis y conclusion."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion confiable."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de fuentes consultables y metadatos completos."
        },
        {
          "source": "Supuesto explicitado",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Evita presentar inferencias como hechos confirmados."
        }
      ],
      "evidence": [
        "README de materia: identidad, estructura y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Plantillas .tex locales: metadatos institucionales y estructura de entrega.",
        "Historial de ciclos previos: incidencias de salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas sin perdida de contenido util.",
      "Ciclo 2: se conserva alerta de parseabilidad JSON como gate critico transversal.",
      "Ciclo 2: se refuerza regla de no transferir contenido tematico entre nodos no equivalentes.",
      "Ciclo 2: se consolida nucleo editorial minimo del destino con vacios locales abiertos."
    ]
  }
}