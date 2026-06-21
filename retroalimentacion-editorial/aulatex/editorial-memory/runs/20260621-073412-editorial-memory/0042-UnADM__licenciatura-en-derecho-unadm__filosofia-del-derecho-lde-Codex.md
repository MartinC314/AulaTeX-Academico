{
  "summary": [
    "Se consolida memoria de materia desde Actividad 1 con abstraccion ascendente y sin regresion.",
    "Se preserva normalizacion estructurada obligatoria antes de cualquier propagacion.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union y deduplicacion.",
    "Se registran salidas no JSON parseable como riesgo de ingesta, sin perder reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, redaccion y formato.",
    "Alinear la materia a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica de asignatura.",
    "Marcar como supuesto todo dato no visible en consigna o fuente local. [supuesto]",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Estructurar productos con: encuadre del problema, conceptos/marco normativo, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Separar entregables por tipo: reporte, presentacion y soporte bibliografico.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de materia."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores como obligatorias para Actividad 1. [supuesto]",
    "Confirmar que el producto final corresponde a la consigna especifica de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Verificar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de tomarlos como canon. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de asignatura cuando sean verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Tratar entradas truncadas como pendientes hasta verificacion local completa. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analitico y .bib local.",
    "Elevar al ancestro patrones argumentativos y puertas de calidad, no redacciones literales.",
    "Mantener trazabilidad de citas recurrentes al subir de actividad a materia.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Conservar registro de riesgos de ingesta por salidas no parseables."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 para fijar producto canonico. [supuesto]",
    "Confirmar nombre canonico final del .bib de la materia frente al placeholder con token Slug. [supuesto]",
    "Confirmar si actividad-1 reutiliza bibliografia existente o requiere .bib propio. [supuesto]",
    "Completar y verificar la entrada scjnIncapacidadResistencia2019 en .bib local. [supuesto]",
    "Sustituir fuentes provisionales heredadas (Codex/GPT-Pro) por evidencia local verificada. [supuesto]"
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible a practica profesional."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos y trazables.",
      "Estandarizar calidad editorial de actividades y entregables LaTeX de la materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable por bloques argumentativos.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de supuestos cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Analizar con postura propia y evidencia.",
      "Cerrar con conclusion aplicable y verificable."
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
          "justification": "Permite evaluar validez, alcance y consecuencias de normas."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra discusion axiologica y juridica en el curso."
        },
        {
          "source": "Marco normativo y doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion exige sustento verificable en fuentes."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "filosofia-del-derecho-clean.bib y filosofia-del-derecho.bib: base de citas trazables.",
        "Actividad 1: patron estable problema-conceptos-evidencia-analisis-conclusion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perdida de contenido normativo.",
      "Se elevo de actividad a materia el patron argumentativo reusable.",
      "Se reforzaron puertas de calidad y trazabilidad bibliografica.",
      "Se conservaron supuestos explicitos y riesgos de ingesta no parseable.",
      "Se evitó copiar redaccion literal extensa del hijo; se sintetizaron patrones transferibles."
    ]
  }
}