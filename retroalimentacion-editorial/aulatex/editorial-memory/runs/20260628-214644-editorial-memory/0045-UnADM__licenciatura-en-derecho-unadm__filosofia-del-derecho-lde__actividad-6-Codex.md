{
  "summary": [
    "Se consolida memoria lateral de actividad 1 a actividad 6 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: normalizar salidas no estructuradas antes de propagar.",
    "Se evita traslado de conclusiones o bibliografia exclusiva de un hermano a otro sin confirmacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar contexto curricular: semestre 1, bloque 2, obligatoria, 8 creditos cuando aplique.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social desde el inicio.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar que conclusion derive del desarrollo.",
    "Validar trazabilidad de afirmaciones a fuente o supuesto."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anomales antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, editor o nota, URL si existe.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que clean.bib aplica a actividad 6 sin confirmacion de consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal entre hermanos.",
    "Propagar identidad curricular verificada a nodos hermanos de la asignatura.",
    "Mantener advertencias historicas de salidas no parseables en nodos con herencia dudosa.",
    "Aplicar union-dedupe lossless sin recorte de reglas utiles.",
    "Cuando falte dato local, propagar estructura base y abrir pregunta."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para actividad 6.",
    "Confirmar si actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
    "Confirmar si fuentes de interpretacion juridica de clean.bib aplican formalmente a actividad 6.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX."
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
      "Conceptos y normas pertinentes.",
      "Producto segun planeacion.",
      "Analisis propio con postura.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos utiles y verificables.",
      "Sostener rigor juridico con evidencia y criterio propio."
    ],
    "style_markers": [
      "Inicio con delimitacion del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura diferenciada.",
      "Cierre aplicable a practica juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Defender postura propia fundamentada.",
      "Concluir con implicacion practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Hermeneutica juridica [supuesto condicionado]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de uso por actividad]"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del razonamiento previo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Se evita contaminar nodos con salidas no parseables."
        }
      ],
      "evidence": [
        "README: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Memoria origen: regla reiterada de JSON parseable y normalizacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: deduplicacion de reglas repetidas y variantes ortograficas.",
      "Ciclo 2: se preservan reglas utiles previas sin recorte.",
      "Ciclo 2: se refuerza transferencia lateral por patrones reutilizables.",
      "Ciclo 2: se mantienen supuestos abiertos donde falta consigna local."
    ]
  }
}