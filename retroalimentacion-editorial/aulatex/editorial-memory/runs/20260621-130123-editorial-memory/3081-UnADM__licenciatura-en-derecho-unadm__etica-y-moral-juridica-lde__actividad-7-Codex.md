{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral juridica con deduplicacion lossless.",
    "Se preserva identidad UnADM y contexto curricular verificable del nodo destino.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion cuando no haya JSON parseable o estructura incompleta.",
    "Se agrega control de supuestos y trazabilidad para datos no visibles en la consigna.",
    "Se conserva compatibilidad LaTeX y normalizacion de tokens Slug sin expandir en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como [Supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para sustento de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la planeacion semanal de la actividad.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de semanas o materias distintas sin validacion.",
    "Confirmar que el tipo de entrega corresponde a la consigna de Actividad 7."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar que no se eliminen reglas utiles previas.",
    "Marcar supuestos explicitos cuando falten datos locales.",
    "Validar correspondencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables y evitar rupturas por renombre arbitrario.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas y nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Aplicar deduplicacion por equivalencia bibliografica sin perder trazabilidad de claves previas. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones ni redaccion literal.",
    "Reutilizar compuertas de calidad institucional sin perder especificidad local.",
    "Si falta consigna textual local, propagar estructura base y abrir preguntas.",
    "Aplicar estrategia progresiva por analogia controlada entre materias hermanas."
  ],
  "open_questions": [
    "Confirmar consigna exacta y tipo de producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Confirmar politica local de alias de claves BibTeX para duplicados existentes.",
    "Confirmar si las claves duplicadas actuales del .bib deben mantenerse por retrocompatibilidad. [Supuesto]",
    "Confirmar fuentes obligatorias de la semana de Etica y Moral juridica para Actividad 7."
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
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en producto academico verificable.",
      "Asegurar fundamento juridico, evidencia y criterio propio.",
      "Mantener continuidad editorial entre nodos de la misma licenciatura."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Citas explicitas y verificables.",
      "Supuestos etiquetados cuando aplique.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Contraste de posturas con evidencia.",
      "Toma de posicion del estudiante.",
      "Conclusion aplicable al ejercicio juridico."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Practica juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El desarrollo argumentativo parte del problema para construir postura."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar del razonamiento y evidencia presentados."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es base recurrente para argumentacion en la materia."
        },
        {
          "source": "Moral",
          "target": "Practica juridica",
          "kind": "depends_on",
          "justification": "La valoracion moral incide en criterios de actuacion profesional."
        }
      ],
      "evidence": [
        "README de Etica y Moral juridica: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes de trabajo y proposito de realizacion.",
        "Archivo etica-y-moral-juridica.bib: base bibliografica local con duplicados observables."
      ]
    },
    "reinforcement_log": [
      "Se preservaron reglas utiles previas del destino y del origen sin recorte semantico.",
      "Se deduplicaron formulaciones repetidas manteniendo alcance normativo.",
      "Se reforzaron patrones transferibles laterales sin copiar conclusiones especificas del nodo hermano.",
      "Se etiquetaron como [Supuesto] los puntos que requieren confirmacion local."
    ]
  }
}