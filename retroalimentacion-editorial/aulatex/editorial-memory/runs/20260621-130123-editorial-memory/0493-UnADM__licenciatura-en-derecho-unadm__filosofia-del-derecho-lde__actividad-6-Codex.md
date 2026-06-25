{
  "summary": [
    "Se consolida refuerzo lateral desde actividad 1 hacia actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y contexto curricular verificado: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se mantiene trazabilidad entre fuentes, supuestos marcados y afirmaciones relevantes."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear cada actividad a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular cuando contextualice: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisionales las fuentes heredadas no verificadas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema solicitado sin claves extra.",
    "Organizar desarrollo academico en: problema, marco conceptual-normativo, desarrollo del producto, analisis propio y conclusion.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas o sin criterio juridico propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas en consolidacion.",
    "Validar consistencia entre citas en texto y .bib activo.",
    "Revisar que la conclusion derive del desarrollo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correctos en espanol.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a un uso tematico (interpretacion juridica) y no sustituye automaticamente el .bib canonico general."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones ni redaccion literal entre hermanos.",
    "Mantener union-dedupe lossless para evitar regresiones.",
    "Conservar advertencias historicas de salidas no estructuradas en nodos con herencia similar.",
    "Si falta consigna local, propagar estructura base y dejar preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 6; confirmar producto exacto requerido.",
    "Confirmar rubrica especifica de evaluacion de actividad 6.",
    "Confirmar si actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver y coexistencia de archivos .bib.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos y utiles para practica juridica.",
      "Preservar consistencia editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Apertura con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con trazabilidad.",
      "Diferenciacion visible entre fuente y postura personal.",
      "Cierre con criterio juridico aplicado."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar doctrina, norma y evidencia.",
      "Sostener postura propia con justificacion.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Trazabilidad de fuentes"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay analisis solido sin delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Trazabilidad de fuentes",
          "kind": "supports",
          "justification": "La estructura estable permite verificar citas, supuestos y evidencia."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo obligatorios.",
        "Historial de ciclo: necesidad de bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicacion de reglas repetidas y preservacion de reglas utiles previas.",
      "Ciclo 14: refuerzo lateral de identidad, estructura y control de calidad sin mover contenido especifico de conclusiones.",
      "Ciclo 14: mantenimiento de supuestos abiertos por falta de consigna local verificable."
    ]
  }
}