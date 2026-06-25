{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe lossless entre actividad y materia no equivalente.",
    "Se preservan reglas institucionales UnADM, estructura argumentativa reusable y control de calidad estricto.",
    "Se incorporan solo abstracciones estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho por falta de equivalencia curricular.",
    "Se refuerza normalizacion de placeholders y nombres corruptos detectados en README y programa analitico del destino."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
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
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders sin expandir y rutas con caracteres corruptos antes de compilar."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Evitar tokens de automatizacion sin expandir en README, programa y archivos finales.",
    "Completar campos pendientes de portada solo con datos confirmados; si no, marcar como supuesto."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico del destino.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de materia y bibliografia especifica de actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura, calidad y trazabilidad.",
    "No propagar metadatos ni contenidos tematicos de Filosofia del Derecho a nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Mantener antecedente institucional: salidas no estructuradas requieren normalizacion manual previa.",
    "Priorizar grafo conceptual transversal sobre redaccion literal de actividades."
  ],
  "open_questions": [
    "Supuesto: creditos oficiales de la electiva aun no confirmados.",
    "Supuesto: nombre oficial de figura docente pendiente.",
    "Confirmar si LDE-S8B1 es codigo oficial o provisional.",
    "Confirmar limpieza total de placeholders Slug en README y programa analitico.",
    "Confirmar si la plantilla de presentacion replica metadatos de portada del reporte."
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
      "Analisis propio con evidencia.",
      "Conclusion juridica aplicable.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para practica juridica.",
      "Sostener continuidad editorial institucional sin regresiones.",
      "Permitir propagacion recursiva confiable mediante estructura y calidad controlada."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables y reutilizables.",
      "Postura propia sustentada.",
      "Cierre juridico transferible.",
      "Supuestos marcados cuando falte evidencia."
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
          "justification": "El marco institucional define tono, formato y criterio de cierre."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Las inferencias juridicas requieren evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Calidad de compilacion LaTeX",
          "kind": "supports",
          "justification": "Eliminar tokens sin expandir evita errores de rutas y nombres."
        }
      ],
      "evidence": [
        "README y programa del destino muestran placeholders Slug sin expandir.",
        "La plantilla de reporte del destino fija identidad institucional y metadatos base.",
        "El .bib local contiene fuentes institucionales verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se preserva ADN institucional y se refuerzan gates de calidad sin recorte.",
      "Ciclo 15: se deduplican reglas repetidas y se mantiene compresion lossless.",
      "Ciclo 15: se limita transferencia a abstracciones estables por relacion transversal no equivalente.",
      "Ciclo 15: se mantienen vacios locales abiertos con etiqueta de supuesto."
    ]
  }
}