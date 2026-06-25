{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura reusable, gates de calidad y patron argumentativo.",
    "Se mantiene compresion lossless por union-deduplicacion.",
    "Se preserva regla de bloqueo ante salida no JSON parseable.",
    "Se refuerza normalizacion de rutas y tokens slug sin expandir en README y programa analitico.",
    "Supuesto: no existe consigna local de actividad especifica en este ciclo."
  ],
  "identity_rules": [
    "Conservar identidad UnADM en tono, portada y metadatos.",
    "Mantener contexto curricular local: Derecho fiscal y tributario, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear el producto final con planeacion semanal y consigna.",
    "Corregir rutas truncadas o rotas en README antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Vincular analisis fiscal-tributario con aplicacion profesional concreta."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Cerrar correctamente entornos tabular y documento antes de compilar.",
    "Completar campos pendientes de plantilla antes de entrega."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir a nodos no equivalentes solo reglas editoriales generales, no contenido tematico literal.",
    "Evitar transferir bibliografia tematica de Filosofia del Derecho como obligatoria en Fiscal.",
    "Mantener union-dedupe como metodo de compresion en ciclos siguientes.",
    "Priorizar mejoras verificables del contexto local antes de lateralizar."
  ],
  "open_questions": [
    "Confirmar consigna local de la siguiente actividad para ajustar tipo de producto.",
    "Confirmar formato de citacion requerido por la materia.",
    "Confirmar nombre de figura docente en plantilla.",
    "Confirmar si autor y matricula deben permanecer en versiones compartidas.",
    "Resolver definitivamente rutas truncadas en README (reporte y referencias)."
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
        "Supuestos etiquetados y trazables.",
        "Fuentes heredadas tratadas como provisionales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico inicial claro.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio con postura.",
      "Evidencia verificable con citas.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos solidos y verificables.",
      "Sostener coherencia institucional, metodologica y tecnica en toda entrega."
    ],
    "style_markers": [
      "Sin afirmaciones sin fuente o supuesto.",
      "Secciones funcionales y cierre profesional.",
      "Redaccion no descriptiva: priorizar argumentacion."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco -> analisis -> conclusion.",
      "Norma y doctrina como soporte de la postura propia.",
      "Cierre con impacto practico profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Problema juridico",
        "Marco normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Consistencia .tex/.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura requiere conflicto definido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica exige fundamento explicito."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y verificabilidad."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "derecho-fiscal-y-tributario.bib: fuentes institucionales base.",
        "Supuesto: transferencia transversal limitada a patrones metodologicos estables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion completa de reglas repetidas.",
      "Ciclo 18: refuerzo de gates criticos heredados (JSON, supuestos, citas, .bib).",
      "Ciclo 18: consolidacion de patron argumentativo reusable sin arrastre tematico indebido.",
      "Ciclo 18: persistencia de identidad UnADM y contexto curricular local."
    ]
  }
}