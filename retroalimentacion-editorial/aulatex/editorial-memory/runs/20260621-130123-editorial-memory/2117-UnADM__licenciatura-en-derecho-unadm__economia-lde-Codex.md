{
  "summary": [
    "Se consolida sincronizacion transversal desde actividad de Filosofia del Derecho hacia materia Economia sin mover contenido literal.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa en cinco ejes, evidencia verificable y cierre juridico transferible.",
    "Se refuerza normalizacion obligatoria: bloquear propagacion si no hay JSON parseable y estructura minima completa.",
    "Se mantiene estrategia progresiva y conservadora con compresion lossless por deduplicacion.",
    "Se corrigen como incidencia tecnica los tokens y artefactos de plantilla en README/programa antes de reutilizar rutas o nombres."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local verificado de Economia LDE: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Conservar voz formal, clara y juridicamente precisa.",
    "Marcar como supuesto cualquier dato no visible en consigna o planeacion oficial.",
    "Tratar fuentes heredadas de modelos como provisionales hasta validacion local.",
    "No usar salidas de modelos como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal o datos, analisis propio y cierre.",
    "Alinear cada entrega al producto exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional o impacto social.",
    "Mantener carpeta de materia como punto de entrada canonico."
  ],
  "activity_rules": [
    "Adaptar cada actividad a reporte, presentacion o producto visual segun consigna.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir hechos/datos economicos de argumentos juridicos.",
    "No asumir fuentes de semanas posteriores sin confirmacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y economia.bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar correspondencia entre producto entregado y consigna vigente."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Conservar metadatos academicos completos en portada.",
    "Mantener estilo de citacion consistente con plantilla.",
    "Evitar paquetes o comandos no estandar sin justificacion tecnica.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa antes de referenciar archivos."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canonico local de la materia.",
    "Priorizar fuentes institucionales UnADM y normativas/doctrinales verificables.",
    "Registrar solo fuentes realmente consultables; no inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, año y fuente/URL.",
    "Agregar fecha de consulta en recursos web cuando aplique.",
    "Separar bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables: identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "No propagar contenido tematico especifico de Filosofia del Derecho como si fuera propio de Economia.",
    "Aplicar union-dedupe sin recorte para evitar regresion de reglas utiles.",
    "Mantener alerta persistente por historial de salidas no parseables hasta cierre documentado.",
    "Si falta contexto local de actividad, crear cerebro minimo y dejar vacios abiertos."
  ],
  "open_questions": [
    "Confirmar si Economia tiene rubrica formal por actividad ademas del programa analitico.",
    "Confirmar nombre canonico definitivo del .bib en README tras resolver token Slug.",
    "Confirmar figura docente para portada.",
    "Supuesto: no se cuenta aun con consignas textuales de actividades especificas de Economia.",
    "Confirmar si existe formato institucional adicional para productos visuales en Economia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Economia LDE en semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Carpeta de materia como entrada canonica."
      ]
    },
    "essence": [
      "Problema",
      "Conceptos y datos pertinentes",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables claros, verificables y utiles para practica juridica.",
      "Sostener continuidad editorial entre nodos sin perder identidad local."
    ],
    "style_markers": [
      "Frases directas y accionables.",
      "Secciones argumentativas explicitas.",
      "Supuestos marcados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual/normativo o datos.",
      "Analisis critico propio con evidencia.",
      "Cierre con implicacion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Evidencia verificable",
        "Analisis juridico aplicado",
        "Conclusion transferible",
        "Normalizacion JSON",
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
          "justification": "La identidad institucional exige trazabilidad y formato verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico aplicado",
          "kind": "depends_on",
          "justification": "Sin respaldo, el analisis queda en opinion."
        },
        {
          "source": "Analisis juridico aplicado",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento sustentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar ruido y conserva reglas auditables."
        }
      ],
      "evidence": [
        "README de Economia: identidad, ubicacion curricular y pauta editorial.",
        "programa-analitico-economia.md: proposito y cinco ejes de trabajo.",
        "economia.bib: base institucional local.",
        "Regla transversal vigente: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se deduplican reglas repetidas y se conserva cobertura funcional completa.",
      "Ciclo 2: se refuerza transferencia transversal por abstracciones estables, no por redaccion literal.",
      "Ciclo 2: se mantiene sin regresion la politica de supuestos y fuentes verificables.",
      "Ciclo 2: se registra incidencia tecnica de tokens Slug sin expandir como gate previo a propagacion."
    ]
  }
}