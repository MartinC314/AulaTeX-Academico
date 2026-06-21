{
  "summary": [
    "Sincronizacion transversal ciclo 24 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho a Antropologia.",
    "Se evita transferir contenido tematico exclusivo del nodo origen.",
    "Se refuerza normalizacion obligatoria ante salidas no JSON parseables.",
    "Se mantiene alerta de fuentes heredadas no verificadas como provisionales.",
    "Se consolida base minima de materia con vacios locales abiertos y marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No trasladar metadatos curriculares de otras materias al destino."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el producto al entregable de la planeacion semanal.",
    "Separar artefactos: reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias canonicas.",
    "Resolver placeholders y tokens dinamicos en rutas y nombres antes de usar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Cerrar con conclusion transferible a la practica juridica.",
    "Evitar extrapolar fuentes de semanas o materias no confirmadas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Revisar y normalizar manualmente respuestas no estructuradas heredadas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia entre metadatos del documento y contexto local de materia.",
    "No promover reglas provisionales a definitivas sin validacion disciplinar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y formato base de la plantilla salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle segun actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir rutas con caracteres truncados en README y archivos fuente."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales aplicables.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad de procedencia cuando se usen archivos locales."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Transferir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia literal de redaccion y contenidos tematicos del origen.",
    "Preservar siempre reglas utiles previas; consolidar por union-dedupe sin recorte.",
    "Registrar incidencias de parseo como alertas transversales reutilizables."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividades especificas de Antropologia; confirmar formatos exactos.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o clave operativa local.",
    "Confirmar si la conclusion juridica es obligatoria en todas las actividades de la materia.",
    "Confirmar politica final para resolucion automatica de tokens tipo Slug en README y programa."
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
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Garantizar coherencia entre identidad institucional, evidencia y argumentacion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> fuente -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos explicitos",
        "Separacion de artefactos editoriales"
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
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal gana solidez con respaldo comprobable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion aplicada deriva del razonamiento y no del resumen."
        },
        {
          "source": "Supuestos explicitos",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Marcar incertidumbre evita afirmaciones infundadas."
        }
      ],
      "evidence": [
        "README de materia: identidad UnADM y pauta editorial.",
        "Programa analitico: ejes problema, conceptos, evidencia, analisis y cierre.",
        "Archivo .bib local con fuentes institucionales base.",
        "Historial de incidencias: salidas no estructuradas requieren normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida semantica.",
      "Se conservaron gates criticos heredados de parseo y normalizacion.",
      "Se reforzo politica de supuestos y fuentes provisionales.",
      "Se incorporaron patrones argumentativos estables del origen sin arrastre tematico.",
      "Se mantuvo estrategia progresiva y conservadora con no regresion."
    ]
  }
}