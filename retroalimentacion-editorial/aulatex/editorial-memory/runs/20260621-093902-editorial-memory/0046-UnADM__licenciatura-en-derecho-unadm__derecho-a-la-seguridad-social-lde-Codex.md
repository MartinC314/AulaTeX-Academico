{
  "summary": [
    "Se mantiene sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad parseable.",
    "Se transfiere patron estable: problema, fundamento, evidencia, analisis propio y conclusion juridica.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho al destino.",
    "Se refuerza compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y formato.",
    "Usar datos curriculares oficiales del destino: semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local [supuesto].",
    "No sobrescribir reglas validas previas; solo unir y deduplicar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Mantener consistencia entre README, programa analitico, reporte y presentacion.",
    "Usar estructura minima verificable: portada, desarrollo, conclusion y referencias."
  ],
  "activity_rules": [
    "Delimitar problema y objetivo desde el inicio.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Distinguir hechos, normas, conceptos y opinion propia.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de propagacion recursiva.",
    "Confirmar que cada afirmacion relevante tenga respaldo o marca [supuesto].",
    "Comprobar correspondencia entre producto entregado y consigna vigente.",
    "Verificar que no se eliminen reglas utiles previas."
  ],
  "latex_rules": [
    "Conservar plantilla base de la materia y personalizar solo campos variables.",
    "Mantener metadatos institucionales y de curso consistentes en .tex.",
    "Mantener compatibilidad tecnica; evitar cambios de clase sin justificacion.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas validas.",
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Normalizar nombres de archivo cuando existan marcadores corruptos o tokens sin expandir."
  ],
  "bibliography_rules": [
    "Usar derecho-a-la-seguridad-social.bib como fuente bibliografica central local.",
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias; registrar faltantes como pendientes o [supuesto].",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/URL.",
    "Validar correspondencia entre citas en texto y claves BibTeX.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables a nodos laterales no equivalentes.",
    "Compartir gates de calidad, identidad y estructura reusable; no redaccion literal.",
    "Mantener reglas curriculares especificas solo dentro de la materia destino.",
    "Aplicar union-dedupe en cada ciclo para evitar regresion.",
    "Conservar alerta historica: ciclo 1 requirio normalizacion manual por salida no parseable.",
    "Si falta contexto local, preservar cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar norma de citacion exigida por la materia (APA, ISO o institucional) [supuesto].",
    "Confirmar si sigue vigente la fuente provisional heredada desde ingenieria [supuesto].",
    "Confirmar datos de figura docente para plantillas de portada.",
    "Verificar consignas reales de Actividad 1 en planeaciones locales.",
    "Validar si existen nuevos criterios jurisprudenciales obligatorios para citar."
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
      "Evidencia suficiente y trazable.",
      "Analisis propio argumentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir consignas en productos juridicos verificables sin perder identidad institucional.",
      "Asegurar consistencia editorial entre actividades, plantillas y memoria persistente."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Etiquetado explicito de [supuesto].",
      "Separacion clara entre marco, analisis y cierre.",
      "Cierre con utilidad profesional."
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
        "JSON parseable",
        "Compresion union-dedupe",
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
          "justification": "Sin pregunta delimitada no hay analisis juridico consistente."
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
          "justification": "La consolidacion lossless requiere estructura valida."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Calidad editorial transversal",
          "kind": "supports",
          "justification": "La identidad fija estandares comunes entre nodos."
        }
      ],
      "evidence": [
        "README de destino define estructura canonica y artefactos base.",
        "Programa analitico de destino define proposito y ejes de trabajo.",
        "Archivo .bib local confirma base normativa e institucional verificable.",
        "Historial de ciclo 1 confirma necesidad de normalizacion manual por salida no parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 46: se consolida transferencia transversal de reglas estables sin mezclar contenido tematico de filosofia.",
      "Ciclo 46: se refuerza gate de JSON parseable como requisito de propagacion recursiva.",
      "Ciclo 46: se mantiene compresion lossless por union-dedupe y politica de no regresion."
    ]
  }
}