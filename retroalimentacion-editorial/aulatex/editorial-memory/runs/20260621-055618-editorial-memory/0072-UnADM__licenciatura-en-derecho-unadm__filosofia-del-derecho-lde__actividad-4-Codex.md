{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM y marco curricular verificable de Filosofia del Derecho.",
    "Se mantiene normalizacion estructurada y validacion JSON estricta como puerta de propagacion.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Supuesto: la consigna textual de Actividad 4 no esta completa; mantener plantilla base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica alineados a UnADM.",
    "Vincular siempre la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear forma final al producto exigido por la planeacion semanal."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 4.",
    "Transferir solo patrones reutilizables de estructura y calidad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o etiqueta de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia exacta entre producto y consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol consistentes en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX ya usadas en documentos activos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de referenciar archivos.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Agregar al .bib de asignatura solo fuentes realmente usadas en Actividad 4.",
    "Supuesto: filosofia-del-derecho-clean.bib pertenece a Semana 7; validar si aplica o no a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Conservar reglas utiles previas sin regresion.",
    "Aplicar union y deduplicacion lossless en cada ciclo.",
    "Propagar lateralmente patrones institucionales, no redacciones literales.",
    "Mantener bandera de normalizacion manual para ciclos con antecedentes no estructurados."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica especifica de evaluacion para nivel de profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del archivo .bib tras resolver plantilla Slug."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro",
        "Juridicamente preciso",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica en carpeta de asignatura",
        "Normalizacion obligatoria antes de propagar"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Filosofia del Derecho",
        "Semestre 1, bloque 2",
        "Asignatura obligatoria de 8 creditos"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y marco normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y salida tecnica."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones funcionales claras",
      "Postura personal justificada",
      "Supuestos etiquetados cuando falten datos",
      "Cierre con aplicabilidad profesional"
    ],
    "argumentative_patterns": [
      "Plantear problema",
      "Exponer conceptos y normas",
      "Contrastar evidencia",
      "Desarrollar postura propia",
      "Concluir juridicamente"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad"
      ],
      "citations": [
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales de Filosofia del Derecho",
          "kind": "supports",
          "justification": "Define tono, alcance y criterio academico comun entre actividades hermanas."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere salida estructurada y parseable."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Integridad academica y verificabilidad",
          "kind": "develops",
          "justification": "Los ejes exigen evidencia, analisis propio y conclusion sustentada."
        }
      ],
      "evidence": [
        "Pauta editorial del README",
        "Proposito y ejes del programa analitico",
        "Antecedentes de salidas no parseables en ciclos previos"
      ]
    },
    "reinforcement_log": [
      "Ciclo 72: deduplicacion de reglas repetidas en tono, estructura y calidad.",
      "Ciclo 72: conservada regla de bloqueo por JSON no parseable.",
      "Ciclo 72: reforzada separacion entre patrones reutilizables y contenido especifico de actividad.",
      "Ciclo 72: mantenidos supuestos abiertos por falta de consigna local completa."
    ]
  }
}