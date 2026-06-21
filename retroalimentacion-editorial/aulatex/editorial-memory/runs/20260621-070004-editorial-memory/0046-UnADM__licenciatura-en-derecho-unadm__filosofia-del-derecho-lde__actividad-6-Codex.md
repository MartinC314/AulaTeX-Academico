{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se refuerza control de supuestos cuando no exista consigna local visible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea sea de consolidacion de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir actividad con encuadre breve del problema juridico o social.",
    "Separar bloques en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por planeacion semanal.",
    "Cerrar con conclusion juridica derivada del analisis."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si Actividad 6 aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Confirmar trazabilidad minima de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre canonico esperado de .bib es filosofia-del-derecho.bib por Slug visible."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Marcar como supuesto cualquier dato bibliografico incompleto hasta verificarlo.",
    "No asumir que filosofia-del-derecho-clean.bib aplica automaticamente a toda actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones ni bibliografia exclusiva de hermano.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Mantener advertencia historica de salidas no parseables en nodos con herencia provisional.",
    "Aplicar union-dedupe lossless en ciclos siguientes.",
    "Si falta consigna local, propagar estructura base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib por coexistencia de archivo base y clean.",
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
      "Uso de conceptos, normas y doctrina pertinentes.",
      "Producto alineado a la planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a la practica."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos verificables.",
      "Sostener escritura juridica con evidencia y criterio propio.",
      "Garantizar continuidad editorial entre actividades hermanas sin perder control de calidad."
    ],
    "style_markers": [
      "Inicio breve con problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con trazabilidad.",
      "Postura propia diferenciada de la fuente.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de teorizar.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes y seleccionar criterio.",
      "Desarrollar postura propia fundamentada.",
      "Derivar conclusion del analisis, no decorativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual y normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion de salida estructurada"
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
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "Cuando hay interpretacion normativa, la hermeneutica sustenta la argumentacion."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura valida evita propagar errores y mantiene trazabilidad."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Historial de ciclos: existencia de salidas no parseables y necesidad de normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 46: se refuerza transferencia lateral por patrones reutilizables, sin copiar contenido especifico de Actividad 1.",
      "Ciclo 46: se mantiene politica lossless por union-dedupe y no regresion.",
      "Ciclo 46: se preservan reglas de calidad, LaTeX y bibliografia con control explicito de supuestos."
    ]
  }
}