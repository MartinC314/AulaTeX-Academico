{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y sin regresión.",
    "Se preservan reglas institucionales UnADM, normalización JSON y estructura argumentativa reusable.",
    "Se transfieren solo abstracciones estables desde actividad de Filosofía del Derecho a materia de Responsabilidad Civil y Daños.",
    "Se mantiene separación entre reglas editoriales generales y contenido temático específico de cada materia.",
    "Se refuerzan incidencias locales verificadas: rutas truncadas, placeholders sin resolver y plantilla .tex incompleta [supuesto técnico]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar la carpeta de materia como entrada canónica.",
    "Marcar como supuesto todo dato no confirmado por consigna o guía oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta confirmación local.",
    "Conservar contexto curricular local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 créditos.",
    "No declarar oficial el código de curso sin fuente documental explícita [supuesto: LDE-S6B1].",
    "No alterar la convención local danos/daños sin validación documental."
  ],
  "structure_rules": [
    "Iniciar cada entrega con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto con la planeación semanal y la consigna vigente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener separación editorial entre reporte, presentación, programa analítico y bibliografía .bib."
  ],
  "activity_rules": [
    "Formular problema jurídico pertinente a responsabilidad civil y daño.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Separar fundamento jurídico, evidencia y análisis propio.",
    "No trasladar contenido temático literal desde materias no equivalentes.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que toda afirmación jurídica tenga fuente o marca de análisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar control de no regresión sobre reglas útiles previas.",
    "Detectar y corregir placeholders y rutas truncadas antes de consolidar memoria."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres truncados de archivos antes de referenciarlos.",
    "Completar plantilla .tex truncada antes de uso productivo [supuesto técnico: bloque authortable incompleto]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar vacíos de referencia como preguntas abiertas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y transversales.",
    "Evitar propagar contenido temático puntual de una actividad a toda la materia.",
    "Reutilizar gates institucionales de calidad sin perder contexto local.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Mantener alerta histórica de normalización manual por salidas no estructuradas en ciclos previos."
  ],
  "open_questions": [
    "Confirmar convención final de nombres con danos/daños en todo el árbol.",
    "Confirmar oficialidad documental del código de curso LDE-S6B1.",
    "Corregir en README y programa analítico los placeholders de .bib.",
    "Corregir en README los nombres truncados de reporte y referencias.",
    "Completar y validar la sección authortable de la plantilla .tex.",
    "Confirmar si existe guía oficial de formato por actividad para esta materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no verificados."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Entrada canónica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos.",
        "Asignatura: Derecho de la responsabilidad civil y daños [convención local pendiente].",
        "Fuente curricular: UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf."
      ]
    },
    "essence": [
      "Problema jurídico.",
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Disciplina editorial con verificación técnica y documental."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos verificables.",
      "Garantizar consistencia institucional, argumentativa y técnica en cada entrega.",
      "Sostener una memoria editorial reusable sin arrastre temático indebido."
    ],
    "style_markers": [
      "Declarar supuestos de forma explícita.",
      "Priorizar estructura funcional y trazable.",
      "Cierre con utilidad profesional jurídica.",
      "Evitar redacción literal heredada entre nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo con evidencia.",
      "Análisis propio con criterio jurídico.",
      "Conclusión aplicada a práctica profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Responsabilidad civil",
        "Daño",
        "Integridad académica",
        "Trazabilidad editorial"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "La estructura parseable evita ambigüedad en propagación recursiva."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta jurídica delimitada."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de fundamento normativo verificable."
        },
        {
          "source": "Responsabilidad civil",
          "target": "Daño",
          "kind": "depends_on",
          "justification": "La materia estructura sus productos sobre la relación entre daño y responsabilidad."
        },
        {
          "source": "Estructura argumentativa reusable",
          "target": "Sincronización transversal",
          "kind": "develops",
          "justification": "Permite transferir método sin trasladar contenido temático literal."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analítico local.",
        "Archivo .bib local con entradas institucionales.",
        "Plantilla .tex local con truncamiento detectable [supuesto técnico verificable por inspección].",
        "Memoria origen con reglas estables de calidad y estructura."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicación completa de reglas repetidas sin pérdida semántica.",
      "Ciclo 20: se refuerza gate de JSON parseable como condición de propagación.",
      "Ciclo 20: se consolida patrón transversal problema-conceptos-evidencia-análisis-conclusión.",
      "Ciclo 20: se mantiene alerta de placeholders/rutas truncadas como control técnico general.",
      "Ciclo 20: se conserva política de supuestos explícitos para datos no confirmados."
    ]
  }
}