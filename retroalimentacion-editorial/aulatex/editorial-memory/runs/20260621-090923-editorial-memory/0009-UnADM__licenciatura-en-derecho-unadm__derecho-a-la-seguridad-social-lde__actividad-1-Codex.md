{
  "summary": [
    "Se consolida memoria lateral con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM con contexto local verificado en README y programa analitico.",
    "Se mantiene secuencia editorial estable: problema, fundamento, analisis, evidencia, postura y cierre profesional.",
    "Se refuerza control de calidad: bloquear JSON invalido y normalizar salidas no estructuradas.",
    "Se aplica compresion lossless por deduplicacion sin recorte de reglas utiles previas.",
    "Se evita copiar contenido tematico exclusivo, redaccion literal o conclusiones del nodo hermano."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y juridicamente preciso.",
    "Vincular toda actividad a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Usar la carpeta de asignatura como entrada canonica editorial.",
    "Basar ubicacion curricular en semestre 2, bloque 1, obligatoria, 8 creditos.",
    "Usar README y programa analitico locales como fuentes primarias de identidad.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato y alcance al producto pedido en la consigna semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Adaptar salida a reporte, presentacion o formato mixto solo si la consigna lo permite."
  ],
  "activity_rules": [
    "Sustentar cada afirmacion con fuente verificable y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Evitar entregas de resumen sin analisis juridico propio.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Confirmar correspondencia exacta del entregable con Actividad 1 local.",
    "No asumir fuentes de otras semanas sin validar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar ajuste del producto a la consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres canonicos de archivos segun README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canonica local.",
    "Corregir rutas o caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes especificas de actividad en el .bib local.",
    "Distinguir bibliografia base y bibliografia especifica de actividad.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente editorial o URL.",
    "Usar cpeum2026, lss2026 y lissste2026 solo cuando la consigna los requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad y patrones argumentativos.",
    "Aplicar analogia controlada: primero identidad y calidad; luego estructura y conceptos.",
    "No copiar redaccion literal, conclusiones ni bibliografia exclusiva entre hermanos.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables sin regresion.",
    "Si faltan datos locales, propagar plantilla base y abrir preguntas, sin inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si el formato requerido es reporte, presentacion o mixto.",
    "Confirmar rubrica especifica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana en planeacion local.",
    "Confirmar si la actividad exige jurisprudencia especifica."
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
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Fundamento constitucional y legal verificable.",
      "Analisis propio con postura argumentada.",
      "Evidencia trazable en citas y .bib.",
      "Cierre profesional transferible a practica juridica."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto juridico verificable.",
      "Asegurar coherencia entre identidad institucional, metodo y evidencia.",
      "Evitar regresiones editoriales en propagacion lateral recursiva."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Marcado explicito de supuestos.",
      "Conclusiones no descriptivas."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> analisis -> evidencia -> conclusion.",
      "Regla general -> contraste con contexto -> postura -> implicacion practica.",
      "Pregunta guia -> criterios juridicos -> inferencia razonada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho a la seguridad social",
        "Marco constitucional en Mexico",
        "Ley del Seguro Social",
        "Ley del ISSSTE",
        "Universalidad",
        "Progresividad",
        "Igualdad y no discriminacion",
        "Acceso, cobertura y justiciabilidad",
        "Control editorial por JSON estructurado"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Marco constitucional en Mexico",
          "target": "Derecho a la seguridad social",
          "kind": "supports",
          "justification": "Define el fundamento juridico primario del derecho."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Concreta prestaciones y regimen aplicable."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula cobertura para trabajadores del Estado."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar alcance real y barreras de acceso."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite medir avances y evitar retrocesos."
        },
        {
          "source": "Control editorial por JSON estructurado",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay transferencia confiable."
        }
      ],
      "evidence": [
        "README local de Derecho a la Seguridad Social.",
        "Programa analitico local de la asignatura.",
        "Archivo derecho-a-la-seguridad-social.bib con claves verificables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicacion completa de reglas repetidas en identidad, estructura, actividad y calidad.",
      "Ciclo 9: mantenimiento de regla dura de bloqueo por JSON invalido.",
      "Ciclo 9: refuerzo lateral por analogia controlada sin arrastre tematico exclusivo de Filosofia del Derecho.",
      "Ciclo 9: conservacion de bibliografia local canonica y control de supuestos."
    ]
  }
}