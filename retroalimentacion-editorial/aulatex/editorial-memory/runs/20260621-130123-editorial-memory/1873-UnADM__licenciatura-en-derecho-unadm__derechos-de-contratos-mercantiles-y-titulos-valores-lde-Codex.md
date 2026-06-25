{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa juridica y control de calidad por JSON parseable.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al dominio mercantil.",
    "Se refuerza normalizacion de artefactos y trazabilidad entre README, programa, .tex y .bib.",
    "Supuesto: persiste alerta institucional por salidas no estructuradas hasta evidencia de resolucion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Usar tono juridico-formal con claridad argumentativa.",
    "Cerrar con postura academica propia y criterio juridico.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre consigna, desarrollo y conclusion.",
    "Usar la carpeta de materia como entrada canonica para README, programa, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, argumentos y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Comprobar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresion de reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar espanol correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres truncados en README antes de referenciar archivos.",
    "Resolver placeholders de slug en README y programa analitico.",
    "Revisar y completar macros truncadas de plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Agregar fecha de consulta en recursos web."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico de otra asignatura.",
    "Aplicar compresion lossless por union y deduplicacion.",
    "Mantener alerta de normalizacion manual para ciclos heredados 1 a 6.",
    "Promover refuerzo progresivo sin borrar reglas previas utiles."
  ],
  "open_questions": [
    "Confirmar si la incidencia de salida no JSON parseable ya fue resuelta en flujos actuales.",
    "Confirmar correccion definitiva de nombres truncados en README.",
    "Confirmar resolucion definitiva de placeholders de slug en README y programa.",
    "Confirmar plantilla oficial de presentacion para esta materia.",
    "Supuesto: la macro truncada en plantilla .tex aun requiere cierre y validacion.",
    "Confirmar politica de year fijo vs fecha de consulta para sitio institucional UnADM."
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
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Sostener continuidad editorial institucional entre actividades y materia.",
      "Garantizar trazabilidad, calidad tecnica y coherencia argumentativa."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados cuando falte evidencia.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion juridica siempre con respaldo verificable.",
      "Separar descripcion de valoracion critica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
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
          "justification": "La propagacion recursiva segura exige estructura valida."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La postura propia se fortalece con soporte comprobable."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo reutilizables.",
        ".bib local existente con fuentes institucionales UnADM.",
        "Historial de incidencias de salida no estructurada en memoria heredada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion completa de reglas repetidas en tono, estructura y calidad.",
      "Ciclo 7: transferencia transversal limitada a abstracciones editoriales estables.",
      "Ciclo 7: preservacion de controles de JSON parseable y normalizacion previa.",
      "Ciclo 7: refuerzo de grafo conceptual comun sin contaminar dominio tematico mercantil.",
      "Ciclo 7: mantenimiento de supuestos abiertos para vacios locales verificables."
    ]
  }
}