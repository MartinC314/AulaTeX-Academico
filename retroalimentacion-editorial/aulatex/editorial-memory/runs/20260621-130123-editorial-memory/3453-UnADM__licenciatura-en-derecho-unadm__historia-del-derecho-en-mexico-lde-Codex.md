{
  "summary": [
    "Se consolida memoria transversal minima para Historia del Derecho en Mexico con estrategia conservadora.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless por union.",
    "Se transfiere solo abstraccion estable desde Filosofia del Derecho: identidad UnADM, cinco ejes, gates de calidad y normalizacion.",
    "Se evita transferir contenido tematico o bibliografia especifica de Filosofia del Derecho.",
    "Se mantiene alerta historica por salidas no JSON parseables y se refuerza bloqueo preventivo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre oficial local de materia: Historia del Derecho en Mexico [supuesto: acentuacion pendiente].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en consigna o no confirmado localmente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, analisis propio, conclusion transferible.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "No mezclar contenido tematico de otra materia sin evidencia local verificable."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Adaptar salida a reporte, presentacion o producto visual segun consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizacion aguas abajo.",
    "Normalizar respuestas no estructuradas antes de propagar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Aplicar union-dedupe sin recortar reglas utiles previas."
  ],
  "latex_rules": [
    "Usar reporte-historia-del-derecho-en-mexico.tex como base para reportes.",
    "Usar presentacion-historia-del-derecho-en-mexico.tex para productos tipo presentacion.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Actualizar documentsubtitle con numero y nombre real de actividad.",
    "Mantener tabla de autor con alumno, matricula, figura docente, semestre/bloque y tipo/creditos.",
    "No eliminar campos institucionales; solo actualizar valores concretos.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir placeholders/tokens Slug en README y programa antes de automatizar o citar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio bibliografico local canonico.",
    "Conservar entradas institucionales UnADM existentes.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Registrar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir trazabilidad minima: origen y fecha de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No propagar bibliografia de Filosofia del Derecho sin consulta efectiva local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales transversales verificables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar datos curriculares especificos de esta materia a nodos laterales no equivalentes.",
    "Mantener alerta de salidas no parseables en niveles superiores y hermanos.",
    "Aplicar normalizacion manual cuando se detecte salida heredada no estructurada.",
    "Preservar sin regresion reglas utiles ya validadas en ciclos previos."
  ],
  "open_questions": [
    "Confirmar acentuacion oficial en nombre de materia: Mexico/México.",
    "Confirmar si LDE-S1B1 es codigo oficial o solo codigo de plantilla [supuesto].",
    "Definir nombre oficial de figura docente para plantillas.",
    "Confirmar fuente operativa definitiva de consolidacion; Codex y GPT-Pro siguen provisionales [supuesto].",
    "Corregir en README entradas con render anomalo de nombres de archivo [supuesto].",
    "Confirmar consigna local de actividades para ajustar granularidad de productos."
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
        "Materia: Historia del Derecho en Mexico.",
        "Semestre 1, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Identidad institucional consistente.",
      "Cinco ejes editoriales estables.",
      "Analisis propio con sustento verificable.",
      "Cierre juridico transferible.",
      "Control estricto de calidad estructural."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables.",
      "Garantizar coherencia entre consigna, argumentacion, evidencia y formato.",
      "Sostener un cerebro editorial reutilizable sin contaminar temas no equivalentes."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explicito antes del desarrollo.",
      "Secciones funcionales y trazables.",
      "Citas explicitas y verificables.",
      "Marcado explicito de supuestos.",
      "Conclusion juridica con criterio propio."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion aplicada.",
      "Afirmacion sustantiva -> evidencia verificable -> interpretacion del estudiante.",
      "Consigna local -> producto alineado -> validacion de cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Integridad academica",
        "Normalizacion JSON",
        "Trazabilidad bibliografica",
        "Coherencia entre consigna y producto",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "La identidad institucional exige verificabilidad y forma academica."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia entre consigna y producto",
          "kind": "supports",
          "justification": "Los ejes ordenan el desarrollo y evitan desalineacion."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La integridad depende de fuentes consultables y metadatos completos."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion aplicada debe derivar de razonamiento propio sustentado."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial e identidad.",
        "Programa analitico: proposito y cinco ejes.",
        "historia-del-derecho-en-mexico.bib: base institucional local.",
        "Plantillas .tex locales: metadatos y estructura academica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: deduplicacion completa sin recorte de reglas validas.",
      "Ciclo 6: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 6: se mantiene bloqueo por no-JSON parseable como gate critico.",
      "Ciclo 6: se preserva separacion entre identidad editorial y contenido tematico de materias no equivalentes."
    ]
  }
}