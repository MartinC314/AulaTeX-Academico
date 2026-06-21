{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio, conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se conserva trazabilidad de fuentes provisionales heredadas y su necesidad de validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular cuando se contextualice la asignatura: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio, cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica aplicable a practica profesional.",
    "Alinear el formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Confirmar que cada afirmacion relevante tenga fuente o etiqueta de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No propagar conclusiones especificas de un hermano a otro."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el archivo bibliografico activo.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo.",
    "Marcar como supuesto cualquier nombre canonico ambiguo hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes nuevas en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; verificar consigna local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables, no redaccion literal.",
    "Conservar alertas historicas de salidas no estructuradas en nodos con herencia Codex o equivalente.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Propagar identidad curricular verificada a actividades hermanas.",
    "No convertir supuestos en hechos al propagar."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si la bibliografia de interpretacion juridica (clean.bib) es obligatoria o solo contextual para Actividad 6."
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
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Normalizacion estructurada antes de propagar."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos y trazables.",
      "Sostener calidad editorial estable entre actividades hermanas.",
      "Preservar memoria util sin perdida y sin invencion."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la fuente.",
      "Cierre con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de teorizar.",
      "Definir conceptos y marco normativo.",
      "Contrastar fuentes verificables.",
      "Tomar postura razonada con evidencia.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion JSON"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho-clean.bib",
        "filosofia-del-derecho.bib"
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
          "justification": "El analisis requiere un objeto de estudio delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del razonamiento expuesto."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "Cuando hay interpretacion normativa, la hermeneutica fundamenta la argumentacion."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "No se propaga memoria sin estructura parseable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Memoria origen: regla persistente de normalizacion antes de propagacion.",
        "Contexto local: coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 38: se refuerza transferencia lateral controlada por patrones, sin copiar conclusiones especificas.",
      "Ciclo 38: se mantiene regla de bloqueo por JSON no parseable.",
      "Ciclo 38: se conserva trazabilidad de supuestos y fuentes provisionales.",
      "Ciclo 38: se depura duplicados semanticos y se preserva contenido valido previo."
    ]
  }
}