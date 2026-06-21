{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables reutilizables.",
    "Se preserva identidad UnADM del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron comun: problema, fundamento normativo, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe y politica de no regresion.",
    "Se conserva gate critico: no propagar si la salida no es JSON parseable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema juridico desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que no haya regresion de reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Usar codificacion y acentos en espanol de forma consistente en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Normalizar nombres de archivo si aparecen tokens o marcadores sin expandir [supuesto]."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como base bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo fuentes realmente consultables con metadatos minimos completos.",
    "No inventar referencias; marcar faltantes como pendientes [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita usada tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo reglas abstractas y estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas locales del destino como autoridad primaria.",
    "Aplicar union-dedupe en cada ciclo para evitar duplicados y perdida.",
    "Conservar bandera historica de riesgo por salidas no parseables en ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar si el codigo local LDE-S2B1 es oficial o solo interno [supuesto].",
    "Confirmar norma de citacion exigida por la materia (APA, ISO, institucional o juridica) [supuesto].",
    "Confirmar si todas las plantillas de Actividad-1 listadas en README existen fisicamente.",
    "Confirmar dato oficial de figura docente para metadatos de portada [supuesto].",
    "Confirmar si persiste alguna fuente provisional heredada desde nodos no juridicos [supuesto]."
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
        "Materia destino: Derecho a la seguridad social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Identidad institucional consistente.",
      "Problema juridico bien delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia y analisis propio articulados.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles.",
      "Preservar memoria editorial persistente sin perdida ni regresion.",
      "Permitir reutilizacion transversal segura entre nodos compatibles."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Trazabilidad de decisiones editoriales por ciclo."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
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
        "Compresion union-dedupe",
        "No regresion editorial"
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
          "justification": "Sin delimitacion del problema no hay argumentacion valida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia se fortalece con pruebas y fuentes."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "No regresion editorial",
          "kind": "supports",
          "justification": "Permite conservar reglas utiles sin recorte."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y archivos base.",
        "Programa analitico destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional vigente.",
        "Historial institucional reporta incidentes de salida no parseable y exige normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se transfieren solo abstracciones estables desde actividad de Filosofia hacia materia de Seguridad Social.",
      "Ciclo 15: se preservan reglas locales del destino como prioridad semantica.",
      "Ciclo 15: se refuerzan gates JSON, trazabilidad de supuestos y control bibliografico.",
      "Ciclo 15: se elimina duplicidad textual por union-dedupe sin perdida de reglas utiles."
    ]
  }
}