{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con union-dedupe sin perdida.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad JSON como nucleo estable.",
    "Se mantiene separacion: reglas editoriales transferibles si, contenido tematico de Filosofia no.",
    "Se refuerza patron comun reusable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se integra canon local del destino: README, programa analitico y .bib de seguridad social.",
    "Se conserva alerta historica: salidas no parseables requieren normalizacion manual antes de propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Vincular el desarrollo con derecho a la seguridad social cuando corresponda.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que afirmaciones relevantes tengan respaldo o marca [supuesto].",
    "Verificar consistencia entre citas en texto y archivo .bib local.",
    "Confirmar compresion lossless por union-dedupe y sin regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Normalizar rutas o nombres con marcadores corruptos antes de compilar.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Verificar que toda cita LaTeX tenga clave BibTeX existente."
  ],
  "propagation_hints": [
    "Propagar lateral y arriba solo reglas estables ya validadas.",
    "Compartir abstractions editoriales, no redaccion literal ni contenido tematico ajeno.",
    "Propagar reglas curriculares solo dentro de la misma materia.",
    "Propagar reglas generales de calidad, JSON, citas y supuestos a nodos compatibles.",
    "Mantener bandera de riesgo historica por ciclos con salida no parseable.",
    "Aplicar estrategia progresiva y conservadora en cada ciclo."
  ],
  "open_questions": [
    "Confirmar si sigue vigente la referencia provisional heredada desde ingenieria [supuesto].",
    "Confirmar norma de citacion exigida en esta materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar datos oficiales de figura docente para plantilla [supuesto].",
    "Confirmar si cada actividad exige reporte, presentacion o ambos.",
    "Confirmar si hay rubrica formal para ponderar profundidad argumentativa.",
    "Confirmar vigencia periodica de URLs normativas del .bib local."
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
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para la practica.",
      "Preservar memoria editorial persistente sin perdida ni regresion.",
      "Asegurar coherencia institucional, tecnica y argumentativa entre entregables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
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
        "JSON parseable",
        "Compresion union-dedupe",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Derecho a la seguridad social"
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
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere base legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion segura exige estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "La identidad comun permite sincronizacion transversal sin perder contexto local."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos y control editorial.",
        "Programa analitico local define proposito y ejes de trabajo de la materia.",
        ".bib local contiene base institucional y normativa verificable.",
        "Historial conserva regla de bloqueo por salida no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se reforzo nucleo estable transversal sin mezclar contenido tematico de Filosofia.",
      "Ciclo 5: se consolidaron gates de calidad y trazabilidad de supuestos.",
      "Ciclo 5: se mantuvo compresion lossless por union-dedupe y sin regresion."
    ]
  }
}