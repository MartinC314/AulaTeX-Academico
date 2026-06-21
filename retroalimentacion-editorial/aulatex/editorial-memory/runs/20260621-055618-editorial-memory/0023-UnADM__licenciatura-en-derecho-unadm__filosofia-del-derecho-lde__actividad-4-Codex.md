{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se refuerza validacion JSON estricta antes de propagacion recursiva.",
    "Se transfieren solo patrones reutilizables de estructura, calidad y argumentacion.",
    "Supuesto: la consigna local de Actividad 4 no esta visible; se mantiene plantilla base."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato academico.",
    "Alinear la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar Actividad 4 a los ejes del programa analitico.",
    "Supuesto: confirmar producto exacto, extension y rubrica de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "No renombrar claves BibTeX usadas en documentos activos.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a otra actividad; verificar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin copiar contenido especifico entre hermanos.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar union-dedupe lossless en ciclos posteriores.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4.",
    "Confirmar producto requerido: reporte, presentacion u otro formato.",
    "Confirmar rubrica de evaluacion especifica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del archivo .bib."
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
        "Entrada canonica en carpeta de asignatura."
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
      "Convertir planeacion semanal en productos academicos solidos.",
      "Sostener calidad editorial uniforme en actividades.",
      "Asegurar trazabilidad entre problema, evidencia y conclusion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales con logica juridica.",
      "Citas explicitas para afirmaciones clave.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y normas relevantes.",
      "Contrastar fuentes con analisis propio.",
      "Fijar postura argumentada.",
      "Concluir con aplicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica",
        "Ejes editoriales de Filosofia del Derecho",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor formal."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere estructura parseable."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Relacion problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el argumento desde el problema hasta el cierre."
        }
      ],
      "evidence": [
        "README define identidad UnADM, entrada canonica y criterio de conclusion juridica.",
        "Programa analitico define cinco ejes reutilizables para todas las actividades.",
        "Antecedentes de salidas no parseables justifican gate tecnico de JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 23: deduplicacion de reglas repetidas y preservacion lossless.",
      "Ciclo 23: refuerzo lateral sin traslado de conclusiones ni bibliografia exclusiva del hermano.",
      "Ciclo 23: mantenimiento de supuestos abiertos por falta de consigna local visible."
    ]
  }
}