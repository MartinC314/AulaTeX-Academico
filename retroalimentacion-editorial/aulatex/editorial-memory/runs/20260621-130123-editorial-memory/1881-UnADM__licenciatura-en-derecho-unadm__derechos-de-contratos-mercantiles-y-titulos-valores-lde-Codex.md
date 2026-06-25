{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa y control de calidad.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al campo mercantil.",
    "Se refuerza deduplicacion lossless por union sin recorte de reglas utiles previas.",
    "Se mantiene alerta institucional por salidas no estructuradas hasta verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y al contexto de la materia destino.",
    "Conservar tono juridico-formal con postura academica propia en el cierre.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar carpeta de materia como entrada canonica editorial."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin evidencia local. [supuesto]"
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Verificar correspondencia entre citas en texto y archivo .bib.",
    "Evitar regresion de reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar espanol con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Corregir macros truncadas antes de compilar.",
    "Resolver placeholders de slug en README y programa analitico.",
    "Corregir nombres truncados de archivos en README.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar solo fuentes realmente consultables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables entre nodos no equivalentes.",
    "No transferir redaccion literal ni contenido doctrinal especifico del origen.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar compresion union-dedupe lossless en cada ciclo.",
    "Mantener alertas de normalizacion manual heredadas hasta cierre verificable.",
    "Si falta contexto local, crear minima base y dejar vacios como preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar resolucion definitiva de salidas no JSON en flujos actuales.",
    "Confirmar plantilla oficial de presentacion de la materia destino.",
    "Confirmar correccion total de placeholders slug en README y programa.",
    "Confirmar correccion de nombres truncados de archivos en README.",
    "Confirmar politica local de year fijo vs fecha de consulta para fuente institucional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta canonica como punto de entrada."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Materia destino: contratos mercantiles y titulos valores."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio no descriptivo.",
      "Cierre con aplicacion profesional.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Estandarizar productos academicos reutilizables con rigor juridico.",
      "Garantizar trazabilidad entre afirmaciones, evidencia y conclusion.",
      "Sostener memoria editorial persistente sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Apertura breve orientada a problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados cuando falte evidencia.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/normas -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion juridica siempre respaldada por fuente verificable.",
      "Consistencia entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "JSON parseable",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible"
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion recursiva segura requiere estructura valida."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumento pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional necesita base juridica explicita."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        ".bib local confirmado: derechos-de-contratos-mercantiles-y-titulos-valores.bib.",
        "Regla heredada institucional: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicadas reglas repetidas de tono, estructura y calidad.",
      "Ciclo 9: mantenida estrategia conservadora de transferencia transversal.",
      "Ciclo 9: reforzada separacion entre abstracciones editoriales y contenido tematico local.",
      "Ciclo 9: preservadas alertas historicas de normalizacion manual como provisionales."
    ]
  }
}