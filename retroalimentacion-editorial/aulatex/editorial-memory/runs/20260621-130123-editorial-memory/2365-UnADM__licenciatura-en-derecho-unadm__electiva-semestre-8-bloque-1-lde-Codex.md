{
  "summary": [
    "Sincronizacion transversal aplicada con estrategia conservadora y union-dedupe lossless.",
    "Se preserva ADN institucional UnADM y se transfieren solo abstracciones estables.",
    "Se refuerzan ejes reutilizables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se mantiene control estricto de calidad: JSON parseable, trazabilidad y supuestos marcados.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho por no equivalencia nodal."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Marcar como supuesto todo dato no visible o no confirmado.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos/fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar fuentes o contenidos de otras semanas sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Corregir placeholders y literales corruptos en README y programa antes de cierre editorial."
  ],
  "latex_rules": [
    "Mantener plantilla LaTeX base de la materia para reportes y presentaciones.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Mantener consistencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Completar campos pendientes de portada con datos confirmados; si faltan, marcar como supuesto."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico.",
    "Priorizar fuentes institucionales UnADM como base contextual.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura, calidad y trazabilidad.",
    "No propagar metadatos ni contenido tematico especifico entre nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Mantener antecedente institucional: salidas no estructuradas requieren normalizacion manual previa.",
    "Registrar supuestos abiertos para que nodos hijos completen contexto local."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la asignatura electiva, si difiere del actual.",
    "Confirmar figura docente para plantilla.",
    "Confirmar si todas las actividades requeriran reporte, presentacion o ambos.",
    "Supuesto: la bibliografia local actual es suficiente como base minima; validar con consigna real."
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
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos, normas, doctrina o datos",
      "Producto solicitado por planeacion",
      "Analisis propio con postura academica",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos estructurados y verificables.",
      "Garantizar consistencia editorial institucional entre actividades y materia.",
      "Asegurar trazabilidad de fuentes y calidad formal reproducible."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Afirmaciones con evidencia",
      "Postura propia sustentada",
      "Cierre con implicacion practica"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia verificable -> inferencia juridica",
      "Descripcion breve -> posicion critica -> transferencia profesional"
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
          "justification": "La identidad define tono, formato y criterio de cierre."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "La argumentacion requiere evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay control de calidad reutilizable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Normalizacion JSON",
          "kind": "develops",
          "justification": "Eliminar tokens corruptos mejora consistencia tecnica y editorial."
        }
      ],
      "evidence": [
        "README del destino muestra placeholders sin expandir y nombres corruptos.",
        "Programa analitico del destino confirma ejes editoriales reutilizables.",
        "Archivo .bib local contiene base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: transferencia transversal conservadora ejecutada.",
      "Se deduplicaron reglas repetidas sin perdida de contenido util.",
      "Se reforzaron gates de JSON, supuestos y trazabilidad bibliografica.",
      "Se conservaron vacios locales abiertos sin inventar datos."
    ]
  }
}