{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de origen hacia materia destino sin transferir redaccion literal.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa en cinco ejes, evidencia verificable y conclusion juridica transferible.",
    "Se mantiene politica de normalizacion obligatoria: bloquear propagacion si no hay JSON parseable.",
    "Se refuerza estrategia conservadora: union-dedupe lossless, sin regresion y con marcado explicito de supuestos.",
    "Se crea base minima robusta para Economia LDE con vacios locales abiertos para validacion posterior."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular verificado de Economia LDE: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Conservar voz formal, clara y juridicamente precisa.",
    "Marcar como supuesto todo dato no confirmado en consigna o planeacion oficial.",
    "Tratar salidas de modelos y fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear siempre el producto al formato exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional o impacto social."
  ],
  "activity_rules": [
    "Adaptar cada entrega al tipo solicitado: reporte, presentacion o producto visual.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir datos economicos, conceptos juridicos y argumentos propios."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Revisar y normalizar respuestas no estructuradas antes de propagacion recursiva."
  ],
  "latex_rules": [
    "Mantener codificacion correcta de espanol y acentos en .tex y .bib.",
    "Conservar metadatos academicos completos en portada.",
    "Usar estilo de citacion consistente con plantilla activa.",
    "Evitar paquetes o comandos no estandar sin justificacion tecnica verificable.",
    "Corregir tokens sin expandir en README, programa y rutas antes de compilar."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canonico de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Agregar solo referencias realmente consultables y usadas en el producto.",
    "No inventar fuentes ni usar salidas de modelos como bibliografia academica.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL; incluir fecha de consulta en web."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No propagar datos especificos de una actividad como regla global de materia.",
    "Mantener alerta persistente de parseo heredado hasta cierre editorial documentado.",
    "Aplicar ciclo progresivo y conservador: anexar mejoras verificables sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar guia formal de formato adicional para Economia LDE.",
    "Confirmar si README debe mostrar solo economia.bib como nombre canonico.",
    "Validar actualizacion anual de year y fecha de consulta en unadmSitioWeb.",
    "Confirmar nombre de figura docente en metadatos de portada.",
    "Supuesto: la incidencia de tokens de plantilla en README sigue abierta hasta correccion local."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Economia LDE: semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Planeacion semanal como guia del tipo de producto."
      ]
    },
    "essence": [
      "Problema relevante.",
      "Conceptos y marco pertinente.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en entregables academicos utiles y verificables.",
      "Asegurar coherencia entre identidad institucional, metodo argumentativo y evidencia."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Secciones argumentativas explicitas.",
      "Supuestos marcados de forma visible.",
      "Sin redaccion literal heredada entre nodos."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual/normativo.",
      "Analisis critico propio con evidencia.",
      "Cierre con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Evidencia verificable",
        "Analisis juridico aplicado",
        "Conclusion transferible",
        "Compresion union-dedupe"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico aplicado",
          "kind": "depends_on",
          "justification": "El analisis valido requiere respaldo comprobable."
        },
        {
          "source": "Analisis juridico aplicado",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento sustentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Compresion union-dedupe",
          "kind": "supports",
          "justification": "La estructura valida permite consolidacion lossless sin regresion."
        }
      ],
      "evidence": [
        "README de Economia LDE.",
        "programa-analitico-economia.md.",
        "economia.bib local.",
        "Regla persistente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se refuerza transferencia transversal por abstracciones estables.",
      "Ciclo 15: se deduplican reglas sin recorte de contenido util.",
      "Ciclo 15: se conserva alerta de parseo y normalizacion obligatoria.",
      "Ciclo 15: se evita traslado de contenido especifico de Filosofia del Derecho a Economia salvo patrones editoriales reutilizables."
    ]
  }
}