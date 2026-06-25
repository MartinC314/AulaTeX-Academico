{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables reutilizables: identidad UnADM, estructura argumentativa y control de calidad.",
    "Se mantiene deduplicacion lossless sin recorte de reglas utiles previas.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al dominio mercantil.",
    "Se refuerza que la carpeta de materia es punto canonico para README, programa, .tex y .bib.",
    "Se mantiene alerta institucional: no propagar salidas no JSON parseables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal, claro y argumentativo.",
    "Cerrar con postura academica propia y criterio juridico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar carpeta de materia como entrada canonica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Mantener consistencia entre consigna, desarrollo y conclusion.",
    "Mantener consistencia entre README, programa, .tex y .bib."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, argumentos y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se inventen fuentes.",
    "Evitar regresion de reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar espanol correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Corregir macros truncadas antes de compilar.",
    "Resolver placeholders de slug en README y programa.",
    "Corregir nombres de archivos truncados en README.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "No usar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar derechos-de-contratos-mercantiles-y-titulos-valores.bib como .bib local confirmado.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Agregar al .bib solo fuentes realmente consultables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenidos tematicos de otra asignatura.",
    "Mantener estrategia progresiva y conservadora en cada ciclo.",
    "Aplicar union-dedupe lossless en cada fusion.",
    "Mantener alerta heredada de normalizacion manual en ciclos previos cuando aplique."
  ],
  "open_questions": [
    "Confirmar si la incidencia de salidas no JSON parseables ya esta cerrada en flujo actual.",
    "Confirmar plantilla oficial de presentacion para esta materia.",
    "Confirmar resolucion total de placeholders de slug en README y programa.",
    "Confirmar correccion final de nombres truncados de archivos en README.",
    "Supuesto: year 2026 en unadmSitioWeb se conserva como dato de registro y no de vigencia normativa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro y argumentativo."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar."
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
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Trazabilidad editorial y tecnica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos y verificables.",
      "Asegurar coherencia entre consigna, evidencia y conclusion profesional.",
      "Sostener memoria editorial estable para propagacion segura."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis propio -> conclusion.",
      "Toda afirmacion juridica requiere respaldo verificable.",
      "Analisis predomina sobre descripcion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "JSON parseable",
        "Normalizacion estructurada",
        "Problema juridico delimitado",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Consistencia README-programa-tex-bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "El cierre profesional requiere fundamento juridico explicito."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad reduce afirmaciones infundadas."
        },
        {
          "source": "Consistencia README-programa-tex-bib",
          "target": "Normalizacion estructurada",
          "kind": "develops",
          "justification": "La coherencia documental estabiliza el nodo editorial."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo y proposito.",
        ".bib local con entradas institucionales confirmadas.",
        "Regla heredada activa: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se transfiere solo abstraccion estable transversal.",
      "Ciclo 18: se preservan gates tecnicos y academicos sin regresion.",
      "Ciclo 18: se mantiene estrategia conservadora, sin arrastre tematico de Filosofia del Derecho.",
      "Ciclo 18: se refuerza deduplicacion lossless por union."
    ]
  }
}