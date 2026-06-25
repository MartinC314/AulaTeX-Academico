{
  "summary": [
    "Sincronizacion transversal aplicada desde actividad origen a materia destino con enfoque conservador.",
    "Se preservan reglas utiles previas y se deduplican sin perdida semantica.",
    "Se transfieren solo abstracciones estables: identidad, estructura, calidad y trazabilidad.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se refuerza control de placeholders y literales corruptos detectados en README y programa.",
    "Se evita traslado de contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Marcar como supuesto todo dato no visible o no confirmado en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar carpeta de materia como entrada canonica."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes o contenidos de otras materias sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y caracteres corruptos en rutas y nombres de archivo antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes y presentaciones.",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README, programa y referencias.",
    "Completar campos pendientes de portada antes de entrega, en especial creditos y figura docente [supuesto]."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico [supuesto].",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; incluir solo fuentes consultadas y verificables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Distinguir bibliografia base institucional de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura, calidad y trazabilidad.",
    "No propagar metadatos locales de esta electiva a nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Registrar ciclos con normalizacion manual cuando se detecte salida no estructurada.",
    "Priorizar validaciones tecnicas primero: JSON, rutas, placeholders, consistencia .bib."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la asignatura y codigo si difieren del provisional LDE-S8B1.",
    "Confirmar figura docente para plantilla final.",
    "Confirmar si existe consigna local que ajuste profundidad argumentativa por actividad.",
    "Confirmar si presentacion-electiva-semestre-8-bloque-1.tex mantiene las mismas reglas de portada."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Juridicamente preciso.",
        "Claro y verificable.",
        "Sobrio ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica por carpeta de materia.",
        "Supuestos etiquetados sin ambiguedad."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 1, tipo Electiva.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y fuentes pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundamentados y verificables.",
      "Estandarizar calidad editorial sin perder flexibilidad por actividad.",
      "Asegurar trazabilidad de decisiones y fuentes en todo el ciclo de propagacion."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables y reutilizables.",
      "Afirmaciones con respaldo.",
      "Supuestos marcados.",
      "Cierre juridico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> postura critica -> implicacion practica."
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
          "justification": "Define tono, formato y criterios de coherencia."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "Sostiene la validez academica de la postura final."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay auditoria confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Normalizacion JSON",
          "kind": "supports",
          "justification": "Reduce ruido tecnico y errores de propagacion."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Ordena el razonamiento hasta un cierre aplicable."
        }
      ],
      "evidence": [
        "README local con tokens Slug sin expandir.",
        "Programa analitico con ejes editoriales estables.",
        "Archivo .bib local con base institucional verificable.",
        "Antecedente institucional de salidas no estructuradas en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se refuerza ADN transversal sin trasladar contenido tematico no equivalente.",
      "Ciclo 7: se conserva regla de bloqueo por JSON no parseable.",
      "Ciclo 7: se consolida gate de trazabilidad cita-texto-.bib.",
      "Ciclo 7: se mantiene estrategia progresiva y conservadora con supuestos marcados."
    ]
  }
}