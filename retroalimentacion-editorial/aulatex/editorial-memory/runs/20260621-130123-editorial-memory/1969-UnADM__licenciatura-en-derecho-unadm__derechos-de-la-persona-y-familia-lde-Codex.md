{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia de Derechos de la persona y familia sin arrastrar contenido tematico no equivalente.",
    "Se conserva el nucleo editorial estable: problema, conceptos y normas, evidencia, analisis propio y conclusion juridica transferible.",
    "Se refuerza gate critico de normalizacion: no propagar salidas no estructuradas ni no-JSON.",
    "Se mantiene identidad institucional UnADM y contexto curricular local del destino.",
    "Se consolida correccion de placeholders y rutas corruptas en README y programa analitico como requisito operativo."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada, metadatos y formato.",
    "Usar nombre canonico de asignatura: Derechos de la persona y familia.",
    "Alinear productos a Licenciatura en Derecho, semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no confirmado por consigna o documento local.",
    "No modificar datos de alumno o matricula sin verificacion local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion.",
    "Alinear el producto final a la planeacion semanal o rubrica vigente.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "activity_rules": [
    "Identificar consigna, rubrica y producto solicitado antes de redactar.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Evitar texto generico; conectar argumentos con el problema juridico concreto.",
    "No transferir contenido tematico de otra materia sin validar pertinencia. [supuesto]",
    "Registrar vacios de contexto como preguntas abiertas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura minima completa del esquema de memoria antes de guardar.",
    "Exigir respaldo verificable o marca [supuesto] en afirmaciones no confirmadas.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia entre consigna, producto y estructura de entrega.",
    "Corregir placeholders de slug y nombres de archivo corruptos antes de compilar."
  ],
  "latex_rules": [
    "Mantener documentclass article en espanol, letterpaper y oneside salvo consigna distinta.",
    "Completar metadatos institucionales y academicos antes de redactar contenido.",
    "Usar espanol academico con terminologia juridica consistente.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin expandir.",
    "Resolver placeholders tipo $(@{...}.Slug) en README, programa analitico y referencias.",
    "Verificar rutas y nombres canonicos de archivos .tex y .bib antes de compilar."
  ],
  "bibliography_rules": [
    "Usar derechos-de-la-persona-y-familia.bib como archivo canonico local.",
    "Priorizar fuentes institucionales UnADM y normas juridicas verificables.",
    "Agregar solo referencias consultables y pertinentes a cada actividad.",
    "No inventar referencias; marcar faltantes como pendiente.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y gates de calidad.",
    "Transferir solo abstracciones estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual sobre redaccion literal.",
    "Evitar regresiones: conservar reglas utiles previas y deduplicar sin recorte semantico.",
    "Si reaparecen salidas no estructuradas, forzar normalizacion manual antes de propagar."
  ],
  "open_questions": [
    "Confirmar si el dato de figura docente ya es definitivo. [supuesto]",
    "Confirmar vigencia de nombre de alumno y matricula en plantilla local. [supuesto]",
    "Confirmar si el codigo LDE-S3B1 es obligatorio en todos los productos.",
    "Confirmar si existe formato institucional obligatorio adicional para presentaciones.",
    "Validar correccion definitiva de rutas corruptas en README (reporte y referencias).",
    "Validar sustitucion definitiva del placeholder de .bib en README y programa analitico."
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
        "Entrada canonica desde carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 3, bloque 1, obligatoria seriada, 8 creditos.",
        "Asignatura: Derechos de la persona y familia."
      ]
    },
    "essence": [
      "Problema juridico o social como detonante.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable con citas trazables.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos juridicos claros, sustentados y aplicables.",
      "Asegurar consistencia editorial, tecnica y bibliografica en toda entrega."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Separacion clara entre marco conceptual y postura propia.",
      "Etiquetado explicito de [supuesto] en datos no confirmados.",
      "Coherencia entre consigna, desarrollo y cierre."
    ],
    "argumentative_patterns": [
      "Problematizar primero.",
      "Fundamentar con norma, doctrina o fuente verificable.",
      "Analizar con criterio propio.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Integridad de evidencia y citas",
        "Estructura argumentativa juridica",
        "Consistencia tecnica LaTeX-BibTeX",
        "Conclusion juridica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida estructurada no hay reutilizacion segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "El marco institucional define tono, formato y exigencia academica."
        },
        {
          "source": "Integridad de evidencia y citas",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La validez de la conclusion depende de sustento verificable."
        },
        {
          "source": "Consistencia tecnica LaTeX-BibTeX",
          "target": "Integridad de evidencia y citas",
          "kind": "supports",
          "justification": "Evita referencias rotas y perdida de trazabilidad."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia problema-fundamento-analisis produce cierre aplicable."
        }
      ],
      "evidence": [
        "README local de la materia destino.",
        "Programa analitico local de la materia destino.",
        "Archivo derechos-de-la-persona-y-familia.bib.",
        "Regla estable heredada: bloquear no-JSON y normalizar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion lossless aplicada sin eliminar reglas utiles previas.",
      "Ciclo 9: se transfiere solo abstraccion estable transversal, no contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 9: se refuerzan gates de calidad, consistencia tecnica y trazabilidad de evidencia."
    ]
  }
}