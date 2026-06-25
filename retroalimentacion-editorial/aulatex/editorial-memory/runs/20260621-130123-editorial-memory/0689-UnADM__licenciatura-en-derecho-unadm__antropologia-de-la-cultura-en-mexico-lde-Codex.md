{
  "summary": [
    "Sincronizacion transversal ciclo 19 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia de la cultura en Mexico.",
    "Se incorporan del origen solo abstracciones estables: objetivo puntual, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se mantiene regla critica: bloquear propagacion si no hay JSON parseable.",
    "Se refuerza normalizacion de placeholders en README, programa analitico y rutas de bibliografia."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Respetar contexto local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Cerrar con conclusion transferible a la practica juridica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Integrar conceptos culturales y juridicos con puente argumentativo explicito.",
    "No transferir contenido tematico especifico de Filosofia del Derecho a Antropologia sin justificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que no existan placeholders sin resolver en README, programa, .tex y .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex de la materia como punto de partida.",
    "Conservar configuracion de espanol, letterpaper y oneside salvo instruccion valida en contrario.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener coursename de la materia destino y metadatos institucionales coherentes.",
    "Usar acentos y codificacion correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias consultables.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar traslado de redaccion literal y metadatos curriculares de otra materia.",
    "Mantener compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Etiquetar incidencias de parseo como alertas reutilizables inter-materias.",
    "Si falta contexto local en nodos vecinos, propagar nucleo minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Supuesto: confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Confirmar estandar de citacion unico para la licenciatura.",
    "Confirmar si todas las actividades de Antropologia exigen conclusion juridica explicita.",
    "Confirmar formato exacto por actividad: reporte, presentacion u otro.",
    "Confirmar si persisten fuentes heredadas de ingenieria activas en este nodo y depurarlas."
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
        "Integridad academica con trazabilidad.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Antropologia de la cultura en Mexico.",
        "Contexto local: semestre 4, bloque 2, obligatoria, 8 creditos."
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
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar calidad editorial constante entre actividades y materias.",
      "Sostener sincronizacion transversal sin contaminar contexto disciplinar local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados cuando falte evidencia.",
      "Cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Coherencia vertical entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Sincronizacion transversal conservadora"
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
          "justification": "La postura personal exige respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion util surge del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun habilita reglas compartibles entre materias."
        }
      ],
      "evidence": [
        "README y programa analitico del destino fijan ejes y contexto curricular.",
        "Bibliografia local contiene bases institucionales verificables.",
        "Memoria origen confirma regla estable de parseo JSON y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion completa de reglas repetidas.",
      "Ciclo 19: preservadas reglas utiles previas sin recorte.",
      "Ciclo 19: transferidas solo abstracciones estables del origen transversal.",
      "Ciclo 19: mantenida alerta de fuentes heredadas no verificadas como provisionales."
    ]
  }
}