{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas editoriales estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron comun reusable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva alerta institucional: no propagar salidas no parseables sin normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Relacionar cada actividad con seguridad social cuando aplique."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Normalizar manualmente respuestas no estructuradas antes de propagar.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Normalizar nombres de archivo si aparecen tokens o caracteres corruptos."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "Verificar que cada cita LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y estables en nodos no equivalentes.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar transferencia de identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas locales del destino como autoridad para decisiones curriculares.",
    "Conservar bandera de riesgo historica por salidas no parseables de ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar si LDE-S2B1 es codigo oficial del curso en fuentes institucionales [supuesto].",
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si la plantilla de Actividad 1 del destino exige secciones adicionales de rubrica [supuesto].",
    "Confirmar nombre oficial de figura docente para metadatos de portada [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Marco normativo y doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio argumentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para practica profesional.",
      "Asegurar consistencia editorial entre reporte, presentacion y memoria.",
      "Permitir propagacion segura por reglas parseables, trazables y deduplicadas."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Marcado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La validez de la conclusion exige fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo documental."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura requiere estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "El sello institucional orienta claridad, rigor y aplicabilidad profesional."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y control editorial.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local del destino contiene base institucional y normativa vigente.",
        "Memoria origen aporta patron estable de problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 38: se transfieren abstracciones estables sin contenido tematico ajeno.",
      "Ciclo 38: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 38: se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles.",
      "Ciclo 38: se fortalece grafo conceptual comun para sincronizacion transversal."
    ]
  }
}