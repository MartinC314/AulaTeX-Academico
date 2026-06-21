{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de Filosofia del Derecho y materia Derecho a la Seguridad Social.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, evidencia verificable, analisis propio y conclusion juridica.",
    "Se mantiene control institucional: no propagar salidas no parseables sin normalizacion.",
    "Se confirma compresion lossless por union-dedupe y sin regresion.",
    "Se evita transferir contenido tematico literal de Filosofia; solo se transfieren abstracciones editoriales reutilizables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia destino como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato y alcance al producto solicitado en planeacion semanal.",
    "Mantener consistencia editorial entre README, programa analitico, reporte y presentacion."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar cada producto con el campo de seguridad social cuando corresponda.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres de archivo y resolver tokens o marcadores sin expandir antes de compilar.",
    "Verificar rutas contra README y programa analitico antes de fijarlas como canon."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y normativa juridica vigente verificable.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "Agregar nuevas referencias solo tras verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "En saltos transversales, transferir solo abstracciones estables y no redaccion literal.",
    "Conservar reglas locales del destino cuando exista conflicto tematico.",
    "Mantener bandera de riesgo por antecedentes de salidas no parseables en ciclos tempranos.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin reemplazar."
  ],
  "open_questions": [
    "Confirmar rubrica de evaluacion especifica de la materia para ajustar profundidad argumentativa.",
    "Confirmar si existe norma de citacion obligatoria adicional (APA, ISO o juridica mexicana) [supuesto].",
    "Confirmar vigencia de cualquier fuente provisional heredada de nodos no juridicos [supuesto].",
    "Verificar estado completo y vigencia de notas en .bib local (entrada LISSSTE parece truncada) [supuesto]."
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
      "Problema juridico delimitado.",
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en un producto juridico verificable y util para la practica profesional.",
      "Preservar memoria editorial persistente sin perdida de reglas utiles.",
      "Garantizar calidad tecnica y academica en produccion LaTeX."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de fuentes y decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Presentar evidencia pertinente.",
      "Fijar postura propia razonada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Trazabilidad bibliografica"
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
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion confiable."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Evita duplicados y conserva reglas utiles sin recorte."
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
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar fuentes y evitar invenciones."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y archivos oficiales.",
        "Programa analitico del destino fija proposito y ejes juridicos.",
        "Archivo .bib local contiene base normativa e institucional verificable.",
        "Memorias previas registran necesidad de normalizacion ante salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: se refuerza patron transversal problema-fundamento-evidencia-analisis-conclusion.",
      "Ciclo 69: se mantiene regla dura de JSON parseable antes de propagacion.",
      "Ciclo 69: se preserva identidad UnADM y curricularidad local del destino.",
      "Ciclo 69: se evita importar contenido tematico literal de Filosofia del Derecho."
    ]
  }
}