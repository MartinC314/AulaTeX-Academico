{
  "summary": [
    "Se consolida memoria lateral para Actividad 4 con deduplicacion lossless.",
    "Se preservan reglas institucionales UnADM y ejes editoriales comunes de la asignatura.",
    "Se refuerza validacion JSON estricta por antecedentes de salida no parseable.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografia exclusiva de Actividad 1.",
    "Supuesto: la consigna local de Actividad 4 no esta visible completa y requiere confirmacion."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar referencia curricular: semestre 1, bloque 2, obligatoria, 8 creditos."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio en toda entrega.",
    "Sustentar afirmaciones con cita explicita y fuente verificable.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Adaptar Actividad 4 a los ejes del programa analitico.",
    "Supuesto: confirmar producto exacto, extension y rubrica de Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Verificar correspondencia del producto con la consigna vigente de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de compilar.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por slug del README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 4 sin confirmacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Preservar reglas utiles previas y evitar regresiones.",
    "Aplicar union-dedupe en laterales; no copiar contenido especifico entre hermanos.",
    "Cuando falte consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener bandera de normalizacion manual para ciclos con historial no estructurado."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar tipo de producto final: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion y criterios de profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar nombre canonico final del archivo .bib por token slug no resuelto.",
    "Confirmar si bibliografia de interpretacion juridica (Semana 7) aplica o no a Actividad 4."
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
        "Entrada canonica en carpeta de asignatura.",
        "Normalizacion obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos verificables.",
      "Garantizar claridad, fundamento juridico, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Objetivo explicito antes del desarrollo.",
      "Secciones funcionales con logica juridica.",
      "Cita explicita para cada afirmacion clave.",
      "Marcado de supuestos cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Fijar postura justificada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Integridad academica y verificabilidad",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Relacion problema-evidencia-conclusion juridica"
      ],
      "citations": [
        "README.md de asignatura",
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
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Estructura de actividad",
          "kind": "develops",
          "justification": "Los ejes ordenan problema, fuentes, analisis y cierre."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion valida requiere evidencia trazable."
        }
      ],
      "evidence": [
        "README define identidad UnADM, trazabilidad y conclusion juridica con criterio propio.",
        "Programa analitico define cinco ejes reutilizables.",
        "Historial de salidas no parseables justifica gate de JSON estricto.",
        "Token slug sin resolver en README justifica validacion de nombres de archivo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 79: union-dedupe de reglas repetidas con conservacion total de patrones utiles.",
      "Ciclo 79: refuerzo lateral desde hermano sin copiar redaccion ni conclusiones especificas.",
      "Ciclo 79: se mantiene distincion entre reglas generales y datos sujetos a supuesto.",
      "Ciclo 79: se preserva prioridad de normalizacion estructurada previa a propagacion."
    ]
  }
}