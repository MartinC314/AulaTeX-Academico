{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y control de supuestos.",
    "Se refuerza marco reusable: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "No se transfiere contenido doctrinal especifico de Filosofia del Derecho al destino por no equivalencia disciplinar.",
    "Se mantiene alerta activa por tokens Slug sin expandir y artefactos en nombres de archivo del README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial local de la materia en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en consigna o no confirmado por archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Usar la carpeta de materia y README como entrada canonica.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar cada entrega en: problema, conceptos, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener correspondencia entre .tex, presentacion y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local.",
    "Evitar asumir fuentes de otras semanas o materias sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion por union-dedupe.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de generar entregables."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Actualizar documenttitle y documentsubtitle por actividad concreta.",
    "Resolver tokens $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con artefactos de salto antes de compilar.",
    "Verificar cierre completo de entornos LaTeX en el reporte local [supuesto: archivo truncado]."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes a la materia destino.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No trasladar automaticamente bibliografia doctrinal de Filosofia del Derecho al destino transversal."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion de JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar contenido tematico local como regla institucional global.",
    "Mantener normalizacion manual obligatoria en ciclos con antecedentes de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna y rubrica de la primera actividad real de la materia destino.",
    "Confirmar si documentauthor debe parametrizarse por actividad o mantenerse fijo.",
    "Confirmar expansion final del Slug en README y programa analitico.",
    "Confirmar si el .tex local esta truncado en repositorio o solo en captura.",
    "Confirmar criterio bibliografico para year=2026 en unadmSitioWeb (ano de publicacion vs consulta)."
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
      "Problema juridico",
      "Conceptos pertinentes",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible",
      "Control de supuestos",
      "Normalizacion estructurada previa a propagacion"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos y verificables.",
      "Asegurar coherencia entre identidad institucional, argumentacion juridica y evidencia.",
      "Permitir propagacion segura entre nodos sin perder reglas utiles."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Supuestos etiquetados de forma explicita.",
      "Sin afirmaciones sin fuente.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo/doctrinal como soporte del criterio personal.",
      "Consistencia estricta entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Control de supuestos",
        "Evidencia verificable",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Propagacion recursiva segura"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige sustento documental y normativo."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Evita mezclar inferencias con hechos no confirmados."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion recursiva segura",
          "kind": "develops",
          "justification": "Estandariza tono y forma entre nodos transversales."
        }
      ],
      "evidence": [
        "README local: ubicacion curricular y pauta editorial.",
        "Programa analitico local: ejes de trabajo y proposito.",
        "Archivo .bib local: claves institucionales base.",
        "Memoria origen: regla estable de normalizacion y calidad JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se consolida transferencia transversal por abstracciones estables.",
      "Ciclo 12: se mantiene regla de no propagar contenido doctrinal especifico entre materias no equivalentes.",
      "Ciclo 12: se refuerzan gates de JSON, supuestos y trazabilidad bibliografica.",
      "Ciclo 12: se conserva alerta tecnica por Slug sin expandir y artefactos en nombres de archivo."
    ]
  }
}