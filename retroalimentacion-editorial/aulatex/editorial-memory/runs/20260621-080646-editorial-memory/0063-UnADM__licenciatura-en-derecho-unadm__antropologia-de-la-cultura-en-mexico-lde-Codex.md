{
  "summary": [
    "Sincronizacion transversal consolidada por union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y marco curricular local de Antropologia de la cultura en Mexico.",
    "Se transfieren solo abstracciones estables del origen: objetivo, evidencia, analisis propio y cierre transferible.",
    "Se mantiene regla de normalizacion estructurada obligatoria antes de propagar.",
    "Se refuerza control de placeholders y rutas corruptas detectadas en README y programa analitico.",
    "Se conserva alerta historica: salidas no JSON parseable deben bloquear propagacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar nombre canonico de materia: Antropologia de la cultura en Mexico.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de usar.",
    "Corregir rutas con caracteres truncados antes de compilar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar extrapolar fuentes de otras semanas sin confirmacion.",
    "Relacionar conceptos antropologicos con impacto juridico mediante puente argumentativo.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar consistencia entre metadatos del documento y malla curricular local.",
    "Verificar que no existan supuestos sin marcar.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como referencia inicial.",
    "Conservar clase article, letterpaper y oneside salvo instruccion distinta.",
    "Mantener configuracion de espanol y acentos correctos en .tex y .bib.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename y coursecode locales salvo cambio institucional confirmado.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver placeholders en nombres de archivos antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Mantener trazabilidad de procedencia de archivos locales.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en el .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Evitar transferencia de contenido tematico literal entre materias distintas.",
    "Registrar incidencias de parseo como alertas reutilizables inter-materias.",
    "Aplicar estrategia progresiva y conservadora: agregar sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "[Supuesto] Confirmar si LDE-S4B2 es clave institucional oficial o clave local.",
    "[Supuesto] Confirmar estandar unico de citas para la licenciatura (APA u otro).",
    "[Supuesto] Confirmar si conclusion juridica es obligatoria en todas las actividades de Antropologia.",
    "[Supuesto] Confirmar si autor y matricula de plantilla deben mantenerse o variar por entrega.",
    "[Supuesto] Confirmar si existe rubrica formal de evaluacion por actividad en esta materia."
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
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Compresion lossless por deduplicacion sin recorte."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles profesionalmente.",
      "Preservar coherencia institucional y calidad tecnica en toda entrega."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con transferencia juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Consistencia entre pregunta guia y respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Validacion JSON parseable",
        "Normalizacion estructurada"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad y rigor."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio personal se sostiene con respaldo comprobable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La utilidad profesional depende del razonamiento propio."
        },
        {
          "source": "Validacion JSON parseable",
          "target": "Normalizacion estructurada",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay propagacion confiable."
        }
      ],
      "evidence": [
        "README de materia destino con pauta editorial UnADM.",
        "Programa analitico con ejes de trabajo reutilizables.",
        "Archivo .bib local con unadmSitioWeb y unadmMallaDerecho2024."
      ]
    },
    "reinforcement_log": [
      "Ciclo 63: se consolidan abstracciones estables desde actividad de Filosofia del Derecho sin arrastrar contenido tematico especifico.",
      "Ciclo 63: se mantiene bloqueo por no-JSON parseable y normalizacion obligatoria.",
      "Ciclo 63: se refuerza resolucion de placeholders y limpieza de rutas en artefactos."
    ]
  }
}