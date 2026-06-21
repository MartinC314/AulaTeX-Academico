{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantiene control de supuestos cuando falte consigna local de Actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica aplicable a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia de forma explicita.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos y normas con el problema delimitado.",
    "Supuesto: si la consigna aborda interpretacion juridica, integrar hermeneutica y argumentacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar trazabilidad de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar que la conclusion derive del analisis y no sea decorativa.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Marcar como supuesto cualquier dato bibliografico incompleto.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; tratarlo como corpus tematico especifico."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Mantener advertencia historica sobre salidas no estructuradas en herencias antiguas.",
    "Aplicar normalizacion manual cuando aparezcan nodos con formato defectuoso.",
    "Propagar identidad curricular verificada a nodos hermanos de la asignatura.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si la actividad exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por coexistencia de archivos y token Slug sin resolver.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib son obligatorias en Actividad 6."
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
      "Conceptos, normas o doctrina pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Estandarizar calidad editorial entre actividades hermanas sin perder especificidad local."
    ],
    "style_markers": [
      "Inicio con problema delimitado.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre con utilidad juridica profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes pertinentes.",
      "Sostener postura propia con evidencia.",
      "Concluir con consecuencia juridica aplicable."
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
        "Argumentacion juridica"
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
          "justification": "La pauta institucional exige citas verificables y formato academico consistente."
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
          "justification": "La conclusion valida debe derivar del razonamiento desarrollado."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion sustenta la justificacion argumentativa cuando la consigna lo requiere."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, pauta editorial y ubicacion curricular.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Presencia de token Slug sin resolver en README y programa analitico.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin eliminar reglas utiles previas.",
      "Se reforzo la distincion entre patrones generales transferibles y contenido especifico no transferible.",
      "Se conservaron advertencias de calidad sobre JSON parseable y normalizacion previa.",
      "Se mantuvo marcado explicito de supuestos por falta de consigna local completa."
    ]
  }
}