{
  "summary": [
    "Se consolida memoria de materia desde actividad-1 con abstraccion ascendente y deduplicacion lossless.",
    "Se preserva identidad UnADM, trazabilidad curricular y control de calidad sin regresion.",
    "Se mantienen ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion obligatoria para insumos no JSON parseable antes de propagar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redaccion y formato.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como [supuesto] todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guia al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta, desarrollo y conclusion.",
    "No asumir fuentes de semanas posteriores para actividad-1 sin verificacion. [supuesto]",
    "Confirmar que el producto final corresponde a la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Exigir marca [supuesto] cuando falte evidencia local.",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Confirmar no eliminacion de reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Corregir rutas o nombres anómalos del README antes de compilar. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar bibliografia especifica de actividad en el .bib de materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia puntual por actividad.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Elevar al ancestro reglas generales, no redaccion literal de actividad.",
    "Conservar trazabilidad de conceptos y citas recurrentes al subir nivel.",
    "Reutilizar puertas de calidad institucional en nodos laterales.",
    "Aplicar union-dedupe lossless para evitar duplicados sin perder informacion.",
    "Mantener bandera de normalizacion manual en ciclos con insumos no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1. [supuesto]",
    "Confirmar formato exigido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de la materia.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-1 o solo semana 7. [supuesto]",
    "Completar y verificar entrada scjnIncapacidadResistencia2019 truncada. [supuesto]"
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
        "Carpeta de materia como entrada canonica editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social activa el trabajo academico.",
      "Conceptos y marco normativo sostienen el analisis.",
      "Evidencia verificable respalda afirmaciones.",
      "Postura propia evita resumen meramente descriptivo.",
      "Conclusion juridica debe ser transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Estandarizar calidad editorial de actividades y entregables LaTeX.",
      "Preservar continuidad institucional y curricular entre nodos."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable y funcional.",
      "Marcado explicito de supuestos.",
      "Cierre con criterio juridico propio.",
      "Trazabilidad de fuentes y decisiones editoriales."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> objetivo puntual -> desarrollo sustentado -> postura -> conclusion.",
      "Marco conceptual + marco normativo + evidencia -> inferencia juridica.",
      "Coherencia entre pregunta guia, argumento y cierre."
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
        "finnis_estudios_2017",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermeneutica e interpretacion juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion fundamenta la construccion de razones juridicas."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Analisis critico del fenomeno juridico",
          "kind": "develops",
          "justification": "Permite evaluar normas, hechos y consecuencias."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiologico y validez normativa."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion requiere soporte verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Actividad-1: patron estable de escritura juridica academica.",
        "Bib local: citas recurrentes de UNAM, SCJN y doctrina base.",
        "Incidencias previas: salidas no parseables requieren normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte de informacion util.",
      "Se elevaron patrones reutilizables del hijo al ancestro sin copiar redaccion literal.",
      "Se preservaron riesgos de ingesta y controles de normalizacion.",
      "Se reforzo trazabilidad entre identidad, estructura, evidencia y calidad."
    ]
  }
}