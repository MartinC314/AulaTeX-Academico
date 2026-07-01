{
  "summary": [
    "Se sincroniza memoria transversal hacia Economia LDE sin trasladar redaccion literal de Filosofia del Derecho.",
    "Se conserva identidad UnADM, estructura por ejes y control de calidad de parseo y trazabilidad.",
    "Se deduplican reglas repetidas y se refuerza compresion lossless por union-dedupe sin regresion.",
    "Se crea cerebro editorial minimo del destino con vacios locales abiertos y marcados como supuesto."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y metadatos.",
    "Usar contexto curricular verificado de Economia LDE: semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Conservar voz academica formal, clara y juridicamente precisa.",
    "Marcar como supuesto todo dato no confirmado por consigna o planeacion oficial.",
    "Tratar salidas heredadas no verificadas de modelos como provisionales, no como fuente academica.",
    "Usar la carpeta de materia como entrada canonica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos o datos pertinentes, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el producto a la planeacion semanal y al tipo solicitado.",
    "Cerrar con conclusion juridica transferible a practica profesional o impacto social."
  ],
  "activity_rules": [
    "Adaptar cada entrega al formato pedido: reporte, presentacion o producto visual.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir conceptos economicos, datos empiricos y argumentos juridicos.",
    "No inventar hechos, normas ni referencias."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Bloquear si hay campos criticos vacios sin marca de supuesto.",
    "Verificar correspondencia del producto con la consigna vigente."
  ],
  "latex_rules": [
    "Conservar plantilla base de reporte-economia.tex como referencia.",
    "Mantener metadatos academicos completos en portada.",
    "Usar espanol y letterpaper salvo instruccion oficial distinta.",
    "Mantener estilo de citacion consistente con setcitestyle definido.",
    "Evitar paquetes o comandos no estandar sin justificacion verificable.",
    "Compilar sin errores criticos, sin referencias rotas y con rutas limpias.",
    "Resolver tokens sin expandir en README o programa analitico antes de publicar."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio local canonico de la materia.",
    "Priorizar fuentes institucionales UnADM y documentos oficiales verificables.",
    "Agregar al .bib solo referencias realmente usadas en el producto.",
    "No inventar referencias ni usar salidas de modelos como bibliografia.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Registrar fecha de consulta en recursos web cuando aplique."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar datos tematicos especificos de Filosofia del Derecho a Economia.",
    "Mantener estrategia progresiva y conservadora: anexar mejoras verificables sin borrar reglas utiles previas.",
    "Aplicar union-dedupe en cada ciclo para compresion lossless.",
    "Mantener alerta de normalizacion manual mientras existan antecedentes de salida no parseable."
  ],
  "open_questions": [
    "Confirmar nombre oficial de figura docente para portada.",
    "Confirmar si existe rubrica especifica por actividad en Economia LDE.",
    "Confirmar periodicidad de actualizacion de year y fecha de consulta de unadmSitioWeb.",
    "Supuesto: economia.bib es el nombre canonico final y unico del archivo bibliografico local.",
    "Confirmar si el README debe corregir artefactos de tokens y saltos de linea rotos."
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
        "Carpeta de materia como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Economia LDE en semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos con fundamento, evidencia y utilidad profesional.",
      "Sostener consistencia editorial institucional entre actividades y materias."
    ],
    "style_markers": [
      "Enunciados breves y verificables.",
      "Supuestos explicitados cuando falte contexto.",
      "Separacion clara entre descripcion, analisis y conclusion."
    ],
    "argumentative_patterns": [
      "Del problema al concepto, del concepto a la evidencia, de la evidencia al analisis propio, del analisis al cierre juridico.",
      "Afirmacion respaldada por fuente verificable y cita trazable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Trazabilidad de fuentes",
        "Problema juridico-social",
        "Analisis propio",
        "Conclusion transferible",
        "Economia LDE",
        "Planeacion semanal"
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
          "justification": "La identidad institucional exige evidencia verificable y formato consistente."
        },
        {
          "source": "Planeacion semanal",
          "target": "Producto alineado",
          "kind": "depends_on",
          "justification": "El tipo de entrega se define por consigna semanal."
        },
        {
          "source": "Problema juridico-social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de un problema concreto y no de resumen generico."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica valida deriva de argumentacion propia y evidencia."
        }
      ],
      "evidence": [
        "README de Economia LDE: pauta editorial institucional y ubicacion curricular.",
        "programa-analitico-economia.md: proposito y ejes de trabajo.",
        "economia.bib: fuentes base institucionales existentes."
      ]
    },
    "reinforcement_log": [
      "Se conservaron gates de parseo JSON y normalizacion previa.",
      "Se consolido patron estructural reusable problema-conceptos-evidencia-analisis-cierre.",
      "Se evito transferencia de contenido tematico especifico de Filosofia del Derecho.",
      "Se reforzo uso canonico de economia.bib y no invencion de fuentes.",
      "Se marcaron supuestos de contexto local pendiente."
    ]
  }
}