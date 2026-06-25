{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica con transferencia de patrones reutilizables.",
    "Se preservan reglas utiles previas y se deduplican sin recorte semantico.",
    "Se mantiene bloqueo de propagacion para salidas no parseables y normalizacion obligatoria.",
    "Se refuerza estructura nuclear: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se agrega verificacion local de README, programa analitico y estado real del .bib.",
    "Se mantiene trazabilidad de supuestos cuando falte consigna textual de Actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Usar tono academico-juridico claro y argumentativo.",
    "Cerrar con criterio propio y aplicacion juridica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear estructura al producto solicitado por la planeacion semanal.",
    "Asegurar coherencia entre objetivo, desarrollo y conclusion.",
    "Mantener plantilla reutilizable para reporte y presentacion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Verificar correspondencia entre consigna de Actividad 6 y tipo de producto.",
    "Traducir el analisis a aplicacion profesional juridica cuando proceda.",
    "No copiar conclusiones especificas de nodos hermanos."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalizacion manual.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas utiles previas en cada fusion.",
    "Validar consistencia entre consigna, estructura, citas y conclusion.",
    "Registrar supuestos explicitos cuando falte dato formal."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad con reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Evitar comandos o paquetes no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Normalizar nombres de archivo con caracteres anomales antes de compilar."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas de la actividad en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM y bibliografia base verificable.",
    "No inventar fuentes ni completar datos sin respaldo documental.",
    "Conservar metadatos minimos: autor/editor, titulo, anio, fuente/editorial o URL.",
    "Deduplicar claves equivalentes sin perder trazabilidad historica.",
    "Resolver duplicados verificados: huertaEticaConClasicos2000/huerta2000etica, ronquilloarmasEticaGeneralProfesional2018/ronquillo2018etica, singerCompendioEtica1995/singer1995compendio.",
    "Bloquear cita operativa de entradas truncadas hasta completar campos minimos.",
    "[Supuesto] sierraUniversidadNacional1910 esta incompleta y requiere curacion antes de uso."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo reglas generales ya validadas.",
    "Transferir identidad, estructura, calidad y patrones argumentativos; no contenido tematico especifico.",
    "Aplicar analogia controlada: misma arquitectura editorial, distinto contenido disciplinar.",
    "Mantener deduplicacion lossless por union semantica, no por recorte.",
    "Conservar trazabilidad de fallas historicas de parseo como contexto no operativo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar formato exigido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Definir politica canonica de clave BibTeX para deduplicacion estable.",
    "Completar entrada sierraUniversidadNacional1910 y validar cierre de campos."
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
        "Asignatura destino: Etica y Moral juridica.",
        "[Supuesto] Actividad 6 pertenece formalmente a Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social como disparador.",
      "Conceptos, normas, doctrina y evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a practica profesional.",
      "Calidad editorial basada en JSON parseable y trazabilidad."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos.",
      "Asegurar coherencia entre objetivo, desarrollo, evidencia y cierre.",
      "Preservar identidad institucional y rigor juridico en cada entrega."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables en afirmaciones sustantivas.",
      "Uso explicito de [Supuesto] cuando falta dato.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion transferible.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion juridica.",
      "Consigna -> objetivo puntual -> desarrollo coherente -> validacion final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion JSON parseable",
        "Deduplicacion bibliografica canonica"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y tono institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El problema activa el razonamiento y la postura del estudiante."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "depends_on",
          "justification": "La conclusion valida depende del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion JSON parseable",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion segura de memoria."
        },
        {
          "source": "Deduplicacion bibliografica canonica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita duplicidad de citas y conserva trazabilidad."
        }
      ],
      "evidence": [
        "README local define identidad UnADM, integridad academica y conclusion con criterio propio.",
        "Programa analitico define ejes: problema, conceptos, producto, analisis y conclusion.",
        "README y programa muestran token Slug sin expandir que debe resolverse.",
        ".bib local contiene duplicados verificables y una entrada truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se refuerzan patrones laterales reutilizables sin mover contenido especifico de Filosofia del Derecho.",
      "Ciclo 11: se preservan compuertas de calidad y normalizacion parseable como regla dura.",
      "Ciclo 11: se consolida control bibliografico con deduplicacion canonica y bloqueo de entradas incompletas."
    ]
  }
}