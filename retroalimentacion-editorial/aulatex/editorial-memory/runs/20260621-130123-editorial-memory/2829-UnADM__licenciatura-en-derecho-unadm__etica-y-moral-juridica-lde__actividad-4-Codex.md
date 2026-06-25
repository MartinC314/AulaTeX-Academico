{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral Juridica con transferencia de patrones reutilizables.",
    "Se preserva identidad institucional UnADM y ubicacion curricular verificada: Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica de normalizacion: no propagar salidas no parseables sin convertir a JSON valido.",
    "Se refuerza estructura comun: problema, conceptos y fuentes, analisis propio, conclusion juridica.",
    "Se evita transferir redaccion literal, conclusiones especificas y bibliografia exclusiva del nodo hermano.",
    "Se agregan mejoras verificables locales: correccion de tokens Slug sin expandir y deteccion de entrada .bib truncada [supuesto confirmado por contexto parcial]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular toda actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como base de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Asegurar coherencia entre actividad, reporte y presentacion cuando coexistan."
  ],
  "activity_rules": [
    "Adaptar la argumentacion al campo de Etica y Moral Juridica sin copiar redaccion de nodos hermanos.",
    "Incluir postura propia sustentada; evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Explicar relacion operativa entre etica, moral y norma juridica cuando la consigna lo pida [supuesto].",
    "No asumir bibliografia de semanas o materias distintas sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar deduplicacion lossless por union sin eliminar reglas utiles previas.",
    "Verificar correspondencia del producto con la consigna de Actividad 4 [pendiente de consigna]."
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
    "Depurar duplicados de entradas BibTeX equivalentes con politica de clave canonica [supuesto hasta definir politica local].",
    "Marcar y reparar entradas BibTeX truncadas antes de citar [supuesto fuerte por corte en campo n de sierraUniversidadNacional1910]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones generales de identidad, estructura, calidad y metodo argumentativo.",
    "No propagar conclusiones tematicas ni bibliografia exclusiva entre materias hermanas.",
    "Aplicar normalizacion manual cuando se detecten salidas no estructuradas en nodos vecinos.",
    "Mantener historial de ciclos con fallas de parseo para prevencion de regresiones."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4 para ajustar producto y profundidad.",
    "Confirmar rubrica de evaluacion especifica de Actividad 4.",
    "Confirmar si el entregable principal es reporte, presentacion u otro formato.",
    "Confirmar politica local de deduplicacion BibTeX por clave canonica.",
    "Confirmar y reparar completamente la entrada truncada sierraUniversidadNacional1910 en el .bib."
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
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Etica y Moral Juridica."
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
      "Transformar la planeacion semanal en entregables con evidencia verificable y cierre argumentativo.",
      "Conservar coherencia institucional y calidad tecnica en LaTeX y bibliografia.",
      "Producir analisis juridico transferible a la practica profesional."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales sin relleno.",
      "Citas en afirmaciones fuertes.",
      "Conclusiones con implicacion juridica practica.",
      "Etiquetado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema -> definir conceptos -> aplicar marco normativo/doctrinal -> argumentar postura -> concluir.",
      "Contrastar categorias afines sin confundir planos descriptivo, valorativo y normativo.",
      "Evitar resumen pasivo; priorizar inferencia justificada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Conceptos clave",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Norma juridica"
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
          "justification": "El analisis requiere un caso o pregunta delimitada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del razonamiento sustentado."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Son categorias relacionadas pero no equivalentes."
        },
        {
          "source": "Moral",
          "target": "Norma juridica",
          "kind": "contrasts",
          "justification": "La validez juridica no depende automaticamente del juicio moral."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma ejes de trabajo en cinco pasos.",
        "Archivo .bib local evidencia duplicados y una entrada truncada [supuesto confirmado por fragmento visible].",
        "Memoria origen aporta regla robusta de normalizacion y compresion lossless por deduplicacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se transfiere nucleo institucional y metodologico desde nodo hermano sin copiar contenido especifico.",
      "Ciclo 4: se consolida gate de JSON parseable como condicion previa de propagacion recursiva.",
      "Ciclo 4: se refuerza estructura editorial comun aplicable a actividades de Derecho UnADM.",
      "Ciclo 4: se agregan controles tecnicos locales para Slug sin expandir y saneamiento BibTeX."
    ]
  }
}