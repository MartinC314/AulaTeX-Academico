{
  "summary": [
    "Sincronizacion transversal ciclo 12 aplicada por union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia de la cultura en Mexico.",
    "Se incorporan del origen solo abstracciones estables: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseables y normalizacion previa obligatoria.",
    "Se refuerza resolucion de placeholders tipo Slug en README, programa analitico y rutas de archivos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Usar la carpeta de materia como entrada canonica.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar nombre canonico de materia: Antropologia de la cultura en Mexico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta validacion local.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o teorico, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura reusable.",
    "Resolver nombres y rutas con tokens dinamicos antes de compilar o citar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Integrar conceptos antropologicos y juridicos con puente argumentativo explicito.",
    "Cerrar con conclusion transferible a la practica juridica cuando la consigna lo permita."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar memoria.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna real.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como referencia inicial.",
    "Usar configuracion en espanol consistente y acentos correctos en .tex y .bib.",
    "Mantener clase article, letterpaper y oneside salvo instruccion distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Corregir caracteres truncados en nombres de archivo y rutas antes de compilar.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa y referencias."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No citar claves inexistentes en .bib.",
    "Mantener entradas base locales unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstraidas, no redaccion literal.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-materias.",
    "Conservar metodo union-dedupe sin eliminar reglas utiles previas.",
    "Cuando falte consigna local, propagar solo reglas generales estables y marcar supuestos.",
    "Mantener alerta historica: ciclos con salida no estructurada requieren normalizacion manual."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas de Antropologia; confirmar productos requeridos.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar politica final para resolver placeholders Slug en todos los documentos fuente."
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
      "Problema, conceptos, evidencia, analisis propio y cierre transferible.",
      "Normalizacion estructurada antes de cualquier propagacion.",
      "Compresion lossless por deduplicacion y sin regresion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos trazables y coherentes.",
      "Sostener calidad editorial transversal entre nodos no equivalentes."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos etiquetados.",
      "Conclusiones utiles para practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente verificable -> interpretacion propia.",
      "Coherencia completa entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
        "Resolucion de placeholders Slug"
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
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "El criterio propio requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional surge del razonamiento, no del resumen."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Resolucion de placeholders Slug",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "Evita rutas rotas y referencias ambiguas en memoria y compilacion."
        }
      ],
      "evidence": [
        "README local define identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local fija ejes de trabajo y proposito de realizacion.",
        "Bib local contiene unadmSitioWeb y unadmMallaDerecho2024 como base verificable.",
        "Memoria origen confirma gates de parseo JSON y normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se preservan reglas previas validas sin eliminaciones.",
      "Ciclo 12: se deduplican reglas repetidas y se mantienen equivalentes utiles.",
      "Ciclo 12: se transfieren solo abstracciones estables desde Filosofia del Derecho.",
      "Ciclo 12: se evita mover contenido tematico exclusivo del origen al destino."
    ]
  }
}