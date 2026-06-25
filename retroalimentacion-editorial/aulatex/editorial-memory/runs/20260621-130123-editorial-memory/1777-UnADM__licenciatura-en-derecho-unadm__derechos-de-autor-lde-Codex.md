{
  "summary": [
    "Consolidar cerebro editorial de materia para Derechos de autor con identidad UnADM.",
    "Preservar compresion lossless por union y deduplicacion sin regresion.",
    "Mantener normalizacion estructurada obligatoria antes de toda propagacion.",
    "Transferir solo abstracciones estables desde nodos transversales no equivalentes.",
    "Marcar como provisionales las herencias Codex y GPT-Pro hasta validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Soportar ubicacion curricular con malla-curricular-derecho-unadm.pdf.",
    "Supuesto: clave local LDE-S5B1 se mantiene vigente."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Conservar separacion entre reporte, presentacion y bibliografia local.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Corregir tokens de plantilla sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al archivo derechos-de-autor.bib.",
    "No asumir fuentes de otras semanas sin validacion de consigna.",
    "Verificar que cada producto corresponda a la consigna de su actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Auditar README y programa analitico por caracteres anomales y marcadores pendientes.",
    "Corregir campos pendientes como Nombre por definir antes de entrega final."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Declarar metadatos antes de \\input{template}.",
    "Mover paquetes al preambulo valido segun plantilla.",
    "No dejar comandos truncados como \\usepackage sin argumento.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni paquetes incompletos.",
    "Corregir nombres de archivo corruptos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir lateralmente solo reglas generales de identidad, estructura y calidad.",
    "No transferir redaccion literal ni contenido tematico propio de Filosofia del Derecho.",
    "Mantener bandera de normalizacion manual para herencias de ciclos iniciales.",
    "Evitar regresiones: conservar toda regla util ya validada en destino."
  ],
  "open_questions": [
    "Confirmar oficialidad de la clave LDE-S5B1 en toda la suite.",
    "Confirmar nombre de figura docente para sustituir marcador pendiente.",
    "Validar si Roma Norte, Ciudad de Mexico debe permanecer fija en portada.",
    "Confirmar orden definitivo de carga de paquetes respecto de \\input{template}.",
    "Confirmar correccion final de tokens $(@{...}.Slug) en README y programa analitico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
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
      "Transformar planeacion semanal en productos academicos trazables.",
      "Sostener calidad institucional y consistencia editorial reusable."
    ],
    "style_markers": [
      "Declarar supuestos explicitamente.",
      "Usar secciones funcionales y trazables.",
      "Mantener consistencia entre portada, desarrollo y bibliografia."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita cierre profesional util."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entrega",
          "kind": "depends_on",
          "justification": "La forma del producto debe reflejar marco institucional."
        }
      ],
      "evidence": [
        "README de Derechos de autor.",
        "programa-analitico-derechos-de-autor.md.",
        "derechos-de-autor.bib.",
        "Regla heredada valida: bloquear no-JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: deduplicacion completa de reglas repetidas.",
      "Ciclo 5: se preservan gates de JSON y normalizacion estructurada.",
      "Ciclo 5: se transfiere patron argumentativo estable sin contenido tematico no equivalente.",
      "Ciclo 5: se refuerza control de supuestos y fuentes provisionales.",
      "Ciclo 5: se mantiene ADN institucional UnADM sin regresion."
    ]
  }
}