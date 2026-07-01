{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derechos de autor con identidad UnADM.",
    "Se preservan reglas validas previas y se aplica deduplicacion sin perdida.",
    "Se refuerza normalizacion estructurada: no propagar salidas no JSON parseable.",
    "Se transfieren solo abstracciones estables desde actividad origen hacia materia destino.",
    "Se mantiene pauta editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se integra contexto local verificable de README, programa analitico y derechos-de-autor.bib.",
    "Se marca como provisional toda herencia de fuentes no verificadas localmente [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Tratar herencias Codex y GPT-Pro como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre reporte, presentacion y bibliografia de materia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "No asumir fuentes de semanas o materias distintas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna vigente.",
    "Auditar README y programa analitico para detectar tokens sin expandir y nombres corruptos."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos de documento antes de cargar plantilla.",
    "Evitar comandos incompletos o paquetes sin argumento.",
    "Mover paquetes al preambulo efectivo cuando la plantilla lo exija.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Normalizar nombres de archivo segun slug canonico de la asignatura."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales institucionales o verificables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables y trazables.",
    "Registrar nuevas entradas en derechos-de-autor.bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir lateralmente solo reglas generales de identidad, estructura y calidad.",
    "Evitar transferir redaccion literal entre nodos no equivalentes.",
    "Mantener estrategia progresiva y conservadora sin regresion de reglas utiles.",
    "Conservar bandera de normalizacion manual para ciclo 1 cuando haya herencia provisional.",
    "Propagar advertencias de fuentes provisionales solo como estado transitorio."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial estable en toda la suite [supuesto].",
    "Definir nombre de figura docente para retirar marcador pendiente.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe permanecer fija en portada [supuesto].",
    "Corregir tokens $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo corruptos en README: eporte y eferencias.",
    "Validar orden definitivo entre \\input{template} y carga de paquetes en la plantilla local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Trazable y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "README como entrada canonica.",
        "Programa analitico como marco editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor.",
        "Clave local LDE-S5B1 [supuesto]."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos juridicos claros y verificables.",
      "Asegurar coherencia entre consigna, desarrollo, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos explicitamente marcados.",
      "Sin afirmaciones sin fuente.",
      "Separacion estable por bloques argumentativos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Consigna -> desarrollo alineado -> verificacion de producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Calidad bibliografica"
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
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay memoria reutilizable confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una delimitacion clara del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe derivar de fundamentos verificables."
        }
      ],
      "evidence": [
        "README de Derechos de autor: ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib: base institucional local verificable.",
        "Regla heredada estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas institucionales utiles sin eliminacion.",
      "Se deduplican variantes repetidas manteniendo contenido semantico.",
      "Se refuerza gate de JSON parseable como requisito transversal.",
      "Se incorpora marcado explicito de supuestos en datos no visibles.",
      "Se mantiene separacion entre reglas estables y vacios de contexto local."
    ]
  }
}