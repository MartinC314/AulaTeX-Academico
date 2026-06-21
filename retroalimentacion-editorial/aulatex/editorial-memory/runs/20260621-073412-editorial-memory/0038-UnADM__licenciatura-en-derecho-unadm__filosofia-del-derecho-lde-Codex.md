{
  "summary": [
    "Consolidar memoria de materia con abstraccion ascendente desde actividad-1.",
    "Preservar reglas validas previas sin regresion y con union-dedupe lossless.",
    "Mantener normalizacion obligatoria de insumos no estructurados antes de propagar.",
    "Fijar eje transversal: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de actividades y entregables.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad a malla-curricular-derecho-unadm.pdf como respaldo curricular."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1 sin verificacion.",
    "Validar que el producto corresponda exactamente a la consigna activa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar no eliminacion de reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "No adoptar nombres de archivo anomalos como canon hasta correccion local. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar deduplicacion sin perdida y trazabilidad de claves recurrentes.",
    "Tratar entradas truncadas como pendientes hasta verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones reutilizables; no copiar redaccion literal de actividades hijas.",
    "Transferir citas recurrentes como trazas, no como obligatoriedad universal.",
    "Aplicar primero filtros de calidad institucional antes de propagacion lateral o ascendente.",
    "Mantener etiqueta de compresion lossless por union-dedupe en cada salto."
  ],
  "open_questions": [
    "Confirmar nombre canonico final del .bib de la materia tras resolver token Slug. [supuesto]",
    "Confirmar consigna textual exacta de actividad-1 para cerrar reglas de formato.",
    "Confirmar si filosofia-del-derecho-clean.bib es auxiliar o canon de materia. [supuesto]",
    "Completar y verificar la entrada scjnIncapacidadResistencia2019 truncada. [supuesto]",
    "Confirmar rubrica oficial para calibrar profundidad argumentativa por actividad."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social como punto de partida.",
      "Conceptos y marco normativo con evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable a practica profesional.",
      "Normalizacion estructurada como condicion de reutilizacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos trazables.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y evidencia.",
      "Sostener memoria editorial persistente sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Marcado explicito de [supuesto].",
      "Cierre juridico transferible.",
      "Trazabilidad .tex/.bib."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y norma aplicable.",
      "Contrastar o desarrollar con evidencia.",
      "Fijar postura propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Problema-conceptos-evidencia-analisis-conclusion"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018"
      ],
      "relations": [
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "Permite justificar postura y evaluar consecuencias."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida requiere soporte normativo verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra debate axiologico y validez juridica."
        }
      ],
      "evidence": [
        "README de materia y programa analitico como base institucional.",
        "Regla persistente de bloqueo por no-JSON parseable.",
        "Bibliografia local con claves recurrentes y verificables.",
        "Transferencia ascendente desde actividad-1 sin copia literal."
      ]
    },
    "reinforcement_log": [
      "Ciclo 38: se refuerza abstraccion ascendente actividad->materia.",
      "Ciclo 38: se deduplican reglas repetidas sin recorte semantico.",
      "Ciclo 38: se preserva control de calidad heredado (JSON, estructura, citas).",
      "Ciclo 38: se mantienen fuentes provisionales bajo etiqueta [supuesto] hasta verificacion."
    ]
  }
}