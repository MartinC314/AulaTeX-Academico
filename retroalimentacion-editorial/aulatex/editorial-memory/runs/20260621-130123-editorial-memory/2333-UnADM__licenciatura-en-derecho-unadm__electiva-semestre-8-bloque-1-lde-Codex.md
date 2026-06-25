{
  "summary": [
    "Sincronizacion transversal conservadora aplicada con union-dedupe lossless.",
    "Se preservan reglas institucionales UnADM, estructura reusable y gates de calidad.",
    "Se agrega mejora verificable: normalizar placeholders Slug y nombres corruptos en README/programa.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo.",
    "Se refuerza cerebro editorial minimo de materia con vacios locales marcados como supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener codigo provisional LDE-S8B1 hasta confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Marcar como supuesto todo dato no confirmado en consigna o metadatos.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No renombrar asignatura sin confirmacion oficial."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar secciones en: conceptos o fuentes, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Usar carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular cada producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes de otras materias o semanas sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con cita o marca de supuesto.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y literales corruptos antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla base de reporte y presentacion de la materia.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Mantener claves y nombres canonicos: coursename, coursecode, documentsubject.",
    "Completar campos pendientes de portada antes de entrega (docente, creditos si aplica).",
    "No dejar tokens sin expandir tipo $(@{...}.Slug) en archivos finales.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Mantener claves BibTeX estables y descriptivas."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables: identidad, estructura, calidad y grafo.",
    "No propagar metadatos o contenido tematico especifico entre nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Si falta contexto local, conservar cerebro minimo y abrir preguntas.",
    "Registrar como antecedente toda salida no estructurada para control futuro."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva siguen no confirmados.",
    "Supuesto: figura docente en portada sigue no confirmada.",
    "Confirmar nombre oficial definitivo de la asignatura electiva.",
    "Confirmar si existe rubrica formal por actividad en esta materia.",
    "Confirmar correccion completa de nombres corruptos en README (reporte/referencias)."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Juridicamente preciso",
        "Claro y verificable",
        "Sobrio ante datos no confirmados"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica por carpeta de materia",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8, bloque 1, tipo Electiva",
        "Codigo provisional LDE-S8B1",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y fuentes verificables",
      "Analisis propio argumentado",
      "Conclusion juridica aplicable",
      "Normalizacion estructurada previa a propagacion"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Garantizar consistencia editorial institucional en nodos relacionados.",
      "Evitar ruido por herencias no verificadas."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura propia sustentada",
      "Cierre juridico transferible",
      "Supuestos marcados"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia -> inferencia juridica",
      "Descripcion breve -> posicion critica -> implicacion practica"
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
          "justification": "Define tono, formato y criterio comun de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones y evita contenido inventado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay transferencia confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Reduce fallos por tokens sin expandir y rutas corruptas."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Ordena el razonamiento hacia utilidad profesional."
        }
      ],
      "evidence": [
        "README local con placeholders Slug sin expandir.",
        "Programa analitico local con ejes editoriales estables.",
        "Bib local con claves institucionales definidas.",
        "Antecedente de salida no JSON parseable en memoria heredada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: dedupe semantico completado sin eliminar reglas utiles previas.",
      "Ciclo 12: reforzada regla de bloqueo por JSON no parseable.",
      "Ciclo 12: reforzada normalizacion de placeholders y nombres corruptos.",
      "Ciclo 12: preservada separacion entre abstracciones transferibles y contenido tematico no equivalente."
    ]
  }
}