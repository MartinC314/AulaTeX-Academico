{
  "summary": [
    "Se refuerza memoria lateral de Actividad 1 a Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM, ubicacion curricular y ejes editoriales de Filosofia del Derecho.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion previa.",
    "Se conserva separacion entre reglas verificadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Contextualizar con semestre 1, bloque 2, obligatoria, 8 creditos cuando aplique.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar el problema juridico o social que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion, vincular hermeneutica y argumentacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Separar reglas verificadas de supuestos editoriales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar que la conclusion derive del desarrollo."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug del README; confirmar localmente."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Marcar como supuesto todo dato bibliografico incompleto hasta verificarlo."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redaccion literal ni conclusiones especificas.",
    "Propagar identidad curricular verificada a nodos hermanos de la misma asignatura.",
    "Mantener advertencia historica de salidas no parseables en herencias de baja confianza.",
    "Aplicar union-dedupe lossless y evitar recortes.",
    "Si falta consigna local, propagar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib de la asignatura por token Slug sin resolver.",
    "Confirmar si se reutiliza filosofia-del-derecho-clean.bib o se requiere .bib especifico de actividad."
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico, evidencia y criterio propio.",
      "Asegurar trazabilidad editorial entre problema, desarrollo argumentativo y conclusion profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura propia diferenciada.",
      "Cierre con utilidad juridica practica.",
      "Supuestos etiquetados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia fundamentada.",
      "Concluir con regla o criterio transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermenutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
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
          "justification": "El analisis se construye desde un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermenutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo estables.",
        "Regla historica consolidada: normalizar antes de propagar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando cobertura funcional.",
      "Se mantuvo la regla de bloqueo por JSON no parseable.",
      "Se reforzo marcaje de supuestos para datos no visibles.",
      "Se evito transferir conclusiones especificas de Actividad 1 hacia Actividad 6.",
      "Se conservaron patrones reutilizables de identidad, estructura, calidad y bibliografia."
    ]
  }
}