{
  "summary": [
    "Sincronizacion transversal conservadora aplicada desde actividad origen hacia materia destino.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa reusable y control de calidad.",
    "Se mantiene compresion lossless por union-dedupe sin eliminar reglas utiles previas.",
    "Se refuerza normalizacion de placeholders y literales corruptos detectados en README y programa.",
    "Se evita transferencia de contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio.",
    "Conservar contexto curricular local del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener codigo provisional LDE-S8B1 hasta confirmacion oficial distinta.",
    "Conservar autor y matricula definidos en plantilla base mientras no exista instruccion institucional en contrario.",
    "Marcar como supuesto todo dato no visible o no confirmado en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No renombrar asignatura ni metadatos curriculares sin confirmacion oficial."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secuencia estable: problema, conceptos o fuentes, analisis propio, cierre.",
    "Separar marco normativo o doctrinal cuando aplique por consigna.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar la carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular cada producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes o contenidos de otras materias sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y literales corruptos antes de entrega.",
    "Confirmar existencia de rutas locales citadas antes de usarlas como fuente.",
    "Marcar como pendiente todo dato no confirmado, en especial creditos y figura docente."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y plantilla base consistentes para reportes y presentaciones.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar claves BibTeX estables para evitar rupturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo corruptos en README (reporte y referencias).",
    "No dejar creditos vacios si el dato oficial esta disponible."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No inventar referencias; incluir solo obras consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura y calidad.",
    "No propagar metadatos especificos de esta electiva a nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Propagar regla de no inventar fuentes a nodos relacionados.",
    "Registrar y conservar antecedente de normalizacion manual para salidas no estructuradas (ciclo 1 y 2).",
    "Si falta consigna local, propagar solo abstracciones editoriales generales."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de figura docente en plantilla.",
    "Confirmar si el nombre oficial de la asignatura difiere del actual.",
    "Confirmar vigencia oficial del codigo LDE-S8B1.",
    "Confirmar que presentacion-electiva-semestre-8-bloque-1.tex mantiene metadatos alineados.",
    "Confirmar correccion final de placeholders Slug en README y programa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Verificable y sobrio.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
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
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, sustentados y transferibles.",
      "Asegurar trazabilidad de fuentes y calidad formal en LaTeX.",
      "Sostener continuidad editorial entre nodos sin contaminar contexto local."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables y reutilizables.",
      "Postura propia sustentada.",
      "Cierre juridico transferible.",
      "Supuestos marcados cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema -> fuentes -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> postura critica -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales"
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
          "justification": "Define tono, formato y criterios minimos de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones con evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "Permite propagacion confiable y auditable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Normalizacion JSON",
          "kind": "supports",
          "justification": "Reduce ambiguedad tecnica y errores de integracion."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Conduce del problema al cierre profesional."
        }
      ],
      "evidence": [
        "README local con placeholders Slug sin expandir.",
        "Programa analitico local con ejes editoriales estables.",
        "Archivo .bib local con fuentes institucionales verificables.",
        "Antecedentes de salida no estructurada en ciclos previos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion semantica aplicada sin recorte de reglas utiles.",
      "Ciclo 13: reforzadas reglas estables de identidad, estructura, calidad y bibliografia.",
      "Ciclo 13: mantenida politica conservadora de no transferir contenido tematico no equivalente.",
      "Ciclo 13: consolidado cerebro editorial minimo con vacios locales abiertos como supuestos."
    ]
  }
}