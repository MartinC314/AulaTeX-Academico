{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM y ubicacion curricular verificada de la asignatura.",
    "Se mantienen ejes editoriales base: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se refuerza regla de normalizacion: no propagar salidas no estructuradas.",
    "Se conserva compresion lossless por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Vincular actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Diferenciar sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de Actividad 1 a Actividad 6.",
    "Si la consigna lo exige, transformar salida a reporte o presentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Confirmar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: nombre canonico esperado del .bib es filosofia-del-derecho.bib hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que clean.bib aplica a toda actividad sin confirmacion de consigna.",
    "Marcar como supuesto cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre hermanos.",
    "Evitar copiar redaccion literal, conclusiones o bibliografia exclusiva de otro hermano.",
    "Mantener advertencia historica de salidas no estructuradas en ciclos previos.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Cuando falte dato local, propagar plantilla base y pregunta abierta."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si Actividad 6 exige formato juridico de citacion adicional a BibTeX.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver.",
    "Confirmar si fuentes de interpretacion juridica de clean.bib son obligatorias en Actividad 6."
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
      "Problema juridico o social delimitado.",
      "Conceptos y normas pertinentes al caso.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes.",
      "Sostener rigor juridico y trazabilidad de fuentes.",
      "Formar criterio profesional desde argumentacion propia."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Fijar postura propia fundada.",
      "Derivar conclusion del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Hermeneutica juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado]"
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
          "justification": "Sin problema delimitado no hay argumentacion pertinente."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo y no ser decorativa."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Se evita heredar errores de salidas no parseables."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Marco normativo o doctrinal",
          "kind": "develops",
          "justification": "Aplica solo si la actividad aborda interpretacion juridica."
        }
      ],
      "evidence": [
        "README fija identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico define cinco ejes de trabajo.",
        "Memoria origen confirma regla de normalizacion previa a propagacion.",
        "Contexto local muestra token Slug sin resolver y requiere control editorial."
      ]
    },
    "reinforcement_log": [
      "Ciclo 91: refuerzo lateral aplicado por analogia controlada entre hermanos.",
      "Se conservaron reglas utiles previas y se eliminaron duplicados semanticos.",
      "Se agregaron solo mejoras verificables de control de estructura y trazabilidad.",
      "Se mantuvieron supuestos abiertos donde falta consigna local."
    ]
  }
}