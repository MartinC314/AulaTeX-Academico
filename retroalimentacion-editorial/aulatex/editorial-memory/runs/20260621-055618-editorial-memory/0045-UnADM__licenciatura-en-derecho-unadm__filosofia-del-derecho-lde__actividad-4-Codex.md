{
  "summary": [
    "Se refuerza memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y pauta editorial comun de Filosofia del Derecho.",
    "Se mantiene gate critico: no propagar si JSON no es parseable ni estructura minima completa.",
    "Se transfieren solo patrones reutilizables desde Actividad 1: estructura, calidad, trazabilidad y metodo argumentativo.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible; se conserva plantilla base verificable."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Vincular contexto curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Incluir problema, conceptos, evidencia y analisis propio de forma explicita.",
    "Sustentar afirmaciones con fuente verificable y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 4.",
    "Adaptar solo patrones metodologicos reutilizables al tema local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar respuestas heredadas no estructuradas y normalizar antes de uso.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Verificar consistencia entre citas en texto y archivo .bib.",
    "Validar correspondencia entre producto entregado y consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "Mantener claves BibTeX estables para no romper compilacion.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias rotas y sin tokens sin resolver.",
    "Resolver plantillas tipo $(@{...}.Slug) en nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en .bib solo fuentes consultables y pertinentes a la actividad local.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece de Semana 7; confirmar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar union-dedupe para compresion lossless y evitar regresiones.",
    "Reforzar reglas institucionales comunes y no copiar redaccion literal entre hermanos.",
    "Transferir patrones, no contenido tematico cerrado ni bibliografia exclusiva.",
    "Mantener banderas de normalizacion manual para ciclos con historial no parseable."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extension y criterios.",
    "Confirmar rubrica docente especifica para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del archivo .bib segun slug resuelto.",
    "Confirmar si Actividad 4 requiere .bib propio o reutiliza uno existente.",
    "Confirmar si los titulos y fuentes periodisticas actuales son obligatorias o solo contextuales."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro.",
        "Juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1.",
        "Bloque 2.",
        "Obligatoria.",
        "8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en producto academico verificable.",
      "Asegurar fundamento juridico y evidencia trazable.",
      "Formar criterio propio con cierre profesional aplicable."
    ],
    "style_markers": [
      "Definir objetivo antes del desarrollo.",
      "Mantener separacion funcional por secciones.",
      "Citar cada afirmacion sustantiva.",
      "Marcar supuestos de forma explicita.",
      "Evitar inflar contenido sin respaldo."
    ],
    "argumentative_patterns": [
      "Plantear problema inicial.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Fijar postura razonada.",
      "Cerrar con conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion",
        "Ejes editoriales de Filosofia del Derecho"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta institucional exige trazabilidad de fuentes y tono academico."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "La propagacion segura requiere formato parseable y completo."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Relacion problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan la argumentacion desde planteamiento hasta cierre juridico."
        }
      ],
      "evidence": [
        "README define entrada canonica y pauta editorial.",
        "Programa analitico define cinco ejes de trabajo.",
        "Historial de ciclos reporta salidas no parseables; se mantiene gate estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 45: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 45: preservadas reglas utiles previas sin eliminacion regresiva.",
      "Ciclo 45: agregado control de transferencia entre hermanos para evitar copia literal.",
      "Ciclo 45: mantenidas preguntas abiertas donde faltan datos locales."
    ]
  }
}