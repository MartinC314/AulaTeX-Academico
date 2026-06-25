{
  "summary": [
    "Se consolida sincronizacion transversal conservadora desde actividad origen hacia materia destino.",
    "Se preservan reglas estables: identidad UnADM, estructura por ejes, analisis propio, conclusion juridica y trazabilidad de fuentes.",
    "Se refuerza normalizacion obligatoria: no propagar memoria no parseable ni artefactos con placeholders.",
    "Se mantiene compresion lossless por union-dedupe sin recorte de reglas utiles previas.",
    "Se evita transferencia de contenido tematico especifico de Filosofia del Derecho por no equivalencia de nodos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 8, bloque 2, tipo Electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado en consigna o documentos locales.",
    "Mantener autor y matricula confirmados en front matter: Martin Jonathan de la Cruz, ES2611202040.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib."
  ],
  "activity_rules": [
    "Traducir cada consigna semanal a producto concreto solicitado.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Vincular conceptos, normas, doctrina o datos con el problema juridico tratado.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar ausencia de placeholders y tokens sin expandir en README, programa, .tex y .bib.",
    "Verificar que el producto corresponda a la consigna vigente de la actividad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Usar reporte-electiva-semestre-8-bloque-2.tex y presentacion-electiva-semestre-8-bloque-2.tex como bases.",
    "Reemplazar placeholders como Actividad X antes de compilar.",
    "Corregir rutas y nombres truncados o con tokens tipo $(@{...}.Slug)."
  ],
  "bibliography_rules": [
    "Registrar fuentes especificas por actividad en electiva-semestre-8-bloque-2.bib.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar [supuesto] cuando falten datos bibliograficos confirmados."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas abstractas y estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar redaccion literal ni contenido doctrinal especifico del origen.",
    "Mantener etiqueta de herencia provisional para fuentes no verificadas.",
    "Aplicar union-dedupe en cada ciclo para evitar regresiones y duplicados.",
    "Usar ciclo 1 y 2 heredados como insumo normalizado, no evidencia final."
  ],
  "open_questions": [
    "[supuesto] Confirmar creditos oficiales de la materia destino para metadatos.",
    "[supuesto] Confirmar nombre oficial de figura docente para portada.",
    "[supuesto] Confirmar politica institucional para year y fecha de consulta en @misc.",
    "[supuesto] Confirmar si existe nombre oficial alterno de la electiva.",
    "[supuesto] Confirmar si la bibliografia local requiere archivo adicional por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Conservador ante datos no confirmados."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de materia como entrada canonica.",
        "Control visible de supuestos.",
        "Trazabilidad entre documentos locales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 8, bloque 2, tipo Electiva.",
        "Codigo LDE-S8B2.",
        "[supuesto] Creditos pendientes de confirmacion."
      ]
    },
    "essence": [
      "Problema juridico.",
      "Conceptos y marco normativo.",
      "Producto solicitado.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada.",
      "Trazabilidad cita-texto-bib."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros y verificables.",
      "Sostener rigor editorial transversal sin perder identidad institucional.",
      "Permitir propagacion segura entre nodos mediante reglas estables."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y ordenadas.",
      "Postura propia respaldada por evidencia.",
      "Cierre aplicable a practica juridica.",
      "Marcado explicito de [supuesto]."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion relevante -> evidencia verificable -> inferencia juridica.",
      "Evitar descripcion pura; priorizar juicio juridico razonado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
        "Control de supuestos",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Trazabilidad cita-texto-bib",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables y reglas ambiguas."
        },
        {
          "source": "Integridad academica",
          "target": "Trazabilidad cita-texto-bib",
          "kind": "depends_on",
          "justification": "La verificabilidad requiere correspondencia entre afirmaciones y fuentes."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La transferencia profesional surge del razonamiento y no del resumen."
        },
        {
          "source": "Control de supuestos",
          "target": "Rigor editorial",
          "kind": "supports",
          "justification": "Separa datos confirmados de pendientes y reduce errores."
        }
      ],
      "evidence": [
        "README local de materia.",
        "Programa analitico local.",
        "electiva-semestre-8-bloque-2.bib.",
        "Reglas heredadas de calidad sobre JSON parseable y normalizacion manual."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicadas reglas repetidas de origen y destino sin perdida semantica.",
      "Ciclo 4: reforzada barrera de calidad JSON parseable antes de propagacion.",
      "Ciclo 4: mantenida estrategia conservadora de no transferir contenido doctrinal especifico entre nodos no equivalentes.",
      "Ciclo 4: reforzada correccion de placeholders y tokens Slug como riesgo operativo transversal."
    ]
  }
}