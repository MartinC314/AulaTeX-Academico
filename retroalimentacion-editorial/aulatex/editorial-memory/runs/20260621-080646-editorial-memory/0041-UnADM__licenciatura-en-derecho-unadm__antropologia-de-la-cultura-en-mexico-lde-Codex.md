{
  "summary": [
    "Sincronizacion transversal conservadora aplicada con union-dedupe lossless.",
    "Se preserva identidad UnADM y contexto curricular local de la materia destino.",
    "Se transfieren solo abstracciones estables desde actividad origen no equivalente.",
    "Se refuerzan ejes reutilizables: objetivo, problema, evidencia, analisis propio y cierre.",
    "Se mantiene alerta de salidas no parseables y normalizacion obligatoria previa a propagacion.",
    "Se evita trasladar contenido tematico especifico de Filosofia del Derecho al nodo de Antropologia.",
    "Se consolida cerebro editorial minimo del destino con vacios locales abiertos como supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en la planeacion semanal.",
    "Distinguir artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de nombres de archivo antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar conceptos antropologicos, culturales y juridicos con puente argumentativo explicito.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo requiera.",
    "No asumir fuentes de otras semanas o materias sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto final y consigna vigente.",
    "No convertir reglas provisionales en definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia y clase article salvo justificacion.",
    "Usar configuracion en español coherente y acentos correctos en .tex y .bib.",
    "Mantener campos institucionales completos y actualizados por actividad.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin resolver.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas truncadas o caracteres anomalos en README, programa y .tex."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Marcar como supuesto cualquier enlace bibliografico no confirmado localmente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas ya validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico exclusivo de origen.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materia.",
    "Preservar reglas utiles previas; consolidar por union-dedupe sin regresion."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas de Antropologia; confirmar formato exacto por semana.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave institucional definitiva o local.",
    "Confirmar si el nombre .bib dinamico ya quedo fijado en antropologia-de-la-cultura-en-mexico.bib."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Cierre transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener coherencia entre consigna, desarrollo y resultado.",
      "Preservar calidad editorial institucional en cada entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia local.",
      "Conclusiones con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> respuesta coherente y verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Separacion de artefactos editoriales",
        "Control de supuestos"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El argumento personal requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Separacion de artefactos editoriales",
          "kind": "supports",
          "justification": "La pauta institucional exige orden documental y trazabilidad."
        }
      ],
      "evidence": [
        "README de materia destino.",
        "Programa analitico de la materia destino.",
        "Archivo .bib local con entradas institucionales.",
        "Historial de alerta por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 41: se deduplican reglas repetidas y se conserva cobertura completa.",
      "Ciclo 41: se incorporan abstracciones estables de actividad origen sin arrastre tematico.",
      "Ciclo 41: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 41: se mantiene politica de supuestos y fuentes provisionales no verificadas."
    ]
  }
}