{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables y reutilizables.",
    "Se preserva identidad UnADM y contexto curricular local de Derecho a la Seguridad Social.",
    "Se refuerza patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se conserva alerta por antecedentes de salida no parseable y necesidad de normalizacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas o materias sin validacion local [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Mantener codificacion en español y acentos correctos en .tex y .bib.",
    "Conservar plantilla base y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Resolver tokens o marcadores sin expandir en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y marcos juridicos verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar fuentes ni claves BibTeX.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico propio de Filosofia del Derecho.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener reglas locales de Seguridad Social como capa dominante del destino.",
    "Aplicar estrategia progresiva y conservadora: primero validar, despues propagar.",
    "Conservar trazabilidad de reglas provisionales con etiqueta [supuesto]."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si existe rubrica oficial por actividad para modular profundidad argumentativa [supuesto].",
    "Confirmar datos faltantes de plantilla (figura docente u otros) [supuesto].",
    "Confirmar vigencia de cualquier fuente provisional heredada de otros dominios [supuesto]."
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
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Producto juridico verificable orientado por problema, fundamento, evidencia, analisis y cierre.",
      "Persistencia editorial sin regresion mediante union-dedupe.",
      "Transferencia transversal de metodo, no de contenido tematico."
    ],
    "reason_for_being": [
      "Estandarizar entregas academicas con calidad verificable y utilidad profesional.",
      "Garantizar memoria editorial reutilizable entre actividades y materias compatibles.",
      "Reducir errores de forma, citacion y estructura antes de evaluacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y conclusion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Encuadre del problema.",
      "Objetivo puntual.",
      "Marco normativo/doctrinal.",
      "Contraste de evidencia.",
      "Postura propia sustentada.",
      "Conclusion transferible a practica profesional."
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
          "justification": "Sin delimitacion del problema no hay analisis juridico pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "La postura academica gana solidez con respaldo documental."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicacion."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos y control editorial.",
        "Programa analitico local define proposito y ejes de trabajo de la materia.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Regla transversal consolidada: normalizar salidas no estructuradas antes de propagacion."
      ]
    },
    "reinforcement_log": [
      "Se reforzo identidad UnADM sin mover contexto curricular local del destino.",
      "Se integraron patrones de actividad estables del origen como abstracciones metodologicas.",
      "Se excluyo transferencia de contenido doctrinal especifico de Filosofia del Derecho por no equivalencia temática.",
      "Se mantuvo control de calidad por JSON parseable y trazabilidad de supuestos.",
      "Se consolido memoria minima robusta y expandible para propagacion transversal."
    ]
  }
}