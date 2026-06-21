{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con transferencia reusable desde Actividad 1.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales sin copiar contenido especifico.",
    "Se refuerza normalizacion estructurada y bloqueo por JSON no parseable antes de propagar.",
    "Se mantiene regla de marcar como supuesto todo dato no visible en la consigna local.",
    "Se conserva que la carpeta de asignatura es el punto de entrada canonico."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica de UnADM.",
    "Alinear contenido a Licenciatura en Derecho y Filosofia del Derecho.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto cualquier dato no verificable en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Aplicar los cinco ejes del programa analitico en toda entrega.",
    "Incluir postura argumentada del estudiante y evitar solo descripcion.",
    "Sustentar afirmaciones con evidencia verificable y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir conclusiones especificas de Actividad 1 a Actividad 4.",
    "No asumir fuentes de semanas distintas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Verificar esquema completo antes de reutilizacion recursiva.",
    "Normalizar respuestas no estructuradas heredadas antes de propagar.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar correspondencia del producto con la consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en .bib para evitar referencias rotas.",
    "Mantener claves BibTeX estables; no renombrar sin necesidad justificada.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Verificar nombres de archivo del README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de referenciar rutas.",
    "Compilar sin errores criticos ni citas rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente o URL.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a interpretacion juridica de Semana 7; verificar aplicabilidad en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura minima.",
    "Transferir solo patrones reutilizables de identidad, estructura y calidad.",
    "Evitar copiar redaccion literal o conclusiones de nodos hermanos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar deduplicacion lossless por union semantica, no por recorte."
  ],
  "open_questions": [
    "Confirmar consigna textual de Actividad 4: producto, extension y rubrica.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del .bib ante token Slug sin resolver en README.",
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
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y trazabilidad.",
      "Estandarizar calidad editorial para propagacion segura entre actividades."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales claras.",
      "Citas explicitas en afirmaciones clave.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Desarrollar conceptos y norma aplicable.",
      "Contrastar evidencia y analisis propio.",
      "Fijar postura justificada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Validacion JSON estricta",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion segura."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes definen orden y cierre argumentativo."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida requiere respaldo trazable."
        },
        {
          "source": "Transferencia entre hermanos",
          "target": "No copiar contenido especifico",
          "kind": "contrasts",
          "justification": "Se transfieren patrones, no redacciones ni conclusiones concretas."
        }
      ],
      "evidence": [
        "Pauta editorial del README.",
        "Ejes de trabajo del programa analitico.",
        "Antecedentes de salidas no parseables en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 26: se deduplican reglas repetidas y se preserva cobertura completa.",
      "Ciclo 26: se refuerza gate de JSON parseable por historial de fallas.",
      "Ciclo 26: se mantiene separacion entre patrones transferibles y contenido especifico de actividad hermana.",
      "Ciclo 26: se mantienen supuestos abiertos donde faltan datos locales verificables."
    ]
  }
}