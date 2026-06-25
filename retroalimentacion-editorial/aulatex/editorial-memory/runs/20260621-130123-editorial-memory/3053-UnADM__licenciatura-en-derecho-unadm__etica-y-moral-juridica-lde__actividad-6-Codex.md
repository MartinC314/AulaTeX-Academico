{
  "summary": [
    "Se preserva la base editorial vigente de Actividad 6 y su trazabilidad de fallas de parseo como contexto no operativo.",
    "Se refuerzan patrones laterales reutilizables desde Filosofia del Derecho: identidad UnADM, estructura argumentativa, compuertas de calidad y normalizacion previa a propagacion.",
    "Se mantiene compresion lossless por deduplicacion, sin recorte de reglas utiles ni copia de contenido especifico del nodo origen.",
    "Se agregan mejoras verificables del contexto local: token Slug sin expandir en README/programa y entrada .bib truncada marcada como [Supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Usar tono academico-juridico, claro y con cierre argumentativo propio.",
    "Marcar como [Supuesto] todo dato no visible en la consigna de Actividad 6.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sustentar ubicacion curricular con UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener coherencia entre objetivo, desarrollo y conclusion.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca [Supuesto].",
    "Verificar correspondencia entre consigna de Actividad 6 y tipo de producto entregado.",
    "Traducir el analisis a aplicacion profesional juridica cuando proceda.",
    "No asumir fuentes de otras semanas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalizacion manual.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas en cada fusion.",
    "Validar consistencia entre consigna, estructura, citas y conclusion.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad con reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar referencias.",
    "Mantener consistencia terminologica entre .tex, README y programa analitico."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de la actividad en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias ni completar metadatos sin respaldo.",
    "Conservar metadatos minimos: autor/editor, titulo, anio y fuente editorial o URL.",
    "Deduplicar entradas equivalentes por clave canonica sin perder trazabilidad.",
    "Detectar y resolver duplicados evidentes: huertaEticaConClasicos2000/huerta2000etica, ronquilloarmasEticaGeneralProfesional2018/ronquillo2018etica, singerCompendioEtica1995/singer1995compendio.",
    "Bloquear uso operativo de entradas truncadas hasta completar campos minimos.",
    "[Supuesto] La entrada sierraUniversidadNacional1910 esta truncada y requiere curacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, generales y parseables.",
    "Transferir lateralmente identidad, estructura, calidad y patrones argumentativos; no copiar conclusiones ni bibliografia exclusiva.",
    "Aplicar analogia controlada: conservar esqueleto editorial comun y ajustar solo con evidencia local.",
    "Si falta consigna textual, propagar plantilla base y abrir preguntas en lugar de inventar contenido.",
    "Mantener trazabilidad de ciclos con fallas de parseo como historial, no como regla operativa."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de la Actividad 6.",
    "Confirmar formato de entrega exigido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Definir clave canonica oficial para cada par duplicado en .bib.",
    "[Supuesto] Confirmar y corregir cierre del campo incompleto en sierraUniversidadNacional1910."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
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
      "Transformar la planeacion semanal en productos academicos con evidencia y utilidad profesional.",
      "Garantizar coherencia entre consigna, argumentacion y cierre juridico.",
      "Preservar memoria editorial reutilizable con compresion lossless."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables en afirmaciones sustantivas.",
      "Cierre con implicacion juridica aplicable.",
      "Etiquetado [Supuesto] para vacios de informacion."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis propio -> conclusion transferible.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Consigna -> objetivo puntual -> desarrollo coherente -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Normalizacion JSON parseable",
        "Estructura argumentativa comun",
        "Deduplicacion bibliografica canonica",
        "Analogia controlada lateral"
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
          "target": "Estructura argumentativa comun",
          "kind": "supports",
          "justification": "La pauta editorial institucional exige formato y razonamiento consistentes."
        },
        {
          "source": "Normalizacion JSON parseable",
          "target": "Analogia controlada lateral",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura entre nodos."
        },
        {
          "source": "Deduplicacion bibliografica canonica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Reduce ambiguedad de claves y mejora trazabilidad de citas."
        },
        {
          "source": "Estructura argumentativa comun",
          "target": "Conclusion transferible a la practica juridica",
          "kind": "develops",
          "justification": "El cierre depende de un desarrollo previo basado en problema, marco y analisis."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, citas verificables y conclusion con criterio propio.",
        "Programa analitico local: ejes problema, conceptos, producto, analisis y conclusion.",
        ".bib local: duplicados verificables y entrada truncada [Supuesto].",
        "Regla heredada valida: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se consolidan reglas laterales reutilizables sin copiar contenido especifico del origen.",
      "Ciclo 16: se preservan todas las compuertas de calidad previas y se deduplican formulaciones equivalentes.",
      "Ciclo 16: se refuerza control de supuestos y curacion bibliografica local verificable."
    ]
  }
}