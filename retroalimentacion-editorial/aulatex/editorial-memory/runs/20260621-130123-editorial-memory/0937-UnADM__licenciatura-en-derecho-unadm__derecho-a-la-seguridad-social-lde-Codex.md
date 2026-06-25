{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y estructura por ejes sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza control de calidad: JSON parseable, normalizacion previa y trazabilidad de supuestos.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Se actualiza canon local con README y programa analitico del destino como fuentes rectoras."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README y programa analitico como canon de estructura local.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Mantener consistencia entre reporte, presentacion y bibliografia local."
  ],
  "activity_rules": [
    "Delimitar problema y objetivo desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion relevante tenga respaldo o marca [supuesto].",
    "Verificar correspondencia entre producto entregado y consigna vigente.",
    "Confirmar compresion lossless por union-dedupe y ausencia de regresion."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener compatibilidad de compilacion sin errores criticos ni referencias rotas.",
    "Usar codificacion correcta para espanol en .tex y .bib.",
    "Mantener nombres de archivo canonicos del README.",
    "Corregir rutas, marcadores o tokens no resueltos antes de compilar.",
    "No introducir comandos no estandar sin justificacion tecnica."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central del destino.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Validar correspondencia entre citas en texto y entradas BibTeX.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo reglas generales estables ya validadas.",
    "No propagar contenido tematico especifico de Filosofia del Derecho al destino.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener bandera historica de riesgo por salidas no parseables en ciclos tempranos.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin recorte."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia destino (APA, ISO o institucional) [supuesto].",
    "Confirmar si LDE-S2B1 es codigo oficial o solo etiqueta local [supuesto].",
    "Confirmar datos faltantes de plantilla (figura docente) cuando exista fuente oficial.",
    "Confirmar si la alerta heredada desde ingenieria sigue vigente para este dominio juridico [supuesto].",
    "Confirmar consignas activas por actividad para ajustar profundidad argumentativa."
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
      "Marco normativo y doctrinal verificable.",
      "Evidencia pertinente.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir cada consigna en producto juridico verificable y util para practica profesional.",
      "Preservar memoria editorial persistente sin perdida y sin regresion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto] cuando falte evidencia.",
      "Separacion clara entre marco, analisis y cierre."
    ],
    "argumentative_patterns": [
      "Encuadrar problema.",
      "Fijar objetivo.",
      "Fundamentar con normas y doctrina.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Cerrar con implicacion juridica practica."
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
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La reutilizacion segura exige estructura valida."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin duplicar ni recortar."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y artefactos base.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local del destino contiene base institucional y normativa verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se transfiere patron editorial comun desde actividad fuente como abstraccion estable.",
      "Ciclo 15: se evita transferencia de redaccion literal y contenido tematico no equivalente.",
      "Ciclo 15: se refuerzan gates de parseo JSON, supuestos y trazabilidad de fuentes provisionales.",
      "Ciclo 15: se mantiene canon local del destino y control bibliografico central."
    ]
  }
}