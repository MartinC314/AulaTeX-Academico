{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Derecho financiero y bancario.",
    "Se preservan reglas institucionales utiles previas sin regresion y con deduplicacion semantica.",
    "Se refuerza nucleo estable: identidad UnADM, estructura reusable, evidencia verificable, analisis propio y conclusion juridica transferible.",
    "Se mantiene gate critico: bloquear propagacion si la salida no es JSON parseable.",
    "Se conserva normalizacion obligatoria de respuestas no estructuradas antes de reutilizar.",
    "Se mantienen abiertos los vacios locales con marca de supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar programa academico Licenciatura en Derecho y datos curriculares locales verificados.",
    "Mantener materia destino: Derecho financiero y bancario, semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no confirmado en consigna o plantilla.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas distintas sin confirmacion local.",
    "Adaptar reporte o presentacion segun consigna vigente."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a contexto local o memoria heredada.",
    "Validar deduplicacion semantica antes de guardar.",
    "Bloquear guardado si hay afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Reemplazar tokens de plantilla sin expandir en README y programa analitico.",
    "Sincronizar titulo, subtitulo y materia con actividad real antes de entrega.",
    "Completar campos pendientes como Figura docente o marcar [Supuesto]."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y normativas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y deduplicadas.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No transferir redaccion literal de actividades origen.",
    "Aplicar normalizacion manual si reaparece salida no estructurada en ciclos previos.",
    "Conservar politica de no regresion en cada ciclo."
  ],
  "open_questions": [
    "[Supuesto] Confirmar nombre real de figura docente.",
    "[Supuesto] Confirmar formato de citacion obligatorio de la materia.",
    "[Supuesto] Confirmar si grupo debe aparecer en tabla de identificacion.",
    "[Supuesto] Confirmar planeacion semanal vigente antes de bajar a actividades.",
    "[Supuesto] Confirmar si localizacion de portada se mantiene por lineamiento oficial."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Trazabilidad documental entre README, programa, .tex y .bib."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Fuente curricular institucional: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundamentados y utiles.",
      "Estandarizar calidad editorial sin perder contexto local de cada actividad."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos etiquetados de forma explicita.",
      "Sin fuentes inventadas.",
      "Consistencia entre narrativa, citas y estructura."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo.",
      "Analisis propio con evidencia.",
      "Cierre con implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Consistencia .tex-.bib"
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
          "justification": "La identidad exige trazabilidad y evidencia verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional debe derivar de respaldo comprobable."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema define el eje argumentativo."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial y ubicacion curricular.",
        "Programa analitico con proposito y ejes de trabajo.",
        "Archivo derecho-financiero-y-bancario.bib con fuentes institucionales base.",
        "Regla heredada valida: revisar y normalizar respuestas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: deduplicacion semantica aplicada sin recorte de reglas utiles.",
      "Ciclo 17: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 17: se mantiene gate de JSON parseable como condicion de propagacion.",
      "Ciclo 17: se preserva politica de supuestos explicitos para vacios locales."
    ]
  }
}