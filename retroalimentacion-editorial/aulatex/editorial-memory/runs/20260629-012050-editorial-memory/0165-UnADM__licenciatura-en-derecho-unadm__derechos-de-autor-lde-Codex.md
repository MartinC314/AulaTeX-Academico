{
  "summary": [
    "Se sincroniza memoria transversal hacia Derechos de autor con estrategia conservadora.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se refuerza normalizacion estructurada antes de toda propagacion recursiva.",
    "Se mantiene ADN editorial UnADM: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se prioriza abstraccion estable; no se transfiere redaccion literal de Filosofia del Derecho.",
    "Se mantiene estado provisional de herencias no verificadas (Codex y GPT-Pro) hasta confirmacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura y README como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener separacion entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local de la materia.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir marcadores de plantilla y nombres de archivo corruptos antes de publicar.",
    "Mantener normalizacion manual para contenido heredado de ciclos previos."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Declarar metadatos del documento antes de cargar plantilla.",
    "Evitar paquetes incompletos o comandos truncados en el preambulo.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo materiales verificables.",
    "Priorizar fuentes institucionales UnADM y normativas aplicables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Incluir fecha de consulta en fuentes web."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar datos personales ni redaccion literal entre materias.",
    "Mantener advertencias sobre herencia provisional como estado de riesgo controlado.",
    "Aplicar union-dedupe en cada ciclo para compresion lossless sin recorte."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial o solo etiqueta local. [supuesto]",
    "Definir nombre de figura docente en plantilla de reporte.",
    "Validar ubicacion institucional fija en portada (Roma Norte, Ciudad de Mexico). [supuesto]",
    "Confirmar orden correcto de paquetes respecto a la plantilla en LaTeX local.",
    "Verificar si se mantiene o se retira definitivamente la herencia provisional Codex/GPT-Pro."
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
        "Clave local LDE-S5B1. [supuesto]"
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar coherencia entre consigna, desarrollo, evidencia y cierre.",
      "Sostener calidad institucional en produccion LaTeX de la materia."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Cierre con postura juridica propia."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Consigna -> producto solicitado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Calidad bibliografica",
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
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La memoria solo se propaga cuando es parseable y estructurada."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad exige trazabilidad, citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis nace de un problema delimitado y no de resumen aislado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida depende de fundamentos verificables."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib: base institucional verificable.",
        "Regla vigente: bloquear salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se deduplican reglas repetidas y se preserva contenido valido.",
      "Ciclo 2: se refuerzan gates de calidad y normalizacion previa a propagacion.",
      "Ciclo 2: se mantiene transferencia por abstracciones estables entre nodos transversales.",
      "Ciclo 2: se conservan riesgos abiertos de herencia provisional para validacion local."
    ]
  }
}