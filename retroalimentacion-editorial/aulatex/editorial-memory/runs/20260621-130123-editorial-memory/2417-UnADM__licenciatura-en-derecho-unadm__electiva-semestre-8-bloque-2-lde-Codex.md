{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para materia destino no equivalente.",
    "Se preservan reglas estables del origen: normalizacion estructurada, ejes editoriales y conclusion juridica transferible.",
    "Se refuerza control de calidad JSON, trazabilidad cita-texto-bib y marcado explicito de supuestos.",
    "Se mantiene identidad UnADM con contexto curricular local de semestre 8, bloque 2, electiva.",
    "Se incorporan mejoras verificables del contexto local: correccion de placeholders y nombres truncados en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar la carpeta de materia como entrada canonica.",
    "Fijar autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Usar codigo de curso LDE-S8B2 en metadatos.",
    "Marcar como [supuesto] todo dato no confirmado, incluidos creditos y figura docente.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Vincular conceptos, normas, doctrina o datos con el problema tratado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir contenido tematico especifico de Filosofia del Derecho sin validacion local."
  ],
  "quality_gates": [
    "Bloquear consolidacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar recursivamente.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders o tokens sin expandir en README, programa, .tex y .bib.",
    "Corregir nombres truncados de archivos antes de entrega.",
    "Mantener normalizacion manual para herencias historicas de ciclo 1/2 no estructuradas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Conservar plantilla base reporte-electiva-semestre-8-bloque-2.tex.",
    "Actualizar Actividad X por numero real antes de compilar.",
    "Completar solo con datos confirmados los campos de figura docente y creditos; si no, marcar [supuesto].",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens tipo $(@{...}.Slug) a nombres literales en README y programa."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Verificar consistencia de fecha de consulta en fuentes web institucionales."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos transversales.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico local no validado.",
    "Aplicar union-dedupe sin recorte y sin regresion de reglas utiles.",
    "Si falta contexto local en nodo hijo, crear base minima y abrir preguntas explicitas."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia.",
    "[supuesto] Confirmar nombre de figura docente para front matter.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar si la bibliografia base actual requiere ampliacion obligatoria por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Control explicito de supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo LDE-S8B2.",
        "[supuesto] Creditos por confirmar."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada previa a propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y transferibles.",
      "Preservar coherencia editorial entre documentos de la materia.",
      "Garantizar memoria reutilizable sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Marcado [supuesto] cuando aplique.",
      "Cierre con aplicacion profesional."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Cada afirmacion relevante debe poder rastrearse a evidencia.",
      "La conclusion deriva del razonamiento del estudiante, no de copia de fuentes."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Trazabilidad cita-texto-bib",
        "Control de supuestos",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Correccion de placeholders"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Reduce herencia de salidas no parseables."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige correspondencia explicita."
        },
        {
          "source": "Analisis juridico propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La transferencia profesional surge de argumentacion propia."
        },
        {
          "source": "Correccion de placeholders",
          "target": "Calidad documental",
          "kind": "supports",
          "justification": "Evita errores operativos en archivos y referencias."
        }
      ],
      "evidence": [
        "README local con identidad, pauta editorial y estructura.",
        "Programa analitico local con ejes de trabajo.",
        "Archivo .bib local con claves institucionales verificables.",
        "Plantilla .tex local con metadatos de alumno y curso."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 11: se preservan gates historicos de JSON parseable y normalizacion manual.",
      "Ciclo 11: se refuerza regla transversal de no transferir contenido tematico no validado entre materias no equivalentes.",
      "Ciclo 11: se integra riesgo operativo local de placeholders/tokens sin expandir como regla estable."
    ]
  }
}