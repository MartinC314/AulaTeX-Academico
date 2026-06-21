{
  "summary": [
    "Se consolida memoria lateral A1→A6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantienen ejes editoriales estables: problema, conceptos, producto, analisis propio, conclusion juridica.",
    "Se refuerza regla critica: no propagar salidas no estructuradas.",
    "Se conserva traza de fuentes provisionales hasta validacion local.",
    "Se mantiene uso canonico de carpeta de asignatura como entrada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho y Filosofia del Derecho.",
    "Contextualizar con semestre 1, bloque 2, obligatoria, 8 creditos cuando aplique.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema solicitado sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos, marco normativo o doctrinal, analisis propio, cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto exigido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar el problema que activa la respuesta.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna trata interpretacion juridica, vincular hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar trazabilidad de afirmaciones a fuente o supuesto.",
    "Revisar que la conclusion derive del analisis.",
    "Validar consistencia entre citas en texto y .bib activo."
  ],
  "latex_rules": [
    "Mantener acentos y codificacion correcta en espanol en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) antes de fijar nombres canonicos.",
    "Marcar como supuesto el .bib canonico mientras persista ambiguedad README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No forzar uso de clean.bib fuera de su contexto sin confirmacion local.",
    "Marcar como supuesto cualquier dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no conclusiones especificas entre hermanos.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Conservar advertencias historicas sobre salidas no estructuradas.",
    "Aplicar normalizacion manual a memorias de baja confianza antes de reuso.",
    "Propagar identidad curricular verificada a nodos hermanos de la asignatura."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige formato adicional de citacion juridica.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto.",
    "Confirmar si Actividad 6 reutiliza clean.bib o requiere .bib propio."
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
      "Problema juridico o social delimitado.",
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Asegurar coherencia entre evidencia, postura y cierre profesional."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura propia diferenciada.",
      "Cierre aplicable a practica juridica.",
      "Supuestos marcados cuando falte dato local."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual-normativo.",
      "Contrastar fuentes relevantes.",
      "Formular postura propia fundamentada.",
      "Concluir con criterio juridico derivado del desarrollo."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica",
        "Normalizacion estructurada previa a propagacion"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
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
          "justification": "El analisis valido parte de una delimitacion clara del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento y evidencia."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta argumentos."
        },
        {
          "source": "Normalizacion estructurada previa a propagacion",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita arrastre de errores y mantiene trazabilidad editorial."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Registro historico: salidas no JSON parseable requieren normalizacion previa.",
        "clean.bib: corpus de interpretacion juridica util bajo consigna confirmada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 71: deduplicacion completa de reglas repetidas sin recorte semantico.",
      "Ciclo 71: se preservan reglas troncales de A1 y se aplican lateralmente a A6.",
      "Ciclo 71: se evita traslado de conclusiones especificas o bibliografia exclusiva no confirmada.",
      "Ciclo 71: se mantienen supuestos abiertos por falta de consigna local completa."
    ]
  }
}