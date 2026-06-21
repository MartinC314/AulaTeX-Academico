{
  "summary": [
    "Sincronizacion transversal conservadora aplicada por union-dedupe sin regresion.",
    "Se preserva identidad UnADM y contexto curricular local de Antropologia en Mexico.",
    "Se incorporan abstracciones estables del origen: objetivo puntual, evidencia verificable, postura propia y coherencia cierre-desarrollo.",
    "Se mantiene regla de normalizacion obligatoria antes de propagacion recursiva.",
    "Se refuerza control de placeholders y rutas corruptas en README, programa y LaTeX.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No trasladar metadatos curriculares de otras materias."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en: conceptos clave, marco teorico/normativo, analisis propio y cierre.",
    "Alinear producto al entregable de planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Cerrar con conclusion transferible a practica juridica."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones juridicas o culturales sin puente argumentativo."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar.",
    "Normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar trazabilidad de cada afirmacion o marcar supuesto.",
    "Validar consistencia entre citas en texto y .bib.",
    "Verificar correspondencia entre producto y consigna local.",
    "No promover reglas provisionales a definitivas sin validacion local."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con plantilla local.",
    "Mantener clase article, letterpaper y oneside salvo instruccion distinta.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Resolver tokens dinamicos tipo $(@{...}.Slug) antes de compilar.",
    "Corregir rutas truncadas o caracteres anomalos en README y .tex.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables.",
    "Mantener .bib local de la materia como registro canonico.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/URL.",
    "Distinguir bibliografia base y bibliografia especifica por actividad.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Etiquetar incidencias de parseo como alerta transversal reutilizable.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna puntual de actividades especificas en esta materia.",
    "Confirmar estandar unico de citacion institucional para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o local.",
    "Confirmar si conclusion juridica es obligatoria en todas las actividades antropologicas."
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
        "Integridad academica con trazabilidad.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 4, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Antropologia de la cultura en Mexico."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion transferible.",
      "Normalizacion estructurada previa a toda propagacion.",
      "Sincronizacion transversal sin contaminar contenido disciplinar."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos verificables y utiles profesionalmente.",
      "Conservar coherencia institucional y calidad tecnica editorial."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Supuestos marcados cuando falte evidencia directa.",
      "Secciones funcionales y cierre con valor profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Consigna -> desarrollo -> cierre coherente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible"
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
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
          "justification": "La postura academica requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y pauta editorial.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-conclusion.",
        ".bib local: fuentes institucionales base verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 35: se consolidan abstracciones estables de actividad origen sin traslado tematico.",
      "Ciclo 35: se mantiene gate de JSON parseable y normalizacion manual para salidas no estructuradas.",
      "Ciclo 35: se refuerza deduplicacion lossless y politica de no regresion."
    ]
  }
}