{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas con union-dedupe lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada sin cambios.",
    "Se mantienen ejes editoriales estables: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se refuerza regla critica: no propagar salidas no estructuradas sin normalizacion.",
    "Se conserva separacion entre reglas verificadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Contextualizar ubicacion curricular al citarla: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisionales las fuentes heredadas no verificadas localmente.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea sea de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar la redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar el problema que activa la respuesta.",
    "Relacionar conceptos, normas o doctrina con el problema delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes frente a postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar cualquier respuesta no estructurada antes de reutilizar.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Aplicar deduplicacion por union sin perdida semantica."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo anommalos antes de compilar.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente editorial o URL.",
    "Marcar como supuesto cualquier dato bibliografico incompleto.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones recurrentes.",
    "No transferir redaccion literal ni conclusiones especificas entre hermanos.",
    "Etiquetar como provisionales las reglas con fuente no confirmada localmente.",
    "Mantener advertencia historica de salidas no parseables en nodos con herencia Codex.",
    "Aplicar normalizacion manual a ciclos tempranos antes de reuso."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del archivo .bib por coexistencia de archivos y token Slug sin resolver.",
    "Confirmar si se requiere formato de citacion juridica adicional a BibTeX institucional.",
    "Confirmar si las fuentes de interpretacion juridica son obligatorias o solo opcionales en Actividad 6."
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
      "Problema juridico o social como punto de partida.",
      "Conceptos y normas pertinentes al caso.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura argumentada.",
      "Conclusion juridica aplicable a la practica."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Preservar identidad UnADM en entregas tecnicas y academicas.",
      "Garantizar transferibilidad profesional del cierre argumentativo."
    ],
    "style_markers": [
      "Inicio breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura personal diferenciada.",
      "Cierre no decorativo derivado del analisis.",
      "Supuestos siempre etiquetados."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Sostener postura propia fundamentada.",
      "Concluir con criterio juridico transferible."
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
        "Argumentacion juridica",
        "Normalizacion de salida estructurada"
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
          "justification": "La pauta institucional exige verificabilidad y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis valido requiere delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion fundamenta la justificacion de decisiones juridicas."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita propagacion de errores y preserva trazabilidad editorial."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Regla historica consolidada: bloquear propagacion de salida no parseable.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib con token Slug sin resolver."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se reforzo lateralmente identidad, estructura y calidad sin copiar contenido especifico del hermano.",
      "Ciclo 6: se mantuvo compresion lossless por deduplicacion y union de reglas reutilizables.",
      "Ciclo 6: se conservaron advertencias de fuentes provisionales y supuestos pendientes de validacion local."
    ]
  }
}