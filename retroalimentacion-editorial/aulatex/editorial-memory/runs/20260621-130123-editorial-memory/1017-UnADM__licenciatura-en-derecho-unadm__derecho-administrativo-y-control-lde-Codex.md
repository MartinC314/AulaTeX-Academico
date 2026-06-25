{
  "summary": [
    "Se sincroniza memoria transversal hacia la materia sin mover contenido doctrinal especifico de Filosofia del Derecho.",
    "Se preservan reglas institucionales validas y se consolidan por union-dedupe lossless.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, analisis propio, conclusion juridica transferible.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseables.",
    "Se crea cerebro editorial minimo suficiente para destino con vacios locales abiertos."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada, metadatos y formato.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los productos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar encuadre curricular local: semestre 6, bloque 1, obligatoria, 8 creditos."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Mantener consistencia entre README, .tex y .bib.",
    "Corregir placeholders y tokens sin expandir en README y programa analitico."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre consigna, desarrollo y conclusion.",
    "Explicitar tipo de producto antes de desarrollar: reporte, presentacion o visual.",
    "Vincular analisis con control administrativo y aplicacion profesional.",
    "No asumir fuentes de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Verificar que reglas heredadas no contradigan programa analitico local."
  ],
  "latex_rules": [
    "Mantener espanol y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Asegurar coherencia entre \\documenttitle, \\documentsubtitle y actividad real.",
    "Reemplazar 'Actividad X' y 'Nombre por definir' antes de entrega.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en nombres de archivo."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas por actividad en derecho-administrativo-y-control.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar malla curricular local como fuente de ubicacion curricular."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar a nodos transversales solo abstracciones editoriales estables.",
    "No propagar redaccion literal ni doctrina especifica no verificada.",
    "Mantener estrategia progresiva y conservadora sin regresion.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Conservar alertas de calidad institucional en niveles superiores."
  ],
  "open_questions": [
    "Confirmar formato de citacion obligatorio para esta materia.",
    "Confirmar nombre oficial de figura docente en plantilla.",
    "Confirmar convencion final para carpeta/archivo de referencias.",
    "Confirmar si el anio de consulta 2026 del sitio UnADM se mantiene. [supuesto]",
    "Confirmar correccion definitiva de artefactos en README (eporte-, eferencias-). [supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional y conservador ante fuentes no verificadas."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada previa a propagacion.",
        "No invencion de fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derecho administrativo y control."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con rigor juridico y utilidad profesional.",
      "Asegurar trazabilidad entre consigna, argumento y evidencia.",
      "Sostener continuidad editorial institucional entre actividades y materia."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y ordenadas.",
      "Supuestos marcados de forma visible.",
      "Cierre practico obligatorio."
    ],
    "argumentative_patterns": [
      "Problema -> objetivo -> marco -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> criterio propio.",
      "Norma o doctrina -> contraste con caso -> implicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Normalizacion estructurada",
        "Problema juridico",
        "Marco normativo/doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Control administrativo"
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
          "justification": "La identidad institucional exige trazabilidad y rigor de fuentes."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion practica necesita sustento juridico verificable."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar errores de forma y contenido."
        },
        {
          "source": "Control administrativo",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La materia exige aplicacion profesional en gestion y control publico."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "derecho-administrativo-y-control.bib.",
        "Regla institucional heredada: bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: se refuerza transferencia transversal solo de abstracciones estables.",
      "Ciclo 13: se mantiene union-dedupe lossless sin eliminar reglas utiles previas.",
      "Ciclo 13: se preserva gate critico de JSON parseable y normalizacion previa.",
      "Ciclo 13: se evita traslado de contenido doctrinal especifico de Filosofia del Derecho."
    ]
  }
}