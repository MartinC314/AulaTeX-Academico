{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerzan abstracciones estables: identidad UnADM, cinco ejes, normalizacion JSON y trazabilidad bibliografica.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo de Historia del Derecho en Mexico.",
    "Se mantiene alerta historica por salidas no JSON parseables y se bloquea propagacion sin estructura valida."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de la materia: Historia del Derecho en Mexico [supuesto: acentuacion institucional pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio, conclusion transferible.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Corregir placeholders de Slug en README y programa antes de automatizar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Comprobar que el producto corresponda a la consigna de la actividad local.",
    "No asumir que bibliografia o insumos de otras semanas aplican a la actividad actual.",
    "No mezclar contenido tematico de otra materia sin evidencia local verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizacion aguas abajo.",
    "Validar estructura minima completa del esquema editorial antes de propagar recursivamente.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar union-dedupe sin recortar reglas utiles previas.",
    "Mantener alerta activa por historial de salidas no parseables en ciclos previos."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex y presentacion-historia-del-derecho-en-mexico.tex segun producto.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener campos institucionales y tabla de autor; solo actualizar valores concretos.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa antes de compilar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local.",
    "Conservar fuentes institucionales UnADM y malla curricular como base.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Registrar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva en esta materia."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico no equivalente.",
    "Reutilizar control de normalizacion JSON en nodos hermanos y superiores.",
    "No propagar datos curriculares especificos de esta materia a otras materias."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial del nombre de la materia: Mexico o México.",
    "Confirmar si LDE-S1B1 es codigo oficial o codigo local de plantilla.",
    "Definir nombre oficial de figura docente para plantillas.",
    "Verificar y corregir artefactos de render en README (eporte, eferencias) [supuesto].",
    "Confirmar fuente operativa definitiva para reemplazar referencias provisionales de motor."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante inferencias no verificadas."
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
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Cinco ejes editoriales como columna vertebral de cada entrega.",
      "Coherencia entre consigna, evidencia, analisis propio y cierre juridico.",
      "Transferencia transversal por abstraccion, no por copia tematica.",
      "Seguridad editorial basada en parseabilidad, normalizacion y trazabilidad."
    ],
    "reason_for_being": [
      "Guiar productos academicos juridicos claros, verificables y transferibles a practica profesional.",
      "Convertir planeacion semanal en entregables consistentes con identidad UnADM.",
      "Proteger continuidad editorial del nodo mediante reglas reutilizables y auditables."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo puntual explicito.",
      "Secciones funcionales y trazables.",
      "Citas explicitas y verificables.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema inicial -> objetivo -> desarrollo conceptual/normativo.",
      "Evidencia verificable -> contraste -> postura del estudiante.",
      "Sintesis final -> conclusion juridica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Normalizacion JSON",
        "Integridad academica",
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
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal conservadora",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay reutilizacion segura."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Los ejes ordenan estructura, evidencia y cierre."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad depende de fuentes consultables y metadatos minimos."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "El marco institucional exige rigor formal y cita verificable."
        },
        {
          "source": "Propagacion transversal conservadora",
          "target": "Coherencia consigna-producto",
          "kind": "develops",
          "justification": "Transfiere solo reglas estables y evita ruido tematico entre materias no equivalentes."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y estructura local.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Historial de salidas no JSON parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se deduplican reglas repetidas y se preserva cobertura util sin recorte.",
      "Ciclo 16: se incorpora del origen solo abstraccion estable (cinco ejes, gates, supuestos, trazabilidad).",
      "Ciclo 16: se mantiene barrera de seguridad parseable JSON + normalizacion previa.",
      "Ciclo 16: se evita arrastre de contenido tematico especifico de Filosofia del Derecho."
    ]
  }
}