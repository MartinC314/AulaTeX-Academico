{
  "summary": [
    "Se consolida memoria lateral A1->A6 con union-dedupe lossless y sin recorte.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantiene regla critica: no propagar contenido no estructurado sin normalizacion.",
    "Se refuerzan ejes editoriales estables: problema, conceptos, producto, analisis propio y conclusion juridica.",
    "Se conserva separacion entre reglas confirmadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Contextualizar ubicacion curricular al citar la materia: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar regla de no regresion editorial en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido y sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final a la consigna semanal real.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna de A6 aborda interpretacion juridica, integrar hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas verificadas de supuestos marcados.",
    "Confirmar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Mantener compatibilidad .tex-.bib y compilacion sin referencias rotas.",
    "No cambiar claves BibTeX ya citadas en archivos .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico de .bib mientras exista ambiguedad local."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editor o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad.",
    "Supuesto: clean.bib esta orientado a interpretacion juridica (Semana 7) hasta confirmacion de consigna A6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables, no conclusiones especificas.",
    "Aplicar union-dedupe lossless para evitar duplicados y perdida de reglas.",
    "Mantener advertencias historicas de salidas no parseables en nodos con herencia incierta.",
    "Propagar identidad curricular verificada a actividades hermanas de la misma asignatura.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar formato exigido en A6: reporte, presentacion u otro.",
    "Confirmar si A6 requiere bibliografia propia o reutiliza parte de la existente.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver.",
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
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto alineado a planeacion semanal.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos rigurosos.",
      "Sostener decisiones editoriales con evidencia verificable.",
      "Asegurar utilidad profesional de la conclusion juridica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y ordenadas.",
      "Postura personal diferenciada de la sintesis.",
      "Cierre con aplicabilidad juridica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Contrastar fuentes verificables.",
      "Tomar postura fundamentada.",
      "Derivar conclusion del analisis."
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
        "Normalizacion estructurada"
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
          "justification": "La pauta institucional exige citas verificables y forma academica."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis se valida solo con problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion legitima deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "La interpretacion fundamenta la justificacion argumentativa cuando aplica la consigna."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita reutilizar salidas defectuosas o no parseables."
        }
      ],
      "evidence": [
        "README de asignatura: identidad y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Supuesto marcado sobre uso condicionado de clean.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 92: deduplicacion completa de reglas repetidas en destino.",
      "Ciclo 92: preservadas reglas utiles previas sin eliminacion.",
      "Ciclo 92: reforzada frontera entre hechos verificados y supuestos.",
      "Ciclo 92: mantenida transferencia lateral por patrones reutilizables."
    ]
  }
}