{
  "summary": [
    "Se consolida memoria editorial de Actividad 6 con deduplicacion lossless y sin recorte de reglas utiles.",
    "Se refuerzan patrones laterales reutilizables desde Filosofia del Derecho: identidad UnADM, estructura argumentativa y compuertas de calidad.",
    "Se mantiene regla de bloqueo: no propagar salidas no estructuradas ni JSON no parseable.",
    "Se agregan mejoras verificables locales: token Slug sin expandir en README/programa y entrada .bib truncada.",
    "Se preserva trazabilidad de fallas historicas de parseo como contexto no operativo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Usar tono academico-juridico claro, con conclusion de criterio propio.",
    "Marcar como [Supuesto] cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sustentar ubicacion curricular con UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura y profundidad al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Verificar coherencia entre objetivo, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca [Supuesto].",
    "Traducir el analisis a implicaciones juridicas profesionales cuando proceda.",
    "Verificar correspondencia entre consigna de Actividad 6 y tipo de producto entregado.",
    "No reutilizar conclusiones especificas de actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalizacion manual.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que la fusion no elimine reglas utiles previas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que toda afirmacion sustantiva tenga respaldo o marca [Supuesto]."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad con reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener secciones estables para reutilizacion entre reporte y presentacion.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de la actividad en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "No inventar referencias ni completar metadatos sin respaldo.",
    "Conservar metadatos minimos: autor/editor, titulo, anio, fuente/editorial o URL.",
    "Deduplicar entradas equivalentes por clave canonica sin perder trazabilidad.",
    "Resolver duplicados locales verificables: huertaEticaConClasicos2000/huerta2000etica, ronquilloarmasEticaGeneralProfesional2018/ronquillo2018etica, singerCompendioEtica1995/singer1995compendio.",
    "Bloquear uso operativo de entradas truncadas hasta completar campos minimos.",
    "[Supuesto] sierraUniversidadNacional1910 esta truncada y requiere curacion antes de citar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales validadas y parseables.",
    "Transferir lateralmente patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener compresion lossless por union y deduplicacion semantica.",
    "Aplicar normalizacion manual si un nodo vecino devuelve salida no estructurada.",
    "Preservar trazabilidad de supuestos y de fuentes provisionales en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar formato exigido de entrega: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar criterio formal de clave canonica para deduplicacion .bib.",
    "Confirmar y completar el campo faltante de sierraUniversidadNacional1910.",
    "[Supuesto] Validar si Actividad 6 exige fuentes obligatorias adicionales de semana."
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
        "[Supuesto] Actividad 6 pertenece formalmente a Etica y Moral juridica."
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
      "Transformar planeacion semanal en productos academicos claros y verificables.",
      "Mantener continuidad editorial entre actividades sin contaminar contenido especifico.",
      "Asegurar trazabilidad argumentativa y aplicabilidad profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables en afirmaciones sustantivas.",
      "Cierre con criterio juridico propio.",
      "Marcado explicito de [Supuesto] cuando falten datos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> analisis propio -> conclusion transferible.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Consigna -> objetivo -> desarrollo -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "JSON parseable",
        "Deduplicacion bibliografica canonica"
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
          "justification": "La pauta local exige identidad y citas verificables en cada entrega."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El programa analitico fija el problema como disparador del razonamiento."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion debe derivar del analisis y no de resumen descriptivo."
        },
        {
          "source": "JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "La memoria solo se reutiliza de forma segura si mantiene estructura valida."
        },
        {
          "source": "Deduplicacion bibliografica canonica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita duplicados, choques de claves y perdida de trazabilidad."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, integridad academica, conclusion con criterio propio.",
        "Programa analitico: ejes problema, conceptos, producto, analisis y conclusion.",
        "README/programa: token Slug sin expandir detectado.",
        ".bib local: duplicados verificables y entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: se transfieren patrones laterales reutilizables desde Filosofia del Derecho sin copiar contenido especifico.",
      "Ciclo 14: se mantiene regla fuerte de normalizacion JSON parseable previa a propagacion.",
      "Ciclo 14: se refuerza estructura argumentativa comun UnADM (problema-conceptos-analisis-conclusion).",
      "Ciclo 14: se consolida deduplicacion .bib con trazabilidad y bloqueo de entradas truncadas."
    ]
  }
}