{
  "summary": [
    "Se mantiene memoria editorial de Actividad 6 con union-dedupe lossless.",
    "Se refuerza identidad UnADM y ubicacion curricular verificada.",
    "Se preserva regla critica de normalizar antes de propagar.",
    "Se transfieren solo patrones reutilizables desde actividad hermana.",
    "Se evita copiar conclusiones o bibliografia exclusiva de Actividad 1.",
    "Se conserva el marco de cinco ejes del programa analitico.",
    "Supuesto: la consigna local de Actividad 6 no esta visible completa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho y Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Estructurar actividad en: problema, conceptos o marco normativo, desarrollo del producto, analisis propio y conclusion.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Delimitar problema juridico o social desde el inicio.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la actividad aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar que no haya contenido no estructurado reutilizado sin normalizacion.",
    "Separar reglas verificadas de supuestos marcados.",
    "Verificar trazabilidad de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Usar acentos y codificacion correcta en español.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base y bibliografia especifica de actividad.",
    "No asumir que clean.bib aplica automaticamente a toda actividad.",
    "Marcar como supuesto datos bibliograficos incompletos hasta verificarlos."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar union-dedupe lossless en nodos hermanos.",
    "Transferir solo patrones generales: identidad, estructura, calidad, conceptos recurrentes.",
    "No propagar redaccion literal ni conclusiones especificas entre hermanos.",
    "Mantener alerta historica de salidas no parseables en cadenas con herencia provisional.",
    "Si falta consigna local, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 6.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si el producto principal es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib de asignatura por token Slug sin resolver.",
    "Confirmar si fuentes de interpretacion juridica de clean.bib son obligatorias en Actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX."
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
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a practica juridica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Garantizar trazabilidad entre problema, evidencia, analisis y cierre.",
      "Sostener coherencia institucional y tecnica en todo nodo de actividad."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma explicita."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Relacionar evidencia con el caso o pregunta.",
      "Tomar postura fundamentada.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado por consigna]"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis juridico valido."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento y evidencia."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado]",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Aplica cuando la actividad trate interpretacion juridica."
        }
      ],
      "evidence": [
        "README: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: no propagar contenido no estructurado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 56: deduplicacion de reglas repetidas y normalizacion semantica.",
      "Ciclo 56: preservada regla de bloqueo por JSON no parseable.",
      "Ciclo 56: reforzada separacion entre hechos verificados y supuestos.",
      "Ciclo 56: transferencia lateral limitada a patrones reutilizables."
    ]
  }
}