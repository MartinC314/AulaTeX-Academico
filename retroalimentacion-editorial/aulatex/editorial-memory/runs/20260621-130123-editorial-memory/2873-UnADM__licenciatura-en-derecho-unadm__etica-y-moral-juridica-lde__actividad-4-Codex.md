{
  "summary": [
    "Se refuerza transferencia lateral reutilizable desde Filosofia del Derecho hacia Etica y Moral Juridica sin copiar contenido especifico.",
    "Se conserva identidad UnADM, ubicacion curricular y ejes editoriales comunes verificados en README y programa analitico.",
    "Se mantiene regla dura de normalizacion: no propagar salidas no parseables sin convertir a JSON valido.",
    "Se deduplican reglas previas sin recorte funcional y se preserva historial de fallas de parseo para trazabilidad.",
    "Se agregan controles verificables locales: token Slug sin expandir en README/programa y entrada BibTeX truncada en .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular Actividad 4 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta confirmacion local.",
    "Conservar registro de ciclo y origen de cada regla propagada."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Evitar secciones vacias y mantener coherencia entre actividad, reporte y presentacion cuando coexistan."
  ],
  "activity_rules": [
    "Adaptar argumentacion al campo de Etica y Moral Juridica sin copiar redaccion de nodos hermanos.",
    "Incluir postura propia sustentada y evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Explicar relacion operativa entre etica, moral y norma juridica cuando la consigna lo pida [supuesto].",
    "Vincular el analisis con un problema juridico o social concreto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 4 [pendiente de consigna].",
    "Registrar incidencias tecnicas locales: tokens sin expandir y entradas BibTeX truncadas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anomalos antes de referenciar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Depurar duplicados de entradas equivalentes y definir clave canonica por obra [supuesto].",
    "Corregir entrada BibTeX truncada detectada en sierraUniversidadNacional1910."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones.",
    "No transferir conclusiones especificas ni bibliografia exclusiva de la asignatura origen.",
    "Aplicar compresion lossless por union y deduplicacion, sin recorte de reglas utiles.",
    "Si falta consigna local, mantener plantilla base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar rubrica de evaluacion especifica para ajustar profundidad argumentativa.",
    "Confirmar si el entregable principal es reporte, presentacion u otro formato.",
    "Confirmar politica local de clave canonica y alias en etica-y-moral-juridica.bib.",
    "Confirmar correccion final de la entrada BibTeX truncada en el archivo local."
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
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral Juridica.",
        "Nodo de trabajo: Actividad 4."
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
      "Transformar la planeacion semanal en productos academicos con fundamento, evidencia y cierre argumentativo.",
      "Garantizar coherencia entre identidad institucional, estructura argumentativa y calidad verificable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y no ornamentales.",
      "Citas verificables en afirmaciones fuertes.",
      "Conclusion juridica con implicacion practica.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Delimitar problema -> definir conceptos -> aplicar marco normativo/doctrinal -> argumentar postura -> concluir.",
      "Contrastar etica, moral y norma juridica cuando sea pertinente.",
      "Evitar resumen pasivo y priorizar inferencia justificada."
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
        "Evidencia verificable",
        "Normalizacion JSON"
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
          "justification": "El marco institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion previa del problema."
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
          "justification": "Son categorias relacionadas pero no equivalentes en uso juridico."
        },
        {
          "source": "Moral",
          "target": "Norma juridica",
          "kind": "contrasts",
          "justification": "La juridicidad no se agota en valoraciones morales."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Solo se propaga memoria estructurada y parseable."
        }
      ],
      "evidence": [
        "README de la asignatura confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico confirma proposito y ejes de trabajo de cinco pasos.",
        "Archivo .bib local evidencia duplicados y una entrada truncada a corregir."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se conserva nucleo institucional y estructura comun transferible.",
      "Ciclo 15: se refuerza control de calidad por parseo JSON obligatorio.",
      "Ciclo 15: se mantiene lateralidad estricta sin copiar conclusiones ni bibliografia exclusiva del nodo origen.",
      "Ciclo 15: se agregan mejoras verificables locales en README/programa/.bib sin inventar fuentes."
    ]
  }
}