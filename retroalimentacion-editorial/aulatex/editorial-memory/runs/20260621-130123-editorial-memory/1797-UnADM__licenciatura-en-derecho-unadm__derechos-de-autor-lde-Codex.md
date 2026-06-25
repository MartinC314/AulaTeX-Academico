{
  "summary": [
    "Consolidar cerebro editorial minimo y estable para Derechos de autor con identidad UnADM.",
    "Mantener compresion lossless por union y deduplicacion, sin recorte de reglas utiles.",
    "Reforzar normalizacion estructurada obligatoria antes de toda propagacion.",
    "Transferir solo abstracciones transversales estables desde Filosofia del Derecho.",
    "Marcar como provisionales las herencias no verificadas (Codex, GPT-Pro) hasta validacion local.",
    "Corregir en destino tokens de plantilla y nombres corruptos detectados en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Mantener enfoque juridico con criterio propio en conclusion.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar malla-curricular-derecho-unadm.pdf como soporte curricular cuando aplique."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por planeacion semanal.",
    "Mantener separacion entre reporte, presentacion y bibliografia local.",
    "Normalizar nombres de archivo con slug canonico derechos-de-autor."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Verificar que el producto corresponda a la consigna de la actividad vigente.",
    "No asumir automaticamente fuentes de otras semanas o materias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Detectar y corregir marcadores pendientes de plantilla.",
    "Auditar README y programa analitico por tokens sin expandir y caracteres anomales."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol y letterpaper salvo instruccion contraria.",
    "Declarar metadatos antes de input de plantilla, segun convencion local.",
    "No dejar comandos incompletos como usepackage sin argumento.",
    "Mantener codificacion y acentos correctos en espanol en tex y bib.",
    "Compilar sin errores criticos, sin referencias rotas y sin rutas corruptas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y marco juridico aplicable.",
    "Registrar fuentes especificas por actividad en derechos-de-autor.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Compartir lateralmente solo reglas generales de identidad, estructura y calidad.",
    "Evitar transferir redaccion literal o contenido tematico especifico de Filosofia del Derecho.",
    "Preservar reglas utiles previas sin regresion.",
    "Mantener bandera de normalizacion manual para contenido heredado de ciclos iniciales."
  ],
  "open_questions": [
    "Confirmar si LDE-S5B1 es clave oficial de uso transversal. [supuesto]",
    "Definir nombre de figura docente en plantilla de reporte.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe permanecer como ubicacion fija. [supuesto]",
    "Confirmar sustitucion definitiva de tokens Slug por derechos-de-autor.bib en todos los archivos.",
    "Confirmar si la herencia Codex y GPT-Pro puede degradarse de provisional a validada."
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
        "Entrada canonica por carpeta de asignatura.",
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Sostener calidad institucional consistente entre actividades y formatos.",
      "Permitir propagacion transversal segura por reglas, no por texto literal."
    ],
    "style_markers": [
      "Supuestos declarados de forma explicita.",
      "Secciones funcionales y trazables.",
      "Consistencia entre portada, contenido y referencias.",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Objetivo puntual.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Conclusion aplicable a practica juridica."
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
          "justification": "Evita heredar salidas no parseables y reduce regresiones."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad bibliografica",
          "kind": "supports",
          "justification": "Toda afirmacion debe mapear a cita trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita cierre profesional util."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Propagacion segura transversal",
          "kind": "supports",
          "justification": "Estabiliza tono, formato y criterios comunes entre nodos."
        }
      ],
      "evidence": [
        "README de Derechos de autor con ubicacion curricular y pauta editorial.",
        "Programa analitico con ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib con base institucional local.",
        "Deteccion local de tokens sin expandir y nombres corruptos en estructura."
      ]
    },
    "reinforcement_log": [
      "Se reforzo gate de JSON parseable como bloqueo duro.",
      "Se preservo regla historica de normalizacion manual para herencia no estructurada.",
      "Se consolido patron argumentativo comun transferible entre materias LDE.",
      "Se mantuvo herencia provisional Codex/GPT-Pro sin promoverla a validada.",
      "Se agrego control explicito de tokens de plantilla sin expandir en archivos fuente."
    ]
  }
}