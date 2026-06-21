{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se conserva regla critica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se refuerza control de supuestos cuando falte consigna local de Actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir con claridad sintesis de fuentes y postura propia.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que cada afirmacion relevante tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas confirmadas de supuestos editoriales."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar codificacion y acentos correctos en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres o rutas anomales antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; verificar consigna.",
    "Marcar como supuesto cualquier dato bibliografico incompleto hasta verificarlo."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones especificas entre hermanos.",
    "Mantener union-dedupe lossless y evitar duplicados semanticos.",
    "Conservar advertencias historicas sobre salidas no parseables de herencia previa.",
    "Propagar identidad curricular verificada a nodos hermanos de la misma asignatura.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX.",
    "Confirmar si la linea de interpretacion juridica aplica formalmente a Actividad 6."
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
      "Marco conceptual, normativo o doctrinal pertinente.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar trazabilidad editorial y tecnica en cada entrega.",
      "Preservar continuidad institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Apertura con problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura diferenciada.",
      "Cierre con utilidad juridica profesional.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer conceptos y normas relevantes.",
      "Contrastar fuentes verificables.",
      "Desarrollar postura propia fundada.",
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
        "Hermeneutica juridica [supuesto condicional por consigna]",
        "Argumentacion juridica [supuesto condicional por consigna]"
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
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicional por consigna]",
          "target": "Argumentacion juridica [supuesto condicional por consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo.",
        "Memoria origen confirma regla de normalizacion previa a propagacion.",
        "Contexto local confirma coexistencia de .bib canonico y .bib depurado."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte de contenido valido.",
      "Se transfirieron solo patrones reutilizables de nodo hermano.",
      "Se excluyeron conclusiones y bibliografia exclusiva no confirmada para Actividad 6.",
      "Se reforzo control de supuestos y verificacion local antes de afirmar hechos."
    ]
  }
}