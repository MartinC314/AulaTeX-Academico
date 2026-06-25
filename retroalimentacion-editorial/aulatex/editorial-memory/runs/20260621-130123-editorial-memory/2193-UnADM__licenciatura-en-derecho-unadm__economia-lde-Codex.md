{
  "summary": [
    "Se consolida memoria transversal minima de Economia LDE con identidad UnADM.",
    "Se preservan reglas estables heredadas: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene normalizacion estructurada obligatoria antes de toda propagacion.",
    "Se refuerza compresion lossless por union-dedupe sin regresion.",
    "Se registra incidencia tecnica local: tokens Slug sin expandir en README y programa analitico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local verificado: Economia LDE, semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion oficial.",
    "Tratar fuentes heredadas de modelos como provisionales hasta validacion local.",
    "No usar salidas de modelos como fuente academica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar: conceptos y datos, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al tipo solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar cada entrega a reporte, presentacion o producto visual segun consigna.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos economicos, conceptos juridicos y valoracion argumentativa.",
    "Conectar conclusion con impacto social o practica juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar que toda afirmacion tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y economia.bib.",
    "Revisar y normalizar respuestas no estructuradas antes de aplicar aguas abajo."
  ],
  "latex_rules": [
    "Mantener plantilla base de reporte-economia.tex como referencia.",
    "Conservar metadatos academicos completos en portada.",
    "Usar espanol y letterpaper salvo instruccion oficial distinta.",
    "Mantener estilo de citacion authoryear consistente con setcitestyle.",
    "Evitar paquetes o comandos no estandar sin justificacion verificable.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canonico local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Agregar solo referencias realmente usadas en el producto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Registrar fecha de consulta en recursos web cuando aplique."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones estables por ser salto transversal entre nodos no equivalentes.",
    "No transferir contenido tematico especifico de Filosofia del Derecho a Economia sin consigna local.",
    "Priorizar identidad, estructura reusable y gates de calidad en propagacion recursiva.",
    "Conservar reglas utiles previas y anexar solo mejoras verificables.",
    "Mantener alerta persistente de parseo hasta cierre editorial documentado."
  ],
  "open_questions": [
    "Confirmar si Economia tiene rubrica formal especifica por actividad.",
    "Confirmar nombre final de figura docente para portada.",
    "Confirmar si README debe mostrar solo economia.bib sin tokens de plantilla.",
    "Supuesto: no hay consigna textual de actividad concreta en este ciclo.",
    "Confirmar periodicidad de actualizacion de year y fecha de consulta en unadmSitioWeb."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Directo y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar.",
        "Validacion local previa a transferencia transversal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Economia LDE en semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Planeacion semanal como guia del tipo de producto."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional."
    ],
    "style_markers": [
      "Frases claras y accionables.",
      "Secciones argumentativas explicitas.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Trazabilidad entre afirmaciones y fuentes."
    ],
    "argumentative_patterns": [
      "Problema breve inicial.",
      "Marco conceptual-normativo pertinente.",
      "Analisis critico con evidencia.",
      "Cierre con implicacion juridica practica."
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
          "justification": "La identidad institucional exige verificabilidad y consistencia editorial."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico aplicado",
          "kind": "depends_on",
          "justification": "El analisis valido requiere sustento documental."
        },
        {
          "source": "Analisis juridico aplicado",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Compresion union-dedupe",
          "kind": "supports",
          "justification": "La estructura valida permite deduplicar sin perdida."
        }
      ],
      "evidence": [
        "README de Economia: ubicacion curricular y pauta editorial.",
        "programa-analitico-economia.md: proposito y ejes de trabajo.",
        "economia.bib: fuentes institucionales locales.",
        "Incidencia tecnica observable: tokens Slug sin expandir en rutas documentales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se transfieren solo abstracciones estables desde actividad de Filosofia del Derecho.",
      "Ciclo 21: se mantiene regla dura de parseo JSON y normalizacion previa.",
      "Ciclo 21: se refuerza no uso de modelos como fuente academica.",
      "Ciclo 21: se agrega control tecnico sobre tokens de plantilla sin expandir."
    ]
  }
}