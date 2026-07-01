{
  "summary": [
    "Se consolida cerebro editorial minimo para Derechos de autor con identidad UnADM.",
    "Se preserva compresion lossless por union y deduplicacion sin regresion.",
    "Se transfiere solo abstraccion estable transversal desde actividad origen.",
    "Se mantiene regla de normalizacion: no propagar salidas no JSON parseable.",
    "Se integra contexto local verificable de README, programa analitico y .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar herencias Codex y GPT-Pro como provisionales hasta verificacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Corregir nombres de archivo corruptos en README antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir fuentes de otras semanas o materias sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar y resolver tokens de plantilla sin expandir en README y programa analitico.",
    "Detectar y corregir campos pendientes como Nombre por definir."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Declarar metadatos antes de cargar plantilla si la plantilla lo exige.",
    "Mover paquetes al preambulo valido y evitar cargas incompletas.",
    "Nunca dejar comandos truncados como usepackage sin argumento.",
    "Compilar sin errores criticos, sin referencias rotas y sin rutas invalidas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y marco juridico aplicable.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Registrar fuentes especificas de actividad en derechos-de-autor.bib."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo reglas estables de identidad, estructura y calidad.",
    "Evitar transferir redaccion literal de actividades no equivalentes.",
    "Mantener normalizacion manual activa en ciclo 1 para herencia provisional.",
    "No propagar datos personales del alumno fuera del nodo local.",
    "Escalar solo cuando JSON y gates de calidad esten validados."
  ],
  "open_questions": [
    "Supuesto: LDE-S5B1 es clave oficial; confirmar contra fuente institucional.",
    "Confirmar nombre de figura docente para reemplazar marcador pendiente.",
    "Confirmar si la ubicacion geografia debe permanecer fija en portada.",
    "Confirmar orden correcto entre template y paquetes en la plantilla local.",
    "Confirmar sustitucion definitiva de tokens Slug por derechos-de-autor.bib."
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
        "README como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Garantizar consistencia editorial y tecnica en LaTeX y bibliografia.",
      "Sostener transferencia profesional del razonamiento juridico."
    ],
    "style_markers": [
      "Frases directas y trazables.",
      "Supuestos explicitamente marcados.",
      "Sin afirmaciones sin fuente.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Consigna -> desarrollo alineado -> verificacion de producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON",
        "Calidad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta local exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El desarrollo parte del problema y culmina en postura argumentada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion juridica debe derivar de fundamentos verificables."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "No se propaga memoria sin estructura parseable."
        }
      ],
      "evidence": [
        "README de Derechos de autor: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib: claves institucionales base existentes."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas manteniendo cobertura completa.",
      "Se conservaron gates institucionales criticos sin recorte.",
      "Se reforzo grafo conceptual transversal sin copiar contenido literal del origen.",
      "Se dejaron vacios locales como preguntas abiertas para validacion posterior."
    ]
  }
}