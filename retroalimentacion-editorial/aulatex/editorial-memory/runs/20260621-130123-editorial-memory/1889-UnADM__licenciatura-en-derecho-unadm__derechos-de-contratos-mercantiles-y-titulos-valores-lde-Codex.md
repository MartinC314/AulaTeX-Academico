{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables transferibles: identidad UnADM, estructura argumentativa, trazabilidad y normalizacion.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo mercantil.",
    "Se refuerza que la carpeta de materia es entrada canonica de README, programa, .tex y .bib.",
    "Se mantiene alerta institucional por salidas no JSON parseable hasta verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal con postura academica propia.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Etiquetar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos o normas, evidencia, analisis propio y cierre.",
    "Alinear el producto final a la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Verificar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar espanol correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Corregir macros truncadas antes de compilar.",
    "Resolver placeholders de slug en README y programa analitico.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local confirmado de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en nodos transversales.",
    "No propagar redaccion literal ni contenido doctrinal especifico de otra materia.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Mantener reglas utiles previas sin regresion.",
    "Escalar recursivamente solo despues de validar JSON y estructura."
  ],
  "open_questions": [
    "Confirmar correccion final de nombres truncados en README.",
    "Confirmar resolucion definitiva de placeholders de slug en README y programa.",
    "Confirmar si la alerta historica de no-JSON ya puede cerrarse. [supuesto]",
    "Confirmar plantilla oficial de presentacion de la materia.",
    "Confirmar criterio institucional para year fijo vs fecha de consulta en recursos web."
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
        "Materia: Derechos de contratos mercantiles y titulos valores."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Garantizar coherencia entre consigna, desarrollo, evidencia y cierre.",
      "Sostener continuidad editorial institucional entre ciclos."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con implicacion profesional.",
      "Sin afirmaciones sin respaldo."
    ],
    "argumentative_patterns": [
      "Problema -> normas y conceptos -> evidencia -> analisis propio -> conclusion.",
      "Toda afirmacion juridica requiere fuente verificable o marca de supuesto.",
      "Priorizar analisis sobre descripcion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico delimitado",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "JSON parseable"
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
          "justification": "La identidad exige trazabilidad y cita verificable."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La aplicacion profesional requiere base juridica explicita."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion recursiva segura requiere estructura valida."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El criterio propio se fortalece con soporte documental."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        ".bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla heredada institucional: normalizar salida no estructurada antes de reutilizar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion completa de reglas repetidas.",
      "Ciclo 11: transferencia transversal solo de abstracciones estables.",
      "Ciclo 11: preservada alerta de calidad sobre JSON parseable.",
      "Ciclo 11: reforzada separacion entre evidencia y postura propia.",
      "Ciclo 11: sin regresion de reglas utiles previas."
    ]
  }
}