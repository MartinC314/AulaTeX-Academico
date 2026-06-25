{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de Filosofia del Derecho y materia de Derecho laboral.",
    "Se preservan reglas utiles previas y se deduplican por equivalencia semantica sin recorte.",
    "Se refuerzan ejes estables transferibles: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate critico: no propagar memoria no parseable sin normalizacion.",
    "Se mantiene identidad UnADM y foco juridico-laboral del destino.",
    "Supuesto: no hay consigna local de actividad especifica en este ciclo; se aplican reglas generales de materia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Vincular entregas a Licenciatura en Derecho y a la materia Derecho laboral y relaciones laborales.",
    "Usar contexto curricular verificado: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o evidencia local.",
    "Tratar como provisionales las memorias heredadas desde salidas no parseables hasta validacion local.",
    "Usar autor de plantilla solo si el alumno lo confirma."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Conservar union-dedupe lossless al agregar nuevas reglas."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral.",
    "No asumir fuentes de semanas distintas sin confirmacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar o propagar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Detectar y corregir marcadores de plantilla sin expandir antes de canonizar nombres."
  ],
  "latex_rules": [
    "Usar plantilla .tex de la materia como base por actividad.",
    "Mantener compilacion en espanol y letterpaper.",
    "Conservar macros institucionales de universidad, curso y licenciatura.",
    "Completar metadatos con datos reales y confirmados.",
    "Completar entornos truncados antes de compilar.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con acentos correctos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y referencias."
  ],
  "bibliography_rules": [
    "Centralizar bibliografia de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Agregar solo entradas BibTeX realmente consultables y pertinentes a la actividad.",
    "No inventar doctrina, normas, jurisprudencia ni URLs.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto cualquier metadato faltante no verificable."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y gates de calidad.",
    "Compartir a nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenidos tematicos no homologos.",
    "Preservar reglas utiles previas sin regresion en ciclos siguientes."
  ],
  "open_questions": [
    "Confirmar formato de citacion exigido por docente en esta materia.",
    "Confirmar si el autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar nombres canonicos finales en README tras corregir tokens sin expandir.",
    "Supuesto: falta consigna de actividad concreta en este ciclo; confirmar producto exacto."
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
        "Normalizacion obligatoria de salidas no estructuradas.",
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Sostener coherencia entre consigna, estructura, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Frases cortas y verificables.",
      "Supuestos etiquetados de forma explicita.",
      "Cierre con criterio juridico propio.",
      "Sin inventar fuentes."
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
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
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
          "justification": "Evita contaminar memoria con reglas ambiguas o defectuosas."
        }
      ],
      "evidence": [
        "README de la materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Archivo .bib local con claves institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: deduplicacion semantica completada sin eliminar reglas utiles previas.",
      "Ciclo 7: se transfiere solo abstraccion estable desde nodo transversal no equivalente.",
      "Ciclo 7: se mantiene gate de JSON parseable y normalizacion previa como regla dura."
    ]
  }
}