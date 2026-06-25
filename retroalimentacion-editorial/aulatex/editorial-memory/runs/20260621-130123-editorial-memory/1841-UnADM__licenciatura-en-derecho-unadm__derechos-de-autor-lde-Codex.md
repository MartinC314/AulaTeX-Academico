{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derechos de autor con identidad UnADM.",
    "Se preservan reglas utiles previas y se deduplican sin perdida semantica.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se transfieren solo abstracciones estables desde Filosofia del Derecho por relacion transversal.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estado provisional para herencias no verificadas localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Mantener enfoque juridico con criterio propio en la conclusion.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf para soporte de ubicacion curricular.",
    "Supuesto: la clave LDE-S5B1 se mantiene como identificador local vigente."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar separacion entre reporte, presentacion y bibliografia de la materia.",
    "Corregir tokens de plantilla no resueltos en README y programa analitico.",
    "Normalizar nombres de archivo con slug de la asignatura."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al archivo BibTeX local.",
    "No asumir fuentes de otras semanas sin validacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Detectar y corregir marcadores pendientes como 'Nombre por definir'.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Declarar metadatos del documento antes de \\input{template}.",
    "No dejar comandos incompletos como \\usepackage sin argumento.",
    "Mover paquetes cargados fuera de lugar al preambulo efectivo segun plantilla.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener claves BibTeX estables para evitar quiebres de compilacion.",
    "Corregir caracteres anomales en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas pertinentes.",
    "Registrar fuentes especificas de cada actividad en derechos-de-autor.bib.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir lateralmente solo reglas generales estables, no redaccion literal.",
    "Evitar regresiones frente a reglas utiles ya consolidadas.",
    "Mantener bandera de normalizacion manual para herencia historica no estructurada.",
    "No propagar datos personales del alumno a otros nodos.",
    "Propagar advertencias sobre Codex y GPT-Pro solo como estado provisional."
  ],
  "open_questions": [
    "Confirmar reemplazo definitivo de tokens Slug en README y programa analitico.",
    "Confirmar nombre de figura docente para eliminar marcador pendiente.",
    "Validar orden final de paquetes LaTeX respecto de \\input{template} en esta plantilla.",
    "Confirmar si LDE-S5B1 es clave oficial transversal o solo local.",
    "Supuesto: la ubicacion institucional en portada puede variar por actividad; confirmar criterio."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Normalizacion estructurada previa a propagacion.",
        "Herencia no verificada tratada como provisional."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura destino: Derechos de autor.",
        "Supuesto: clave local LDE-S5B1."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con trazabilidad.",
      "Analisis propio del estudiante.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos consistentes y verificables.",
      "Sostener un cerebro editorial persistente sin perdida de reglas utiles.",
      "Sincronizar transversalmente materias con abstracciones comunes y control de calidad."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Usar secciones funcionales y trazables.",
      "Mantener consistencia entre portada, desarrollo y referencias.",
      "Evitar literalidad heredada entre nodos no equivalentes."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica",
        "Propagacion segura transversal"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura transversal",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables y reduce ruido editorial."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Toda afirmacion requiere respaldo trazable en .bib."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita cierre aplicable a practica profesional."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion segura transversal",
          "kind": "depends_on",
          "justification": "La coherencia institucional define que reglas son reutilizables entre materias."
        }
      ],
      "evidence": [
        "README de Derechos de autor define identidad y ubicacion curricular.",
        "Programa analitico fija ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene fuentes institucionales base.",
        "Regla consolidada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: deduplicacion lossless aplicada sobre reglas de identidad, estructura y calidad.",
      "Ciclo 21: se refuerza transferencia transversal por abstracciones estables, sin copiar contenido literal.",
      "Ciclo 21: se mantienen advertencias de herencia provisional (Codex/GPT-Pro) hasta validacion local.",
      "Ciclo 21: se refuerza control de tokens de plantilla y comandos LaTeX incompletos."
    ]
  }
}