{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con reglas estables.",
    "Se preserva identidad UnADM y enfoque juridico del destino sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se refuerza patron editorial comun: problema, fundamento, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene compresion lossless por union-dedupe y sin regresion.",
    "Se conserva alerta institucional: salidas no parseables requieren normalizacion manual previa a propagacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Tomar README de materia como canon estructural local.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, producto, analisis y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Mantener consistencia editorial entre reporte, presentacion y programa analitico.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema juridico o social desde el inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar formato y alcance al producto solicitado por planeacion semanal.",
    "No asumir fuentes de semanas o materias distintas sin validacion local [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar aguas abajo.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que toda afirmacion tenga respaldo o marca [supuesto].",
    "Validar correspondencia entre citas en texto y archivo .bib local.",
    "Verificar que la consolidacion sea union-dedupe y sin recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver marcadores o tokens sin expandir en rutas y nombres antes de compilar.",
    "Verificar nombres canonicos de archivos contra README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "Tratar bibliografia heredada de otras materias como no aplicable hasta validacion local [supuesto]."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables a nodos no equivalentes.",
    "Propagar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia literal de redaccion o contenido tematico de Filosofia del Derecho.",
    "Mantener reglas curriculares especificas solo dentro de la misma materia.",
    "Conservar bandera de riesgo por ciclos con salida no parseable.",
    "Aplicar estrategia progresiva y conservadora: agregar mejoras verificables sin eliminar reglas utiles."
  ],
  "open_questions": [
    "Confirmar norma de citacion obligatoria de la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si codigo local de curso LDE-S2B1 sigue vigente [supuesto].",
    "Confirmar si toda plantilla de actividad inicial ya existe y es canonica en README.",
    "Confirmar si persiste alguna fuente provisional heredada ajena a Derecho [supuesto].",
    "Confirmar rubrica oficial para ajustar profundidad argumentativa por actividad."
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
      "Identidad institucional consistente.",
      "Problema juridico delimitado.",
      "Marco normativo verificable.",
      "Evidencia y citas trazables.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto juridico verificable y util profesionalmente.",
      "Garantizar continuidad editorial transversal sin perder contexto local del destino."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Control de trazabilidad de reglas provisionales."
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
          "justification": "Sin delimitacion del problema no hay argumentacion valida."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion juridica exige fundamento legal verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura academica requiere respaldo documental."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe",
          "kind": "depends_on",
          "justification": "La consolidacion segura requiere estructura valida."
        }
      ],
      "evidence": [
        "README local define estructura canonica y artefactos de materia.",
        "Programa analitico local fija proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional.",
        "Reglas heredadas exigen normalizacion previa de salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 71: se transfieren solo abstracciones estables desde actividad de otra materia.",
      "Ciclo 71: se conserva identidad y contexto curricular del destino sin contaminacion tematica.",
      "Ciclo 71: se refuerzan gates de JSON parseable, trazabilidad y control bibliografico.",
      "Ciclo 71: se mantiene compresion lossless por deduplicacion y no por recorte."
    ]
  }
}