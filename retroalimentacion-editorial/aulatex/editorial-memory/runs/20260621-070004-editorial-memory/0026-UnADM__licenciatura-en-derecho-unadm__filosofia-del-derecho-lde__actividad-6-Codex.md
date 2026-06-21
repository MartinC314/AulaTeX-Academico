{
  "summary": [
    "Se refuerza memoria lateral entre actividades hermanas sin copiar conclusiones ni redaccion literal.",
    "Se conserva identidad UnADM y ubicacion curricular verificada: Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantiene regla critica: normalizar antes de propagar; bloquear salida no JSON parseable.",
    "Se consolidan ejes estables de la asignatura: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se preserva trazabilidad bibliografica y uso de fuentes verificables sin invencion."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Alinear cada actividad a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular cuando contextualice la materia: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisional toda fuente heredada no verificada localmente."
  ],
  "structure_rules": [
    "Entregar JSON valido cuando la tarea sea consolidacion de memoria.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Ordenar desarrollo en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo de Actividad 6 sin romper ejes base de la asignatura.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Sostener afirmaciones relevantes con fuentes verificables o marcar supuesto.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Alinear formato final al producto pedido por la planeacion semanal."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar trazabilidad de afirmaciones relevantes a evidencia o supuesto.",
    "Comprobar que la conclusion derive del desarrollo."
  ],
  "latex_rules": [
    "Mantener compatibilidad .tex y .bib sin romper claves citadas.",
    "No cambiar claves BibTeX ya usadas en archivos .tex.",
    "Verificar que toda clave citada exista en el .bib activo.",
    "Usar acentos y codificacion correcta en espanol.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y referencias de archivo.",
    "Supuesto: el .bib canonico esperado por Slug es filosofia-del-derecho.bib hasta confirmacion final."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Registrar fuentes especificas de actividad en el .bib de asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "No asumir que clean.bib aplica a toda actividad; usarlo solo si coincide con consigna.",
    "Marcar como supuesto todo dato bibliografico incompleto."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura, calidad y trazabilidad.",
    "Evitar transferir conclusiones tematicas especificas de una actividad a otra.",
    "Mantener union-dedupe lossless en cada ciclo.",
    "Conservar alertas historicas de salidas no estructuradas para prevenir regresiones.",
    "Si falta consigna local, transferir estructura base y abrir preguntas en vez de inventar contenido."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del .bib por coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
    "Confirmar si el eje tematico local de Actividad 6 coincide con interpretacion juridica."
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
      "Problema juridico delimitado.",
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, verificables y utiles para practica juridica.",
      "Preservar consistencia editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Cierre con utilidad profesional juridica.",
      "Supuestos etiquetados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer conceptos y normas aplicables.",
      "Contrastar fuentes verificables.",
      "Tomar postura fundada.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Normalizacion estructurada",
        "Trazabilidad bibliografica"
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
          "justification": "La pauta institucional exige verificabilidad y forma academica consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis solo es valido si parte de un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion debe derivar del razonamiento y no ser decorativa."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Trazabilidad bibliografica",
          "kind": "supports",
          "justification": "La estructura valida facilita verificar citas, supuestos y evidencia."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion y pauta editorial.",
        "Programa analitico: cinco ejes estables de trabajo.",
        "Regla historica consolidada: bloquear propagacion sin JSON parseable.",
        "Coexistencia de .bib local y clean.bib con uso condicionado por consigna."
      ]
    },
    "reinforcement_log": [
      "Ciclo 26: refuerzo lateral aplicado por analogia controlada entre hermanos.",
      "Se deduplicaron reglas repetidas y se conservaron todas las utiles.",
      "Se eliminaron traslados no reutilizables de contenido especifico de Actividad 1.",
      "Se reforzo gestion de supuestos ante falta de consigna local completa."
    ]
  }
}