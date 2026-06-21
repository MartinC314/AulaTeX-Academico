{
  "summary": [
    "Se consolida memoria lateral A1->A6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantiene regla critica de normalizar antes de propagar.",
    "Se refuerzan ejes estables: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se conserva que fuentes heredadas no verificadas quedan como provisionales.",
    "Se mantiene trazabilidad entre citas en texto y archivo .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Contextualizar con semestre 1, bloque 2, obligatoria, 8 creditos cuando aplique.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Definir objetivo puntual antes del desarrollo."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Supuesto: si la consigna aborda interpretacion juridica, integrar hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar toda respuesta no estructurada antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Validar que la conclusion derive del analisis.",
    "Comprobar trazabilidad minima de afirmaciones a fuente o supuesto.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar codificacion y acentos correctos en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano y editor o URL.",
    "Validar consistencia entre citas del texto y .bib.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones especificas de A1.",
    "Mantener union-dedupe lossless en nodos hermanos.",
    "Preservar advertencias historicas de salidas no parseables en nodos con herencia similar.",
    "Propagar identidad curricular verificada a actividades hermanas.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige formato juridico de citacion adicional a BibTeX.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si se usa filosofia-del-derecho-clean.bib solo para semana de interpretacion juridica.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
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
        "Asignatura Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social bien delimitado.",
      "Base conceptual y normativa pertinente.",
      "Analisis propio sustentado en evidencia.",
      "Cierre juridico transferible.",
      "Normalizacion estructurada antes de toda propagacion."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos.",
      "Asegurar coherencia entre consigna, argumentacion y conclusion.",
      "Sostener calidad institucional y trazabilidad de fuentes."
    ],
    "style_markers": [
      "Inicio breve orientado al problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion clara entre cita y postura propia.",
      "Conclusion con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Presentar marco conceptual y normativo.",
      "Contrastar evidencia y doctrina.",
      "Fijar postura propia fundamentada.",
      "Derivar conclusion juridica aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Conceptos y normas pertinentes",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicional]",
        "Argumentacion juridica [supuesto condicional]",
        "Normalizacion JSON"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
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
          "justification": "El analisis requiere una delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicional]",
          "target": "Argumentacion juridica [supuesto condicional]",
          "kind": "supports",
          "justification": "Si la consigna trata interpretacion, la hermeneutica sustenta la argumentacion."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagacion de memoria ambigua o no verificable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, pauta editorial y ubicacion curricular.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Historial de ciclo: incidencias de salida no parseable y regla de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte de contenido util.",
      "Se conservaron alertas de calidad sobre JSON no parseable.",
      "Se reforzo transferencia lateral por patrones reutilizables y no por texto literal.",
      "Se mantuvieron supuestos explicitamente etiquetados.",
      "Se evitaron fuentes inventadas y se preservo trazabilidad documental."
    ]
  }
}