{
  "summary": [
    "Se consolida sincronizacion transversal hacia Economia LDE sin recortar reglas utiles previas.",
    "Se preserva el nucleo estable: problema, conceptos, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se refuerza compresion lossless por union-dedupe y control de no regresion.",
    "Se incorpora contexto local verificado de Economia LDE: semestre 3, bloque 2, obligatoria, 8 creditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar contexto curricular local verificado de Economia LDE.",
    "Marcar como supuesto todo dato no visible en consigna o planeacion oficial.",
    "Tratar salidas heredadas de modelos como provisionales hasta verificacion local.",
    "No usar salidas de modelos como fuente academica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos y datos, marco normativo o doctrinal, analisis propio, cierre.",
    "Alinear el producto al formato exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a practica profesional o impacto social."
  ],
  "activity_rules": [
    "Adaptar cada entrega al tipo solicitado: reporte, presentacion o producto visual.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Distinguir hechos economicos, conceptos tecnicos y argumentos juridicos.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y economia.bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizacion."
  ],
  "latex_rules": [
    "Mantener plantilla base y metadatos academicos completos en portada.",
    "Conservar espanol y letterpaper salvo instruccion oficial distinta.",
    "Usar codificacion correcta y acentos consistentes en .tex y .bib.",
    "Resolver tokens sin expandir en README, programa analitico y rutas de archivos.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canonico local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Agregar solo referencias realmente usadas en el producto.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables por relacion transversal.",
    "No transferir redaccion literal ni supuestos especificos de otra materia.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Mantener estrategia progresiva y conservadora en cada ciclo.",
    "Registrar refuerzos en log para auditoria de no regresion."
  ],
  "open_questions": [
    "Confirmar guia formal adicional de formato para Economia LDE.",
    "Confirmar nombre definitivo de figura docente en metadatos de portada.",
    "Confirmar politica local de actualizacion anual para unadmSitioWeb.",
    "Supuesto: el nombre canonico del .bib es economia.bib; validar en README final.",
    "Confirmar consignas por actividad para afinar artefactos soportados."
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
        "Economia LDE en semestre 3, bloque 2, obligatoria, 8 creditos.",
        "Carpeta de materia como entrada canonica."
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
      "Convertir planeacion semanal en entregables academicos solidos y verificables.",
      "Asegurar transferencia profesional del analisis juridico en contexto economico."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Secciones argumentativas explicitas.",
      "Uso obligatorio de marca de supuesto cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis critico sustentado en evidencia.",
      "Cierre con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion JSON",
        "Evidencia verificable",
        "Analisis juridico aplicado",
        "Conclusion transferible"
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
          "justification": "La identidad institucional exige trazabilidad y citas verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar ruido no estructurado."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico aplicado",
          "kind": "depends_on",
          "justification": "El analisis valido requiere sustento comprobable."
        },
        {
          "source": "Analisis juridico aplicado",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        }
      ],
      "evidence": [
        "README de Economia: pauta editorial y ubicacion curricular.",
        "programa-analitico-economia.md: proposito y ejes de trabajo.",
        "economia.bib: base institucional local verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion completa de reglas repetidas sin perdida semantica.",
      "Ciclo 10: se refuerza gate de JSON parseable como condicion de propagacion.",
      "Ciclo 10: se estabiliza transferencia transversal en abstractions editoriales."
    ]
  }
}