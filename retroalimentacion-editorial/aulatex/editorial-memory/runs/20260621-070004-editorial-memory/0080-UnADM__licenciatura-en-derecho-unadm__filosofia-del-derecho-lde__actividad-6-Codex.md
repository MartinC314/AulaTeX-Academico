{
  "summary": [
    "Consolidacion lateral aplicada desde actividad 1 a actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se conserva trazabilidad de fuentes provisionales y se exige marcarlas como supuesto cuando falte verificacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Contextualizar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Conservar regla de no regresion en consolidaciones editoriales."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado en planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas o doctrina con el problema delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Revisar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Separar reglas confirmadas de supuestos editoriales.",
    "Validar correspondencia entre producto y consigna de actividad 6.",
    "Revisar que conclusion derive del analisis y no sea decorativa.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en espanol en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Mantener compatibilidad .tex-.bib para evitar compilaciones rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomales antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Marcar como supuesto datos bibliograficos incompletos hasta verificacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones especificas de un hermano.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Conservar advertencias historicas sobre salidas no estructuradas.",
    "No propagar supuestos como hechos confirmados.",
    "Si falta consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 6; confirmar producto exacto.",
    "Confirmar rubrica especifica de evaluacion para actividad 6.",
    "Confirmar si actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si bibliografia de interpretacion juridica aplica formalmente a actividad 6.",
    "Confirmar si se exige formato juridico adicional a BibTeX institucional."
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
      "Problema juridico bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio diferenciable.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Garantizar consistencia editorial entre actividades hermanas.",
      "Preservar memoria util sin perdida por deduplicacion controlada."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones claras y ordenadas.",
      "Citas trazables.",
      "Postura personal argumentada.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes.",
      "Tomar postura fundamentada.",
      "Derivar conclusion del desarrollo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual y normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion de salidas"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
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
          "justification": "La conclusion valida deriva del razonamiento desarrollado."
        },
        {
          "source": "Normalizacion de salidas",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagar errores estructurales y mantiene trazabilidad."
        }
      ],
      "evidence": [
        "README: identidad institucional, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Historial: salidas no JSON parseable requieren bloqueo y normalizacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recortar contenido util.",
      "Se reforzo regla de normalizacion previa a propagacion recursiva.",
      "Se mantuvo separacion entre hechos confirmados y supuestos.",
      "Se evitaron traslados de conclusiones especificas desde actividad hermana."
    ]
  }
}