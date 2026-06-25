{
  "summary": [
    "Se sincroniza memoria transversal con transferencia de reglas estables, sin mezclar contenido tematico de Filosofia del Derecho.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad JSON parseable como nucleo persistente.",
    "Se refuerza compresion lossless por union-dedupe y no regresion de reglas utiles.",
    "Se mantiene la materia destino como nodo canonico con enfoque juridico verificable en seguridad social."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada, metadatos y redaccion.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No sobrescribir reglas validas previas; aplicar union-dedupe sin regresion."
  ],
  "structure_rules": [
    "Tomar README y programa analitico de la materia como canon estructural local.",
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en bloques: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio de cada entrega.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos, normas, doctrina y opinion propia.",
    "Relacionar contenido con seguridad social cuando corresponda."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar respaldo verificable o marca [supuesto] en afirmaciones relevantes.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la compresion sea union-dedupe y no recorte."
  ],
  "latex_rules": [
    "Conservar plantilla base de materia y personalizar solo campos variables.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos, sin referencias rotas y sin claves BibTeX faltantes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Normalizar nombres/rutas de archivos antes de compilar.",
    "Resolver marcadores o tokens sin expandir en README, programa y rutas."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas vigentes verificables.",
    "No inventar referencias; registrar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Verificar que toda cita en LaTeX tenga entrada BibTeX correspondiente."
  ],
  "propagation_hints": [
    "Propagar a laterales y arriba solo reglas validadas y estructuradas.",
    "Compartir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Propagar reglas curriculares especificas solo dentro de la misma materia.",
    "Mantener bandera de riesgo por antecedente de salida no parseable en ciclo 1.",
    "Aplicar estrategia progresiva y conservadora: reforzar sin reemplazar."
  ],
  "open_questions": [
    "Confirmar norma de citacion requerida en la materia (APA, ISO, institucional o juridica mexicana) [supuesto].",
    "Confirmar vigencia de cualquier fuente provisional heredada externa a Derecho [supuesto].",
    "Verificar si todas las plantillas de actividad del README existen fisicamente y estan limpias de marcadores.",
    "Definir dato oficial de figura docente cuando este disponible [supuesto]."
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
      "Fundamento normativo y doctrinal verificable.",
      "Evidencia y citas trazables.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables y evaluables sin perder identidad institucional.",
      "Sostener una memoria editorial persistente, reutilizable y sin regresiones."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion visible entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco normativo/doctrinal.",
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
          "justification": "El analisis requiere una pregunta juridica delimitada."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida depende de fundamento legal verificable."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Compresion union-dedupe",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "Conserva reglas utiles sin perdida ni duplicado."
        }
      ],
      "evidence": [
        "README de la materia como estructura canonica local.",
        "Programa analitico con proposito y ejes verificables.",
        "Archivo derecho-a-la-seguridad-social.bib como base normativa local.",
        "Antecedente institucional de salida no parseable en ciclo 1."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se transfieren solo abstracciones estables desde actividad de otra materia.",
      "Ciclo 13: se evita migrar contenido tematico de Filosofia del Derecho al destino.",
      "Ciclo 13: se refuerzan gates de JSON, trazabilidad de supuestos y control bibtex.",
      "Ciclo 13: se consolida ADN editorial minimo, reconstruible y sin duplicados."
    ]
  }
}