{
  "summary": [
    "Consolidar memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Preservar identidad UnADM, trazabilidad curricular y control de calidad sin regresion.",
    "Mantener normalizacion obligatoria de insumos no estructurados antes de propagacion recursiva.",
    "Fijar eje comun transferible: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de la asignatura.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar referencia curricular verificable en malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar cada producto con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de materia."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Validar que el producto corresponda a la consigna de la actividad.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a actividad-1.",
    "Agregar fuentes especificas de actividad solo despues de verificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Confirmar no regresion: no eliminar reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves citadas sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de tratarlos como canonicos. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Registrar fuentes de actividad en el .bib de la asignatura tras verificacion.",
    "Tratar entradas truncadas como pendientes de integridad hasta completar campos. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON, estructura y trazabilidad.",
    "Elevar al ancestro solo patrones reutilizables, no redaccion literal de actividades.",
    "Reutilizar puertas de calidad institucionales sin perder especificidad local.",
    "Mantener compresion union-dedupe lossless en cada salto.",
    "Evitar propagar placeholders de nombres de archivo hasta correccion local.",
    "Ciclo 1, 2 y 3 requieren normalizacion manual cuando la fuente de entrada no es estructurada."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de actividad-1 para fijar producto exacto. [supuesto]",
    "Confirmar nombre canonico final del archivo .bib de la materia. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib es solo Semana 7 o reutilizable en otras actividades. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019 en .bib. [supuesto]",
    "Sustituir fuentes provisionales heredadas (Codex, GPT-Pro) por fuente local verificada. [supuesto]"
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
        "Carpeta de materia como punto de entrada canonico."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable con cita explicita.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, fundados y transferibles.",
      "Estandarizar calidad editorial LaTeX con trazabilidad entre consigna, analisis y bibliografia.",
      "Preservar memoria util sin perdida y sin regresion entre ciclos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por ejes.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar evidencia y doctrina.",
      "Sostener postura propia.",
      "Concluir con aplicacion juridica concreta."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Ejes editoriales de actividad transferidos a materia"
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
          "justification": "La interpretacion sustenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar normas, hechos y consecuencias."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida requiere base normativa verificable."
        },
        {
          "source": "Actividad-1",
          "target": "Memoria de materia",
          "kind": "develops",
          "justification": "Se eleva patron editorial reutilizable por abstraccion ascendente."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib: claves juridicas verificables y recurrentes.",
        "Reglas heredadas: bloqueo por JSON no parseable y normalizacion previa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion completa de reglas repetidas con preservacion de contenido util.",
      "Ciclo 3: se reforzo no regresion y control de calidad estructural.",
      "Ciclo 3: se elevaron patrones de actividad a nivel materia sin copiar redaccion literal.",
      "Ciclo 3: se conservaron citas recurrentes y trazabilidad conceptual.",
      "Ciclo 3: se mantuvieron fuentes provisionales marcadas como [supuesto] hasta verificacion."
    ]
  }
}