{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se incorporan mejoras verificables del origen: objetivo explicito, trazabilidad de supuestos y bloqueo por no-JSON.",
    "Se evita transferencia literal de contenido de Filosofia del Derecho al dominio laboral.",
    "Se mantiene correccion de marcadores PowerShell sin expandir en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y materia Derecho laboral y relaciones laborales.",
    "Usar contexto curricular verificado: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar autor de plantilla solo si el alumno lo confirma."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social laboral.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la planeacion semanal y consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Corregir nombres de archivo mal renderizados antes de canonizarlos."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en un conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral.",
    "Confirmar que el producto final coincide con la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar o propagar.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar consistencia entre README, programa analitico y plantilla LaTeX."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Completar entornos truncados de plantilla antes de compilar.",
    "Verificar rutas y nombres reales de archivos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Marcar como supuesto cualquier metadato faltante."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Preservar reglas utiles previas aunque provengan de memoria institucional.",
    "Evitar transferir redaccion literal o contenidos tematicos no pertinentes."
  ],
  "open_questions": [
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar formato de cita juridica exigido por docente (supuesto: no definido).",
    "Confirmar si el autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias.",
    "Confirmar si hay lineamientos locales para jurisprudencia laboral en .bib."
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
        "Semestre 7, bloque 1, obligatoria, 8 creditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema juridico o social laboral.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos con fundamento juridico y aplicacion profesional.",
      "Asegurar coherencia entre consigna, estructura, evidencia y conclusion.",
      "Preservar memoria editorial reutilizable sin contaminar nodos laterales."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos etiquetados de forma explicita.",
      "Sin afirmaciones sin fuente o sin marca de supuesto.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer marco normativo/doctrinal.",
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
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion de salidas no parseables"
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
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento juridico."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar memoria defectuosa."
        }
      ],
      "evidence": [
        "README de la materia: pauta editorial e identidad UnADM.",
        "Programa analitico: ejes de trabajo y proposito editorial.",
        "Archivo .bib local con claves institucionales verificables.",
        "Supuesto: formato de cita juridica docente aun no confirmado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se refuerza regla de objetivo explicito antes del desarrollo.",
      "Ciclo 13: se consolida bloqueo por salida no JSON parseable.",
      "Ciclo 13: se mantiene deduplicacion lossless sin eliminar reglas utiles previas.",
      "Ciclo 13: se evita arrastre tematico de Filosofia del Derecho al dominio laboral."
    ]
  }
}