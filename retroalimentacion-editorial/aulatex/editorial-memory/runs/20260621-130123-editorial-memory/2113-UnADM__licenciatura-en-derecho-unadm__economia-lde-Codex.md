{
  "summary": [
    "Se consolida cerebro editorial minimo para Economia LDE con identidad UnADM.",
    "Se preservan reglas estables transversales: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene politica de normalizacion JSON obligatoria antes de propagacion.",
    "Se aplica compresion lossless por union-dedupe sin recorte.",
    "Se corrigen artefactos de plantilla detectados en README como incidencia tecnica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular local verificado: Licenciatura en Derecho, semestre 3, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en consigna o planeacion.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificacion local.",
    "No usar salidas de modelos como fuente academica."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar cada actividad al entregable solicitado: reporte, presentacion o producto visual.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir datos economicos, conceptos y argumento juridico aplicado."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y economia.bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas."
  ],
  "latex_rules": [
    "Mantener plantilla base de reporte-economia.tex como referencia.",
    "Conservar metadatos completos en portada: alumno, matricula, figura docente, semestre, bloque, tipo, creditos.",
    "Mantener estilo de citacion authoryear consistente.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Mantener espanol y letterpaper salvo instruccion oficial distinta."
  ],
  "bibliography_rules": [
    "Usar economia.bib como repositorio canonico local.",
    "Priorizar fuentes institucionales UnADM y documentos juridicos verificables.",
    "Agregar en .bib solo fuentes realmente usadas en cada actividad.",
    "No inventar referencias; conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Registrar fecha de consulta en recursos web cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones estables, no redaccion literal.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferir detalles propios de Filosofia del Derecho no requeridos por Economia.",
    "Mantener estrategia progresiva y conservadora: anexar mejoras verificables sin regresion.",
    "Si falta consigna local, propagar solo reglas generales y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar planeacion oficial de actividades de Economia para ajustar tipos de producto.",
    "Confirmar nombre de figura docente para metadatos finales.",
    "Confirmar si existe guia formal adicional de formato para Economia LDE.",
    "Supuesto: economia.bib es el archivo canonico definitivo; validar en README corregido.",
    "Supuesto: incidencias de tokens en README provienen de plantilla y no de version final aprobada."
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
        "Economia LDE: semestre 3, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar trazabilidad entre afirmaciones, fuentes y conclusion juridica."
    ],
    "style_markers": [
      "Frases claras y directas.",
      "Separacion explicita de secciones argumentativas.",
      "Uso explicito de supuestos cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo pertinente.",
      "Analisis critico propio con evidencia.",
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
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Analisis juridico aplicado",
          "kind": "depends_on",
          "justification": "El analisis no debe quedar en opinion sin respaldo."
        },
        {
          "source": "Analisis juridico aplicado",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion transversal",
          "kind": "supports",
          "justification": "Evita heredar ruido no estructurado."
        }
      ],
      "evidence": [
        "README de Economia: identidad UnADM, ubicacion curricular y pauta editorial.",
        "programa-analitico-economia.md: proposito y cinco ejes de trabajo.",
        "economia.bib: base institucional local verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas con variantes ortograficas.",
      "Se conservaron reglas utiles previas sin eliminacion regresiva.",
      "Se reforzo gate de JSON parseable por historial de salidas no estructuradas.",
      "Se agrego incidencia tecnica de tokens sin expandir como mejora verificable.",
      "Se mantuvo separacion entre reglas estables y contexto local pendiente."
    ]
  }
}