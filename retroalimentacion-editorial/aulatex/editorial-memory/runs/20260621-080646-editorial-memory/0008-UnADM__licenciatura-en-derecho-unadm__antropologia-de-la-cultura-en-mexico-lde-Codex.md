{
  "summary": [
    "Sincronizacion transversal ciclo 8 aplicada con union-dedupe lossless y sin regresion.",
    "Se preservan reglas institucionales UnADM y estructura canonica de la materia destino.",
    "Se incorporan abstracciones estables del origen: objetivo, evidencia verificable, postura propia y coherencia argumentativa.",
    "Se evita transferir contenido tematico exclusivo de Filosofia del Derecho al nodo de Antropologia.",
    "Se refuerza normalizacion obligatoria para salidas no JSON parseables y fuentes heredadas provisionales."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Mantener ubicacion curricular local: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional.",
    "No trasladar metadatos curriculares de Filosofia del Derecho al destino."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado en la planeacion semanal.",
    "Mantener separacion de artefactos: reporte, presentacion y bibliografia.",
    "Resolver placeholders y tokens dinamicos en README, programa y rutas antes de uso."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir evidencia, interpretacion y opinion personal.",
    "Evitar afirmaciones culturales o juridicas sin puente argumentativo.",
    "Cerrar con conclusion transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa del esquema antes de reutilizar.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que rutas y nombres no contengan tokens sin expandir."
  ],
  "latex_rules": [
    "Usar configuracion en espanol coherente con la plantilla local.",
    "Mantener clase y formato base salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir caracteres anommalos o rutas truncadas antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como supuesto cualquier uso de fuente heredada no confirmada localmente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y abstractas entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenidos disciplinares cerrados del origen.",
    "Preservar reglas utiles previas; solo agregar mejoras verificables.",
    "Mantener alertas de parseo y normalizacion manual como controles transversales."
  ],
  "open_questions": [
    "Supuesto: falta consigna local de actividad especifica en la materia destino.",
    "Confirmar estandar de citacion institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial o convencion local.",
    "Confirmar si toda actividad de la materia exige conclusion juridica explicita.",
    "Confirmar si persiste algun token dinamico sin resolver en archivos auxiliares."
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
      "Convertir planeacion semanal en productos academicos solidos.",
      "Sostener calidad transversal con reglas estables y verificables."
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
      "Pregunta guia -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON parseable",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos marcados",
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
          "justification": "Sin parseo valido no hay memoria reutilizable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion surge del razonamiento argumentado."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal conservadora",
          "kind": "supports",
          "justification": "La identidad comun permite reglas compartidas entre materias."
        }
      ],
      "evidence": [
        "README y programa analitico del destino fijan ejes y tono.",
        "Bibliografia local contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "Historial heredado reporta incidencias de salida no estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se consolida transferencia abstracta estable desde actividad origen a materia destino.",
      "Ciclo 8: se refuerzan gates de parseo JSON y normalizacion previa a propagacion.",
      "Ciclo 8: se mantiene politica de no inventar fuentes y marcar supuestos."
    ]
  }
}