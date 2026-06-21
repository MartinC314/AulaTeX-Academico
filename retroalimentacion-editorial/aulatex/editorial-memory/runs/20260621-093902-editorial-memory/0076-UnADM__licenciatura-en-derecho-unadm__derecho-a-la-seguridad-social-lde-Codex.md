{
  "summary": [
    "Se consolida sincronizacion transversal con union-dedupe sin regresion.",
    "Se preserva identidad UnADM y enfoque juridico del destino.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
    "Se refuerza patron editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de JSON parseable y normalizacion previa a propagacion.",
    "Se evita mezclar contenido tematico especifico de Filosofia en Seguridad Social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar cada entrega con el campo de seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que la compresion sea lossless por union-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla base y personalizar solo campos variables.",
    "Mantener metadatos institucionales y curriculares consistentes en .tex.",
    "Usar estructura minima: portada, desarrollo, conclusion y referencias.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas, marcadores o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que cada cita del .tex exista en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y estructuradas.",
    "Compartir a laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico no equivalente.",
    "Mantener alerta de normalizacion manual para antecedentes no parseables.",
    "Priorizar gates de calidad, identidad y grafo conceptual en saltos transversales.",
    "Evitar regresion de reglas utiles ya consolidadas."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o etiqueta operativa interna [supuesto].",
    "Confirmar si la figura docente debe permanecer como pendiente en plantillas base.",
    "Validar vigencia de toda fuente provisional heredada ajena al dominio juridico.",
    "Confirmar consignas de Actividad 1 en esta materia para ajustar granularidad estructural."
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
      "Marco normativo y conceptual pertinente.",
      "Evidencia verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util.",
      "Preservar identidad institucional sin perder rigor tecnico.",
      "Garantizar memoria editorial reutilizable entre nodos compatibles."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo o doctrinal.",
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
        "Compresion lossless por union-dedupe"
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
          "justification": "Sin delimitacion del problema no hay analisis pertinente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura propia exige respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion lossless por union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y archivos base.",
        "Programa analitico del destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Memoria origen aporta patron editorial estable reutilizable transversalmente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 76: se refuerza sincronizacion transversal sin arrastre tematico indebido.",
      "Ciclo 76: se consolidan gates de JSON parseable, trazabilidad y supuestos.",
      "Ciclo 76: se preserva ADN argumentativo comun entre materias de Derecho."
    ]
  }
}