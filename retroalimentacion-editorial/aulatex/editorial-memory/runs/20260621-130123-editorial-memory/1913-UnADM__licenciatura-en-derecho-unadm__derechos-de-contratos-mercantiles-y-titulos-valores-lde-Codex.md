{
  "summary": [
    "Se mantiene memoria transversal con identidad UnADM para la materia destino.",
    "Se preserva compresion lossless por union y deduplicacion sin eliminar reglas utiles.",
    "Se refuerzan ejes estables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene gate critico: bloquear propagacion si la salida no es JSON parseable.",
    "Se conserva estrategia conservadora: no transferir contenido tematico especifico de Filosofia del Derecho.",
    "Se confirma contexto local verificable: semestre 6, bloque 2, obligatoria, 8 creditos y .bib local existente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono juridico-formal, claro y argumentativo.",
    "Cerrar con postura academica propia y criterio juridico.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Etiquetar como provisionales las fuentes heredadas no verificadas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Incluir en el cierre transferencia a practica profesional."
  ],
  "activity_rules": [
    "Contextualizar cada actividad con problema concreto y delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir evidencia citada de interpretacion propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes o contenidos de semanas no confirmadas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Comprobar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no se inventen fuentes.",
    "Evitar regresion de reglas utiles previas."
  ],
  "latex_rules": [
    "Usar español con acentos consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir nombres truncados en README antes de referenciar archivos.",
    "Resolver placeholders de slug en README y programa analitico.",
    "Corregir macros truncadas en plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-contratos-mercantiles-y-titulos-valores.bib como archivo local canonico.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar en .bib fuentes especificas de cada actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas normalizadas y parseables.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico local no transversal.",
    "Mantener alerta heredada de normalizacion manual en ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar correccion final de nombres truncados en README.",
    "Confirmar resolucion definitiva de placeholders de slug en README y programa.",
    "Confirmar plantilla oficial de presentacion para esta materia.",
    "Supuesto: persiste alerta historica por salidas no JSON parseables; validar estado actual.",
    "Confirmar si year en unadmSitioWeb se mantiene o se usa solo fecha de consulta."
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
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica profesional.",
      "Sostener una memoria editorial estable, reusable y sin regresiones."
    ],
    "style_markers": [
      "Apertura breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con implicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> evidencia -> analisis propio -> conclusion.",
      "Cada afirmacion juridica debe tener respaldo verificable.",
      "Diferenciar descripcion de argumentacion."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
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
          "justification": "La identidad exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis pertinente requiere problema delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La transferencia profesional requiere fundamento juridico."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README de materia con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes de trabajo y proposito.",
        ".bib local con unadmSitioWeb y unadmMallaDerecho2024."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicacion completa aplicada sin recorte semantico.",
      "Ciclo 17: se conservaron gates criticos heredados de calidad.",
      "Ciclo 17: se reforzo transferencia transversal por abstracciones estables.",
      "Ciclo 17: se mantuvo separacion entre reglas editoriales y contenido tematico local."
    ]
  }
}