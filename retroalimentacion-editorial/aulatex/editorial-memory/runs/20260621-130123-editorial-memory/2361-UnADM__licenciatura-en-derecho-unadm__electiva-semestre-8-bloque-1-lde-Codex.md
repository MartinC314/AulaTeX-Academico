{
  "summary": [
    "Se sincroniza memoria transversal desde Actividad 1 de Filosofia del Derecho hacia materia Electiva S8 B1 con estrategia conservadora.",
    "Se preservan reglas institucionales, de estructura y de calidad ya validadas en UnADM.",
    "Se aplica compresion lossless por deduplicacion semantica sin recorte de reglas utiles.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodo.",
    "Se refuerza normalizacion de placeholders y nombres de archivo corruptos detectados en README y programa.",
    "Se mantiene antecedente de salidas no parseables como riesgo operativo activo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional LDE-S8B1 sin confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Marcar como supuesto todo dato no visible en consigna o metadatos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Usar carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones reutilizables: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Diferenciar explicitamente resumen de fuentes y postura propia.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Vincular cada actividad con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "No extrapolar contenidos de otras materias o semanas sin evidencia local.",
    "Transformar la planeacion en reporte, presentacion o producto visual segun consigna.",
    "Verificar que el producto final coincida con la consigna activa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Corregir placeholders sin expandir y rutas con caracteres corruptos antes de entrega.",
    "Confirmar existencia de rutas y archivos citados en README/programa."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y plantilla base del destino salvo instruccion institucional verificada.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "No dejar tokens tipo $(@{...}.Slug) en archivos finales.",
    "Corregir nombres corruptos en README: reporte y referencias.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico del destino.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables de identidad, estructura y calidad.",
    "No propagar metadatos especificos de una materia a nodos no equivalentes.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar duplicados semanticos.",
    "Mantener regla global de no inventar fuentes en nodos relacionados.",
    "Registrar como deuda tecnica toda salida no estructurada detectada."
  ],
  "open_questions": [
    "Supuesto: creditos de la electiva siguen sin confirmacion oficial en README y portada.",
    "Supuesto: figura docente sigue sin nombre confirmado.",
    "Confirmar si el nombre oficial de la electiva difiere de la plantilla actual.",
    "Confirmar si existe consigna local que requiera ajustar tipos de producto por actividad.",
    "Confirmar limpieza completa de placeholders Slug en todos los documentos del destino."
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
      "Problema juridico delimitado.",
      "Conceptos y fuentes pertinentes.",
      "Analisis propio sustentado.",
      "Cierre juridico transferible.",
      "Normalizacion estructurada obligatoria."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Asegurar coherencia argumentativa y trazabilidad de fuentes.",
      "Sostener continuidad editorial entre nodos con control de riesgo."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones estables reutilizables.",
      "Postura propia con evidencia.",
      "Supuestos visibles.",
      "Conclusion aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion.",
      "Afirmacion -> evidencia verificable -> inferencia juridica.",
      "Descripcion breve -> posicion critica -> implicacion practica."
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
          "justification": "Fija tono, forma y criterios de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Evita afirmaciones sin respaldo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion segura."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Calidad de compilacion LaTeX",
          "kind": "supports",
          "justification": "Reduce fallas por tokens y rutas defectuosas."
        }
      ],
      "evidence": [
        "README local con placeholders Slug sin expandir.",
        "README local con nombres de archivo corruptos en estructura.",
        "Programa analitico con ejes editoriales reutilizables.",
        "Archivo .bib local con claves institucionales existentes.",
        "Antecedente heredado de salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion semantica completada sin regresion.",
      "Ciclo 19: reforzada regla de no transferir contenido tematico entre nodos no equivalentes.",
      "Ciclo 19: reforzados gates de parseo JSON, trazabilidad y consistencia bib.",
      "Ciclo 19: reforzada higiene LaTeX sobre placeholders y rutas.",
      "Ciclo 19: preservada memoria institucional heredada como capa minima comun."
    ]
  }
}