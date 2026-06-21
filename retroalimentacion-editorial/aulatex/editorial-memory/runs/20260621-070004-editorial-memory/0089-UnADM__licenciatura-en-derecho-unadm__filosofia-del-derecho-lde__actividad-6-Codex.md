{
  "summary": [
    "Se conserva memoria editorial de Actividad 6 con union y deduplicacion lossless.",
    "Se refuerza identidad UnADM y ubicacion curricular verificada sin cambios de fondo.",
    "Se mantiene regla critica de normalizar salidas no estructuradas antes de propagar.",
    "Se preservan ejes estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica.",
    "Se evita traslado literal de conclusiones o bibliografia exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, Filosofia del Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido, sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Organizar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la consigna semanal (reporte, presentacion u otro).",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Definir objetivo puntual de Actividad 6 antes del desarrollo.",
    "Explicitar el problema que activa la respuesta.",
    "Relacionar conceptos, normas, doctrina y datos con el problema delimitado.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar texto solo descriptivo; priorizar argumentacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si el JSON no es parseable.",
    "Verificar estructura minima completa antes de aplicar aguas abajo.",
    "Separar reglas verificadas de supuestos marcados.",
    "Comprobar coherencia entre pregunta, desarrollo y conclusion.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Aplicar deduplicacion por union sin perdida de reglas vigentes."
  ],
  "latex_rules": [
    "Mantener compatibilidad .tex/.bib y claves BibTeX estables.",
    "No cambiar claves ya citadas en archivos .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en español.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas confiables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, año, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a un contexto de Semana 7 y no se fuerza a Actividad 6 sin consigna."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones nucleares.",
    "No propagar redaccion literal ni conclusiones especificas entre hermanos.",
    "No propagar bibliografia exclusiva sin evidencia de uso local.",
    "Mantener advertencia historica sobre salidas no estructuradas en ciclos previos.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 exige formato juridico de citacion adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib ante coexistencia de archivos y token Slug sin resolver.",
    "Confirmar si el corpus de hermeneutica/argumentacion aplica formalmente a Actividad 6."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social delimitado.",
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico.",
      "Garantizar trazabilidad entre fuentes, analisis y conclusion.",
      "Sostener continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de teorizar.",
      "Construir marco conceptual y normativo pertinente.",
      "Contrastar fuentes verificables.",
      "Tomar postura fundada del estudiante.",
      "Derivar conclusion del analisis, no agregarla de forma decorativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion de salida estructurada"
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
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge del desarrollo argumentativo."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La estructura parseable reduce errores de propagacion y perdida de contexto."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo recurrentes.",
        "Regla historica consolidada: no propagar salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 89: deduplicacion de reglas repetidas sin recorte semantico.",
      "Ciclo 89: refuerzo lateral de ejes editoriales comunes entre actividades hermanas.",
      "Ciclo 89: mantenimiento de supuestos abiertos por falta de consigna local verificable."
    ]
  }
}