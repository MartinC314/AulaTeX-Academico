{
  "summary": [
    "Se sincroniza memoria transversal con abstracciones estables entre actividad y materia.",
    "Se conserva identidad UnADM y marco de Licenciatura en Derecho sin mezclar asignaturas.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se preserva gate critico: no propagar insumos no parseables sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar encuadre curricular local del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Marcar como supuesto todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No mezclar identidad ni contenido curricular de otras carreras o materias."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar transferir contenido tematico especifico de otra asignatura sin validacion documental.",
    "Registrar supuestos operativos cuando falten instrucciones de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizacion recursiva.",
    "Validar estructura minima completa del esquema editorial.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener plantilla base de la materia como punto de partida.",
    "Corregir placeholders o tokens sin expandir en README y programa analitico antes de compilar.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Compilar sin errores criticos, referencias rotas ni rutas invalidas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes al encargo local.",
    "Centralizar bibliografia de materia en electiva-semestre-7-bloque-2.bib.",
    "Agregar fuentes especificas por actividad con metadatos minimos completos.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables, no redaccion literal.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener bandera de normalizacion manual cuando aparezcan salidas no estructuradas.",
    "Aplicar union-dedupe en cada ciclo para evitar duplicados y perdida de reglas utiles.",
    "Si falta contexto local de actividad, conservar nucleo minimo y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales para portada y README.",
    "Confirmar figura docente para reemplazar placeholder.",
    "Supuesto: la consigna de cada actividad aun no esta incorporada en memoria local.",
    "Confirmar politica local para year vs fecha de consulta en fuentes web institucionales."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, tipo electiva.",
        "Producto alineado a planeacion semanal."
      ]
    },
    "essence": [
      "Problema juridico o social como disparador.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable con citas consistentes.",
      "Analisis propio del estudiante.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos con fundamento juridico y utilidad profesional.",
      "Sostener continuidad editorial entre nodos sin contaminar contexto tematico local."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos etiquetados cuando falta evidencia.",
      "Separacion clara entre descripcion, analisis y cierre."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer conceptos y marco normativo.",
      "Contrastar fuentes con postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion de memoria",
        "JSON parseable"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El analisis parte de un caso o tension concreta."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva de razonamiento y evidencia."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La norma editorial exige citas verificables y coherencia formal."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicacion curricular.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Archivo .bib local: claves base institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas del origen y destino sin perdida semantica.",
      "Se transfirieron solo abstracciones estables por relacion transversal.",
      "Se excluyo contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo.",
      "Se reforzo gate de parseabilidad JSON como requisito de propagacion."
    ]
  }
}