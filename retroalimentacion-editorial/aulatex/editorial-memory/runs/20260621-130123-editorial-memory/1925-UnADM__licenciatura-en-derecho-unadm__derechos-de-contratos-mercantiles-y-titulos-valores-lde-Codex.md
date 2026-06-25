{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas estables reutilizables: identidad UnADM, estructura argumentativa y control de calidad.",
    "Se evita transferir contenido tematico propio de Filosofia del Derecho al curso mercantil.",
    "Se refuerza normalizacion obligatoria: solo memoria estructurada y JSON parseable.",
    "Se mantiene contexto local verificado del destino: semestre 6, bloque 2, obligatoria, 8 creditos y .bib local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal, claro y argumentativo.",
    "Cerrar con postura academica propia y criterio juridico.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar la carpeta de materia como entrada canonica para README, programa, .tex y .bib.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave y marco normativo o doctrinal.",
    "Distinguir evidencia citada de analisis propio.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, argumentos y cierre.",
    "No asumir bibliografia de otras semanas o asignaturas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresion de reglas utiles heredadas."
  ],
  "latex_rules": [
    "Usar espanol correcto con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres truncados y tokens de slug sin expandir en README y programa.",
    "Completar y validar macros incompletas de plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente consultables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No propagar redaccion literal ni contenido doctrinal especifico del origen.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener compresion lossless por union y deduplicacion.",
    "Mantener alerta heredada de normalizacion manual en ciclos tempranos como antecedente institucional."
  ],
  "open_questions": [
    "Confirmar si ya se resolvieron todos los tokens de slug en README y programa.",
    "Confirmar correccion completa de nombres truncados en README.",
    "Confirmar plantilla oficial de presentacion para esta materia.",
    "Confirmar si la alerta historica de salida no JSON parseable puede cerrarse.",
    "Supuesto: la macro de plantilla reportada como incompleta sigue pendiente de cierre tecnico."
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
        "Asignatura mercantil con enfoque profesional."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables evaluables con rigor juridico.",
      "Asegurar coherencia entre consigna, fuentes, analisis y cierre profesional."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> postura propia -> conclusion.",
      "Afirmacion juridica siempre con respaldo verificable.",
      "Separar descripcion de interpretacion."
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
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional debe estar fundada juridicamente."
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
          "justification": "La postura propia se fortalece con soporte documental."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        ".bib local confirmado: derechos-de-contratos-mercantiles-y-titulos-valores.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicacion completa de reglas repetidas.",
      "Ciclo 20: preservacion de gates criticos de JSON y normalizacion.",
      "Ciclo 20: refuerzo de patron argumentativo transversal sin contaminar contenido tematico.",
      "Ciclo 20: mantenimiento de fuentes heredadas como provisionales."
    ]
  }
}