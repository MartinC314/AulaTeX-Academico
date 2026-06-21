{
  "summary": [
    "Se mantiene sincronizacion transversal sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron estable: problema, conceptos/norma, evidencia, analisis propio y conclusion juridica.",
    "Se conserva identidad UnADM y estructura canonica del destino como fuente principal.",
    "Se preserva compresion lossless por union-dedupe y regla de no regresion.",
    "Se mantiene alerta por salidas no parseables historicas y normalizacion manual obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Alinear entregas a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Usar estructura minima: portada, desarrollo por ejes, conclusion y referencias.",
    "Mantener consistencia entre reporte, presentacion y actividad.",
    "Alinear formato y alcance al producto pedido en planeacion semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual y problema juridico al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir hechos, norma, doctrina y postura propia.",
    "Evitar entregas solo descriptivas; exigir argumentacion del estudiante.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion aplicada sea union-dedupe sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar.",
    "Compilar sin errores criticos, sin referencias ni citas rotas.",
    "Verificar nombres canonicos de archivos contra README local."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; agregar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni conceptos tematicos exclusivos de Filosofia del Derecho.",
    "Propagar reglas generales de integridad, estructura, calidad y trazabilidad.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Reforzar control JSON parseable en toda propagacion recursiva."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, juridica mexicana o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 se usa oficialmente en entregables [supuesto].",
    "Confirmar datos faltantes de figura docente para portada [supuesto].",
    "Confirmar vigencia de fuentes provisionales heredadas de nodos no juridicos [supuesto]."
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
      "Marco normativo y doctrinal pertinente.",
      "Evidencia verificable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles profesionalmente.",
      "Preservar memoria editorial estable, trazable y reusable sin perdida."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Control estricto de estructura JSON."
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
          "justification": "Sin delimitacion del problema no hay analisis pertinente."
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
          "justification": "La postura argumentativa exige respaldo comprobable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La deduplicacion lossless exige estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos.",
        "Programa analitico local fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa institucional.",
        "Memoria historica confirma gate de normalizacion para salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 43: se transfieren solo abstracciones editoriales estables desde nodo transversal.",
      "Ciclo 43: se refuerza gate JSON parseable y normalizacion manual previa.",
      "Ciclo 43: se mantiene ADN UnADM y se evita contaminacion tematica entre materias no equivalentes.",
      "Ciclo 43: consolidacion lossless por union-dedupe sin eliminar reglas utiles previas."
    ]
  }
}