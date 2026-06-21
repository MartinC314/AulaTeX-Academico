{
  "summary": [
    "Se mantiene identidad UnADM y canon local de la materia destino.",
    "Se refuerza sincronizacion transversal con reglas estables no tematicas.",
    "Se preserva compresion lossless por union-dedupe sin regresion.",
    "Se mantiene alerta por salidas no parseables y normalizacion manual cuando aplique.",
    "Se consolida patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Alinear cada entrega a ejes: problema, conceptos/norma, evidencia, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en marco conceptual-normativo, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Confirmar soporte verificable o marca [supuesto] en cada afirmacion relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta de espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar rutas y nombres de archivo corruptos antes de compilar.",
    "Resolver tokens sin expandir en README o programa analitico antes de canonizar nombres."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar nuevas fuentes solo si son pertinentes al tema del destino."
  ],
  "propagation_hints": [
    "Propagar a laterales no equivalentes solo abstracciones editoriales estables.",
    "No transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Propagar recursivamente solo tras pasar gates de JSON y estructura.",
    "Reforzar reglas globales: identidad, calidad, trazabilidad y control bibliografico.",
    "Mantener reglas locales del destino como prioridad semantica."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia [supuesto].",
    "Confirmar si existe rubrica oficial por actividad en esta materia [supuesto].",
    "Verificar nombre oficial de figura docente para plantilla [supuesto].",
    "Confirmar si la alerta de fuente provisional externa sigue vigente en Derecho [supuesto]."
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
      "Identidad institucional consistente.",
      "Problema juridico delimitado.",
      "Fundamento normativo verificable.",
      "Evidencia trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable.",
      "Asegurar calidad reproducible entre nodos y ciclos.",
      "Conservar memoria editorial sin perdida ni regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Marcado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Evita duplicados y conserva reglas utiles."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de fundamento legal verificable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Coherencia editorial transversal",
          "kind": "supports",
          "justification": "Unifica tono, formato y criterios de calidad."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y archivos base.",
        "Programa analitico del destino define proposito y ejes juridicos.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Regla persistente: normalizar salidas no estructuradas antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 61: se transfieren solo abstracciones estables entre nodos no equivalentes.",
      "Ciclo 61: se evita mezclar contenido tematico de Filosofia con Seguridad Social.",
      "Ciclo 61: se refuerzan gates de JSON, trazabilidad y evidencia.",
      "Ciclo 61: se mantiene estrategia conservadora sin eliminar reglas utiles previas."
    ]
  }
}