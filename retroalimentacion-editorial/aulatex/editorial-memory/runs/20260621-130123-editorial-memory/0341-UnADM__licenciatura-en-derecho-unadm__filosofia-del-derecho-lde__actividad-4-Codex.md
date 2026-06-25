{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con union-dedupe y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes de la asignatura.",
    "Se refuerza gate estricto de JSON parseable por antecedentes de salidas no estructuradas.",
    "Se transfieren solo patrones reutilizables desde Actividad 1, sin copiar conclusiones ni bibliografia exclusiva."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear la actividad a Licenciatura en Derecho y Filosofia del Derecho.",
    "Mantener referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y postura propia en la actividad.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar automaticamente fuentes de otras semanas.",
    "Supuesto: confirmar consigna exacta de Actividad 4 antes de fijar contenido especifico."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Verificar que el producto final corresponda a la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en español consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables ya usadas en documentos activos.",
    "Citar solo claves existentes en el .bib para evitar errores de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens no expandidos tipo $(@{...}.Slug) antes de compilar.",
    "Corregir nombres de archivo con caracteres dañados detectados en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Agregar al .bib solo fuentes realmente consultables para la actividad.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, año y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a otra actividad; confirmar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar refuerzo-lateral con patrones, no con contenido literal entre hermanos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Evitar regresiones de calidad en nodos vecinos.",
    "Cuando falte consigna local, propagar plantilla estructural y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y criterios.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar rubrica docente especifica para profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de asignatura.",
    "Confirmar si la bibliografia de interpretacion juridica aplica o no a Actividad 4."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Obligatoria, 8 creditos."
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
      "Transformar la planeacion semanal en entregables con fundamento juridico y criterio propio.",
      "Asegurar trazabilidad de fuentes y calidad editorial consistente entre actividades."
    ],
    "style_markers": [
      "Definir objetivo al inicio.",
      "Separar hechos, conceptos, argumentos y postura.",
      "Usar citas explicitas para afirmaciones sustantivas.",
      "Marcar supuestos de forma visible."
    ],
    "argumentative_patterns": [
      "Problema inicial -> marco conceptual/normativo -> analisis propio -> postura -> conclusion.",
      "Relacionar evidencia con inferencia juridica antes del cierre.",
      "Evitar saltos de conclusion sin soporte."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Integridad academica",
        "Ejes editoriales de Filosofia del Derecho",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal y precision juridica",
          "kind": "supports",
          "justification": "La pauta editorial institucional exige consistencia de voz."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay reutilizacion confiable."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Coherencia problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion requiere respaldo verificable."
        }
      ],
      "evidence": [
        "Pauta editorial del README: identidad, integridad, citas verificables y conclusion propia.",
        "Programa analitico: cinco ejes reutilizables.",
        "Antecedentes de salida no parseable: gate JSON estricto obligatorio."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: refuerzo lateral aplicado por analogia controlada entre hermanos.",
      "Se deduplicaron reglas redundantes conservando semantica valida.",
      "Se evitaron traslados de contenido especifico de Actividad 1.",
      "Se mantuvieron supuestos abiertos donde falta consigna local verificable."
    ]
  }
}