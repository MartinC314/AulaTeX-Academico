{
  "summary": [
    "Se sincroniza memoria transversal hacia la materia destino sin mover contenido doctrinal especifico de Filosofia del Derecho.",
    "Se conserva compresion lossless por union-dedupe y sin regresion editorial.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar nada sin JSON parseable y estructura minima valida.",
    "Se prioriza identidad UnADM, trazabilidad de fuentes y marcado explicito de supuestos."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, metadatos y formato.",
    "Usar nombre exacto de materia: Derecho administrativo y control.",
    "Conservar enfoque de Licenciatura en Derecho en todos los entregables.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como [supuesto] cualquier dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Mantener encuadre curricular local: semestre 6, bloque 1, obligatoria, 8 creditos."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener consistencia entre README, programa analitico, .tex y .bib.",
    "Corregir placeholders y tokens sin expandir en README y programa. [supuesto]"
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar solo descripcion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Explicitar tipo de producto antes de desarrollar: reporte, presentacion o visual.",
    "Vincular el analisis con control administrativo y aplicacion profesional.",
    "No asumir bibliografia de otras semanas o materias sin validacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Detener si hay campos criticos vacios o respuesta no estructurada.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca [supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib local.",
    "Revisar que reglas heredadas no contradigan el programa analitico local."
  ],
  "latex_rules": [
    "Mantener espanol y codificacion correcta en .tex y .bib.",
    "Conservar formato letterpaper segun plantilla local.",
    "Completar metadatos institucionales antes de compilar.",
    "Reemplazar Actividad X por numero y nombre real.",
    "Sustituir Nombre por definir por figura docente oficial.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, sin referencias ni citas rotas."
  ],
  "bibliography_rules": [
    "Registrar fuentes de actividad en derecho-administrativo-y-control.bib.",
    "Priorizar fuentes institucionales UnADM y normativas verificables.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener trazabilidad entre afirmaciones y soporte bibliografico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Compartir a nodos transversales solo abstracciones editoriales estables.",
    "No propagar redaccion literal ni contenido doctrinal no verificado.",
    "Preservar reglas utiles previas y agregar solo mejoras verificables.",
    "Aplicar estrategia progresiva y conservadora en cada fusion."
  ],
  "open_questions": [
    "Confirmar rubrica de evaluacion especifica de la materia para ajustar profundidad argumentativa.",
    "Confirmar convencion final del archivo de referencias y carpetas auxiliares.",
    "Confirmar si los tokens PowerShell en README/programa son artefactos a corregir. [supuesto]",
    "Confirmar nombre oficial de figura docente en plantilla.",
    "Confirmar vigencia del anio de consulta del sitio UnADM en .bib."
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
        "Normalizacion estructurada antes de propagacion."
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
      "Convertir la planeacion semanal en productos academicos con rigor juridico y utilidad profesional.",
      "Asegurar coherencia entre identidad institucional, estructura argumentativa y trazabilidad de fuentes."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Objetivo explicito.",
      "Secciones funcionales y no decorativas.",
      "Marcado visible de supuestos.",
      "Cierre con criterio aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> evidencia -> analisis propio -> conclusion.",
      "Afirmacion -> cita verificable -> interpretacion juridica -> implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion estructurada",
        "Integridad academica",
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
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay reutilizacion segura."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La identidad institucional exige trazabilidad y rigor."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere problema delimitado."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusion transferible",
          "kind": "supports",
          "justification": "La conclusion practica necesita sustento juridico."
        },
        {
          "source": "Control administrativo",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La materia orienta aplicacion profesional en administracion y control."
        }
      ],
      "evidence": [
        "README local con pauta editorial y ubicacion curricular.",
        "Programa analitico local con proposito y ejes de trabajo.",
        "Archivo derecho-administrativo-y-control.bib con fuentes institucionales base."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: deduplicacion completa de reglas repetidas en origen y destino.",
      "Ciclo 3: transferencia limitada a abstracciones estables por relacion transversal.",
      "Ciclo 3: se preservan alertas por salidas no estructuradas (Codex/GPT-Pro) como provisionales.",
      "Ciclo 3: no se transfiere doctrina especifica de Filosofia del Derecho al destino."
    ]
  }
}