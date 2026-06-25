{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM, ubicacion curricular y pauta editorial institucional.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: no propagar salidas no estructuradas y bloquear JSON no parseable.",
    "Se mantiene separacion entre reglas confirmadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Contextualizar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir conclusiones especificas de Actividad 1 a Actividad 6.",
    "No transferir bibliografia exclusiva del hermano sin validacion local.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Separar reglas verificadas de supuestos editoriales.",
    "Validar coherencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Revisar que la conclusion derive del analisis."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: nombre canonico esperado del .bib por Slug es filosofia-del-derecho.bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que clean.bib aplica automaticamente a Actividad 6 sin consigna.",
    "Marcar como supuesto todo dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura, calidad y conceptos recurrentes.",
    "Evitar copiar redaccion literal entre hermanos.",
    "Evitar copiar conclusiones especificas entre hermanos.",
    "Conservar advertencia historica sobre salidas no estructuradas en ciclos previos.",
    "Aplicar normalizacion manual cuando aparezca memoria no parseable."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si el producto principal es reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si Actividad 6 requiere corpus de interpretacion juridica de clean.bib o bibliografia distinta.",
    "Confirmar si existe formato de citacion juridica adicional a BibTeX institucional."
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
      "Producto segun planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Sostener continuidad editorial entre actividades sin perder especificidad local."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Tomar postura fundamentada.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
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
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere problema delimitado."
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
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo.",
        "Memoria origen confirma regla de normalizacion previa a propagacion.",
        "Contexto local muestra token Slug sin resolver para nombre .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se preservan reglas utiles previas sin recorte.",
      "Ciclo 3: se deduplican variantes semanticas repetidas.",
      "Ciclo 3: se refuerza transferencia lateral por patrones, sin copiar contenido especifico.",
      "Ciclo 3: se mantienen supuestos abiertos donde faltan datos locales."
    ]
  }
}