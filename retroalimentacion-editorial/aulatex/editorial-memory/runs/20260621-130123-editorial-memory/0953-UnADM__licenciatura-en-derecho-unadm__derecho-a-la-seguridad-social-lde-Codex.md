{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y sin regresion.",
    "Se preservan reglas validas del destino y se incorporan abstracciones estables del origen.",
    "Se refuerza patron comun: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene identidad UnADM y control de normalizacion estructurada antes de propagar.",
    "Se actualiza estructura canonica local con archivos de Actividad 1 visibles en README.",
    "Se conserva compresion lossless por union-dedupe."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato al producto solicitado por planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Distinguir hechos, conceptos, norma y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con consigna local de actividad."
  ],
  "latex_rules": [
    "Conservar plantilla base local y personalizar solo campos variables.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener metadatos institucionales y de curso consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Resolver nombres o tokens corruptos en rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas vigentes verificables.",
    "Agregar solo referencias consultables y pertinentes a la actividad.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Propagar recursivamente solo reglas validadas en JSON y estructura.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Reforzar en laterales: identidad, estructura reusable, quality gates y grafo conceptual.",
    "Si falta consigna local, propagar reglas generales y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 1 en Seguridad Social.",
    "Confirmar si la materia exige norma de citacion especifica (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 sigue oficial en documentos de entrega [supuesto].",
    "Verificar vigencia de fuentes provisionales heredadas desde nodos no juridicos [supuesto].",
    "Confirmar si se requiere archivo .bib complementario por actividad o basta el .bib central."
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
      "Fundamento normativo verificable.",
      "Evidencia pertinente.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Sostener continuidad editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
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
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura gana solidez con fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Preserva reglas utiles sin perdida ni duplicados."
        }
      ],
      "evidence": [
        "README local define estructura canonica y archivos base de actividad.",
        "Programa analitico local define proposito y ejes juridicos.",
        "Archivo .bib local aporta base institucional y normativa verificable.",
        "Memoria origen confirma patron reusable de cinco ejes y quality gates."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: se transfirieron solo abstracciones estables por relacion transversal.",
      "Ciclo 19: se evitaron contenidos tematicos especificos de Filosofia del Derecho.",
      "Ciclo 19: se reforzaron identidad, estructura reusable, gates de calidad y grafo conceptual.",
      "Ciclo 19: se mantuvo compresion lossless por deduplicacion sin recorte."
    ]
  }
}