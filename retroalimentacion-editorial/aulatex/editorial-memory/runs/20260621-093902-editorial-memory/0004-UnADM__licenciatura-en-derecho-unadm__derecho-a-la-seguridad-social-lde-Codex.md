{
  "summary": [
    "Se consolida sincronizacion transversal entre nodos no equivalentes con union-dedupe lossless.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad sin regresion.",
    "Se transfiere patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene prioridad del canon local del destino para contenido tematico de seguridad social.",
    "Se conserva alerta institucional por salidas no parseables en ciclos previos y normalizacion manual obligatoria."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin recorte.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Tomar README y programa analitico del destino como canon estructural.",
    "Alinear cada entrega a ejes: problema, fundamento, evidencia, analisis, conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en encuadre, marco normativo/doctrinal, analisis propio y cierre.",
    "Mantener consistencia entre reporte, presentacion y actividad."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Ajustar formato y alcance al producto solicitado en planeacion semanal."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar recursivamente.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib local."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir rutas, nombres corruptos o tokens sin expandir antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente central local.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No transferir redaccion literal ni contenido tematico exclusivo de Filosofia del Derecho.",
    "Propagar reglas generales de identidad, calidad, JSON y trazabilidad.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Conservar bandera de riesgo por historial de salida no parseable en ciclo 1."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia [supuesto].",
    "Confirmar si codigo local LDE-S2B1 se usa en todas las portadas [supuesto].",
    "Confirmar si fuente provisional heredada desde ingenieria sigue vigente para Derecho [supuesto].",
    "Confirmar rubrica oficial por actividad para ajustar profundidad argumentativa [supuesto].",
    "Confirmar vigencia periodica de URLs legales en .bib local [supuesto]."
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
      "Fundamento normativo verificable.",
      "Evidencia y fuentes trazables.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y profesionalmente utiles.",
      "Preservar continuidad editorial entre actividades y materias sin mezclar dominios tematicos.",
      "Garantizar memoria persistente con compresion lossless por deduplicacion."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explicita de [supuesto] cuando falte evidencia local.",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo y doctrinal.",
      "Contrastar evidencia relevante.",
      "Fijar postura propia sustentada.",
      "Concluir con efecto juridico practico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresion union-dedupe lossless",
        "Problema juridico",
        "Marco normativo",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible"
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
          "justification": "El analisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende del fundamento legal."
        },
        {
          "source": "JSON parseable",
          "target": "Compresion union-dedupe lossless",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay consolidacion segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Problema juridico",
          "kind": "develops",
          "justification": "Orienta el enfoque academico y profesional de cada entrega."
        }
      ],
      "evidence": [
        "README del destino define estructura canonica y archivos base.",
        "Programa analitico del destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base institucional y normativa vigente.",
        "Historial de ciclo previo confirma necesidad de gate JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se refuerza transferencia transversal de reglas estables, no contenido literal.",
      "Ciclo 4: se mantiene canon local del destino como fuente primaria de estructura.",
      "Ciclo 4: se preservan gates de calidad y trazabilidad de supuestos sin regresion.",
      "Ciclo 4: se consolida ADN editorial minimo reconstruible para propagacion recursiva."
    ]
  }
}