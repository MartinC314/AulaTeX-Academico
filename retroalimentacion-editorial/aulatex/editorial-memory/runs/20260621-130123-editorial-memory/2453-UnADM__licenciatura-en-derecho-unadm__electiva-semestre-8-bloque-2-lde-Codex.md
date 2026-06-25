{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad y materia no equivalente.",
    "Se preservan reglas utiles previas y se deduplican sin recorte.",
    "Se refuerza ADN UnADM: identidad juridica, estructura reusable, trazabilidad y conclusion profesional.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables.",
    "Se agrega control operativo transversal de placeholders y nombres truncados en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canonica.",
    "Conservar tono academico-juridico claro y argumentativo.",
    "Marcar como [supuesto] todo dato no confirmado localmente.",
    "Mantener autor y matricula confirmados en front matter.",
    "Tratar herencias no verificadas como provisionales hasta validacion manual."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto con la consigna y planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a un producto concreto.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Vincular conceptos, normas, doctrina o datos con el problema tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir contenido tematico especifico de otra materia sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar manualmente herencias de ciclo 1/ciclo 2 antes de aplicar.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders visibles o tokens sin expandir.",
    "Validar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir placeholders tipo $(@{...}.Slug) a nombres literales.",
    "Corregir nombres truncados en listados de estructura antes de entrega.",
    "Actualizar titulo, subtitulo y numero real de actividad antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como [supuesto] cualquier dato bibliografico no confirmado."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico local no verificado.",
    "Aplicar union-dedupe lossless y sin regresion de reglas utiles.",
    "Mantener etiqueta provisional en herencias no verificadas hasta confirmacion."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino.",
    "[supuesto] Confirmar figura docente para front matter.",
    "[supuesto] Confirmar politica institucional para year/fecha de consulta en @misc.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar si hay rubrica local que ajuste profundidad argumentativa."
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
        "Normalizacion estructurada antes de propagar.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo de curso LDE-S8B2.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y fuentes pertinentes.",
      "Producto solicitado.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Trazabilidad cita-texto-bib."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y transferibles.",
      "Sostener consistencia editorial entre documentos de la materia.",
      "Reducir riesgo de errores de forma y de verificabilidad."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas.",
      "Postura propia sustentada.",
      "Marcado de [supuesto] cuando aplique.",
      "Cierre profesional aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Evitar descripcion pura; priorizar juicio juridico razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Trazabilidad cita-texto-bib",
        "Analisis juridico propio",
        "Conclusion juridica transferible",
        "Compresion union-dedupe lossless"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables y errores de forma."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad requiere correspondencia explicita entre texto y fuentes."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La transferencia profesional surge del razonamiento, no del resumen."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Distingue datos confirmados de pendientes y evita afirmaciones impropias."
        }
      ],
      "evidence": [
        "README local: pauta editorial UnADM y entrada canonica.",
        "Programa analitico local: ejes de trabajo reutilizables.",
        "Bib local: base institucional verificable.",
        "Historial de incidencias: salidas no JSON y placeholders sin expandir."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 20: preservada regla de bloqueo por JSON no parseable.",
      "Ciclo 20: reforzada regla transversal de resolver placeholders/tokens en rutas.",
      "Ciclo 20: mantenida estrategia conservadora de no trasladar contenido tematico no verificado.",
      "Ciclo 20: consolidado nucleo editorial minimo reutilizable para propagacion transversal."
    ]
  }
}