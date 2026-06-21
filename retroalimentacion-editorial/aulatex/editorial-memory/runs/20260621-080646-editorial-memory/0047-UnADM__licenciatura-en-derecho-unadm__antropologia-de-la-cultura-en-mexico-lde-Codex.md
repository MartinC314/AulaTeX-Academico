{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad de Filosofia del Derecho hacia materia de Antropologia con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, estructura canonica y gates de calidad sin regresion.",
    "Se transfieren solo abstracciones editoriales estables: objetivo, evidencia, analisis propio, coherencia y cierre transferible.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al nodo destino no equivalente.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se refuerza normalizacion obligatoria cuando existan salidas no JSON parseables heredadas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Conservar adscripcion a Licenciatura en Derecho.",
    "Conservar ubicacion curricular local del destino: semestre 4, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisional toda fuente heredada no verificada disciplinarmente.",
    "No trasladar metadatos curriculares de Filosofia del Derecho a Antropologia."
  ],
  "structure_rules": [
    "Iniciar cada producto con objetivo puntual y encuadre del problema juridico o social.",
    "Organizar secciones en: conceptos clave, marco teorico o normativo, analisis propio y cierre.",
    "Alinear el formato del artefacto con la planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia.",
    "Usar README y programa analitico como guias de estructura editable.",
    "Resolver placeholders en rutas y nombres antes de compilar o citar."
  ],
  "activity_rules": [
    "Definir problema y alcance al inicio.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Distinguir evidencia, interpretacion y opinion.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion transferible a practica profesional juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Exigir esquema minimo completo antes de reutilizar memoria.",
    "Normalizar respuestas no estructuradas antes de propagacion recursiva.",
    "Confirmar consistencia entre metadatos del documento y datos curriculares locales.",
    "Validar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No promover reglas provisionales a definitivas sin verificacion local."
  ],
  "latex_rules": [
    "Mantener plantilla base .tex del destino como referencia canonica.",
    "Usar configuracion en espanol y acentos correctos en .tex y .bib.",
    "Mantener clase y formato por defecto salvo justificacion academica.",
    "Actualizar documenttitle y documentsubtitle por actividad real.",
    "Mantener claves BibTeX estables y sin duplicados.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Corregir rutas corruptas detectadas en README antes de enlazar archivos."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo referencias verificables.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales pertinentes.",
    "Registrar fuentes especificas por actividad en antropologia-de-la-cultura-en-mexico.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener entradas base institucionales ya existentes del destino."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas validadas y parseables.",
    "Compartir solo abstracciones estables entre nodos no equivalentes.",
    "Mantener union-dedupe lossless y no eliminar reglas utiles previas.",
    "Registrar incidencias de parseo como alerta transversal reutilizable.",
    "Si falta contexto local, crear cerebro minimo y dejar vacios como preguntas abiertas.",
    "Etiquetar supuestos explicitamente en cada salto recursivo."
  ],
  "open_questions": [
    "Supuesto: falta consigna especifica de actividades actuales de Antropologia; confirmar tipo de entregable por semana.",
    "Confirmar rubrica oficial de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar estandar de citas institucional unico para la licenciatura.",
    "Confirmar si LDE-S4B2 es clave oficial definitiva o clave operativa local.",
    "Confirmar politica de conclusion juridica en actividades con enfoque antropologico-cultural."
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
        "Materia destino: Antropologia de la cultura en Mexico.",
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
      "Estandarizar productos academicos consistentes y verificables.",
      "Asegurar coherencia entre planeacion semanal y entregable final.",
      "Preservar identidad UnADM con rigor editorial transversal."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin relleno.",
      "Supuestos marcados de forma visible.",
      "Citas trazables en puntos clave.",
      "Conclusion util para practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis -> conclusion.",
      "Afirmacion -> respaldo -> interpretacion propia.",
      "Pregunta guia -> desarrollo coherente -> respuesta final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Validacion JSON parseable",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Supuestos marcados"
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
          "justification": "La propagacion confiable exige estructura valida."
        },
        {
          "source": "Integridad academica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "No hay integridad sin respaldo trazable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura personal se fortalece con fuentes comprobables."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion deriva del razonamiento y no del resumen."
        },
        {
          "source": "Supuestos marcados",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Diferencia hechos confirmados de elementos pendientes."
        }
      ],
      "evidence": [
        "README local define identidad UnADM y pauta editorial canonica.",
        "Programa analitico local define ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local contiene fuentes institucionales base verificables.",
        "Memoria heredada reporta incidencias de parseo y obliga normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 47: deduplicadas reglas repetidas de identidad, estructura y calidad.",
      "Ciclo 47: retenidas alertas de parseo no JSON como gate transversal.",
      "Ciclo 47: incorporadas abstracciones estables del origen sin arrastrar contenido tematico no equivalente.",
      "Ciclo 47: preservada estrategia conservadora de no regresion."
    ]
  }
}