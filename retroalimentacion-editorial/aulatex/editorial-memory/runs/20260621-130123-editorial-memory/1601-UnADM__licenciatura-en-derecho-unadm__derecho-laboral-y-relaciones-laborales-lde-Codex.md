{
  "summary": [
    "Sincronizacion transversal consolidada entre actividad origen y materia destino con estrategia conservadora.",
    "Se preservan reglas institucionales estables: identidad UnADM, normalizacion estructurada y trazabilidad de fuentes.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables.",
    "Se conserva deduplicacion lossless por union semantica sin recorte."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia destino.",
    "Usar contexto curricular verificado del destino: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o plantilla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social pertinente.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto solicitado con la planeacion semanal vigente.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener estructura reusable y no transferir redaccion literal entre nodos."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion juridica verificable del curso.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas o materias sin validar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear consolidacion o propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar ausencia de afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre consigna, producto y metadatos."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas y nombres mal renderizados antes de canonizarlos.",
    "Resolver marcadores de plantilla sin expandir tipo $(@{...}.Slug).",
    "Marcar como supuesto el autor de plantilla si no esta confirmado."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Centralizar bibliografia local en el .bib canonico de la materia.",
    "Registrar en .bib las fuentes especificas de cada actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir contenido tematico especifico de Filosofia del Derecho al destino laboral.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar formato de citacion juridica exigido por docente [Supuesto: no definido en archivos locales].",
    "Confirmar si autor de plantilla es fijo institucional o variable por alumno.",
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias tras corregir marcadores."
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
        "Normalizacion obligatoria de salidas no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas o doctrina pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica profesional.",
      "Sostener consistencia editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Coherencia entre consigna, evidencia y cierre.",
      "Sin redaccion literal heredada entre nodos transversales."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
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
          "target": "Integridad academica con citas verificables",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento juridico verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Evita contaminar nodos con memoria no parseable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La postura se fortalece al contrastar fuentes trazables."
        }
      ],
      "evidence": [
        "README de la materia destino: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico destino: proposito y ejes de trabajo.",
        "Regla heredada estable: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se transfiere solo abstraccion estable desde Filosofia del Derecho a Derecho laboral.",
      "Ciclo 5: se preserva regla critica de normalizacion previa a propagacion.",
      "Ciclo 5: se refuerza patron argumentativo comun sin importar tema de materia.",
      "Ciclo 5: se evita traslado de contenido doctrinal especifico no transversal."
    ]
  }
}