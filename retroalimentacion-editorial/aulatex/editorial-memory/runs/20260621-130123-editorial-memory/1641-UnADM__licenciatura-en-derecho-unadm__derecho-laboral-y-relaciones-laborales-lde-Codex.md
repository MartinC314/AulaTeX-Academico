{
  "summary": [
    "Sincronizacion transversal aplicada entre nodos no equivalentes con enfoque conservador.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se agregan mejoras verificables: normalizacion de marcadores PowerShell sin expandir y control de supuestos.",
    "Se evita transferencia de contenido tematico especifico de Filosofia del Derecho al dominio laboral.",
    "Se mantiene compresion lossless por union-dedupe sin recorte de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia destino.",
    "Usar contexto curricular verificado del destino: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible o no confirmado.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la consigna y planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Transformar la planeacion en reporte o presentacion segun consigna."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otras materias sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de consolidar memoria.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna vigente."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Completar metadatos con datos reales y confirmados.",
    "Mantener compilacion en español y letterpaper.",
    "Conservar macros institucionales y evitar comandos no estandar sin justificacion.",
    "Compilar sin errores criticos, referencias rotas ni entornos truncados.",
    "Corregir rutas y nombres mal renderizados antes de canonizarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Centralizar fuentes en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo entradas consultables y pertinentes a la actividad.",
    "No inventar referencias, doctrina, jurisprudencia ni URLs.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto metadatos faltantes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables en saltos transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal o contenido tematico no equivalente entre materias.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar formato de cita juridica exigido por docente [supuesto].",
    "Confirmar si autor de plantilla es fijo institucional o variable por alumno [supuesto].",
    "Confirmar rubrica oficial por actividad para convertirla en checklist [supuesto].",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias [supuesto]."
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
        "Normalizacion obligatoria de salidas no estructuradas.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
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
      "Transformar planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar trazabilidad editorial y consistencia institucional en toda actividad."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin respaldo.",
      "Coherencia entre consigna, estructura y evidencia."
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
        "Normalizacion de salidas no parseables",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La argumentacion pertinente depende de una delimitacion clara del problema."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento normativo y doctrinal."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita contaminar memoria y preserva consistencia verificable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional emerge del razonamiento propio sustentado."
        }
      ],
      "evidence": [
        "README de la materia destino.",
        "Programa analitico de la materia destino.",
        "Archivo .bib local con claves institucionales.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza ADN institucional y argumentativo reusable sin arrastrar contenido tematico de Filosofia.",
      "Ciclo 15: se mantiene gate critico de JSON parseable y normalizacion previa.",
      "Ciclo 15: se consolida manejo de supuestos y fuentes provisionales.",
      "Ciclo 15: se mantiene deduplicacion lossless por union semantica."
    ]
  }
}