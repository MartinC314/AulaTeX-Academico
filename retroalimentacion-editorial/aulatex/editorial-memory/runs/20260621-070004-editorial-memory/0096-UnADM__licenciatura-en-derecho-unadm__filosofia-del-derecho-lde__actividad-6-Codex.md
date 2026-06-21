{
  "summary": [
    "Se consolida memoria lateral A1->A6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantienen ejes editoriales estables: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se refuerza regla critica: no propagar contenido no estructurado sin normalizacion.",
    "Se mantiene traza de fuentes provisionales y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable cuando la tarea sea de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Diferenciar sintesis de fuentes y postura propia.",
    "Sostener afirmaciones relevantes con fuentes verificables.",
    "Evitar desarrollo solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Si la consigna trata interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa [supuesto].",
    "No transferir conclusiones especificas de Actividad 1 a Actividad 6."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Verificar trazabilidad minima de afirmaciones a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico de .bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Mantener metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que clean.bib aplica a toda actividad; confirmar por consigna.",
    "Usar malla curricular de Derecho UnADM para soporte de ubicacion curricular."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables y verificadas.",
    "Aplicar union-dedupe lossless en cada ciclo.",
    "No propagar redaccion literal ni conclusiones locales de otro hermano.",
    "Conservar advertencias historicas de salidas no estructuradas.",
    "Si falta consigna local, propagar estructura base y abrir preguntas.",
    "Etiquetar baja confianza como provisional hasta validacion local."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib de la asignatura.",
    "Confirmar si Actividad 6 reutiliza bibliografia de interpretacion juridica o requiere corpus propio.",
    "Confirmar si se exige estilo juridico de cita adicional a BibTeX."
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
      "Producto segun planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Estandarizar calidad editorial y trazabilidad de evidencias.",
      "Preservar memoria util sin perdida entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio breve con problema delimitado.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables en puntos clave.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre con aplicabilidad juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema -> definir objetivo -> sustentar con marco conceptual y normativo -> analizar -> concluir.",
      "Usar contraste entre fuentes cuando exista tension doctrinal.",
      "Derivar conclusion solo de argumentos desarrollados."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado por consigna]",
        "Argumentacion juridica [supuesto condicionado por consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md"
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
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado por consigna]",
          "target": "Argumentacion juridica [supuesto condicionado por consigna]",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad UnADM, pauta editorial y entrada canonica.",
        "Programa analitico: cinco ejes de trabajo.",
        "Historial de calidad: salidas no JSON deben normalizarse antes de propagar."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte semantico.",
      "Se eliminaron transferencias no reutilizables de hermano a hermano.",
      "Se preservaron reglas utiles previas y se reforzaron compuertas de calidad.",
      "Se marcaron supuestos donde falta consigna local verificable."
    ]
  }
}