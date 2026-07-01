{
  "summary": [
    "Se consolida sincronizacion transversal entre actividad de origen y materia destino con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, normalizacion estructurada y no regresion.",
    "Se refuerza patron reusable: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene filtro transversal: transferir abstracciones estables y excluir contenido tematico especifico de Filosofia del Derecho.",
    "Se conservan incidencias tecnicas locales como controles activos: JSON no parseable previo, rutas truncadas y placeholders sin resolver."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto local confirmado: Licenciatura en Derecho, semestre 6, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no confirmado por consigna o fuente oficial.",
    "Tratar memorias heredadas no verificadas como provisionales hasta validacion local.",
    "No cambiar la convencion local danos/daños sin confirmacion documental."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Mantener separacion explicita entre reporte, presentacion, programa analitico y .bib.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Formular problema juridico vinculado a responsabilidad civil y danos.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Exigir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Separar fundamento juridico, evidencia y analisis propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar contenido tematico de origen si no aplica a responsabilidad civil y danos."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "Aplicar control de no regresion sobre reglas utiles previas.",
    "Confirmar que toda afirmacion juridica tenga fuente o marca de supuesto/analisis propio.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir rutas truncadas y placeholders sin resolver antes de propagar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Completar plantilla local truncada antes de compilar [supuesto].",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y material juridico verificable.",
    "Registrar fuentes especificas por actividad en el .bib local de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Mantener como base confirmada: unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar propagar redaccion literal o contenido tematico puntual del origen.",
    "Mantener alerta de normalizacion manual por antecedentes de salidas no estructuradas.",
    "Conservar compresion lossless por union-dedupe sin recorte semantico."
  ],
  "open_questions": [
    "Confirmar guia oficial de formato por actividad para esta materia.",
    "Confirmar convencion final de nombres con danos versus daños en todo el arbol.",
    "Confirmar si el codigo de curso LDE-S6B1 es oficial [supuesto actual: no confirmado].",
    "Corregir en README nombres truncados de reporte y referencias.",
    "Validar y completar seccion authortable truncada en la plantilla .tex.",
    "Confirmar si cada actividad requiere .bib propio o solo crecimiento del .bib de materia."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho de la responsabilidad civil y danos.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Fundamento normativo y doctrinal verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible.",
      "Trazabilidad tecnica y bibliografica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar coherencia entre identidad institucional, argumentacion juridica y evidencia.",
      "Permitir propagacion segura entre nodos mediante reglas estables."
    ],
    "style_markers": [
      "Frases directas y secciones explicitas.",
      "Supuestos marcados de forma visible.",
      "Citas trazables al .bib local.",
      "Cierre con aplicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Plantear problema y objetivo.",
      "Desarrollar marco conceptual-normativo.",
      "Evaluar con analisis propio y evidencia.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Fundamento normativo/doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Responsabilidad civil y danos",
        "Integridad de citacion"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Normalizacion estructurada",
          "kind": "supports",
          "justification": "La coherencia institucional depende de formato y validacion consistentes."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin pregunta delimitada no hay evaluacion juridica consistente."
        },
        {
          "source": "Fundamento normativo/doctrinal",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion requiere soporte verificable para ser util en practica."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Solo se propaga memoria valida y parseable."
        },
        {
          "source": "Reglas de Filosofia del Derecho",
          "target": "Responsabilidad civil y danos",
          "kind": "develops",
          "justification": "Se heredan patrones editoriales generales, no contenidos tematicos."
        }
      ],
      "evidence": [
        "README local de materia: ubicacion curricular y pauta editorial.",
        "Programa analitico local: proposito y ejes de trabajo.",
        "Bib local: unadmSitioWeb y unadmMallaDerecho2024.",
        "Memoria origen: patron argumentativo y gate de JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 2: se preservan reglas tecnicas criticas de parseo, truncamientos y placeholders.",
      "Ciclo 2: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 2: se mantienen fuentes heredadas no verificadas bajo estatus provisional."
    ]
  }
}