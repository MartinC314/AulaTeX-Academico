{
  "summary": [
    "Se consolida cerebro editorial de materia para Derechos de autor con identidad UnADM.",
    "Se preserva compresión por unión y deduplicación sin regresión.",
    "Se transfieren solo abstracciones estables desde Filosofía del Derecho.",
    "Se mantiene herencia Codex y GPT-Pro como provisional hasta validación local.",
    "Se refuerzan ejes editoriales: problema, conceptos, fuentes, análisis propio y cierre jurídico.",
    "Se conserva README como entrada canónica de la asignatura.",
    "Se fija derechos-de-autor.bib como bibliografía local verificable.",
    "Se detectan marcadores de plantilla y nombres corruptos que requieren corrección antes de publicar."
  ],
  "identity_rules": [
    "Usar identidad institucional UnADM en portada, tono y metadatos.",
    "Alinear entregables con Licenciatura en Derecho.",
    "Usar datos curriculares locales: semestre 5, bloque 1, obligatoria, 8 créditos.",
    "Mantener enfoque jurídico con criterio propio en la conclusión.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Supuesto: la materia conserva nomenclatura local LDE-S5B1 en documentos.",
    "Citar la malla curricular local solo cuando se use para ubicación curricular.",
    "No propagar datos personales del alumno a otras materias."
  ],
  "structure_rules": [
    "Conservar README como índice operativo de la asignatura.",
    "Usar programa analítico como marco editorial.",
    "Organizar productos por problema, conceptos, marco normativo o doctrinal, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear cada entrega al producto solicitado por la planeación semanal.",
    "Mantener separación entre reporte, presentación y referencias.",
    "Guardar bibliografía específica en derechos-de-autor.bib.",
    "Normalizar nombres de archivo con slug derechos-de-autor.",
    "Corregir marcadores literales de plantilla en README y programa analítico.",
    "Corregir nombres corruptos como eporte y eferencias antes de publicar."
  ],
  "activity_rules": [
    "Iniciar cada actividad con problema jurídico o social delimitado.",
    "Vincular conceptos con normas, doctrina o datos verificables.",
    "Cumplir el formato solicitado por la planeación semanal.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión aplicable a la práctica jurídica.",
    "Agregar fuentes específicas por actividad al archivo BibTeX local.",
    "No asumir que fuentes de otra materia correspondan a Derechos de autor."
  ],
  "quality_gates": [
    "Rechazar salidas no JSON parseable antes de propagar memoria.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Verificar consistencia entre portada y datos curriculares locales.",
    "Exigir correspondencia entre citas en texto y .bib local.",
    "Confirmar que toda afirmación tenga respaldo o marca de supuesto.",
    "Detectar y corregir campos pendientes como Nombre por definir.",
    "Auditar README por caracteres extraños y marcadores de plantilla.",
    "Validar que el producto corresponda a la consigna de la actividad.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Bloquear publicación si hay referencias rotas o compilación crítica."
  ],
  "latex_rules": [
    "Mantener documentclass article en español y letterpaper salvo instrucción contraria.",
    "Declarar metadatos con macros antes de \\input{template}.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template}.",
    "Nunca dejar \\usepackage sin argumento.",
    "Evitar paquetes truncados o líneas incompletas en preámbulo.",
    "Mover paquetes cargados después de \\input{template} al preámbulo efectivo si la plantilla lo exige.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener tipografía sans serif si la plantilla local la requiere.",
    "Conservar tabla de autor solo en documentos locales autorizados.",
    "No propagar datos personales ni matrícula fuera del nodo local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de compilar.",
    "Compilar sin errores críticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo materiales institucionales o verificables.",
    "Registrar fuentes base UnADM incluidas en derechos-de-autor.bib.",
    "Conservar entrada local unadmSitioWeb si se cita.",
    "Conservar entrada local unadmMallaDerecho2024 si se cita.",
    "Agregar entradas BibTeX completas por actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No importar bibliografía de Filosofía del Derecho sin pertinencia local verificable.",
    "Asegurar que toda cita en texto tenga entrada en .bib y viceversa."
  ],
  "propagation_hints": [
    "Propagar hacia arriba reglas institucionales validadas en esta materia.",
    "Propagar lateralmente a materias LDE solo reglas genéricas de calidad y estructura.",
    "Compartir solo abstracciones editoriales entre nodos no equivalentes.",
    "No propagar datos personales del alumno.",
    "No propagar marcadores pendientes ni nombres corruptos de archivo.",
    "Propagar advertencia sobre herencia Codex y GPT-Pro solo como provisional.",
    "Mantener auditoría manual para contenido heredado si se reutiliza.",
    "Validar JSON y estructura antes de propagación recursiva.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Crear cerebro editorial mínimo cuando falte consigna local."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial en toda la suite.",
    "Definir nombre de figura docente.",
    "Validar si Roma Norte, Ciudad de México debe mantenerse fija.",
    "Confirmar sustitución definitiva de marcadores literales por derechos-de-autor.bib.",
    "Revisar y corregir errores de nombres de archivo en README.",
    "Validar orden correcto entre paquetes LaTeX y \\input{template} en esta plantilla.",
    "Confirmar fuentes obligatorias específicas de cada semana.",
    "Confirmar rúbricas locales de evaluación.",
    "Confirmar productos esperados por actividad: reporte, presentación u otro formato.",
    "Confirmar si la herencia Codex desde ingeniería sigue vigente o debe archivarse."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Herencia no verificada tratada como provisional.",
        "Normalización estructurada antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derechos de autor.",
        "Semestre 5, bloque 1.",
        "Tipo obligatoria.",
        "8 créditos.",
        "Supuesto: clave local LDE-S5B1."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible.",
      "Integridad bibliográfica local.",
      "Transferencia profesional."
    ],
    "reason_for_being": [
      "Orientar productos académicos de Derechos de autor con claridad jurídica.",
      "Transformar la planeación semanal en entregables verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico aplicable a la práctica profesional.",
      "Conservar trazabilidad entre README, programa analítico, .tex y .bib."
    ],
    "style_markers": [
      "Declarar supuestos de forma explícita.",
      "Usar secciones funcionales y trazables.",
      "Evitar redacción meramente descriptiva.",
      "Mantener consistencia entre portada, contenido y referencias.",
      "Separar marco conceptual de análisis propio.",
      "Cerrar con implicación práctica jurídica.",
      "Corregir plantillas antes de publicar."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo.",
      "Evidencia verificable.",
      "Análisis con postura propia.",
      "Contraste entre fuente y criterio del estudiante.",
      "Conclusión aplicable a la práctica jurídica.",
      "Validación final contra consigna y rúbrica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derechos de autor.",
        "Identidad institucional UnADM.",
        "Licenciatura en Derecho.",
        "Ubicación curricular local.",
        "Normalización estructurada.",
        "Propagación segura.",
        "Problema jurídico o social.",
        "Marco conceptual y normativo.",
        "Evidencia verificable.",
        "Análisis propio.",
        "Conclusión jurídica transferible.",
        "Integridad bibliográfica.",
        "Bibliografía base UnADM.",
        "Bibliografía específica por actividad.",
        "Plantilla LaTeX local.",
        "Marcadores de plantilla pendientes."
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Licenciatura en Derecho",
          "kind": "supports",
          "justification": "La materia pertenece a la ruta local de Derecho en UnADM."
        },
        {
          "source": "Ubicación curricular local",
          "target": "Metadatos de portada",
          "kind": "depends_on",
          "justification": "Semestre, bloque, tipo y créditos deben coincidir con README y malla."
        },
        {
          "source": "README",
          "target": "Punto de entrada canónico",
          "kind": "supports",
          "justification": "El contexto local define la carpeta como entrada canónica de la asignatura."
        },
        {
          "source": "Programa analítico",
          "target": "Ejes editoriales",
          "kind": "develops",
          "justification": "El programa organiza problema, conceptos, producto, análisis y cierre."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Toda afirmación requiere fuente o marca de supuesto."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La postura argumentada permite cierre profesional útil."
        },
        {
          "source": "Bibliografía específica por actividad",
          "target": "derechos-de-autor.bib",
          "kind": "depends_on",
          "justification": "El programa local ordena agregar fuentes específicas al .bib de la asignatura."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables o reglas ambiguas."
        },
        {
          "source": "Marcadores de plantilla pendientes",
          "target": "Publicación final",
          "kind": "contrasts",
          "justification": "Tokens sin resolver y nombres corruptos impiden una entrega limpia."
        },
        {
          "source": "Plantilla LaTeX local",
          "target": "Compilación estable",
          "kind": "depends_on",
          "justification": "El preámbulo debe evitar paquetes truncados y comandos incompletos."
        }
      ],
      "evidence": [
        "README de Derechos de autor define materia, ubicación curricular y pauta editorial.",
        "README local cita UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf como fuente curricular.",
        "Programa analítico local fija propósito de realización y ejes de trabajo.",
        "derechos-de-autor.bib contiene unadmSitioWeb y unadmMallaDerecho2024.",
        "reporte-derechos-de-autor.tex declara metadatos locales de curso y portada.",
        "Contexto local muestra marcador $(@{...}.Slug) pendiente en README y programa analítico.",
        "Contexto local muestra nombres corruptos eporte y eferencias en README.",
        "Contexto local muestra \\usepackage sin argumento al final del preámbulo.",
        "Memoria heredada indica salida no JSON parseable desde Codex para UnADM.",
        "Memoria actual indica herencia Codex y GPT-Pro provisional hasta validación local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8 aplica sincronización transversal conservadora.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se preservan reglas locales de Derechos de autor sobre currículo, README y .bib.",
      "Se incorporan abstracciones estables desde Filosofía del Derecho.",
      "Se excluyen conceptos doctrinales específicos de Filosofía del Derecho por no ser equivalentes.",
      "Se refuerza bloqueo de propagación para salidas no JSON parseable.",
      "Se convierte relación transversal en patrones editoriales reutilizables.",
      "Se mantiene abierta la validación de fuentes, rúbricas y productos locales."
    ]
  }
}