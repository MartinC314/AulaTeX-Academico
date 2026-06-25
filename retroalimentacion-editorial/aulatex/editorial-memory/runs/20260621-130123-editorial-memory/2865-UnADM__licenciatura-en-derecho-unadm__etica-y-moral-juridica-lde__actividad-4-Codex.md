{
  "summary": [
    "Se refuerza transferencia lateral reusable desde Filosofia del Derecho hacia Etica y Moral Juridica sin copiar contenido especifico.",
    "Se conserva identidad UnADM, ubicacion curricular y ejes editoriales comunes verificables.",
    "Se mantiene regla dura de normalizacion: no propagar salidas no parseables.",
    "Se consolida compresion lossless por deduplicacion de reglas equivalentes.",
    "Se agregan controles locales verificables sobre README, programa analitico y .bib del destino.",
    "Se preserva separacion entre patrones transferibles y bibliografia/conclusiones no transferibles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular toda actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar registro de ciclo y origen de propagacion en cada fusion."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Evitar secciones vacias y mantener coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Adaptar la argumentacion al campo de Etica y Moral Juridica sin copiar redaccion de nodos hermanos.",
    "Incluir postura propia sustentada; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir etica, moral y norma juridica cuando la consigna lo requiera [supuesto].",
    "Verificar correspondencia estricta entre consigna de Actividad 4 y entregable final [pendiente de consigna]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Evitar regresiones: no eliminar reglas utiles previamente validadas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos en README antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Depurar duplicados de entradas equivalentes por clave canonica [supuesto].",
    "Marcar y reparar entradas truncadas antes de citar [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No transferir conclusiones especificas ni bibliografia exclusiva entre nodos laterales.",
    "Aplicar analogia controlada: conservar esqueleto editorial y adaptar semantica disciplinar local.",
    "Si falta consigna local, mantener estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar rubrica de evaluacion especifica de Actividad 4.",
    "Confirmar si el entregable principal es reporte, presentacion u otro formato.",
    "Confirmar politica local de clave canonica para deduplicar alias BibTeX.",
    "Confirmar y reparar la entrada truncada en etica-y-moral-juridica.bib [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Prudente ante datos no verificados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion obligatoria antes de propagar.",
        "Trazabilidad de fuente, ciclo y propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 creditos.",
        "Asignatura destino: Etica y Moral Juridica."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos y marco normativo o doctrinal pertinentes.",
      "Analisis propio con postura academica.",
      "Evidencia verificable y citas consistentes.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros y verificables.",
      "Sostener continuidad editorial entre asignaturas sin perder especificidad local.",
      "Asegurar calidad formal, argumentativa y tecnica en LaTeX."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales no ornamentales.",
      "Afirmaciones fuertes siempre con soporte.",
      "Uso explicito de etiqueta [supuesto] cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco -> analisis -> conclusion.",
      "Contrastar categorias proximas sin confundir niveles normativos.",
      "Derivar conclusion desde evidencia y razonamiento, no desde opinion aislada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Conceptos clave",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Norma juridica",
        "Normalizacion JSON",
        "Bibliografia verificable"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del objeto de estudio."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion valida emerge del razonamiento sustentado."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Son categorias relacionadas pero no equivalentes en argumentacion juridica."
        },
        {
          "source": "Moral",
          "target": "Norma juridica",
          "kind": "contrasts",
          "justification": "La validez juridica no se reduce automaticamente a valor moral."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        }
      ],
      "evidence": [
        "README del destino confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico del destino define ejes de trabajo transferibles.",
        "Archivo .bib local evidencia necesidad de deduplicacion y reparacion de truncamiento [supuesto].",
        "Historial local registra fallas repetidas de JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se consolida patron lateral comun de estructura y calidad.",
      "Ciclo 13: se mantiene regla de bloqueo por JSON no parseable.",
      "Ciclo 13: se refuerza separacion entre patrones reutilizables y contenido especifico no transferible.",
      "Ciclo 13: se incorporan controles tecnicos locales de README, tokens Slug y .bib."
    ]
  }
}