{
  "summary": [
    "Sincronizacion transversal ciclo 5 aplicada con union-dedupe lossless y sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia en Mexico.",
    "Se incorporan del origen solo abstracciones estables: objetivo, evidencia, analisis propio, coherencia y cierre transferible.",
    "Se mantiene gate critico: no propagar salidas no JSON parseables sin normalizacion.",
    "Se refuerza resolucion de placeholders en README y programa antes de compilar o propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar contexto local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos especificos de Filosofia del Derecho al nodo de Antropologia."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado en la planeacion semanal.",
    "Mantener separacion de artefactos: reporte, presentacion y bibliografia.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales antes de uso.",
    "Corregir rutas con caracteres truncados en README y estructura local."
  ],
  "activity_rules": [
    "Sustentar afirmaciones relevantes con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar transferir contenido tematico exclusivo de otra materia sin puente disciplinar."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Normalizar manualmente toda salida no estructurada heredada.",
    "Confirmar consistencia entre metadatos de materia y documento final.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla local.",
    "Mantener clase base y formato institucional salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener coursename de la materia destino y coursecode local [Supuesto: LDE-S4B2].",
    "Compilar sin errores criticos ni referencias rotas.",
    "No dejar placeholders sin resolver en .tex, README o programa."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener entradas base locales unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar redaccion literal y contenido tematico no transversal.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables.",
    "Registrar incidencias de parseo como alertas institucionales reutilizables."
  ],
  "open_questions": [
    "[Supuesto] Confirmar si LDE-S4B2 es clave oficial institucional o clave local.",
    "Confirmar estandar unico de citacion para la licenciatura.",
    "Confirmar si toda actividad de Antropologia exige cierre juridico explicito.",
    "Confirmar nomenclatura final obligatoria del .bib cuando hay plantillas dinamicas.",
    "Confirmar rubrica local para calibrar profundidad argumentativa por actividad."
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
        "Semestre 4, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Transferencia profesional del cierre argumentativo.",
      "Sincronizacion transversal sin contaminar contexto local."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Proteger consistencia institucional en toda la suite LaTeX.",
      "Asegurar propagacion segura con compresion lossless por deduplicacion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Supuestos marcados de forma visible.",
      "Citas verificables en cada afirmacion clave.",
      "Cierre con valor practico-juridico."
    ],
    "argumentative_patterns": [
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Problema contextual -> marco conceptual -> postura propia -> conclusion transferible.",
      "Coherencia entre consigna, desarrollo y producto final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Separacion de artefactos",
        "Resolucion de placeholders"
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
          "justification": "La postura academica se legitima con respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El cierre util deriva del razonamiento, no del resumen."
        },
        {
          "source": "Resolucion de placeholders",
          "target": "Separacion de artefactos",
          "kind": "supports",
          "justification": "Rutas y nombres correctos evitan fallas de compilacion y mezcla documental."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y cierre.",
        ".bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: gate de JSON parseable y normalizacion previa obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se preservan reglas previas utiles sin eliminacion.",
      "Ciclo 5: se agregan abstracciones estables del origen no equivalentes tematicamente.",
      "Ciclo 5: se refuerzan gates de parseo, trazabilidad y consistencia bib/tex.",
      "Ciclo 5: se mantiene estrategia progresiva y conservadora."
    ]
  }
}