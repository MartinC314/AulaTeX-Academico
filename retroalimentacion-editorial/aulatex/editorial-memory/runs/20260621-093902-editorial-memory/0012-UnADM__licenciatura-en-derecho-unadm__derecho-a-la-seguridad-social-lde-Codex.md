{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables.",
    "Se preserva identidad UnADM y contexto curricular local del destino.",
    "Se refuerza patron comun: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se conserva compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar nombre local de materia: Derecho a la seguridad social.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas utiles previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de materia como canon estructural local.",
    "Alinear entregas a ejes: problema, conceptos/norma, producto, analisis y conclusion.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y programa analitico."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, conceptos, normas y opinion propia.",
    "Relacionar el contenido con seguridad social cuando corresponda al destino.",
    "No asumir fuentes de semanas posteriores sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar correspondencia del producto con la consigna vigente.",
    "Confirmar que la compresion sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base local y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Normalizar rutas y nombres de archivo antes de compilar.",
    "Resolver tokens sin expandir en README o programa analitico antes de canonizarlos."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar solo referencias nuevas verificadas y pertinentes al producto."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
    "Propagar reglas generales de identidad, estructura, calidad y trazabilidad.",
    "Mantener reglas locales de seguridad social como capa prioritaria del destino.",
    "Conservar alerta historica: ciclos con salida no parseable requieren normalizacion manual."
  ],
  "open_questions": [
    "Confirmar norma formal de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial vigente del curso [supuesto].",
    "Confirmar si la fuente provisional heredada desde ingenieria sigue aplicando al dominio Derecho [supuesto].",
    "Confirmar plantilla oficial para figura docente cuando exista dato institucional."
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
        "Materia destino: Derecho a la seguridad social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema juridico delimitado.",
      "Marco normativo y doctrinal verificable.",
      "Evidencia relevante y trazable.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y utiles para la practica.",
      "Preservar memoria editorial persistente sin perdida por compresion.",
      "Asegurar coherencia transversal entre nodos con contexto local respetado."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto] en vacios de evidencia.",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion profesional concreta."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal pertinente.",
      "Integrar evidencia verificable.",
      "Fijar postura propia con justificacion.",
      "Concluir con efecto juridico practico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion transferible",
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
          "justification": "Sin delimitacion del problema no hay analisis juridico consistente."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica debe sustentarse en fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion lossless exige estructura valida."
        },
        {
          "source": "Identidad UnADM",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La linea institucional orienta el cierre profesional y etico."
        }
      ],
      "evidence": [
        "README local define estructura canonica de archivos.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional vigente.",
        "Memoria origen valida patron editorial comun reusable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: se transfiere solo abstraccion estable desde actividad de Filosofia a materia de Seguridad Social.",
      "Ciclo 12: se refuerzan gates de JSON parseable y normalizacion previa.",
      "Ciclo 12: se evita mezclar contenido tematico especifico del origen en el destino.",
      "Ciclo 12: se preservan reglas locales del destino y se integran mejoras verificables sin recorte."
    ]
  }
}