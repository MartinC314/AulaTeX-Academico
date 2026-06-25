{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se conservan reglas institucionales UnADM, normalizacion previa y trazabilidad de fuentes.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho hacia materia laboral.",
    "Se refuerzan ejes comunes: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene como critica la deteccion y correccion de marcadores de plantilla sin expandir.",
    "Supuesto: no hay consigna local de actividad especifica en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia destino.",
    "Usar contexto curricular verificado: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o rubrica.",
    "Tratar toda memoria heredada no parseable como provisional hasta verificacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Registrar reglas nuevas por union-dedupe sin borrar reglas utiles previas."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral.",
    "Confirmar que el producto final coincide con la consigna vigente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia entre README, programa analitico y plantilla LaTeX."
  ],
  "latex_rules": [
    "Usar plantilla .tex local como base por actividad.",
    "Completar metadatos reales de actividad antes de compilar.",
    "Mantener compilacion en español y letterpaper.",
    "Conservar macros institucionales de universidad, curso y licenciatura.",
    "Corregir nombres y rutas mal renderizados antes de canonizarlos.",
    "Resolver marcadores sin expandir tipo $(@{...}.Slug) en README y programa.",
    "Completar entornos truncados de plantilla antes de compilar.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo referencias realmente consultables y pertinentes a la actividad.",
    "No inventar referencias, jurisprudencia, doctrina ni URLs.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto metadatos faltantes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "Evitar transferir redaccion literal o contenido tematico no transversal.",
    "Preservar reglas utiles previas aunque provengan de memoria institucional.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables, sin recorte."
  ],
  "open_questions": [
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar formato de cita juridica exigido por docente.",
    "Confirmar si autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias.",
    "Supuesto: falta consigna local de actividad concreta para este ciclo."
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
        "Carpeta de materia como entrada canonica.",
        "Normalizacion obligatoria de salidas no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Asegurar coherencia entre consigna, estructura argumentativa y evidencia trazable."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Cierre con criterio juridico propio.",
      "Coherencia entre texto, citas y .bib."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer conceptos y normas.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion de salidas no parseables",
        "Trazabilidad bibliografica"
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
          "justification": "La identidad institucional exige verificabilidad y consistencia editorial."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentativa depende de una delimitacion clara del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La estructura valida evita perdida de correspondencia entre citas y fuentes."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Citas trazables sostienen control de calidad y no invencion de fuentes."
        }
      ],
      "evidence": [
        "README de materia: pauta de identidad UnADM y conclusion juridica propia.",
        "Programa analitico: ejes estables de problema, conceptos, evidencia y analisis.",
        "Archivo .bib local: claves institucionales verificables.",
        "Memoria origen: regla estable de normalizacion previa y JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se consolidan abstracciones transversales sin mover contenido tematico de Filosofia.",
      "Ciclo 17: se mantiene gate duro de JSON parseable y normalizacion previa.",
      "Ciclo 17: se refuerza deduplicacion semantica y no regresion de reglas utiles.",
      "Ciclo 17: se preserva prioridad de identidad institucional y trazabilidad bibliografica."
    ]
  }
}