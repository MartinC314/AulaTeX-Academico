{
  "summary": [
    "Se consolida memoria de materia desde Actividad 1 con abstraccion ascendente.",
    "Se preserva compresion lossless por union-dedupe sin regresion.",
    "Se mantiene normalizacion obligatoria antes de propagar cualquier insumo.",
    "Se refuerzan ejes editoriales transferibles: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se conserva trazabilidad entre consigna, .tex, .bib y evidencias curriculares UnADM."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y rigor academico.",
    "Alinear la materia con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica editorial.",
    "Marcar como [supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local. [supuesto]",
    "Conservar trazabilidad de fuentes provisionales historicas: Codex y GPT-Pro. [supuesto]",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema delimitado y pregunta guia explicita.",
    "Integrar normas, doctrina o datos pertinentes al problema.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que fuentes de semanas posteriores aplican automaticamente a Actividad 1. [supuesto]",
    "Confirmar que el tipo de producto coincide con la consigna activa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y entradas del .bib.",
    "Confirmar que no se eliminen reglas utiles previas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migracion completa.",
    "Compilar sin errores criticos, citas rotas ni referencias faltantes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir nombres/rutas anomalas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto operativo de nombre canonico .bib: filosofia-del-derecho.bib. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con metadatos minimos.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar autor, titulo, año y fuente/editorial o URL en cada entrada.",
    "Preservar claves recurrentes verificables de UNAM/SCJN ya usadas.",
    "No completar entradas truncadas sin verificacion local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Elevar al ancestro reglas generales reutilizables, no redaccion literal de actividades.",
    "Mantener compresion union-dedupe lossless en cada salto.",
    "Propagar puertas de calidad y trazabilidad como nucleo comun institucional.",
    "Evitar propagar nombres de archivo anomalo hasta correccion local. [supuesto]",
    "Cuando falte consigna textual, propagar solo reglas generales verificadas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 1 para fijar producto exacto.",
    "Confirmar si Actividad 1 exige reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica de la actividad.",
    "Confirmar nombre canonico final del .bib de la materia.",
    "Confirmar si filosofia-del-derecho-clean.bib es solo Semana 7 o reutilizable en otras actividades. [supuesto]",
    "Completar y verificar la entrada scjnIncapacidadResistencia2019 en .bib local. [supuesto]"
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
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos y trazables.",
      "Unificar calidad editorial entre actividades y documentos LaTeX.",
      "Sostener coherencia curricular e institucional en toda la materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado estable.",
      "Citas explicitas y verificables.",
      "Marcado claro de [supuesto].",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Construir marco conceptual y normativo.",
      "Aplicar evidencia al caso o pregunta.",
      "Desarrollar analisis critico con postura propia.",
      "Concluir con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofia del Derecho",
        "Hermeneutica juridica",
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
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion fundamenta la justificacion de argumentos."
        },
        {
          "source": "Argumentacion juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Permite pasar de premisas normativas a decisiones justificadas."
        },
        {
          "source": "Marco normativo",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El criterio propio requiere sustento juridico verificable."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra debate axiologico y validez juridica."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y cinco ejes de trabajo.",
        "Bibliografia local .bib: claves juridicas trazables.",
        "Actividad 1: patron argumentativo estable y reusable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se eleva patron de actividad a regla de materia sin perdida semantica.",
      "Ciclo 9: se deduplican reglas repetidas y se conserva todo lo util.",
      "Ciclo 9: se mantiene bloqueo por JSON no parseable como puerta critica.",
      "Ciclo 9: se refuerza trazabilidad cita-.tex-.bib y marcado de supuestos."
    ]
  }
}