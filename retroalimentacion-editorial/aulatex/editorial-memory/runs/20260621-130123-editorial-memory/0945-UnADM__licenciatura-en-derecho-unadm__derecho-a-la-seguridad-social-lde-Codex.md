{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables.",
    "Se preserva identidad UnADM y estructura canonica local de Derecho a la Seguridad Social.",
    "Se refuerza patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union-dedupe sin regresion.",
    "Se conserva alerta institucional: ciclo 1 con salida no parseable requiere normalizacion manual."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y evidencias de la materia."
  ],
  "activity_rules": [
    "Delimitar problema juridico y pregunta guia al inicio.",
    "Vincular argumentos con norma, doctrina o datos verificables.",
    "Incluir postura propia sustentada; evitar texto solo descriptivo.",
    "Distinguir hechos, conceptos, normas y opinion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No asumir fuentes de otras semanas o materias sin verificacion local [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Comprobar correspondencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas, marcadores o tokens sin expandir antes de compilar.",
    "No copiar bloques LaTeX completos en memoria; guardar reglas reutilizables."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales UnADM y normativas vigentes verificables.",
    "Agregar solo referencias consultables con metadatos minimos completos.",
    "No inventar fuentes; marcar faltantes como pendientes o [supuesto].",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en saltos transversales.",
    "No transferir contenido tematico literal de Filosofia del Derecho al destino.",
    "Propagar recursivamente solo reglas validadas por quality gates.",
    "Conservar bandera de riesgo de ciclo 1 en nodos compatibles.",
    "Priorizar identidad, estructura reusable, calidad y grafo conceptual."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si existe rubrica oficial por actividad para ajustar profundidad argumentativa [supuesto].",
    "Verificar vigencia de toda fuente provisional heredada de nodos externos [supuesto].",
    "Confirmar datos faltantes de plantilla institucional (figura docente) cuando sean oficiales."
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
      "Producto juridico verificable centrado en problema, fundamento, evidencia, analisis y cierre.",
      "Transferencia profesional de conclusiones juridicas.",
      "Persistencia editorial sin regresion mediante union-dedupe."
    ],
    "reason_for_being": [
      "Convertir consignas semanales en entregables juridicos claros y verificables.",
      "Garantizar coherencia institucional, metodologica y bibliografica en toda la materia."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y conclusion.",
      "Cierre con utilidad juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con implicacion juridica transferible."
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
          "justification": "El analisis exige pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay consolidacion segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La identidad fija tono, rigor y utilidad profesional del cierre."
        }
      ],
      "evidence": [
        "README de materia define estructura canonica y control editorial.",
        "Programa analitico define proposito y ejes juridicos del destino.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Regla institucional heredada: normalizar salidas no parseables antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se preservan reglas validas previas del destino sin eliminaciones.",
      "Ciclo 17: se transfieren solo abstracciones estables del origen por relacion transversal.",
      "Ciclo 17: se evita mezclar contenido tematico especifico de Filosofia con Seguridad Social.",
      "Ciclo 17: se refuerzan quality gates de JSON parseable, soporte verificable y union-dedupe."
    ]
  }
}