{
  "summary": [
    "Se consolida memoria de materia desde Actividad 1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preservan reglas utiles previas sin regresion y se integran mejoras verificables del contexto local.",
    "Se fija la normalizacion estructurada como requisito previo de propagacion recursiva.",
    "Se refuerza ADN editorial UnADM: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios academicos.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna. [supuesto]",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a Actividad 1. [supuesto]",
    "Verificar que el producto corresponda a la consigna especifica de cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y entradas del .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No adoptar nombres anomalos como canon hasta correccion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar y deduplicar entradas sin perdida de trazabilidad.",
    "Tratar filosofia-del-derecho-clean.bib como apoyo tematico no canonico de Actividad 1 hasta confirmacion. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones transferibles, no redaccion literal de actividades.",
    "Mantener union-dedupe lossless en cada ciclo de consolidacion.",
    "Reutilizar puertas de calidad institucional en nodos ancestro y laterales.",
    "Registrar incidencias de parseo como riesgo de ingesta sin perder contenido util."
  ],
  "open_questions": [
    "Confirmar consigna textual y producto exacto de Actividad 1.",
    "Confirmar nombre canonico final del archivo .bib de la materia.",
    "Confirmar si Actividad 1 requiere .bib propio o reutiliza bibliografia existente.",
    "Completar y verificar campos faltantes de scjnIncapacidadResistencia2019. [supuesto]",
    "Sustituir referencias provisionales heredadas (Codex, GPT-Pro) por fuentes locales verificadas. [supuesto]"
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
        "Materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles profesionalmente.",
      "Estandarizar calidad editorial sin perder especificidad por actividad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Cierre juridico aplicado.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problematizar -> fundamentar -> argumentar -> concluir.",
      "Conectar doctrina, norma y caso para sostener postura propia.",
      "Validar cada afirmacion con evidencia o marca de supuesto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sostiene la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, coherencia y efectos normativos."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate axiologico y la legitimidad juridica."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion profesional requiere soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Reglas heredadas de Actividad 1: estructura argumentativa y control de calidad.",
        "Bibliografia local .bib: claves recurrentes y trazabilidad de citas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 56: se elevo patron de Actividad 1 a nivel materia sin copiar redaccion literal.",
      "Ciclo 56: se mantuvo compresion lossless por union-dedupe y sin regresion.",
      "Ciclo 56: se reforzo bloqueo por JSON no parseable y normalizacion previa.",
      "Ciclo 56: se consolidaron conexiones conceptuales reutilizables para propagacion recursiva."
    ]
  }
}