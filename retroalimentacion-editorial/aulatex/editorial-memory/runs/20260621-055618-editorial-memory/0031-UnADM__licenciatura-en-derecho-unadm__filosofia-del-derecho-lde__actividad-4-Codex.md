{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte de reglas utiles.",
    "Se preserva identidad UnADM y contexto curricular verificable: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene gate estricto de JSON parseable por antecedentes de salidas no estructuradas.",
    "Se evita transferir conclusiones o bibliografia exclusiva de Actividad 1 al nodo hermano."
  ],
  "identity_rules": [
    "Mantener tono formal academico de UnADM.",
    "Alinear cada entrega con Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar integridad academica con citas verificables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto pedido en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a ejes del programa analitico.",
    "Incluir problema juridico o social explicito.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de Semana 7 aplica automaticamente a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregado y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos en README antes de compilar.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado por slug es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a interpretacion juridica Semana 7; validar aplicabilidad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no contenido literal entre hermanos.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar union-dedupe para compresion lossless.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica de Actividad 4.",
    "Confirmar si Actividad 4 exige reporte, presentacion u otro formato.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del archivo .bib por token Slug no resuelto.",
    "Confirmar si se reutiliza bibliografia existente o se crea bloque bibliografico incremental."
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
        "Integridad academica y citas verificables.",
        "Carpeta de asignatura como entrada canonica."
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
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Garantizar trazabilidad editorial y consistencia institucional entre actividades hermanas.",
      "Mantener cierre argumentativo con utilidad profesional."
    ],
    "style_markers": [
      "Objetivo puntual antes del desarrollo.",
      "Secciones funcionales y separadas.",
      "Cita explicita en afirmaciones relevantes.",
      "Supuestos marcados de forma visible.",
      "Cierre con conclusion juridica propia."
    ],
    "argumentative_patterns": [
      "Problematizar el tema al inicio.",
      "Definir marco conceptual y normativo.",
      "Contrastar evidencia con analisis propio.",
      "Fijar postura argumentada.",
      "Concluir con transferibilidad practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica",
        "Consistencia cita-texto-bib"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales de Filosofia del Derecho",
          "kind": "supports",
          "justification": "La identidad define tono y marco de aplicacion de los ejes."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "La propagacion recursiva segura requiere formato parseable."
        },
        {
          "source": "Integridad academica",
          "target": "Consistencia cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad exige trazabilidad bibliografica completa."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Conclusion transferible a la practica juridica",
          "kind": "develops",
          "justification": "El flujo problema-evidencia-analisis culmina en cierre aplicado."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, entrada canonica y exigencia de conclusion juridica propia.",
        "Programa analitico define cinco ejes reutilizables de trabajo.",
        "Antecedentes del nodo registran salidas no parseables y exigen gate JSON."
      ]
    },
    "reinforcement_log": [
      "Ciclo 31: deduplicacion de reglas repetidas en tono, estructura y calidad.",
      "Ciclo 31: refuerzo lateral de patrones reutilizables sin copiar redaccion de Actividad 1.",
      "Ciclo 31: mantenimiento de supuestos abiertos donde falta consigna local verificable.",
      "Ciclo 31: preservacion de reglas tecnicas LaTeX y bibliografia con foco en trazabilidad."
    ]
  }
}