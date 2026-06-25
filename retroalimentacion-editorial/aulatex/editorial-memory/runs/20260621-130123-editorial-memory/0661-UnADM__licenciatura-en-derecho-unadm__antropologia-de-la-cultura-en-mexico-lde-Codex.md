{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Se transfieren solo abstracciones estables: identidad UnADM, estructura reusable, calidad de evidencia y gates de validacion.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de cualquier propagacion recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "No trasladar metadatos especificos de otra asignatura al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco pertinente, analisis propio y cierre.",
    "Alinear el producto al entregable solicitado en planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de nombres de archivo antes de compilar o citar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a practica profesional juridica.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar manualmente salidas no estructuradas.",
    "Confirmar trazabilidad entre citas en texto y archivo .bib.",
    "Validar que no existan placeholders sin resolver en README, programa, .tex y rutas.",
    "No promover reglas provisionales a definitivas sin verificacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base.",
    "Conservar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin claves faltantes.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Actualizar documenttitle y documentsubtitle segun actividad real.",
    "Corregir rutas truncadas o tokens dinamicos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagacion literal de redaccion o contenido tematico especializado del origen.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Mantener union-dedupe lossless en ciclos futuros sin eliminar reglas utiles."
  ],
  "open_questions": [
    "[supuesto] Confirmar si la clave LDE-S4B2 es oficial o solo local.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si toda actividad de la materia exige cierre juridico explicito.",
    "Confirmar rubrica local para ajustar profundidad argumentativa.",
    "Confirmar si existen fuentes base obligatorias adicionales para Antropologia de la cultura en Mexico."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio.",
        "Culturalmente sensible y juridicamente pertinente."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con trazabilidad de fuentes.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Destino local: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema claro.",
      "Conceptos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos trazables y utiles para formacion juridica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Transferencia transversal por abstracciones estables"
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
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "La integridad exige respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia se legitima con fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util deriva del razonamiento."
        },
        {
          "source": "Transferencia transversal por abstracciones estables",
          "target": "Identidad institucional UnADM",
          "kind": "supports",
          "justification": "Permite sincronizar sin contaminar contexto tematico local."
        }
      ],
      "evidence": [
        "README y programa analitico del destino fijan ejes y pauta institucional.",
        "Bib local contiene fuentes base institucionales verificables.",
        "Memoria origen aporta gates de parseo, trazabilidad y coherencia argumentativa reutilizable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se refuerza gate de JSON parseable como bloqueo duro de propagacion.",
      "Ciclo 12: se conserva union-dedupe lossless y no regresion.",
      "Ciclo 12: se agregan solo abstracciones estables del origen; se excluye contenido tematico no transversal.",
      "Ciclo 12: se mantiene politica de supuestos marcados y fuentes provisionales hasta verificacion local."
    ]
  }
}