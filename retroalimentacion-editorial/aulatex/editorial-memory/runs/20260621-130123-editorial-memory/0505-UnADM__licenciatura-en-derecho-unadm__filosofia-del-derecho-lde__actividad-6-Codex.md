{
  "summary": [
    "Se refuerza memoria lateral entre actividades hermanas con union-dedupe sin perdida.",
    "Se conserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se preservan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene tratamiento provisional de fuentes heredadas no verificadas.",
    "Se agrega control local: README y programa analitico contienen token Slug sin resolver [supuesto: pendiente de normalizacion tecnica]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Contextualizar materia como semestre 1, bloque 2, obligatoria, 8 creditos cuando corresponda.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisionales las fuentes heredadas no verificadas hasta confirmacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el tipo de producto a la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones especificas de actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Separar reglas verificadas de supuestos marcados.",
    "Confirmar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Revisar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, editor o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que clean.bib aplica automaticamente a cualquier actividad [supuesto: solo aplica si la consigna coincide].",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no redaccion literal entre hermanos.",
    "Propagar identidad curricular verificada a nodos de la misma asignatura.",
    "Mantener advertencias historicas de salidas no estructuradas cuando exista herencia Codex/GPT-Pro provisional.",
    "Aplicar compresion lossless por union y deduplicacion, sin recorte semantico.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad 6 y producto requerido.",
    "Confirmar rubrica especifica de evaluacion para actividad 6.",
    "Confirmar si actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib de asignatura ante coexistencia de filosofia-del-derecho.bib y clean.bib.",
    "Confirmar si el corpus de interpretacion juridica (clean.bib) es obligatorio o contextual para actividad 6.",
    "Confirmar normalizacion de tokens Slug sin resolver en README y programa analitico."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Sostener argumentacion juridica con evidencia y criterio propio.",
      "Asegurar consistencia editorial institucional entre actividades."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Bloques argumentativos explicitos y ordenados.",
      "Distincion clara entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Presentar marco conceptual y normativo.",
      "Relacionar fuentes con el caso o pregunta.",
      "Desarrollar postura propia fundamentada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [condicional por consigna]",
        "Argumentacion juridica [condicional por consigna]",
        "Normalizacion estructurada previa a propagacion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada previa a propagacion",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita reutilizar salidas no confiables o no parseables."
        },
        {
          "source": "Hermeneutica juridica [condicional por consigna]",
          "target": "Argumentacion juridica [condicional por consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: bloquear propagacion con salida no JSON parseable.",
        "Coexistencia de .bib base y clean.bib: requiere seleccion por consigna."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: refuerzo lateral hermano A1->A6 con deduplicacion lossless.",
      "Se preservaron reglas utiles previas sin eliminaciones.",
      "Se retiraron duplicados literales y se mantuvo equivalencia normativa.",
      "Se marco como condicional el uso de corpus de interpretacion juridica para evitar sobreajuste.",
      "Se mantuvo alerta tecnica por token Slug sin resolver [supuesto hasta validacion local]."
    ]
  }
}