{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM y marco curricular verificable.",
    "Se refuerza normalizacion estructurada y validacion JSON estricta.",
    "Se transfieren solo patrones reutilizables desde Actividad 1.",
    "Supuesto: falta consigna local completa de Actividad 4."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Vincular ubicacion curricular a semestre 1, bloque 2, obligatoria, 8 creditos con fuente institucional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar el artefacto final al tipo solicitado por la actividad.",
    "No arrastrar conclusiones especificas de actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de propagar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas heredadas.",
    "Verificar correspondencia entre producto entregado y consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica de otra semana; validar pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Aplicar union-dedupe para compresion lossless sin recorte.",
    "Evitar regresiones de reglas utiles previas.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna completa de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del .bib cuando hay plantilla Slug sin resolver.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere .bib incremental."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
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
      "Convertir planeacion semanal en productos academicos trazables.",
      "Asegurar calidad juridica, claridad y transferencia profesional.",
      "Preservar coherencia editorial entre actividades hermanas sin copiar contenido especifico."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales y jerarquia clara.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y normas.",
      "Contrastar evidencia.",
      "Desarrollar postura propia.",
      "Cerrar con conclusion aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica",
        "Trazabilidad bibliografica",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal y precision juridica",
          "kind": "supports",
          "justification": "La pauta editorial institucional fija estilo y enfoque."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay transferencia segura."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe derivar de evidencia y analisis."
        },
        {
          "source": "Ejes editoriales",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo."
        }
      ],
      "evidence": [
        "README exige identidad UnADM, citas verificables y conclusion juridica.",
        "Programa analitico define cinco ejes de trabajo reutilizables.",
        "Antecedentes registran salidas no parseables; se mantiene gate JSON estricto.",
        "Supuesto: la consigna completa de Actividad 4 no esta visible."
      ]
    },
    "reinforcement_log": [
      "Ciclo 33: deduplicacion de reglas repetidas con preservacion total de contenido util.",
      "Ciclo 33: se eliminaron patrones de cohesion no estandar en relaciones y se normalizo a esquema permitido.",
      "Ciclo 33: se reforzo separacion entre patrones transferibles y contenido especifico no transferible.",
      "Ciclo 33: se mantuvieron preguntas abiertas donde faltan datos locales verificables."
    ]
  }
}