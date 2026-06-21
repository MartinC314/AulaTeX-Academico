{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con deduplicacion sin perdida.",
    "Se preserva identidad UnADM, ubicacion curricular y ejes editoriales estables.",
    "Se refuerza regla critica: normalizar salida no estructurada antes de propagar.",
    "Se mantiene separacion entre reglas confirmadas y supuestos marcados.",
    "Se conserva compatibilidad LaTeX-BibTeX con claves estables y trazables."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido, sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar sintesis de fuente y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin confirmacion de consigna."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion derive del analisis y no sea decorativa.",
    "Aplicar union-dedupe lossless en cada consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion correcta en español en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico de .bib mientras exista ambiguedad local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a actividad de interpretacion juridica y no sustituye automaticamente el .bib canonico."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo patrones reutilizables, no contenido literal.",
    "Mantener advertencias historicas de salidas no estructuradas en nodos con herencia similar.",
    "Propagar identidad curricular y gates de calidad como nucleo estable.",
    "No propagar supuestos como hechos confirmados.",
    "Si falta consigna local, transferir plantilla estructural y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README.",
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
      "Conceptos y marco normativo.",
      "Producto segun planeacion.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y postura propia.",
      "Asegurar calidad estructural, trazabilidad de fuentes y utilidad profesional del cierre."
    ],
    "style_markers": [
      "Inicio con encuadre breve.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre aplicado a practica juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Presentar marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Sostener postura argumentada.",
      "Concluir con criterio juridico aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion de salidas estructuradas"
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
          "justification": "La pauta institucional exige citas verificables y consistencia formal."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "No hay argumentacion solida sin delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion de salidas estructuradas",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Se evita contaminar nodos hermanos con memoria no parseable."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica estable: bloquear propagacion sin JSON parseable.",
        "Coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib con uso condicionado."
      ]
    },
    "reinforcement_log": [
      "Ciclo 36: refuerzo lateral hermano aplicado con union-dedupe lossless.",
      "Se mantuvieron reglas utiles previas y se eliminaron duplicados semanticos.",
      "Se reforzo separacion entre hechos confirmados y supuestos.",
      "Se conservaron patrones reutilizables sin copiar conclusiones especificas del nodo origen."
    ]
  }
}