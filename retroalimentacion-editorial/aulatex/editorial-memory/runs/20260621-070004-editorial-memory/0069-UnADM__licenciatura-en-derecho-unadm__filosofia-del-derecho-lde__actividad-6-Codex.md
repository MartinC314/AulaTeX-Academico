{
  "summary": [
    "Se consolida refuerzo lateral entre actividades hermanas sin copiar redaccion literal.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se refuerza regla critica: bloquear propagacion de salidas no estructuradas y normalizar antes de reutilizar.",
    "Se mantiene compresion lossless por union y deduplicacion de reglas reutilizables."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear contenido a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar contexto curricular solo con datos verificados: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el desarrollo al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica derivada del analisis."
  ],
  "activity_rules": [
    "Definir objetivo puntual de Actividad 6 antes del desarrollo.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No arrastrar conclusiones especificas de Actividad 1 a Actividad 6."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Revisar que la conclusion no sea decorativa y derive del desarrollo."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar codificacion correcta para espanol en .tex y .bib.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar rutas.",
    "Marcar como supuesto el nombre canonico del .bib hasta confirmacion local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que el clean.bib de Semana 7 aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables: identidad, estructura, calidad, conceptos marco y relaciones recurrentes.",
    "No propagar redaccion literal ni conclusiones particulares entre hermanos.",
    "Mantener advertencia historica sobre salidas no estructuradas en linaje Codex/GPT-Pro.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Cuando falte consigna local, propagar estructura base y dejar preguntas abiertas.",
    "Mantener trazabilidad de supuestos en cada salto recursivo."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar rubrica especifica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de la asignatura por token Slug sin resolver.",
    "Confirmar si Actividad 6 reutiliza bibliografia de interpretacion juridica o requiere corpus propio.",
    "Confirmar formato de citacion juridica adicional, si aplica, aparte de BibTeX."
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
      "Conceptos y marco normativo pertinentes.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible.",
      "Disciplina editorial basada en estructura verificable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y criterio propio.",
      "Garantizar continuidad editorial entre actividades sin perdida de reglas utiles.",
      "Asegurar trazabilidad entre afirmaciones, fuentes y conclusion."
    ],
    "style_markers": [
      "Inicio con problema claro.",
      "Secciones explicitas y ordenadas.",
      "Fuentes verificables con postura diferenciada.",
      "Uso consistente de supuestos marcados.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Fijar postura propia argumentada.",
      "Concluir con criterio aplicable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion JSON"
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
          "justification": "La pauta institucional exige citas verificables y formato academico."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere una delimitacion previa del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar logicamente del desarrollo."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        }
      ],
      "evidence": [
        "README confirma identidad, pauta editorial y ubicacion curricular.",
        "Programa analitico confirma cinco ejes de trabajo recurrentes.",
        "Historial de ciclos confirma necesidad de bloquear salidas no parseables."
      ]
    },
    "reinforcement_log": [
      "Ciclo 69: se mantiene union-dedupe lossless y no regresion.",
      "Ciclo 69: se transfieren solo patrones reutilizables desde hermano Actividad 1.",
      "Ciclo 69: se evita copiar conclusiones especificas o bibliografia exclusiva del hermano.",
      "Ciclo 69: se refuerza control de supuestos ante falta de consigna local completa."
    ]
  }
}