{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar contenido especifico.",
    "Se preserva identidad UnADM, ubicacion curricular y ejes editoriales de la asignatura.",
    "Se mantiene regla critica: normalizar antes de propagar y bloquear salidas no JSON parseable.",
    "Se deduplica memoria por union lossless sin eliminar reglas utiles previas.",
    "Se mantienen como supuestos los datos no visibles en la consigna local de Actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion al consolidar memoria."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea sea de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo de Actividad 6 sin romper ejes base de la materia.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 6.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar que no haya respuesta no estructurada.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar trazabilidad de afirmaciones a fuente o supuesto.",
    "Comprobar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en español en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Supuesto: nombre canonico de .bib pendiente de confirmacion local por coexistencia de archivos .bib."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, año, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Marcar como supuesto cualquier dato bibliografico incompleto.",
    "No citar entradas no usadas en el producto final."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo patrones reutilizables de identidad, estructura, calidad y metodo.",
    "No propagar redaccion literal ni conclusiones especificas entre hermanos.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "Mantener advertencia historica de salidas no parseables en herencias antiguas.",
    "Cuando falte consigna local, propagar plantilla base y dejar preguntas abiertas.",
    "Revalidar supuestos antes de convertirlos en reglas confirmadas."
  ],
  "open_questions": [
    "Confirmar consigna exacta y rubrica de Actividad 6.",
    "Confirmar producto principal exigido: reporte, presentacion u otro.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en documentos base.",
    "Confirmar si se usa bibliografia clean solo cuando la actividad sea interpretacion juridica.",
    "Confirmar si existe formato juridico de citacion adicional al flujo BibTeX institucional."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Disciplina de estructura y trazabilidad."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables.",
      "Garantizar consistencia editorial entre actividades hermanas.",
      "Sostener aprendizaje juridico con evidencia y criterio propio."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes.",
      "Tomar postura fundada.",
      "Derivar conclusion del analisis."
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
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del razonamiento desarrollado."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Solo memoria parseable evita errores y regresiones."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica consolidada: no propagar salida no estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: se refuerzan reglas transversales reutilizables de Actividad 1 hacia Actividad 6.",
      "Ciclo 7: se mantiene deduplicacion lossless y no regresion normativa.",
      "Ciclo 7: se preservan supuestos abiertos por falta de consigna local completa."
    ]
  }
}