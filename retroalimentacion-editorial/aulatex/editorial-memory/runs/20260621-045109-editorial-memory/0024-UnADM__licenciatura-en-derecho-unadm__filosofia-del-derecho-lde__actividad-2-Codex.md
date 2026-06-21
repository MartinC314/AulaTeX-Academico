{
  "summary": [
    "Se consolida actividad-2 con transferencia lateral desde actividad-1 por union y deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa y compuertas de calidad sin regresion.",
    "Se refuerza que solo se transfieren patrones reutilizables entre hermanos, no conclusiones ni bibliografia exclusiva.",
    "Se mantiene normalizacion obligatoria de salidas no estructuradas antes de propagacion recursiva.",
    "Se conserva estado provisional de fuentes heredadas no verificadas y se exige confirmacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre.",
    "Vincular actividad-2 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar postura propia, cita textual y parafrasis.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir tema, semana o formato de actividad-2 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Confirmar que cada afirmacion sustantiva tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrar claves ya citadas.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Verificar y corregir nombres de archivo con caracteres anomalos antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho como base contextual.",
    "Registrar fuentes especificas de actividad en el .bib canonico de la asignatura.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Tratar filosofia-del-derecho-clean.bib como complemento tematico (supuesto) y no como reemplazo automatico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir entre hermanos solo identidad, estructura, calidad y patrones argumentativos reutilizables.",
    "Evitar copiar redaccion literal, conclusiones especificas y bibliografia exclusiva del nodo origen.",
    "Aplicar compresion por union-dedupe lossless, no por recorte.",
    "Mantener trazabilidad del caracter provisional de herencias no verificadas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto solicitado.",
    "Confirmar si existe plantilla docente obligatoria de secciones para actividad-2.",
    "Confirmar estilo de citacion institucional obligatorio (supuesto: no confirmado).",
    "Confirmar nombre canonico final del .bib de asignatura tras resolver token Slug.",
    "Confirmar si las fuentes de interpretacion juridica aplican a actividad-2 o solo a semana 7."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica.",
      "Normalizacion estructurada obligatoria antes de propagar.",
      "Transferencia lateral controlada entre nodos hermanos."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Preservar continuidad editorial sin perder validez institucional ni tecnica.",
      "Asegurar que cada entrega combine fundamento, evidencia y criterio propio."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Cierre juridico con postura propia.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion juridica -> respaldo verificable -> interpretacion propia.",
      "Consigna local -> adecuacion de formato -> verificacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales troncales",
        "Integridad academica",
        "Normalizacion de salidas",
        "Trazabilidad cita-bibliografia",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, formato y finalidad comun."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion segura."
        },
        {
          "source": "Trazabilidad cita-bibliografia",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Permite verificar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad 2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre hermanos."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, citas verificables y conclusion juridica.",
        "Programa analitico fija proposito y ejes de trabajo transferibles.",
        "Regla vigente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 24: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 24: se conserva todo patron reutilizable y se excluye contenido exclusivo de actividad-1.",
      "Ciclo 24: se refuerza control de supuestos y estado provisional de fuentes no verificadas.",
      "Ciclo 24: se mantiene compatibilidad LaTeX/BibTeX y resolucion de tokens Slug pendientes."
    ]
  }
}