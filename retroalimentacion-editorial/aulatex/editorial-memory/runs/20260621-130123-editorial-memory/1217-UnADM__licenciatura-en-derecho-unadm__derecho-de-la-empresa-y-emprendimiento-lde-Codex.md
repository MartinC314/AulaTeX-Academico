{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas utiles previas y se deduplican sin recorte.",
    "Se transfiere solo marco editorial estable: identidad, estructura, calidad y trazabilidad.",
    "Se mantiene alerta por tokens Slug sin expandir y nombres de archivo con artefactos.",
    "Se evita transferir doctrina especifica de Filosofia del Derecho al nodo de empresa.",
    "Se refuerza control de supuestos y bloqueo por salida no JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de materia en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Conservar correspondencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local.",
    "No asumir fuentes de otras semanas o materias como obligatorias locales.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Verificar que README liste archivos reales y rutas existentes.",
    "Aplicar normalizacion manual cuando haya salida no estructurada heredada."
  ],
  "latex_rules": [
    "Usar espanol con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir artefactos de nombre de archivo antes de compilar.",
    "Confirmar cierre completo de entornos truncados en .tex local [supuesto]."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Mantener sin duplicados las claves base locales.",
    "No citar fuentes no registradas en el .bib local.",
    "Etiquetar como supuesto cualquier dato bibliografico incierto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre materias no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar contenido doctrinal especifico de Filosofia del Derecho a Empresa y Emprendimiento.",
    "Propagar alertas tecnicas de tokens Slug y archivos con artefactos a nodos con plantillas similares.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Confirmar consigna local de la primera actividad de la materia destino.",
    "Confirmar si documentauthor debe parametrizarse por actividad.",
    "Confirmar valor final del Slug en README y programa analitico.",
    "Confirmar si el .tex local esta truncado en repositorio o en captura [supuesto].",
    "Confirmar criterio bibliografico de year=2026 en unadmSitioWeb."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Enfoque aplicado con transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Control explicito de supuestos."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos verificables.",
      "Asegurar calidad formal, argumentativa y tecnica en LaTeX.",
      "Preservar continuidad editorial sin mezclar contenidos disciplinares no equivalentes."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Sin afirmaciones sin fuente.",
      "Supuestos marcados de forma explicita.",
      "Cierre con aplicacion practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo como soporte del criterio personal.",
      "Consistencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Control de supuestos",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Separacion entre reglas editoriales y contenido doctrinal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "El cierre profesional requiere respaldo documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Distingue hechos confirmados de inferencias."
        },
        {
          "source": "Separacion entre reglas editoriales y contenido doctrinal",
          "target": "Sincronizacion transversal",
          "kind": "supports",
          "justification": "Permite transferir metodo sin contaminar contexto disciplinar."
        }
      ],
      "evidence": [
        "README local con ubicacion curricular y pauta editorial.",
        "Programa analitico local con ejes de trabajo reutilizables.",
        "Bib local con claves institucionales verificables.",
        "Historial con incidencias de salida no estructurada y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion lossless aplicada sin regresion.",
      "Ciclo 19: se refuerza bloqueo por JSON no parseable.",
      "Ciclo 19: se mantiene regla de no inventar fuentes.",
      "Ciclo 19: se mantiene alerta de tokens Slug sin expandir.",
      "Ciclo 19: se transfiere marco argumentativo reusable y no doctrina especifica."
    ]
  }
}