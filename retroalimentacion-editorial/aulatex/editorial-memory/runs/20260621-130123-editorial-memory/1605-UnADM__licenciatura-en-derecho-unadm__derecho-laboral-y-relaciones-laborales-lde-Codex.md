{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino sin traslado literal.",
    "Se preservan reglas utiles vigentes del destino y se refuerzan abstracciones estables: identidad, estructura, calidad y trazabilidad.",
    "Se mantiene bloqueo de propagacion para salidas no parseables y normalizacion obligatoria previa.",
    "Se confirma contexto curricular local del destino: UnADM, Licenciatura en Derecho, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Se refuerza deduplicacion lossless por union semantica en frases cortas accionables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Anclar cada entrega a Licenciatura en Derecho y a la materia Derecho laboral y relaciones laborales.",
    "Usar contexto curricular verificado del README local: semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o no confirmado por el alumno.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social laboral.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la consigna y planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables y cita explicita.",
    "Incluir postura argumentada propia; evitar entrega solo descriptiva.",
    "Vincular conceptos laborales con aplicacion profesional comprobable.",
    "No trasladar contenido de otras materias sin validar pertinencia laboral y curricular local.",
    "Verificar que el tipo de producto solicitado coincida con la consigna vigente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar o propagar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre README, programa analitico, plantilla LaTeX y producto.",
    "Validar trazabilidad entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base por actividad.",
    "Completar metadatos reales de actividad antes de compilar.",
    "Mantener compilacion en español y letterpaper.",
    "Conservar macros institucionales de universidad, curso y licenciatura.",
    "Corregir marcadores sin expandir tipo $(@{...}.Slug) en nombres de archivo y referencias.",
    "Corregir nombres mal renderizados en README antes de canonizar rutas.",
    "Completar entornos truncados de plantilla antes de compilar.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Centralizar bibliografia en derecho-laboral-y-relaciones-laborales.bib.",
    "Conservar y reutilizar claves institucionales verificadas: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar solo entradas BibTeX verificables y pertinentes a la actividad.",
    "No inventar referencias, jurisprudencia, normas ni URLs.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Marcar como supuesto metadatos faltantes cuando no puedan verificarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura completa.",
    "Transferir entre nodos no equivalentes solo abstracciones estables; no redaccion literal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Preservar reglas utiles previas del destino sin regresion.",
    "Aplicar union-dedupe semantica por frases cortas y accionables.",
    "Si falta contexto local en nodo vecino, crear cerebro minimo y dejar vacios como preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar rubrica oficial por actividad para convertirla en checklist operativo.",
    "Confirmar formato de cita juridica exigido por docente (supuesto: no definido en fuentes visibles).",
    "Confirmar si el autor de plantilla es variable por alumno en todas las actividades.",
    "Confirmar nombres canonicos finales de artefactos y carpeta de referencias tras corregir render roto en README.",
    "Confirmar si existe bibliografia obligatoria adicional por unidad para esta materia."
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
        "Carpeta de materia como entrada canonica.",
        "Normalizacion obligatoria de salidas no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social laboral.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar coherencia entre consigna, estructura argumentativa y soporte bibliografico."
    ],
    "style_markers": [
      "Frases cortas y verificables.",
      "Supuestos marcados de forma explicita.",
      "Sin afirmaciones sin respaldo.",
      "Cierre con aplicacion juridica profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo y marco conceptual-normativo.",
      "Contrastar evidencia y doctrina.",
      "Sostener postura propia.",
      "Concluir con transferencia profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion de salidas no parseables",
        "Propagacion recursiva segura"
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
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Evita contaminar nodos aguas abajo con memoria defectuosa."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica exige respaldo comprobable."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bibliografia local .bib: claves institucionales verificables.",
        "Historial de ciclos: regla persistente de normalizar salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se refuerza transferencia transversal por abstracciones estables sin mover contenido tematico de Filosofia del Derecho.",
      "Ciclo 6: se conserva regla critica de bloqueo por JSON no parseable y normalizacion previa.",
      "Ciclo 6: se consolidan patrones argumentativos reutilizables en materia laboral.",
      "Ciclo 6: se mantiene compresion lossless por deduplicacion semantica sin recorte util."
    ]
  }
}