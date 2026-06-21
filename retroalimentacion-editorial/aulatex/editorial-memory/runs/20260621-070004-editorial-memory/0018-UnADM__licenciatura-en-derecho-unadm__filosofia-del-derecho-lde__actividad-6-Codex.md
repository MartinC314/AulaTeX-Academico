{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 hacia Actividad 6 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerza la regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se mantienen ejes editoriales estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita transferencia de conclusiones o bibliografia exclusiva de un hermano a otro sin validacion local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear toda actividad a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular cuando se contextualice: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al tipo solicitado en la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Distinguir sintesis de fuentes y postura propia del estudiante.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Relacionar conceptos, normas o doctrina con el problema planteado.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica y argumentacion."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Revisar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Separar reglas confirmadas de supuestos editoriales.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "Verificar que la conclusion derive del desarrollo y no sea decorativa.",
    "No propagar supuestos como hechos confirmados."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilacion.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y rutas antes de automatizar.",
    "Marcar como supuesto el nombre canonico del .bib cuando haya ambiguedad."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y juridicas oficiales o academicas.",
    "Registrar fuentes especificas de cada actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No transferir bibliografia exclusiva de un hermano sin confirmacion de consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Aplicar union-dedupe lossless en nodos hermanos.",
    "Reutilizar patrones institucionales y de calidad; no copiar redaccion literal.",
    "Conservar advertencias historicas de salidas no estructuradas para trazabilidad.",
    "Cuando falte dato local, propagar estructura base y abrir pregunta en lugar de inventar.",
    "Mantener mejora progresiva por analogia controlada entre actividades hermanas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si Actividad 6 requiere reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si la bibliografia de interpretacion juridica aplica formalmente a Actividad 6.",
    "Confirmar si se exige formato de citacion juridica adicional a BibTeX institucional."
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
      "Problema juridico o social bien delimitado.",
      "Conceptos y normas pertinentes al caso.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura argumentada.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos.",
      "Unificar rigor juridico, claridad expositiva y utilidad profesional.",
      "Preservar memoria editorial reutilizable sin perdida."
    ],
    "style_markers": [
      "Inicio breve con encuadre del problema.",
      "Bloques seccionales explicitos y ordenados.",
      "Diferenciacion entre fuente y criterio propio.",
      "Cierre con aplicacion juridica concreta.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Contraste de fuentes verificables.",
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
        "Hermeneutica juridica [supuesto condicionado]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
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
          "justification": "El analisis requiere un problema previamente delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida surge del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado]",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Aplica solo si la consigna de Actividad 6 aborda interpretacion juridica."
        }
      ],
      "evidence": [
        "README: define identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: fija cinco ejes de trabajo recurrentes.",
        "Memoria origen: regla estable de normalizacion antes de propagacion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: se deduplican reglas repetidas y se preservan todas las utiles.",
      "Ciclo 18: se elimina ruido de relaciones no validas (p. ej. tipos fuera de esquema) y se conserva semantica verificable.",
      "Ciclo 18: se refuerza transferencia por patrones reutilizables, sin copiar conclusiones especificas de Actividad 1.",
      "Ciclo 18: se mantiene trazabilidad de supuestos y fuentes provisionales."
    ]
  }
}