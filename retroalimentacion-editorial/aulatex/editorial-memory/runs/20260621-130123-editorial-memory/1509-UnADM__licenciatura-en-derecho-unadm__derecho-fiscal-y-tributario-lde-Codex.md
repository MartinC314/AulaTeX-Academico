{
  "summary": [
    "Sincronizacion transversal consolidada con estrategia conservadora y sin regresion.",
    "Se transfieren solo abstracciones estables: identidad UnADM, ejes editoriales, gates y patron argumentativo.",
    "Se mantiene compresion lossless por union-dedupe y normalizacion obligatoria previa a propagacion.",
    "Se refuerza que el destino use contexto local fiscal-tributario y no herede contenido tematico de Filosofia.",
    "Supuesto: no hay consigna de actividad especifica en este salto; se preserva cerebro editorial minimo de materia."
  ],
  "identity_rules": [
    "Conservar identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares verificados del destino: semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir literalidad de nodos no equivalentes; transferir solo patrones estables."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final con la planeacion semanal y la consigna.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Corregir rutas y slugs rotos en README y programa analitico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar entregas solo descriptivas.",
    "Vincular analisis fiscal-tributario con aplicacion profesional concreta.",
    "No asumir fuentes de otras semanas o materias como obligatorias para la actividad actual."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre metadatos de portada y programa analitico.",
    "Verificar que no existan placeholders o tokens sin expandir en README, .tex y .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con entornos cerrados.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Completar campos de portada y authortable antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Registrar fuentes especificas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No trasladar bibliografia tematica de Filosofia como obligatoria en Fiscal sin consigna expresa."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual en saltos transversales.",
    "Evitar transferencia de redaccion literal entre nodos no equivalentes.",
    "Mantener metodo union-dedupe y politica de no regresion en ciclos siguientes.",
    "Aplicar normalizacion manual si una entrada heredada llega no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna concreta de la siguiente actividad fiscal-tributaria para ajustar artefacto.",
    "Confirmar formato de citacion exigido por la asignatura.",
    "Confirmar nombre de figura docente y datos personales finales de plantilla.",
    "Confirmar resolucion definitiva de rutas truncadas en README.",
    "Supuesto: el .bib canonico de materia es derecho-fiscal-y-tributario.bib."
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
        "Carpeta de asignatura como entrada canonica.",
        "Supuestos etiquetados y trazables."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Analisis propio con postura.",
      "Evidencia verificable.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar consistencia editorial entre actividades y materia sin perder contexto local."
    ],
    "style_markers": [
      "Inicio breve y enfocado.",
      "Secciones funcionales sin relleno.",
      "Cierre profesional orientado a practica juridica.",
      "Sin afirmaciones huerfanas de fuente."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion aplicable.",
      "Pregunta guia explicita y respuesta sustentada.",
      "Contraste breve de fuentes con toma de postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
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
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
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
          "justification": "La conclusion juridica valida exige fundamento."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "El marco institucional exige trazabilidad y verificabilidad."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito.",
        "derecho-fiscal-y-tributario.bib: base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se refuerzan reglas estables transversales sin trasladar contenido tematico de Filosofia.",
      "Ciclo 4: se mantiene no regresion y compresion lossless por deduplicacion.",
      "Ciclo 4: se priorizan gates de calidad, estructura reusable y grafo conceptual."
    ]
  }
}