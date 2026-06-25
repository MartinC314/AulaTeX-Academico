{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se mantiene deduplicacion lossless y se eliminan redundancias literales sin perder contenido util.",
    "Se evita transferir contenido tematico propio de Filosofia del Derecho al dominio mercantil.",
    "Se refuerza la normalizacion obligatoria: solo memoria JSON parseable y trazable.",
    "Se confirma contexto local del destino: semestre 6, bloque 2, obligatoria, 8 creditos y .bib local existente.",
    "Supuesto: persiste alerta historica de salidas no estructuradas hasta evidencia de cierre."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal con claridad argumentativa.",
    "Exigir postura academica propia en el cierre.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Corregir placeholders de slug y nombres truncados en README y programa."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Comprobar que el producto entregado coincide con la consigna.",
    "No asumir fuentes de otras semanas o materias sin verificacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar ausencia de fuentes inventadas.",
    "Evitar regresion de reglas utiles previamente consolidadas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Conservar nomenclatura consistente de archivos de reporte y presentacion.",
    "Corregir macros truncadas o incompletas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres de archivo declarados en README antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local confirmado de la materia destino.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre materias distintas.",
    "No propagar redaccion literal ni contenido tematico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar union-dedupe lossless en cada ciclo de fusion.",
    "Mantener alerta heredada de normalizacion manual para ciclos historicos reportados.",
    "Propagar recursivamente solo despues de validar JSON y estructura."
  ],
  "open_questions": [
    "Confirmar cierre de la incidencia historica de salida no JSON parseable en flujos actuales.",
    "Confirmar plantilla oficial de presentacion para esta materia.",
    "Confirmar correccion definitiva de nombres truncados en README.",
    "Confirmar resolucion completa de placeholders de slug en README y programa.",
    "Supuesto: falta inventario local de actividades y rubricas especificas por semana."
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
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Asegurar coherencia entre consigna, argumentacion, evidencia y cierre profesional."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos etiquetados cuando falte evidencia.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> contraste de evidencia -> postura propia -> conclusion.",
      "Cada afirmacion juridica debe tener respaldo verificable.",
      "Priorizar analisis sobre descripcion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "JSON parseable",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
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
          "justification": "La propagacion recursiva requiere estructura valida."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis pertinente exige delimitacion previa del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "El cierre profesional necesita base juridica explicita."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia gana validez cuando contrasta evidencia."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes: problema, conceptos, producto, analisis, conclusion.",
        ".bib local con fuentes institucionales base.",
        "Regla heredada de bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 13: se preservan todas las reglas utiles previas sin recorte semantico.",
      "Ciclo 13: se agrega guardrail transversal para no transferir contenido tematico entre materias no equivalentes.",
      "Ciclo 13: se refuerza correccion de placeholders y nombres truncados como deuda tecnica editorial.",
      "Ciclo 13: se mantiene estado provisional de fuentes heredadas no verificadas."
    ]
  }
}