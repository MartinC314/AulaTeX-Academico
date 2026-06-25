{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho y Economia LDE.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa y normalizacion JSON.",
    "Se transfiere solo abstraccion reusable; no se copia redaccion literal ni contenido tematico de Filosofia.",
    "Se refuerza compresion lossless por union-dedupe sin regresion.",
    "Se mantiene alerta historica: hubo salidas no parseables y requieren gate estricto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular local verificado de Economia LDE: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Conservar voz formal, clara y juridicamente precisa.",
    "Marcar como supuesto todo dato no confirmado en consigna o planeacion.",
    "Tratar salidas heredadas de modelos como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos o datos, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional o impacto social."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas; exigir postura argumentada del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir datos economicos, conceptos y argumento juridico aplicado.",
    "No asumir fuentes de otras semanas sin confirmacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema minimo completo antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y economia.bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar."
  ],
  "latex_rules": [
    "Mantener codificacion correcta en español en .tex y .bib.",
    "Conservar plantilla base de reporte/presentacion sin cambios no justificados.",
    "Mantener metadatos academicos completos en portada.",
    "Evitar comandos o paquetes no estandar sin justificacion verificable.",
    "Compilar sin errores criticos, sin referencias rotas y con claves BibTeX estables.",
    "Resolver tokens sin expandir en README y programa analitico."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canonico local de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Agregar solo fuentes realmente consultables y usadas en el entregable.",
    "No inventar referencias ni usar salidas de modelos como bibliografia academica.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL y consulta si aplica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir a nodos laterales solo reglas abstractas estables.",
    "Evitar transferir contenido tematico especifico de Filosofia a Economia.",
    "Mantener estrategia progresiva y conservadora: anexar mejoras verificables sin borrar reglas utiles previas.",
    "Registrar incidencias de parseo como alerta persistente hasta cierre editorial."
  ],
  "open_questions": [
    "Confirmar guia formal adicional de formato para Economia LDE.",
    "Confirmar nombre de figura docente en portada.",
    "Confirmar si README debe mostrar solo economia.bib como nombre canonico.",
    "Validar actualizacion anual de year y fecha de consulta en unadmSitioWeb.",
    "Supuesto: no se recibio consigna de actividad especifica en este salto transversal."
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
        "Carpeta de materia como entrada canonica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y evidencia pertinente.",
      "Analisis propio.",
      "Conclusion juridica transferible.",
      "Trazabilidad editorial verificable."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos.",
      "Asegurar calidad transversal sin perder contexto local.",
      "Sostener continuidad editorial entre nodos no equivalentes."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Secciones argumentativas explicitas.",
      "Uso explicito de supuestos cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis critico sustentado.",
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
          "justification": "La identidad institucional exige forma y cita verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico aplicado",
          "kind": "depends_on",
          "justification": "Sin evidencia, el analisis queda en opinion."
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
          "justification": "La estructura valida permite deduplicar sin perdida."
        }
      ],
      "evidence": [
        "README de Economia: identidad, ubicacion curricular y pauta editorial.",
        "programa-analitico-economia.md: proposito y ejes de trabajo.",
        "economia.bib: base institucional local verificable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se refuerzan gates de parseo y trazabilidad.",
      "Ciclo 6: se conserva ADN argumentativo transversal problema-conceptos-evidencia-analisis-cierre.",
      "Ciclo 6: se evita traslado de contenido doctrinal especifico de Filosofia.",
      "Ciclo 6: se mantiene politica de no regresion y compresion lossless por dedupe."
    ]
  }
}