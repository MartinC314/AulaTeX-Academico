{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin perdida.",
    "Se preserva identidad UnADM y canon local de Derecho a la Seguridad Social.",
    "Se refuerzan abstracciones estables: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate critico: bloquear propagacion si no hay JSON parseable.",
    "Se conserva trazabilidad de reglas provisionales y marcado explicito de [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino transversal."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia desde el inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar correspondencia entre citas en texto y archivo .bib local.",
    "Comprobar que la compresion sea lossless por union-dedupe y sin regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni rutas corruptas.",
    "Normalizar nombres de archivo con marcadores o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y normativas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar a nodos laterales solo abstracciones editoriales estables.",
    "No propagar datos curriculares especificos fuera de la misma materia.",
    "Propagar recursivamente solo despues de validar JSON y gates de calidad.",
    "Reforzar patrones argumentativos comunes sin copiar redaccion literal.",
    "Mantener bandera historica: ciclo 1 requiere normalizacion manual si se reutiliza."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o etiqueta local [supuesto].",
    "Confirmar si las plantillas de Actividad 1 del destino ya estan materializadas y vigentes.",
    "Confirmar criterio local para jurisprudencia minima por actividad [supuesto]."
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
      "Analisis propio no descriptivo.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util profesionalmente.",
      "Asegurar coherencia editorial entre identidad institucional, estructura y calidad.",
      "Permitir propagacion segura entre nodos por reglas estables y auditables."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Marcado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Trazabilidad de fuentes y decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Encuadrar problema.",
      "Fijar objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con implicacion practica."
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
          "justification": "No hay analisis solido sin pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La validez del cierre depende del fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere respaldo trazable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion lossless por union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README destino define estructura canonica y artefactos.",
        "Programa analitico destino fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Memoria previa confirma gate de JSON parseable y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: se deduplican reglas repetidas y se preservan todas las utiles.",
      "Ciclo 8: se transfiere solo abstraccion estable desde nodo transversal no equivalente.",
      "Ciclo 8: se evita mezclar contenido tematico de Filosofia con Seguridad Social.",
      "Ciclo 8: se mantiene alerta historica por salidas no parseables y control de normalizacion."
    ]
  }
}