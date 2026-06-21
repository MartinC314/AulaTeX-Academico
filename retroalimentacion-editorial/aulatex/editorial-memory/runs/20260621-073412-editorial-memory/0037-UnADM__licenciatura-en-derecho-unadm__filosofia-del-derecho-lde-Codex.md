{
  "summary": [
    "Se consolida en materia la memoria valida de actividad-1 con abstraccion ascendente.",
    "Se preserva compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Se refuerza normalizacion obligatoria para insumos no JSON parseable antes de propagar.",
    "Se fija ADN editorial UnADM con cinco ejes: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de la asignatura.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como base curricular verificada."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de materia."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin verificacion. [supuesto]",
    "Registrar bibliografia especifica de actividad en el .bib de la asignatura."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que el producto corresponda a la consigna de la actividad."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol para .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas anomalas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No completar entradas truncadas sin verificacion local. [supuesto]",
    "Conservar claves recurrentes verificables de SCJN/UNAM cuando ya formen parte del corpus."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Elevar reglas generales reutilizables desde actividades hacia materia y ancestros.",
    "Evitar copiar redaccion literal de hijos; sintetizar patrones transferibles.",
    "Mantener no regresion: nunca eliminar reglas utiles previas.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Registrar incidencias de ingesta no parseable como riesgo sin perder contenido util."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para cerrar supuestos de formato. [supuesto]",
    "Confirmar nombre canonico final del .bib de materia frente a tokens placeholder. [supuesto]",
    "Confirmar si filosofia-del-derecho-clean.bib aplica fuera de Semana 7. [supuesto]",
    "Verificar integridad completa de scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y trazables.",
      "Asegurar fundamento juridico y transferencia profesional en cada entrega."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y explicito.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [supuesto].",
      "Trazabilidad documental entre README, programa, .tex y .bib."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Analizar con postura propia y evidencia.",
      "Concluir con aplicabilidad juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica e interpretacion juridica",
        "Argumentacion juridica",
        "Derecho y moral",
        "Justicia",
        "Analisis critico del fenomeno juridico",
        "Cinco ejes editoriales UnADM"
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
          "justification": "La interpretacion aporta criterios para construir argumentos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar validez, razones y consecuencias."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige soporte juridico verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La asignatura integra debate axiologico y normativo."
        }
      ],
      "evidence": [
        "README de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Reglas heredadas de actividad-1: estructura argumentativa y control de calidad.",
        "Bibliografia local .bib/.clean.bib con claves juridicas recurrentes."
      ]
    },
    "reinforcement_log": [
      "Ciclo 37: se elevo patron de actividad-1 a materia sin perdida semantica.",
      "Ciclo 37: se deduplicaron reglas repetidas y se preservo no regresion.",
      "Ciclo 37: se reforzo bloqueo por JSON no parseable y normalizacion previa.",
      "Ciclo 37: se mantuvo trazabilidad de citas y conceptos reutilizables."
    ]
  }
}