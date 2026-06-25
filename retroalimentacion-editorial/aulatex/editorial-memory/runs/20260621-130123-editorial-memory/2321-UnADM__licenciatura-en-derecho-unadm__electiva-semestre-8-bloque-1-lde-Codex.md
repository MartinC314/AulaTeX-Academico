{
  "summary": [
    "Se sincroniza transversalmente ADN editorial estable desde actividad de Filosofia del Derecho hacia materia Electiva S8 B1.",
    "Se preservan reglas utiles previas con union-dedupe lossless y sin recorte.",
    "Se refuerzan ejes reutilizables: problema, conceptos/fuentes, analisis propio y conclusion juridica transferible.",
    "Se mantiene control estricto de normalizacion JSON antes de propagacion recursiva.",
    "Se consolidan mejoras verificables locales: placeholders Slug sin expandir, nombres corruptos en README y creditos no confirmados [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional LDE-S8B1 sin confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Marcar como [supuesto] todo dato no visible o no confirmado en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar secciones en secuencia estable: conceptos/fuentes, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Diferenciar con claridad resumen de fuentes y postura propia.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Vincular cada producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar contenidos tematicos entre nodos no equivalentes sin evidencia local.",
    "No asumir que bibliografia de otras semanas o materias aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad: afirmacion con cita o marca [supuesto].",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) antes de entrega.",
    "Corregir nombres de archivo corruptos en README antes de reutilizacion.",
    "Confirmar que rutas citadas existan localmente."
  ],
  "latex_rules": [
    "Mantener plantilla base LaTeX de reporte y presentacion del destino.",
    "Conservar clase article con configuracion spanish letterpaper oneside.",
    "Mantener coherencia entre documenttitle, documentsubtitle, documentsubject, coursename y coursecode.",
    "Usar codificacion compatible con espanol y acentos correctos en .tex y .bib.",
    "Completar campos pendientes de portada antes de entrega (figura docente, creditos) [supuesto].",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico.",
    "Registrar fuentes especificas por actividad en el .bib local.",
    "Priorizar fuentes institucionales UnADM para contexto curricular.",
    "No inventar referencias; incluir solo fuentes consultables y verificables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/editorial o URL.",
    "Mantener claves BibTeX estables y descriptivas.",
    "Conservar claves existentes unadmSitioWeb y unadmMallaDerecho2024 sin renombrar."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en relaciones transversales.",
    "No propagar redaccion literal ni contenidos tematicos locales no verificados.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Registrar ciclos previos con salida no estructurada como alerta de normalizacion manual."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de figura docente.",
    "Confirmar si existe nombre oficial alterno de la asignatura.",
    "Confirmar si el codigo LDE-S8B1 es definitivo o provisional.",
    "Confirmar si la presentacion comparte exactamente las mismas reglas de portada.",
    "Confirmar limpieza completa de placeholders y caracteres corruptos en README/programa."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Verificable",
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
      "Analisis propio",
      "Conclusion juridica transferible",
      "Normalizacion estructurada antes de propagacion"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundamentados y trazables.",
      "Asegurar coherencia entre consigna, evidencia y posicion argumentativa.",
      "Sostener una memoria editorial persistente sin regresiones."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura propia sustentada",
      "Cierre transferible a practica",
      "Marca [supuesto] cuando falte verificacion"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia verificable -> inferencia juridica",
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
          "justification": "Fija tono, formato y criterios de entrega."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones con evidencia verificable."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Evita errores por tokens sin expandir y rutas corruptas."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Conduce del problema a una salida profesional aplicable."
        }
      ],
      "evidence": [
        "README local con tokens Slug sin expandir.",
        "README local con nombres de archivo corruptos en estructura.",
        "Programa analitico local con ejes estables reutilizables.",
        "Plantilla .tex local con campos pendientes de creditos y figura docente [supuesto].",
        "Archivo .bib local con claves institucionales ya definidas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se conserva herencia institucional y gate de JSON parseable.",
      "Ciclo 9: se transfiere estructura reusable de Filosofia del Derecho sin contenido tematico literal.",
      "Ciclo 9: se refuerza regla de no inventar fuentes y de marcar [supuesto].",
      "Ciclo 9: se mantienen mejoras locales verificables de placeholders y rutas."
    ]
  }
}