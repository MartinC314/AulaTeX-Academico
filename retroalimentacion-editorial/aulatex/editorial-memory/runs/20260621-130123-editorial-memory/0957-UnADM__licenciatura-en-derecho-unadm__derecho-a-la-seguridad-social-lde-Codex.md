{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofía del Derecho hacia materia de Seguridad Social sin mezclar contenido temático.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, evidencia verificable, análisis propio y conclusión jurídica.",
    "Se mantiene compresión lossless por unión-deduplicación y política de no regresión.",
    "Se refuerza gate crítico: bloquear propagación cuando la salida no sea JSON parseable.",
    "Se conserva alerta histórica de salidas no parseables y normalización manual obligatoria en reutilización de ciclos tempranos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redacción.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "No sobrescribir reglas válidas previas; solo unir y deduplicar.",
    "No propagar datos personales de plantilla a nodos laterales salvo necesidad explícita [supuesto]."
  ],
  "structure_rules": [
    "Tomar README y programa analítico del destino como canon estructural local.",
    "Alinear cada entrega a ejes reutilizables: problema, conceptos/norma, evidencia, análisis propio y conclusión.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en bloques: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeación semanal.",
    "Mantener consistencia editorial entre reporte, presentación y actividad.",
    "Normalizar nombres de archivos con marcadores corruptos antes de usarlos como canon."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, objetivo, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Distinguir hechos, conceptos, norma y opinión propia.",
    "No asumir que fuentes de otras semanas o materias aplican automáticamente."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que toda afirmación relevante tenga respaldo o etiqueta [supuesto].",
    "Validar correspondencia entre producto entregado y consigna vigente.",
    "Verificar consistencia entre citas en texto y archivo .bib local.",
    "Confirmar compresión por unión-deduplicación sin recorte semántico."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener codificación y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos, referencias rotas ni claves BibTeX faltantes.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Corregir rutas, tokens sin expandir y nombres de archivo corruptos antes de compilar.",
    "No cambiar clase o formato global sin justificación técnica."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliográfica central.",
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Agregar solo referencias consultables y pertinentes a la consigna local.",
    "No inventar fuentes; registrar faltantes como pendientes [supuesto].",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Verificar que cada cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables en este ciclo.",
    "Compartir a laterales solo abstracciones estables, no redacción literal.",
    "Propagar reglas curriculares específicas solo dentro de la misma materia.",
    "Propagar transversalmente reglas generales de integridad, estructura y calidad.",
    "Mantener bandera de riesgo por antecedentes de salida no parseable en ciclos previos.",
    "Aplicar estrategia progresiva y conservadora: sumar sin reemplazar reglas útiles."
  ],
  "open_questions": [
    "Confirmar norma de citación exigida por la materia (APA, ISO, institucional o jurídica mexicana) [supuesto].",
    "Confirmar si la regla heredada desde ingeniería sigue vigente en este nodo de Derecho [supuesto].",
    "Confirmar campos oficiales faltantes de plantilla (figura docente) [supuesto].",
    "Confirmar si cada Actividad usa .bib único de materia o anexos bibliográficos por actividad [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico delimitado.",
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia pertinente.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos jurídicos verificables y profesionalmente útiles.",
      "Preservar memoria editorial estable sin perder contexto local del destino.",
      "Garantizar reutilización segura mediante estructura, calidad y trazabilidad."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiqueta explícita de [supuesto] cuando falte verificación.",
      "Separación visible entre marco, análisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
      "Contrastar evidencia.",
      "Fijar postura propia sustentada.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "JSON parseable",
        "Compresión unión-dedupe",
        "Problema jurídico",
        "Marco normativo",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible"
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
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin problema delimitado no hay argumentación evaluable."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere base legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Compresión unión-dedupe",
          "kind": "depends_on",
          "justification": "La consolidación lossless exige estructura válida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Problema jurídico",
          "kind": "develops",
          "justification": "Define enfoque académico y jurídico de cada entrega."
        }
      ],
      "evidence": [
        "README del destino define estructura canónica y artefactos base.",
        "Programa analítico del destino fija propósito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Histórico de calidad exige normalización de salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: se transfiere patrón editorial estable desde Filosofía del Derecho como abstracción reusable.",
      "Ciclo 20: se preservan reglas locales de Seguridad Social sin importar contenido doctrinal específico del origen.",
      "Ciclo 20: se refuerzan gates de parseabilidad JSON, trazabilidad y no invención de fuentes.",
      "Ciclo 20: deduplicación aplicada sin recorte y sin regresión."
    ]
  }
}