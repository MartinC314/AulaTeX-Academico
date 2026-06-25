{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de otra materia sin trasladar contenido doctrinal especifico.",
    "Se preservan reglas institucionales validas de UnADM y se deduplican en modo lossless.",
    "Se refuerza el nucleo reusable: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene como gate obligatorio la normalizacion estructurada y JSON parseable antes de propagar.",
    "Se conserva alineacion curricular local del destino: semestre 6, bloque 1, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Explicitar si el producto es reporte, presentacion o visual antes de redactar.",
    "Vincular el analisis al campo de control administrativo en clave profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar que reglas heredadas no contradigan programa analitico local."
  ],
  "latex_rules": [
    "Mantener espanol y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Reemplazar 'Actividad X' por numero y nombre real.",
    "Completar figura docente antes de entregar. [supuesto]",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa por slug literal.",
    "Corregir nombres de archivo espurios en README (eporte-/eferencias-)."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de cada actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad entre afirmaciones del texto y entradas BibTeX."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir a nodos laterales solo abstracciones editoriales estables.",
    "Evitar transferir redaccion literal o doctrina no verificada de otra materia.",
    "Aplicar estrategia union-dedupe lossless y sin regresion en ciclos futuros.",
    "Preservar alertas institucionales sobre fuentes provisionales y salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar nombre oficial de figura docente en plantilla local.",
    "Confirmar convencion final de carpeta/archivo de referencias en README.",
    "Confirmar si el anio de consulta del sitio institucional permanece en 2026. [supuesto]",
    "Confirmar si existe formato de citacion obligatorio adicional para la carrera.",
    "Confirmar que todos los tokens de slug ya fueron normalizados en archivos locales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion.",
        "No invencion de fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho administrativo y control.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Marco local regido por README y programa analitico."
      ]
    },
    "essence": [
      "Resolver un problema juridico con estructura clara.",
      "Sostener el analisis con conceptos, normas y evidencia verificable.",
      "Aportar postura propia y cierre aplicable a practica profesional.",
      "Proteger consistencia tecnica entre texto, citas y compilacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos evaluables y trazables.",
      "Asegurar rigor juridico y utilidad profesional en cada entrega.",
      "Mantener una memoria editorial reutilizable, estable y sin regresiones."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Objetivo explicito antes del desarrollo.",
      "Secciones funcionales y cierre juridico transferible.",
      "Supuestos visibles y fuentes provisionales etiquetadas."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion aplicable.",
      "Afirmacion -> evidencia/cita -> interpretacion -> implicacion juridica.",
      "Consigna -> producto requerido -> criterios de calidad -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Control administrativo"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor de fuentes."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion practica debe estar juridicamente fundamentada."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Sin estructura valida no hay control confiable de citas y reglas."
        },
        {
          "source": "Control administrativo",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La materia exige aplicacion profesional en ambitos de administracion y control."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "derecho-administrativo-y-control.bib con fuentes base institucionales.",
        "Regla institucional heredada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 18: transferencia transversal limitada a abstracciones estables.",
      "Ciclo 18: se evita traslado de citas doctrinales de Filosofia del Derecho al destino.",
      "Ciclo 18: se refuerzan gates de calidad, estructura reusable y grafo conceptual minimo local."
    ]
  }
}