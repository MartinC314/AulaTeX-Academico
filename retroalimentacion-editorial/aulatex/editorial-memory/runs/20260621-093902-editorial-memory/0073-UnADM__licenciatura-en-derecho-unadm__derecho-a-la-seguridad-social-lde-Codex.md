{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con enfoque conservador.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin regresion.",
    "Se transfiere solo abstraccion estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar salidas no parseables sin normalizacion.",
    "Se confirma uso del canon local del destino: README, programa analitico y .bib propio."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin perdida.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia editorial entre reporte, presentacion y programa analitico.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; exigir argumentacion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar el contenido con seguridad social cuando corresponda al destino.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que la compresion aplicada sea lossless por union-dedupe."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta de espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos, sin referencias ni citas rotas.",
    "Normalizar nombres de archivo y resolver marcadores corruptos antes de compilar.",
    "Mantener metadatos institucionales consistentes en todos los .tex."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar nuevas fuentes solo si son pertinentes al tema y verificables."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir a laterales solo abstracciones editoriales estables, no contenido tematico literal.",
    "Preservar reglas locales del destino sobre seguridad social.",
    "Mantener bandera de riesgo historico por salidas no parseables de ciclos tempranos.",
    "Evitar regresion: identidad UnADM, control JSON, trazabilidad y control bibliografico."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o etiqueta interna [supuesto].",
    "Confirmar rubrica vigente por actividad para ajustar profundidad argumentativa.",
    "Confirmar datos faltantes de portada (figura docente) cuando exista fuente oficial.",
    "Confirmar si persiste alguna fuente provisional heredada no juridica para depuracion [supuesto]."
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
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar coherencia institucional y tecnica entre contenido, estructura y fuentes."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de reglas provisionales."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
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
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar de fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentativa requiere respaldo documental."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion lossless por union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica de archivos.",
        "Programa analitico define proposito y ejes de trabajo juridicos.",
        "Archivo .bib local confirma base normativa e institucional vigente.",
        "Historial institucional reporta salidas no parseables que exigen normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 73: se refuerza patron transversal estable sin mover contenido tematico de filosofia al destino.",
      "Ciclo 73: se mantiene regla de bloqueo por JSON no parseable.",
      "Ciclo 73: se confirma compresion lossless por deduplicacion y sin recorte.",
      "Ciclo 73: se preservan reglas utiles previas y se agregan mejoras verificables del contexto local."
    ]
  }
}