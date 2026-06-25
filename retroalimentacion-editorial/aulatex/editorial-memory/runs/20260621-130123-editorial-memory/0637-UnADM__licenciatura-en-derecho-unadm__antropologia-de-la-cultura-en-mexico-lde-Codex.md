{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preserva identidad UnADM, normalizacion estructurada y compresion union-dedupe sin regresion.",
    "Se transfieren solo abstracciones estables: objetivo, evidencia, analisis propio, coherencia y cierre transferible.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se refuerza control de placeholders y rutas corruptas detectadas en README y programa analitico.",
    "Se mantiene alerta historica por salidas no JSON parseables como gate institucional."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No trasladar metadatos curriculares de otras materias."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear forma de entrega al producto solicitado por planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a practica juridica.",
    "Integrar puentes argumentativos entre dimension cultural y juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local.",
    "Confirmar que todo supuesto este etiquetado como supuesto.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla .tex local como base de trabajo.",
    "Conservar configuracion de espanol y metadatos institucionales consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) a nombres literales antes de compilar.",
    "Corregir rutas con caracteres truncados en README o fuentes antes de referenciar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia de archivos locales en assets-unadm."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar copiar redaccion literal o contenidos tematicos de otra asignatura.",
    "Mantener compresion lossless por union-dedupe y sin eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alertas transversales reutilizables.",
    "Si falta contexto local, conservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: falta confirmacion institucional del estandar unico de citas para la licenciatura.",
    "Supuesto: clave LDE-S4B2 requiere confirmacion oficial.",
    "Confirmar si conclusion juridica aplica a todas las actividades de la materia o depende de consigna.",
    "Confirmar si el nombre final del .bib debe quedar literal y no dinamico en todos los documentos.",
    "Confirmar rubricas locales para calibrar profundidad argumentativa por actividad."
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
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Contexto local: semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Estandar institucional de trazabilidad y validacion estructural.",
      "Sincronizacion transversal por abstracciones estables, no por traslado tematico."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles profesionalmente.",
      "Preservar coherencia editorial entre nodos sin perder contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo verificable -> interpretacion propia.",
      "Consigna -> desarrollo alineado -> validacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Separacion de artefactos editoriales",
        "Control de placeholders en rutas y nombres"
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
          "justification": "Sin parseo valido no hay propagacion segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre profesional surge del razonamiento y no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Separacion de artefactos editoriales",
          "kind": "supports",
          "justification": "La consistencia institucional exige formatos y piezas distinguibles."
        }
      ],
      "evidence": [
        "README destino define identidad UnADM y pauta editorial.",
        "Programa analitico destino fija ejes problema-conceptos-producto-analisis-conclusion.",
        "Memoria origen refuerza gates de JSON y normalizacion previa.",
        "Contexto local evidencia placeholders dinamicos y rutas truncadas a corregir."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se refuerza ADN institucional sin recorte de reglas utiles previas.",
      "Ciclo 6: deduplicacion semantica aplicada a reglas repetidas de origen y destino.",
      "Ciclo 6: transferencia limitada a abstracciones estables por relacion transversal.",
      "Ciclo 6: se preserva alerta historica de parseo no estructurado como gate global."
    ]
  }
}