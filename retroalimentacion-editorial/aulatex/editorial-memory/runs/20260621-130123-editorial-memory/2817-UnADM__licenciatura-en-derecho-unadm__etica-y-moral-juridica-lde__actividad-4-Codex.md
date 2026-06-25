{
  "summary": [
    "Se consolida transferencia lateral desde Filosofia del Derecho hacia Etica y Moral Juridica con deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza estructura editorial comun: problema, conceptos y fuentes, analisis propio, conclusion juridica.",
    "Se mantiene regla de normalizacion: no propagar salidas no parseables sin convertir a JSON valido.",
    "Se agregan controles locales verificables para README, programa analitico y .bib de Etica y Moral Juridica.",
    "Se evita transferir conclusiones o bibliografia exclusiva de Filosofia del Derecho por regla de lateralidad."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Vincular toda actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto cualquier dato ausente en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la argumentacion al campo de Etica y Moral Juridica sin copiar redaccion de nodos hermanos.",
    "Incluir postura propia sustentada, no solo descripcion.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Explicar relacion operativa entre etica, moral y norma juridica cuando la consigna lo pida [supuesto]."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 4 [pendiente de consigna]."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos detectados en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Depurar entradas duplicadas equivalentes manteniendo compatibilidad tecnica de claves activas [supuesto].",
    "Marcar y corregir entradas truncadas del .bib antes de citar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura y calidad.",
    "Evitar regresiones de reglas utiles previas.",
    "Aplicar normalizacion manual en nodos con historial de salida no estructurada.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4 para ajustar producto y profundidad.",
    "Confirmar rubrica de evaluacion especifica de Actividad 4.",
    "Confirmar si el entregable principal es reporte, presentacion u otro formato.",
    "Confirmar politica local para deduplicar claves alias en etica-y-moral-juridica.bib.",
    "Confirmar y reparar la entrada BibTeX truncada detectada al final del archivo .bib."
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
      "Transformar la planeacion semanal en productos academicos claros, fundamentados y transferibles.",
      "Mantener continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no ornamentales.",
      "Citas verificables en puntos de afirmacion fuerte.",
      "Conclusion juridica con implicacion practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema -> definir conceptos -> aplicar marco normativo/doctrinal -> argumentar postura -> concluir.",
      "Contrastar etica y moral con efectos juridicos cuando sea pertinente [supuesto].",
      "Evitar resumen pasivo; priorizar inferencia justificada."
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
        "Norma juridica",
        "Planeacion semanal",
        "Evidencia verificable"
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
          "justification": "La pauta editorial local exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se construye sobre un caso o pregunta delimitada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva de razonamiento y evidencia."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Son categorias relacionadas pero no identicas en uso argumentativo."
        },
        {
          "source": "Moral",
          "target": "Norma juridica",
          "kind": "contrasts",
          "justification": "La validez juridica no se reduce automaticamente a valor moral."
        }
      ],
      "evidence": [
        "README de Etica y Moral Juridica: identidad UnADM, punto de entrada canonico y conclusion juridica.",
        "Programa analitico: ejes de trabajo en cinco pasos reutilizables.",
        "Archivo etica-y-moral-juridica.bib: base bibliografica local y necesidad de depuracion por duplicados/truncamiento."
      ]
    },
    "reinforcement_log": [
      "Se importan patrones transversales validados desde actividad hermana sin copiar contenido especifico.",
      "Se mantiene regla dura de JSON parseable como precondicion de propagacion.",
      "Se fortalece control de supuestos por ausencia de consigna de Actividad 4.",
      "Se ancla bibliografia al .bib local de la asignatura destino.",
      "Se conserva compresion lossless por union y deduplicacion."
    ]
  }
}