{
  "summary": [
    "Se sincroniza memoria transversal desde Actividad 1 de Filosofia del Derecho hacia materia Electiva S8 B1 con estrategia conservadora.",
    "Se preservan reglas institucionales UnADM, estructura reusable y control de calidad sin recortes.",
    "Se aplica compresion lossless por deduplicacion semantica y se eliminan duplicados literales.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable y normalizacion obligatoria.",
    "Se evita transferir contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "Mantener coursecode provisional LDE-S8B1 hasta confirmacion oficial.",
    "No renombrar asignatura sin confirmacion institucional.",
    "Usar carpeta de materia como entrada canonica.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Marcar como supuesto todo dato no visible en consigna o metadatos locales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar secciones en secuencia: conceptos o fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, programa analitico, plantilla de reporte, plantilla de presentacion y .bib local."
  ],
  "activity_rules": [
    "Vincular el producto con al menos un problema juridico o social delimitado.",
    "Relacionar conceptos, normas, doctrina o datos con el producto solicitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar contenidos tematicos de otras materias o semanas sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con evidencia o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de compilar o entregar.",
    "Verificar existencia real de rutas y archivos citados."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener clase y plantilla base de la materia sin cambios no justificados.",
    "Mantener documenttitle, documentsubtitle, documentsubject, coursename y coursecode consistentes.",
    "Conservar claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Resolver literales tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres corruptos de archivos en README (supuesto: faltan letras iniciales por error de generador)."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo bibliografico local canonico.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar en .bib las fuentes especificas de cada actividad.",
    "No inventar referencias; incluir solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Mantener claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas estables entre nodos no equivalentes.",
    "Priorizar transferencia de identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido tematico especifico de Actividad 1.",
    "Aplicar union-dedupe lossless en cada ciclo y evitar regresiones.",
    "Mantener registro de ciclos con normalizacion manual cuando haya salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la asignatura y codigo de curso definitivo.",
    "Confirmar figura docente para plantilla base.",
    "Confirmar si todas las actividades de la materia requieren reporte, presentacion o ambos formatos.",
    "Confirmar correccion final de placeholders y nombres de archivo corruptos en README y programa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Verificable y sobrio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica por carpeta de materia"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8, bloque 1, tipo Electiva",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema",
      "Conceptos y fuentes",
      "Analisis propio",
      "Conclusion juridica transferible",
      "Trazabilidad y normalizacion estructurada"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos consistentes.",
      "Asegurar calidad juridica, evidencia verificable y formato institucional estable."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura propia sustentada",
      "Supuestos etiquetados",
      "Cierre juridico aplicable"
    ],
    "argumentative_patterns": [
      "Problema -> fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia -> inferencia juridica",
      "Descripcion breve -> postura critica -> implicacion practica"
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
          "justification": "Fija tono, formato y criterios minimos de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones con evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Control de placeholders editoriales",
          "kind": "depends_on",
          "justification": "La propagacion confiable requiere salida estructurada y limpia."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Evita fallas de compilacion y mantiene consistencia documental."
        }
      ],
      "evidence": [
        "README local con placeholders Slug sin expandir.",
        "Programa analitico con ejes editoriales estables.",
        "Archivo .bib local con dos fuentes institucionales activas.",
        "Plantilla .tex con metadatos base y campos pendientes visibles."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se refuerza normalizacion JSON como gate duro.",
      "Ciclo 11: se transfiere patron argumentativo estable sin contenido tematico de origen.",
      "Ciclo 11: se conserva regla de no inventar fuentes y de marcar supuestos.",
      "Ciclo 11: se refuerza limpieza de placeholders y rutas corruptas como requisito pre-entrega."
    ]
  }
}