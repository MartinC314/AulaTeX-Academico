{
  "summary": [
    "Se transfiere ADN editorial reusable desde Filosofia del Derecho a Etica y Moral juridica sin copiar contenido tematico especifico.",
    "Se refuerza identidad UnADM, estructura argumentativa comun y control de calidad por JSON parseable.",
    "Se mantiene compresion lossless por union y deduplicacion semantica.",
    "Se conserva regla de marcar supuestos cuando falte consigna local verificable.",
    "Se agrega mejora verificable local: detectar truncamiento en .bib y tokens Slug sin expandir."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Responder siempre en JSON valido y parseable segun esquema.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar estructura base: problema, conceptos, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto pedido en la planeacion semanal."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No arrastrar conclusiones de otra asignatura sin justificacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar.",
    "Confirmar que no se eliminen reglas utiles previas al fusionar.",
    "Validar ausencia de duplicados semanticos tras fusion.",
    "Confirmar respaldo o marca de supuesto en afirmaciones no evidentes.",
    "Validar correspondencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos o paquetes no estandar sin justificacion.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir rutas o nombres con caracteres anomalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base y bibliografia especifica por actividad.",
    "Marcar para revision manual entradas potencialmente duplicadas por autor mas titulo mas anio.",
    "Marcar truncamiento de entrada .bib como incidencia local [supuesto hasta verificacion del archivo completo]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones de origen.",
    "Aplicar analogia controlada entre asignaturas del mismo bloque curricular.",
    "Mantener trazabilidad de origen y destino en cada injerto de memoria.",
    "Si falta consigna local, propagar estructura base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5 en Etica y Moral juridica.",
    "Confirmar tipo de producto final requerido en la semana.",
    "Confirmar rubrica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar si el truncamiento visto en etica-y-moral-juridica.bib existe en archivo real [supuesto].",
    "Confirmar politica local para unificar claves BibTeX duplicadas sin perder trazabilidad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Reflexivo ante dilemas etico-juridicos."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Trazabilidad de memoria editorial y fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Actividad destino: Actividad 5."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Analisis propio con postura academica.",
      "Evidencia verificable.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Sostener continuidad editorial institucional entre actividades.",
      "Garantizar calidad tecnica y argumentativa en cada entrega."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explicitas y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Citas verificables en afirmaciones sustantivas.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Conectar con marco normativo o doctrinal.",
      "Desarrollar analisis critico propio.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Deduplicacion lossless"
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
          "justification": "La pauta institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere respaldo documental."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento del estudiante."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Deduplicacion lossless",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay consolidacion confiable."
        }
      ],
      "evidence": [
        "README local fija identidad UnADM, integridad academica y conclusion juridica con criterio propio.",
        "Programa analitico local fija ejes: problema, conceptos, producto, analisis y conclusion.",
        "README y programa muestran token Slug sin expandir, incidencia tecnica verificable.",
        "Archivo .bib local muestra entrada final truncada, incidencia marcada como supuesto hasta verificacion completa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se refuerzan reglas laterales reutilizables desde Filosofia del Derecho hacia Etica y Moral juridica.",
      "Ciclo 21: no se transfiere bibliografia exclusiva ni conclusiones tematicas del nodo hermano.",
      "Ciclo 21: se mantiene canon de calidad JSON parseable y compresion lossless por deduplicacion."
    ]
  }
}