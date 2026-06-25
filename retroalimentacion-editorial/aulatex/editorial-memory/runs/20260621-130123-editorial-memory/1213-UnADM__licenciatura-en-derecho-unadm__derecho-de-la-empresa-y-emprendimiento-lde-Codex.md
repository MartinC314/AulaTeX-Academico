{
  "summary": [
    "Se conserva memoria institucional UnADM y normalizacion estructurada obligatoria.",
    "Se refuerza marco transversal reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene contexto curricular local del destino: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Se preserva alerta tecnica por JSON no parseable en ciclos previos.",
    "Se preserva alerta local por tokens Slug sin expandir y nombres de archivo con artefactos en README y programa.",
    "Se evita transferir contenido doctrinal especifico de Filosofia del Derecho por no equivalencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado del destino.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar README de materia como entrada canonica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Incluir el producto exacto solicitado por la consigna semanal.",
    "Agregar fuentes especificas de actividad al .bib de la materia.",
    "No asumir fuentes de otras semanas sin confirmacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia del producto con la consigna local vigente.",
    "Revisar y normalizar respuestas no estructuradas antes de propagacion recursiva."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener consistencia de metadatos de curso y licenciatura en macros.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa.",
    "Corregir nombres de archivo con artefactos antes de referenciar o compilar.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes a la materia destino.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Mantener claves BibTeX sin duplicados.",
    "No citar fuentes no presentes en el .bib local.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar contenido doctrinal especifico entre nodos no equivalentes.",
    "Propagar primero identidad, estructura reusable y gates de calidad.",
    "Mantener estrategia progresiva y conservadora: agregar solo mejoras verificables.",
    "Exigir validacion JSON y normalizacion antes de cada salto recursivo."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades locales; confirmar formato exigido por semana.",
    "Confirmar guia de citacion juridica especifica de la materia destino.",
    "Confirmar si el autor visible de plantilla se parametriza por actividad o se mantiene fijo.",
    "Confirmar expansion final del token Slug en README y programa analitico.",
    "Confirmar cierre completo del archivo .tex de reporte local, visible como truncado."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Enfoque de transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia institucional, metodologica y tecnica en entregables LaTeX.",
      "Habilitar propagacion segura de reglas editoriales entre nodos."
    ],
    "style_markers": [
      "Frases directas y trazables.",
      "Supuestos etiquetados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo/doctrinal como soporte de la postura.",
      "Coherencia estricta entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Control de supuestos",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Consistencia entre consigna y producto",
        "Integridad bibliografica"
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
          "justification": "Sin JSON valido no hay transferencia segura entre nodos."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo documental y normativo."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de inferencias provisionales."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Consistencia entre consigna y producto",
          "kind": "supports",
          "justification": "Uniforma tono, formato y criterio academico."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Transforma datos y normas en criterio aplicado."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo .bib local con claves institucionales verificables.",
        "Memoria origen valida para abstracciones metodologicas, no para doctrina especifica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion lossless aplicada sin recorte de reglas utiles.",
      "Ciclo 18: se reforzaron gates de JSON parseable y normalizacion previa.",
      "Ciclo 18: se consolidaron patrones argumentativos transversales reutilizables.",
      "Ciclo 18: se mantuvieron alertas tecnicas locales de Slug y nombres de archivo.",
      "Ciclo 18: se preservo separacion entre reglas estables y contenido disciplinar no transferible."
    ]
  }
}