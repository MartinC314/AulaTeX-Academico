{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 hacia Actividad 6 con union-dedupe lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio, conclusion juridica transferible.",
    "Se mantiene regla critica de normalizar salidas no estructuradas antes de propagar.",
    "Se conserva trazabilidad de fuentes provisionales y obligacion de marcar supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Citar ubicacion curricular cuando aplique: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisionales las fuentes heredadas no verificadas hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Iniciar con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio, cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido en la planeacion semanal.",
    "Cerrar con conclusion juridica derivada del analisis y transferible a practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Diferenciar de forma explicita sintesis de fuentes y postura propia.",
    "Sostener afirmaciones con fuentes verificables o marcar supuesto.",
    "Evitar desarrollo solo descriptivo; exigir toma de postura argumentada.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si la consigna trata interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar coherencia entre citas en texto y .bib activo.",
    "Revisar que la conclusion derive del desarrollo y no sea decorativa.",
    "No propagar contenido no estructurado sin normalizacion manual."
  ],
  "latex_rules": [
    "Mantener codificacion correcta de espanol en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Marcar como supuesto el nombre canonico del .bib si hay ambiguedad hasta confirmacion."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que un .bib depurado de otra semana aplica automaticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura, calidad y trazabilidad.",
    "Evitar transferir conclusiones o bibliografia exclusiva de una actividad a otra.",
    "Mantener union-dedupe lossless y registrar cambios por refuerzo lateral.",
    "Preservar alertas historicas de salida no estructurada en linajes con herencia Codex/GPT-Pro.",
    "Cuando falte consigna local, propagar plantilla base y abrir preguntas en vez de inventar."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6 y producto requerido.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si la bibliografia de interpretacion juridica (Semana 7) aplica total, parcial o no aplica a Actividad 6."
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
      "Problema juridico o social.",
      "Conceptos, normas, doctrina y datos pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar coherencia entre estructura, argumentacion y utilidad profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la fuente.",
      "Cierre con criterio juridico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Contraste y evaluacion de fuentes.",
      "Toma de postura fundamentada.",
      "Conclusion derivada del analisis."
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay analisis pertinente."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida se deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "En actividades de interpretacion, la hermeneutica fundamenta la argumentacion."
        },
        {
          "source": "Normalizacion de salida estructurada",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Evita perdida de reglas y mejora control de calidad editorial."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Regla historica: bloquear propagacion de salidas no JSON parseables.",
        "Existencia local de .bib general y .bib depurado; requiere confirmacion de uso por actividad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 27: se deduplican reglas repetidas y se preserva cobertura completa sin recorte semantico.",
      "Ciclo 27: se refuerza control de supuestos para datos no visibles en consigna.",
      "Ciclo 27: se mantiene separacion entre patrones reutilizables y contenido especifico de actividades hermanas."
    ]
  }
}