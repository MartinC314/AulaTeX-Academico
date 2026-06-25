{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia Electiva S8 B1 con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, estructura reusable y controles de calidad sin recorte.",
    "Se deduplican reglas equivalentes por union semantica lossless.",
    "Se evita transferir contenido tematico especifico de Actividad 1 por no equivalencia de nodos.",
    "Se refuerza normalizacion de placeholders y nombres corruptos detectados en README y programa del destino.",
    "Supuesto: el destino sigue sin consigna local de actividades concretas para reglas tematicas finas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Marcar como supuesto todo dato no visible o no confirmado.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Mantener carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Diferenciar con claridad resumen de fuentes y postura propia.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener estructura reusable para reporte y presentacion."
  ],
  "activity_rules": [
    "Vincular cada producto con un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar contenidos de otras materias o semanas sin evidencia local.",
    "Adaptar profundidad argumentativa a la consigna y rubrica local cuando exista.",
    "Marcar supuestos de forma explicita en texto y metadatos."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y literales corruptos antes de entrega.",
    "Confirmar existencia de rutas y archivos citados como fuente.",
    "Evitar regresiones: no eliminar reglas utiles previas."
  ],
  "latex_rules": [
    "Mantener plantilla base LaTeX de la materia.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Completar campos pendientes de portada antes de entrega.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y artefactos.",
    "Corregir nombres de archivo corruptos en README.",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico mientras no exista reemplazo oficial.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones editoriales estables.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni metadatos hiperlocales a nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Registrar antecedentes de salida no estructurada para control preventivo.",
    "Si falta contexto local, mantener cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la electiva y codigo de curso definitivo.",
    "Confirmar figura docente para plantilla.",
    "Confirmar si todas las actividades requieren reporte, presentacion o ambos.",
    "Confirmar correccion final de nombres corruptos en README (reporte/referencias).",
    "Supuesto: no hay rubrica local cargada; confirmar criterios de evaluacion formales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Argumentativo con criterio propio",
        "Conservador ante datos no confirmados"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica por carpeta de materia",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8",
        "Bloque 1",
        "Tipo Electiva"
      ]
    },
    "essence": [
      "Problema",
      "Conceptos y fuentes",
      "Analisis propio",
      "Cierre juridico transferible",
      "Trazabilidad verificable"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes y evaluables.",
      "Asegurar calidad editorial estable en reportes y presentaciones.",
      "Permitir propagacion segura entre nodos mediante reglas normalizadas."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Afirmacion con evidencia",
      "Postura propia sustentada",
      "Conclusion aplicable a practica juridica"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia -> inferencia juridica",
      "Descripcion breve -> postura critica -> implicacion practica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Fija tono, formato y criterios minimos."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Fortalece validez del cierre argumentativo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Control de placeholders editoriales",
          "kind": "depends_on",
          "justification": "La propagacion confiable exige estructura valida."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Evita errores formales que degradan entrega."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Ordena el razonamiento hasta un cierre aplicable."
        }
      ],
      "evidence": [
        "README del destino con placeholders Slug sin expandir.",
        "README del destino con nombres de archivo corruptos.",
        "Programa analitico con ejes editoriales estables.",
        "Archivo .bib local con claves institucionales existentes.",
        "Antecedentes de salidas no JSON parseable en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 2: se mantiene union-dedupe lossless sin eliminar reglas utiles.",
      "Ciclo 2: se conserva separacion entre reglas estables y contenido tematico local.",
      "Ciclo 2: se prioriza grafo conceptual transversal sobre redaccion literal.",
      "Ciclo 2: se mantienen supuestos abiertos donde falta verificacion local."
    ]
  }
}