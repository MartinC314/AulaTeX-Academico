{
  "summary": [
    "Se mantiene traza de fallas historicas de parseo como contexto no operativo.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se conserva compresion lossless por deduplicacion sin recorte de reglas utiles.",
    "Se transfiere solo patron reusable lateral desde Filosofia del Derecho: problema, conceptos, evidencia, analisis y conclusion.",
    "Se evita copiar conclusiones, redaccion literal y bibliografia exclusiva del nodo origen.",
    "Se consolidan mejoras locales verificables: token Slug sin expandir en README/programa y entrada .bib truncada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Usar tono academico-juridico claro y argumentativo.",
    "Cerrar con criterio propio juridicamente defendible.",
    "Marcar como [Supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sustentar ubicacion curricular con UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto exigido por la planeacion semanal.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener estructura reutilizable para reporte y presentacion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Verificar correspondencia entre consigna de Actividad 6 y tipo de producto.",
    "Traducir el analisis a aplicacion profesional juridica cuando proceda.",
    "No asumir fuentes de otras semanas sin validacion de consigna local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalizacion manual.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que la fusion no elimine reglas utiles previas.",
    "Validar consistencia entre consigna, estructura, citas y conclusion.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Registrar explicitamente supuestos pendientes de verificacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad con reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres/rutas anomalas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni completar campos sin respaldo.",
    "Conservar metadatos minimos: autor/editor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Deduplicar entradas equivalentes por clave canonica sin perder trazabilidad.",
    "Resolver duplicados locales verificables: huertaEticaConClasicos2000/huerta2000etica, ronquilloarmasEticaGeneralProfesional2018/ronquillo2018etica, singerCompendioEtica1995/singer1995compendio.",
    "Bloquear cita operativa de entradas truncadas hasta completar campos minimos."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura completa.",
    "Transferir a nodos laterales solo patrones generales reutilizables.",
    "Evitar trasladar bibliografia exclusiva o conclusiones especificas entre actividades hermanas.",
    "Aplicar analogia controlada: conservar esqueleto argumentativo y adaptar contenido a consigna local.",
    "Mantener historial de fallas de parseo como alerta de calidad, no como regla de contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de la Actividad 6.",
    "Confirmar formato de entrega exigido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar cierre correcto de la entrada sierraUniversidadNacional1910 en .bib.",
    "Definir criterio formal de clave canonica para deduplicacion bibliografica institucional."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Reflexivo en etica y moral juridica."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etica y Moral juridica.",
        "[Supuesto] Actividad 6 pendiente de confirmacion por consigna textual."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo/doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Garantizar trazabilidad entre consigna, argumentos, evidencia y cierre juridico.",
      "Preservar memoria editorial reusable sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explicito de [Supuesto] ante vacios de datos.",
      "Cierre con aplicabilidad juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis propio -> conclusion transferible.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Consigna -> objetivo -> desarrollo -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON parseable",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Deduplicacion bibliografica canonica",
        "Integridad academica"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y consistencia institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El problema activa el razonamiento academico-juridico."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion debe derivar del desarrollo argumentado."
        },
        {
          "source": "Normalizacion JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion segura."
        },
        {
          "source": "Deduplicacion bibliografica canonica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Reduce ambiguedad de claves y mantiene trazabilidad de fuentes."
        }
      ],
      "evidence": [
        "README local define identidad UnADM, integridad academica y conclusion con criterio propio.",
        "Programa analitico local define ejes: problema, conceptos, producto, analisis y conclusion.",
        "README y programa muestran token Slug sin expandir.",
        ".bib local contiene duplicados verificables y entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se refuerzan patrones laterales reutilizables sin transferir contenido especifico de Filosofia del Derecho.",
      "Ciclo 21: se mantiene regla de bloqueo por JSON no parseable.",
      "Ciclo 21: se agrega control verificable sobre token Slug sin expandir y curacion de .bib truncado."
    ]
  }
}