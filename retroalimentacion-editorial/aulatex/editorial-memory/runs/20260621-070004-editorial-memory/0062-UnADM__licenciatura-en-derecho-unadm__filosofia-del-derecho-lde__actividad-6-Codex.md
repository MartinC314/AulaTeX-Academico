{
  "summary": [
    "Se consolida refuerzo lateral desde actividad 1 hacia actividad 6 sin perdida de reglas vigentes.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica de normalizar salidas no estructuradas antes de propagar.",
    "Se conserva deduplicacion lossless por union y sin recorte de reglas utiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones editoriales."
  ],
  "structure_rules": [
    "Entregar JSON valido cuando la tarea sea de consolidacion de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Supuesto: si actividad 6 aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar y normalizar cualquier respuesta no estructurada.",
    "Confirmar que cada afirmacion relevante tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas verificadas de supuestos editoriales."
  ],
  "latex_rules": [
    "Mantener codificacion en español y acentos correctos en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex sin migracion controlada.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: el .bib canonico esperado por Slug es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, año, editorial o nota, y URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a una actividad de interpretacion juridica y no sustituye automaticamente el .bib canonico general."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables: identidad, estructura, calidad y relaciones conceptuales estables.",
    "No propagar redaccion literal ni conclusiones especificas entre hermanos.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Mantener advertencia historica sobre salidas no JSON parseables heredadas.",
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Cuando falte consigna local, transferir estructura base y dejar preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de actividad 6.",
    "Confirmar si actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib de asignatura dada la coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si se requiere formato juridico de citacion adicional a BibTeX institucional.",
    "Confirmar si las fuentes de hermeneutica y SCJN son obligatorias o solo opcionales en actividad 6."
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
      "Conceptos, normas o doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar trazabilidad argumentativa desde problema hasta conclusion.",
      "Preservar continuidad editorial entre actividades hermanas sin contaminar contenidos especificos."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis.",
      "Citas verificables y consistentes con .bib.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes pertinentes.",
      "Sostener postura propia fundada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Hermeneutica juridica [supuesto condicionado]"
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
          "justification": "El analisis requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "No se debe propagar contenido no parseable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, entrada canonica, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Historial de ciclos: necesidad de bloquear salidas no JSON parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 62: refuerzo lateral consolidado con union-dedupe lossless.",
      "Se conservaron reglas nucleares de identidad, estructura, calidad y bibliografia.",
      "Se evito transferencia de conclusiones o redaccion especifica de actividad 1.",
      "Se mantuvieron supuestos explicitamente marcados por falta de consigna local completa."
    ]
  }
}