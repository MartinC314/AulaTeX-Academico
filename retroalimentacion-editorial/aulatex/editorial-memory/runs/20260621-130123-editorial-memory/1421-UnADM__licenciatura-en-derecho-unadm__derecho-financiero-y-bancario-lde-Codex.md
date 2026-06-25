{
  "summary": [
    "Sincronizacion transversal consolidada con compresion lossless por union-dedupe.",
    "Se preservan reglas institucionales UnADM y se transfieren solo abstracciones estables.",
    "Se mantiene el flujo editorial reusable: problema, marco, analisis propio y conclusion juridica.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conserva contexto local de Derecho financiero y bancario sin mezclar contenido especifico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares verificados del destino: Licenciatura en Derecho, semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no confirmado en consigna, docente o grupo.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas distintas sin confirmacion de consigna.",
    "Separar claramente descripcion conceptual, analisis propio y conclusion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Validar deduplicacion semantica antes de guardar memoria.",
    "Bloquear campos obligatorios vacios sin marca de supuesto."
  ],
  "latex_rules": [
    "Mantener codificacion correcta de español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens de plantilla sin expandir en README y programa analitico.",
    "Sincronizar titulo y subtitulo del .tex con actividad real antes de entrega."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Incluir fecha de consulta en referencias web."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir lateralmente solo reglas generales independientes de actividad especifica.",
    "Evitar regresiones: no eliminar reglas utiles previas.",
    "Aplicar estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Mantener compresion lossless por union-dedupe.",
    "Si reaparece salida no estructurada, aplicar normalizacion manual."
  ],
  "open_questions": [
    "Confirmar formato de citacion obligatorio de la materia (supuesto: no definido).",
    "Confirmar nombre real de figura docente para portada.",
    "Confirmar si debe mostrarse grupo en tabla de identificacion.",
    "Confirmar numero y tipo de actividad para reemplazar 'Actividad X'.",
    "Confirmar si la localizacion institucional en portada debe actualizarse."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Trazabilidad entre README, programa, .tex y .bib.",
        "Supuestos marcados de forma explicita."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Sostener identidad institucional y rigor argumentativo.",
      "Garantizar reutilizacion segura de memoria editorial entre nodos."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Sin inventar fuentes.",
      "Sin redaccion literal heredada entre nodos no equivalentes.",
      "Consistencia entre narrativa, citas y estructura."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial breve.",
      "Delimitar objetivo.",
      "Exponer conceptos y marco normativo.",
      "Desarrollar analisis propio con evidencia.",
      "Cerrar con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Coherencia documental .tex-.bib-README-programa"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia trazable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema define el eje argumentativo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional debe derivar de respaldo comprobable."
        }
      ],
      "evidence": [
        "README local: pauta editorial e ubicacion curricular.",
        "Programa analitico local: ejes de trabajo y proposito.",
        "derecho-financiero-y-bancario.bib: fuentes institucionales base.",
        "Regla heredada valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 4: se reforzaron gates de calidad y normalizacion previa a propagacion.",
      "Ciclo 4: se transfirieron patrones argumentativos estables desde nodo transversal.",
      "Ciclo 4: se mantuvieron vacios locales como preguntas abiertas con marca de supuesto."
    ]
  }
}