{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad de origen hacia materia destino.",
    "Se preservan reglas validas previas y se deduplican sin recorte semantico.",
    "Se refuerzan abstracciones estables: identidad UnADM, estructura argumentativa, calidad y normalizacion.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables.",
    "Se incorpora como pendiente local la correccion de tokens sin expandir y caracteres anómalos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local: Bases de derecho internacional publico.",
    "Usar contexto curricular verificado del destino: semestre 4, bloque 1, obligatoria, 8 creditos.",
    "Usar codigo de curso local LDE-S4B1 en metadatos.",
    "No mezclar metadatos curriculares entre materia origen y destino.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas (Codex/GPT-Pro) como trazabilidad provisional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Distinguir formato por consigna: reporte, presentacion o producto visual.",
    "Conservar separacion funcional entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y criterio propio.",
    "No extrapolar fuentes de semanas no confirmadas.",
    "Marcar faltantes de consigna o evidencia como pendientes."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Bloquear afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Verificar correspondencia entre consigna, programa analitico y producto final.",
    "Mantener auditoria de parseo JSON por ciclo."
  ],
  "latex_rules": [
    "Reutilizar plantilla .tex local sin romper identidad institucional.",
    "Mantener compatibilidad con article, spanish, letterpaper, oneside.",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "No usar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No modificar estructura base de portada sin instruccion local."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de actividad en bases-de-derecho-internacional-publico.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Validar que toda clave citada exista en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales estables y verificadas.",
    "Aplicar compresion lossless por union-dedupe; sin recorte de reglas utiles.",
    "Evitar transferencia literal de redaccion entre nodos no equivalentes.",
    "Preservar reglas utiles previas aunque cambien de categoria.",
    "No promover supuestos a regla definitiva sin evidencia local.",
    "Registrar incidencias historicas de salida no estructurada como trazabilidad."
  ],
  "open_questions": [
    "Confirmar criterio editorial final sobre publico/publico con acento en nombres visibles.",
    "Confirmar correccion local de rutas dañadas en README (eporte/eferencias).",
    "Confirmar reparacion del entorno tabular truncado en reporte-bases-de-derecho-internacional-publico.tex.",
    "Confirmar si existe rubrica especifica por actividad en esta materia.",
    "Supuesto: la nomenclatura .bib canónica permanece bases-de-derecho-internacional-publico.bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante evidencia incompleta."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino verificado: semestre 4, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Bases de derecho internacional publico.",
        "No mezclar contexto curricular con materias origen."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos juridicamente solidos.",
      "Garantizar coherencia entre consigna, evidencia y conclusion.",
      "Sostener memoria editorial persistente con trazabilidad verificable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin redundancia.",
      "Supuestos etiquetados.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> posicion propia.",
      "Consigna -> desarrollo alineado -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Consigna de actividad",
        "Estructura argumentativa juridica",
        "Evidencia verificable",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Consistencia cita-bibliografia"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Consigna de actividad",
          "target": "Estructura argumentativa juridica",
          "kind": "depends_on",
          "justification": "El producto define forma y alcance del desarrollo."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida requiere respaldo documental."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo correcto no hay transferencia segura."
        },
        {
          "source": "Consistencia cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita referencias rotas y afirmaciones sin fuente."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "develops",
          "justification": "La identidad se expresa en forma, tono y rigor de entrega."
        }
      ],
      "evidence": [
        "README destino: ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Bibliografia local destino: claves institucionales base.",
        "Regla heredada estable: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se refuerza transferencia transversal de abstracciones estables.",
      "Ciclo 16: se mantiene estrategia progresiva y conservadora sin regresion.",
      "Ciclo 16: se deduplican reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 16: se preserva incidencia historica de salidas no estructuradas.",
      "Ciclo 16: se agrega pendiente local verificable sobre tokens Slug y rutas anómalas."
    ]
  }
}