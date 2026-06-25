{
  "summary": [
    "Sincronizacion transversal ciclo 2 aplicada con union-dedupe lossless.",
    "Se preservan reglas utiles previas del destino y del origen sin recorte.",
    "Se transfieren solo abstracciones estables: identidad, estructura, calidad y trazabilidad.",
    "Se refuerza normalizacion obligatoria de salidas no parseables antes de propagacion.",
    "Se mantiene foco local del destino: Derecho laboral y relaciones laborales en UnADM."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Mantener contexto curricular local verificado: Licenciatura en Derecho, semestre 7, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto a la planeacion semanal y a la consigna vigente.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Contextualizar cada actividad en conflicto o situacion laboral verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada propia y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar contenido de otra materia sin validar pertinencia laboral."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna de actividad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Detectar y resolver tokens de plantilla sin expandir en nombres de archivo.",
    "Completar entornos truncados de plantilla antes de compilar."
  ],
  "bibliography_rules": [
    "Centralizar fuentes de la materia en derecho-laboral-y-relaciones-laborales.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "Priorizar identidad, gates de calidad, estructura reusable y grafo conceptual.",
    "Aplicar deduplicacion semantica por frases cortas y accionables.",
    "Evitar regresiones: no eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividades especificas en la materia destino.",
    "Confirmar formato de cita juridica exigido por docente.",
    "Confirmar si el autor en plantilla es fijo institucional o variable por alumno.",
    "Confirmar nombres canonicos finales en README tras corregir tokens sin expandir.",
    "Confirmar si existe rubrica oficial para convertirla en checklist por actividad."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho laboral y relaciones laborales.",
        "Semestre 7, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos con trazabilidad.",
      "Mantener coherencia entre consigna, estructura, evidencia y conclusion profesional."
    ],
    "style_markers": [
      "Frases precisas y verificables.",
      "Supuestos marcados de forma explicita.",
      "Separacion clara entre marco y postura propia.",
      "Cierre con aplicacion juridica profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar evidencia y doctrina.",
      "Sostener postura propia.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion de salidas no parseables",
        "Problema juridico laboral",
        "Marco normativo o doctrinal",
        "Postura argumentada propia",
        "Conclusion juridica transferible",
        "Trazabilidad de citas y bibliografia"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Trazabilidad de citas y bibliografia",
          "kind": "supports",
          "justification": "La identidad institucional exige integridad academica verificable."
        },
        {
          "source": "Problema juridico laboral",
          "target": "Postura argumentada propia",
          "kind": "depends_on",
          "justification": "La argumentacion pertinente parte de un problema delimitado."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere fundamento juridico."
        },
        {
          "source": "Normalizacion de salidas no parseables",
          "target": "Trazabilidad de citas y bibliografia",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay control confiable de evidencia."
        },
        {
          "source": "Postura argumentada propia",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion sintetiza el criterio juridico construido."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Bib local: claves institucionales verificables.",
        "Antecedente de salidas no parseables: requiere normalizacion obligatoria."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se consolida regla transversal de estructura argumentativa de 5 ejes.",
      "Ciclo 2: se refuerza gate critico de JSON parseable previo a propagacion.",
      "Ciclo 2: se integra control de supuestos como requisito de integridad editorial.",
      "Ciclo 2: se preserva ADN local laboral sin importar redaccion de origen."
    ]
  }
}