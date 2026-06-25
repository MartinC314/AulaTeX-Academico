{
  "summary": [
    "Se consolida sincronización transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas útiles previas y se aplica deduplicación lossless sin recorte.",
    "Se transfiere solo abstracción estable: identidad UnADM, cinco ejes, calidad y normalización.",
    "Se evita traslado de contenido temático específico de Filosofía del Derecho al destino.",
    "Se mantiene alerta histórica por salidas no JSON parseables y se refuerza bloqueo preventivo.",
    "Se confirma base local verificable en README, programa analítico, plantilla LaTeX y .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redacción.",
    "Usar nombre oficial local de materia: Historia del Derecho en México [supuesto: validar acento institucional].",
    "Conservar contexto curricular local: semestre 1, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Mantener fuente curricular local: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Alinear cada entrega a cinco ejes: problema, conceptos/fuentes, producto, análisis propio, conclusión.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato al producto solicitado por la planeación semanal.",
    "Mantener coherencia entre README, programa analítico, .tex y .bib.",
    "No mezclar contenido temático de otras materias sin evidencia local verificable."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Adaptar formato a consigna: reporte, presentación o producto visual.",
    "No asumir que fuentes de semanas o materias distintas aplican a la actividad local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de reutilización recursiva.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que toda afirmación sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar placeholders y tokens sin expandir antes de compilar o citar.",
    "Aplicar unión-dedupe sin eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar plantilla local de reporte o presentación según producto solicitado.",
    "Conservar metadatos clave: documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Mantener campos institucionales; actualizar solo valores concretos por actividad.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Corregir tokens tipo $(@{...}.Slug) en README y programa antes de automatizar."
  ],
  "bibliography_rules": [
    "Usar historia-del-derecho-en-mexico.bib como repositorio local de la materia.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar solo fuentes realmente consultadas; no inventar referencias.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Incluir trazabilidad mínima: origen y fecha de consulta cuando aplique.",
    "No propagar bibliografía de Filosofía del Derecho sin consulta efectiva local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas transversales verificables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redacción entre nodos no equivalentes.",
    "No propagar datos curriculares específicos de esta materia a laterales.",
    "Mantener alerta de salidas no parseables en niveles superiores.",
    "Si falta consigna local, propagar solo abstracciones editoriales estables."
  ],
  "open_questions": [
    "Confirmar acentuación oficial institucional: México/Mexico en nombre de materia.",
    "Confirmar si LDE-S1B1 es código oficial o clave local de plantilla.",
    "Definir nombre oficial de figura docente en plantillas.",
    "Confirmar fuente operativa definitiva de consolidación [supuesto: hoy es provisional].",
    "Corregir y validar saltos anómalos en README (eporte, eferencias) [supuesto de render].",
    "Confirmar consigna concreta de primera actividad local para ajustar profundidad y formato."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante inferencias no verificadas."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Historia del Derecho en México.",
        "Semestre 1, bloque 1, obligatoria, 8 créditos.",
        "Fuente curricular: malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables y verificables.",
      "Sostener coherencia entre consigna, desarrollo, evidencia y cierre jurídico.",
      "Garantizar reutilización segura mediante estructura JSON y control de calidad."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explícito.",
      "Secciones funcionales y trazables.",
      "Citas explícitas y verificables.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo al inicio.",
      "Desarrollar conceptos y marco normativo pertinente.",
      "Contrastar evidencia con postura propia.",
      "Concluir con implicación práctica jurídica.",
      "Verificar correspondencia entre consigna y producto final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Cinco ejes editoriales",
        "Normalización JSON",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Coherencia consigna-producto",
        "Marcado de supuestos",
        "Separación entre abstracción transversal y contenido temático local"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Coherencia consigna-producto",
          "kind": "supports",
          "justification": "Los ejes ordenan problema, evidencia, análisis y cierre."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia segura entre nodos."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La validez académica depende de fuentes consultables y metadatos mínimos."
        },
        {
          "source": "Separación entre abstracción transversal y contenido temático local",
          "target": "Sincronización transversal",
          "kind": "supports",
          "justification": "Permite transferir método editorial sin contaminar contenidos de materias no equivalentes."
        }
      ],
      "evidence": [
        "README local: identidad, estructura y pauta editorial.",
        "Programa analítico local: propósito y cinco ejes de trabajo.",
        "historia-del-derecho-en-mexico.bib: base institucional verificable.",
        "Histórico de salidas no parseables: regla de bloqueo y normalización reforzada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicación integral aplicada sin regresión.",
      "Ciclo 21: se refuerza normalización JSON como gate crítico.",
      "Ciclo 21: se mantiene transferencia conservadora solo de abstracciones estables.",
      "Ciclo 21: se preserva ADN de cinco ejes y cierre jurídico con postura propia."
    ]
  }
}