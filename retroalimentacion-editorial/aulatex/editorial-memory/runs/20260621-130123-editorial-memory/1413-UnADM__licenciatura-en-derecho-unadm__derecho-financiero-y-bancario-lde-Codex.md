{
  "summary": [
    "Sincronizacion transversal ciclo 2 aplicada con union-dedupe sin regresion.",
    "Se preservan reglas institucionales UnADM y ejes editoriales transferibles.",
    "Se consolidan abstracciones estables: identidad, estructura reusable, calidad, LaTeX y bibliografia.",
    "Se mantiene bloqueo de propagacion ante salida no JSON parseable.",
    "Se refuerza trazabilidad a README, programa analitico, .tex y .bib del destino.",
    "Se conserva contexto curricular local: semestre 3, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar Licenciatura en Derecho como programa academico del destino.",
    "Mantener datos curriculares verificados: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar fuentes heredadas de motor como provisionales hasta verificacion local.",
    "Conservar autoria y matricula solo si coinciden con el .tex local vigente."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre README, programa analitico, .tex y .bib.",
    "Corregir artefactos de plantilla en nombres de archivos antes de publicar memoria."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas.",
    "Incluir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de semanas distintas sin confirmacion.",
    "Adaptar profundidad argumentativa a rubrica cuando exista.",
    "Declarar supuestos cuando falte consigna textual de actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de cada regla a memoria heredada o contexto local.",
    "Validar deduplicacion semantica antes de guardar.",
    "Bloquear si hay campos obligatorios vacios sin marca de supuesto.",
    "No agregar reglas sin respaldo verificable."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener documentclass y opciones locales salvo instruccion contraria.",
    "Reemplazar titulo y subtitulo de plantilla por actividad real antes de entrega.",
    "Completar Figura docente con dato real o marca explicita de supuesto.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar derecho-financiero-y-bancario.bib como archivo canonico local.",
    "Mantener entradas institucionales base ya verificadas.",
    "Agregar solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Incluir fecha de consulta en recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a nodos no equivalentes solo abstracciones estables.",
    "Evitar redaccion literal; compartir patrones editoriales reutilizables.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar contingencia de normalizacion manual si reaparece salida no estructurada.",
    "Etiquetar supuestos para auditoria transversal."
  ],
  "open_questions": [
    "Confirmar figura docente real para portada.",
    "Confirmar formato obligatorio de citacion en la materia. [Supuesto: no definido]",
    "Confirmar si el grupo debe incluirse en tabla de identificacion.",
    "Confirmar planeacion semanal vigente antes de generar actividades.",
    "Confirmar si la localizacion institucional de portada sigue vigente.",
    "Confirmar correccion final de nombres de archivo con artefactos de plantilla."
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
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho financiero y bancario.",
        "Semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema delimitado.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis juridico propio.",
      "Conclusion transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y verificables.",
      "Sostener continuidad editorial UnADM entre actividades y materia."
    ],
    "style_markers": [
      "Frases directas y auditables.",
      "Supuestos marcados en forma explicita.",
      "Coherencia entre narrativa, citas y estructura.",
      "Sin inventar fuentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo delimitado.",
      "Analisis propio sustentado en evidencia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis juridico propio",
        "Conclusion transferible",
        "Consistencia .tex-.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion profesional requiere respaldo comprobable."
        },
        {
          "source": "Problema juridico delimitado",
          "target": "Analisis juridico propio",
          "kind": "develops",
          "justification": "El problema define el eje argumentativo."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor."
        }
      ],
      "evidence": [
        "README de materia con pauta editorial y ubicacion curricular.",
        "Programa analitico con proposito y ejes de trabajo.",
        "Archivo .bib local con fuentes institucionales base.",
        "Plantilla .tex local con campos pendientes identificados."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas por union semantica.",
      "Se preservaron reglas heredadas utiles sin recorte funcional.",
      "Se transfirieron solo abstracciones estables desde nodo transversal.",
      "Se mantuvieron vacios locales como preguntas abiertas con supuesto.",
      "Se reforzo gate de JSON parseable como condicion de propagacion."
    ]
  }
}