{
  "summary": [
    "Sincronizacion transversal aplicada entre actividad de Filosofia del Derecho y materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas utiles previas y se deduplican sin recorte semantico.",
    "Se transfieren solo abstracciones estables: identidad, estructura reusable, gates de calidad y coherencia argumentativa.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se mantiene alerta institucional por salidas no JSON parseables y normalizacion obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar metadatos curriculares de materias distintas al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas de estructura.",
    "Resolver placeholders de nombres de archivo antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica del contexto de la materia.",
    "Integrar conceptos antropologicos, culturales y juridicos con puente argumentativo explicito."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que cada afirmacion sensible tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre metadatos del documento y datos curriculares locales.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como referencia inicial.",
    "Conservar configuracion de espanol, letterpaper y oneside salvo instruccion contraria.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener coursename y coursecode locales del destino.",
    "Usar acentos y codificacion consistente en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas truncadas o tokens dinamicos sin expandir en README/programa/.tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No citar claves inexistentes en el .bib local.",
    "Mantener entradas base institucionales ya existentes del destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir entre nodos no equivalentes solo abstracciones estables.",
    "Preservar union-dedupe lossless sin eliminar reglas utiles previas.",
    "Etiquetar incidencias de parseo como alerta reutilizable inter-materias.",
    "Mantener como provisional toda herencia de origen no verificada localmente.",
    "Si falta contexto local, conservar cerebro minimo y abrir vacios en preguntas."
  ],
  "open_questions": [
    "Supuesto: confirmar estandar de citacion oficial para toda la Licenciatura en Derecho.",
    "Supuesto: confirmar si la conclusion juridica aplica a todas las actividades de antropologia o segun consigna.",
    "Confirmar si LDE-S4B2 es clave institucional definitiva o clave local.",
    "Confirmar si existe rubrica transversal oficial para profundidad argumentativa.",
    "Confirmar resolucion definitiva del nombre .bib cuando hay placeholders en documentos fuente."
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
        "Destino: Antropologia de la cultura en Mexico.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
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
      "Convertir la planeacion semanal en productos academicos consistentes.",
      "Asegurar calidad institucional y trazabilidad en cada entrega.",
      "Sostener coherencia argumentativa entre contexto social/cultural y analisis juridico."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Citas verificables en puntos clave.",
      "Conclusion util para practica academica/profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo alineado -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Puente antropologia-cultura-derecho"
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
          "justification": "Sin parseo valido no hay memoria reusable confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El argumento personal requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion se deriva del razonamiento, no del resumen."
        },
        {
          "source": "Puente antropologia-cultura-derecho",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Evita reduccionismo y mejora pertinencia disciplinar."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM, integridad academica y conclusion con criterio propio.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y cierre.",
        "Bib local existente con fuentes institucionales base.",
        "Regla heredada estable: bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 33: consolidacion transversal conservadora aplicada.",
      "Se reforzaron gates de parseo JSON y normalizacion estructurada.",
      "Se reforzo patron argumentativo reusable sin importar materia.",
      "Se mantuvo separacion entre reglas estables y contenido tematico no transferible.",
      "Se marcaron supuestos pendientes de validacion local."
    ]
  }
}