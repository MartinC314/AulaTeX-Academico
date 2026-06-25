{
  "summary": [
    "Sincronizacion transversal ciclo 4 aplicada con union-dedupe lossless.",
    "Se conservan reglas utiles previas y se refuerzan abstractions estables no dependientes de actividad especifica.",
    "Se mantiene identidad UnADM con enfoque juridico-laboral y trazabilidad de supuestos.",
    "Se preserva gate critico: no propagar ni reutilizar salidas no parseables sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia Derecho laboral y relaciones laborales.",
    "Usar contexto curricular verificado: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna o fuentes locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social laboral.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la consigna y planeacion semanal vigentes.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Registrar reglas por union-dedupe sin eliminar reglas vigentes utiles."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar o propagar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Usar plantilla .tex de la materia como base por actividad.",
    "Completar metadatos con datos reales y confirmados.",
    "Mantener compilacion en español y letterpaper sin errores criticos.",
    "Conservar macros institucionales de universidad, curso y licenciatura.",
    "Corregir rutas o nombres mal renderizados antes de canonizarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y referencias.",
    "Completar entorno authortable truncado antes de compilar."
  ],
  "bibliography_rules": [
    "Centralizar fuentes en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Agregar solo entradas BibTeX verificables y pertinentes a la actividad.",
    "No inventar referencias, doctrina, jurisprudencia ni URLs.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto metadatos faltantes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o detalles hiperlocales de otra materia.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar formato de cita juridica exigido por docente (supuesto: no definido).",
    "Confirmar politica de autor en plantilla: fijo institucional o variable por alumno.",
    "Confirmar rubrica oficial por actividad para convertirla en checklist.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias."
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
        "Materia: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico laboral.",
      "Conceptos y marco normativo-doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Asegurar coherencia entre consigna, estructura, evidencia y cierre juridico."
    ],
    "style_markers": [
      "Frases cortas, accionables y verificables.",
      "Supuestos explicitos cuando falte dato.",
      "Trazabilidad de citas y fuentes.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y normas aplicables.",
      "Contrastar evidencia y doctrina.",
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
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
          "justification": "Evita contaminar memoria con estructura defectuosa."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "La postura propia mejora cuando se sustenta en fuentes trazables."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes problema-conceptos-evidencia-analisis-cierre.",
        "Archivo .bib local con claves institucionales verificables.",
        "Antecedente de salidas no parseables en ciclos previos; gate de normalizacion vigente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se consolida transferencia transversal conservadora sin recorte semantico.",
      "Ciclo 4: se mantiene regla critica de JSON parseable como condicion de propagacion.",
      "Ciclo 4: se refuerza patron argumentativo reusable entre materias juridicas no equivalentes.",
      "Ciclo 4: se evita importar contenido literal de Filosofia del Derecho; solo abstracciones estables."
    ]
  }
}