{
  "summary": [
    "Se consolida refuerzo lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales nucleares: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se conserva regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se refuerza control de supuestos cuando falte consigna local de Actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Cuando la tarea sea de memoria editorial, responder en JSON valido y sin claves extra."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas o doctrina con el problema delimitado.",
    "Supuesto: si la consigna aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que cada afirmacion relevante tenga respaldo o marca de supuesto.",
    "Separar reglas confirmadas de supuestos editoriales.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No propagar conclusiones especificas de un hermano a otro."
  ],
  "latex_rules": [
    "Usar codificacion correcta en español en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en archivos .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con caracteres anómalos antes de referenciarlos."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y material juridico verificable.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir automaticamente que filosofia-del-derecho-clean.bib aplica a toda actividad.",
    "Marcar como supuesto cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales.",
    "Evitar copiar redaccion literal, conclusiones puntuales o bibliografia exclusiva entre hermanos.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Conservar advertencias historicas sobre salidas no estructuradas en memorias de baja confianza.",
    "Si faltan datos locales, propagar plantilla base y abrir preguntas en lugar de inventar."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual exacta de Actividad 6; confirmar producto requerido.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige formato adicional de citacion juridica aparte de BibTeX.",
    "Confirmar nombre canonico final del .bib por coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib son obligatorias o solo contextuales para Actividad 6."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Marco conceptual, normativo y doctrinal pertinente.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos consistentes.",
      "Sostener decisiones argumentativas con evidencia verificable.",
      "Formar criterio juridico aplicable a practica profesional."
    ],
    "style_markers": [
      "Apertura con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion clara entre fuente y postura propia.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer marco conceptual-normativo.",
      "Contrastar fuentes relevantes.",
      "Tomar postura fundamentada.",
      "Concluir con implicacion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis valido requiere problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado por consigna]",
          "target": "Argumentacion juridica [supuesto condicionado por consigna]",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "Pauta editorial del README: identidad, integridad y conclusion juridica propia.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Regla historica consolidada: normalizar salidas no estructuradas antes de propagar.",
        "Coexistencia de .bib local y clean.bib; uso condicionado por consigna de actividad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 12: deduplicacion de reglas repetidas y preservacion de reglas utiles previas.",
      "Ciclo 12: refuerzo lateral de patrones transferibles sin copiar conclusiones especificas de Actividad 1.",
      "Ciclo 12: mantenimiento de compuertas de calidad JSON y trazabilidad bibliografica.",
      "Ciclo 12: se mantienen supuestos explicitos donde falta dato local verificable."
    ]
  }
}