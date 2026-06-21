{
  "summary": [
    "Se consolida memoria lateral A1->A6 sin perdida por union-dedupe.",
    "Se preserva identidad UnADM y contexto curricular verificado.",
    "Se mantienen ejes editoriales: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se refuerza regla critica: no propagar contenido no estructurado sin normalizacion.",
    "Se conserva separacion entre reglas verificadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho, Filosofia del Derecho.",
    "Reconocer ubicacion curricular al contextualizar: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Explicitar problema juridico o social al inicio.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si Actividad 6 es de interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Aplicar deduplicacion lossless por union."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que cada clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico de .bib mientras exista ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas confiables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar conclusiones especificas.",
    "Conservar alertas historicas de salidas no estructuradas en nodos con herencia Codex/GPT-Pro.",
    "Propagar identidad curricular verificada a nodos hermanos de la asignatura.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar normalizacion manual a ciclos con ruido historico antes de reuso."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver en README/programa.",
    "Confirmar si fuentes de interpretacion juridica (clean.bib) corresponden formalmente a Actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX."
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
      "Problema juridico o social como detonante.",
      "Conceptos, normas y doctrina con evidencia.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio diferenciado de la sintesis.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos solidos.",
      "Asegurar fundamento juridico, trazabilidad y utilidad profesional.",
      "Preservar memoria editorial estable entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con postura personal diferenciada.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Presentar marco conceptual y normativo.",
      "Contrastar fuentes relevantes.",
      "Fijar postura propia fundamentada.",
      "Cerrar con conclusion derivada del analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado]",
        "Argumentacion juridica [supuesto condicionado]"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [uso condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y forma academica."
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
          "justification": "La conclusion valida debe derivar del razonamiento previo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado]",
          "target": "Argumentacion juridica [supuesto condicionado]",
          "kind": "supports",
          "justification": "Si la consigna es de interpretacion, la hermeneutica sostiene la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM y ubicacion curricular.",
        "Programa analitico confirma cinco ejes de trabajo.",
        "Historial confirma necesidad de normalizar salidas no estructuradas.",
        "Existen dos .bib locales; la seleccion final requiere confirmacion."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas conservando contenido util.",
      "Se mantuvo regla de bloqueo por JSON no parseable.",
      "Se reforzo marcado explicito de supuestos.",
      "Se evitaron traslados literales de conclusiones o bibliografia exclusiva de A1.",
      "Se agrego control de token Slug sin resolver como riesgo tecnico verificable."
    ]
  }
}