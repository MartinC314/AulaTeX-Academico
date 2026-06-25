{
  "summary": [
    "Sincronizacion transversal aplicada con deduplicacion lossless y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se agregan mejoras verificables de normalizacion de tokens de plantilla y JSON parseable.",
    "Se mantiene foco local en Derecho laboral y relaciones laborales con abstracciones transferibles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: Licenciatura en Derecho, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones reutilizables: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la consigna y planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en un conflicto verificable del campo laboral.",
    "Sustentar afirmaciones con norma, doctrina o datos verificables.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otras materias sin validar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizar o propagar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de citas y correspondencia con .bib.",
    "Marcar o corregir afirmaciones sin respaldo o sin etiqueta de supuesto."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base por actividad.",
    "Completar metadatos reales antes de compilar.",
    "Mantener compilacion en español, letterpaper y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y referencias.",
    "Corregir entornos truncados de plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Centralizar bibliografia local en derecho-laboral-y-relaciones-laborales.bib.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "Aplicar estrategia conservadora: agregar mejoras verificables sin eliminar reglas utiles previas.",
    "Cuando falte consigna local, propagar reglas generales y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar formato de citacion exigido por docente en esta materia.",
    "Confirmar si el autor de plantilla es fijo institucional o variable por alumno.",
    "Confirmar rubrica oficial por actividad para convertirla en checklist.",
    "Supuesto: el archivo .bib canonico ya resuelto es derecho-laboral-y-relaciones-laborales.bib; validar en todos los artefactos.",
    "Confirmar nombres canonicos finales de reporte, presentacion y carpeta de referencias."
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
        "Normalizacion obligatoria de salidas no estructuradas."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos coherentes y verificables.",
      "Asegurar trazabilidad editorial y tecnica antes de propagacion recursiva."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos marcados de forma explicita.",
      "Sin redaccion literal heredada entre materias.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y norma aplicable.",
      "Contrastar evidencia.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "JSON parseable",
        "Normalizacion estructurada",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y verificabilidad."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida se propagan errores."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "La postura requiere delimitacion previa del conflicto."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida necesita fundamento juridico."
        }
      ],
      "evidence": [
        "README local: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico local: ejes de trabajo y proposito.",
        "Bibliografia local: claves institucionales verificables.",
        "Historial heredado: necesidad recurrente de normalizacion por salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion semantica aplicada sin recorte de reglas utiles.",
      "Ciclo 12: reforzada regla de bloqueo por JSON no parseable.",
      "Ciclo 12: reforzada resolucion de tokens $(@{...}.Slug) como control transversal.",
      "Ciclo 12: mantenido patron argumentativo comun problema-marco-analisis-conclusion."
    ]
  }
}