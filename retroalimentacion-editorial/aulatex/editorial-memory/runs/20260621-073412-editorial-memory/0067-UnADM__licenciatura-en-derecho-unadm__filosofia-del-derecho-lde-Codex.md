{
  "summary": [
    "Consolidar memoria de materia con abstraccion ascendente desde actividad-1.",
    "Preservar reglas utiles previas sin regresion y con deduplicacion lossless.",
    "Mantener normalizacion estructurada obligatoria antes de cualquier propagacion.",
    "Fijar ADN editorial de la materia: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Registrar salidas no JSON parseable como riesgo de ingesta sin perder contenido valido."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de entregables y fuentes.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado y verificable.",
    "Sustentar afirmaciones sustantivas con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1.",
    "Validar que el producto entregado coincide con la consigna especifica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Confirmar no eliminacion de reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Separar entregables por tipo en archivos .tex dedicados (reporte, presentacion).",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomalos antes de tratarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas por actividad en el .bib de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No completar entradas BibTeX truncadas sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar patrones reutilizables de actividad al nivel materia sin copiar redaccion literal.",
    "Reusar puertas de calidad institucionales en nodos ancestro y laterales.",
    "Evitar propagar nombres de archivo no normalizados hasta correccion local.",
    "Mantener etiqueta de compresion union-dedupe lossless en toda transferencia."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para validar tipo de producto.",
    "Confirmar nombre canonico final del .bib de la materia.",
    "Determinar si filosofia-del-derecho-clean.bib es temporal o definitivo. [supuesto]",
    "Completar y verificar la entrada truncada scjnIncapacidadResistencia2019.",
    "Sustituir fuentes provisionales heredadas por fuentes verificadas locales."
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
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar trazabilidad entre consigna, argumento y evidencia.",
      "Formar criterio juridico aplicable a la practica profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y legible.",
      "Citas explicitas y verificables.",
      "Marcado visible de [supuesto].",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Construir marco conceptual y normativo.",
      "Analizar con postura propia.",
      "Concluir con transferencia practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Problema-conceptos-evidencia-analisis-conclusion"
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
          "justification": "El analisis critico requiere estructura argumentativa."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra validez normativa y dimension axiologica."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida depende de soporte normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bib local: claves recurrentes juridicas y doctrinales.",
        "Actividad-1: patron editorial estable transferible al ancestro."
      ]
    },
    "reinforcement_log": [
      "Se preservan reglas heredadas validas y se elimina duplicacion literal.",
      "Se eleva el patron de actividad a regla marco de materia.",
      "Se mantiene bloqueo por no JSON parseable como puerta critica.",
      "Se conserva trazabilidad de citas recurrentes sin inventar fuentes.",
      "Se refuerza identidad UnADM y control de supuestos en todo el nodo."
    ]
  }
}