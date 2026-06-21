{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe sin perdida.",
    "Se preservan reglas validas del destino y se integran abstracciones estables del origen.",
    "Se refuerza patron comun: problema, conceptos o norma, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene separacion entre reglas editoriales transferibles y contenido tematico local de seguridad social.",
    "Se conserva alerta institucional por antecedentes de salidas no parseables y normalizacion manual obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de la materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; aplicar solo union y deduplicacion.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad del origen de reglas provisionales."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Distinguir hechos, conceptos, normas y postura propia.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas; incluir argumentacion propia.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar manualmente toda salida no estructurada antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Confirmar compresion lossless por union-dedupe, sin recorte ni regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion correcta en español en .tex y .bib.",
    "Mantener metadatos institucionales y de curso consistentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir rutas, nombres y marcadores corruptos antes de compilar.",
    "Compilar sin errores criticos, sin referencias rotas y con citas resueltas."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Verificar correspondencia entre citas en texto y entradas BibTeX.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir a nodos no equivalentes solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico especifico de otra materia.",
    "Mantener bandera de riesgo por ciclos con salida no parseable.",
    "Reforzar en laterales: identidad UnADM, calidad JSON, evidencia y trazabilidad."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local LDE-S2B1 es obligatorio en todas las portadas [supuesto].",
    "Confirmar si actividad por actividad requiere .bib complementario o basta el .bib central.",
    "Verificar si persiste la referencia provisional heredada desde otro dominio y depurarla [supuesto]."
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
      "Producto juridico verificable con problema, fundamento, evidencia, analisis y cierre.",
      "Separacion clara entre marco normativo, analisis propio y conclusion.",
      "Trazabilidad y control de calidad como base de memoria persistente."
    ],
    "reason_for_being": [
      "Convertir consignas en entregables juridicos solidos y auditables.",
      "Garantizar consistencia editorial entre actividades, formatos y ciclos.",
      "Permitir propagacion transversal segura sin contaminar contexto local."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Cierre con utilidad profesional transferible.",
      "Sin duplicados y sin perdida de reglas utiles."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal pertinente.",
      "Contrastar evidencia verificable.",
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
          "justification": "Sin delimitacion inicial no hay argumentacion consistente."
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
          "justification": "La postura propia debe sostenerse con fuentes trazables."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura exige estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica y archivos base.",
        "Programa analitico local define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa.",
        "Memoria previa registra riesgo por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 66: deduplicacion completa de reglas repetidas en identidad, estructura y calidad.",
      "Ciclo 66: incorporado patron transversal del origen sin arrastrar contenido tematico de Filosofia del Derecho.",
      "Ciclo 66: reforzado gate de JSON parseable y normalizacion manual previa a propagacion.",
      "Ciclo 66: mantenida compatibilidad con canon local de Seguridad Social."
    ]
  }
}