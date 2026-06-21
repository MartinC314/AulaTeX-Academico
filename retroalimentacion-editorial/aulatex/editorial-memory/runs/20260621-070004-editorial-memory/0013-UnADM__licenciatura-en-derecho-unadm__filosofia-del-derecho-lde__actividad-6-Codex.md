{
  "summary": [
    "Se consolida memoria lateral de Actividad 1 a Actividad 6 con deduplicacion lossless.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se refuerzan ejes editoriales estables: problema, conceptos o normas, producto, analisis propio, conclusion transferible.",
    "Se mantiene regla critica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se conserva separacion entre reglas confirmadas y supuestos marcados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear cada entrega a Licenciatura en Derecho, asignatura Filosofia del Derecho.",
    "Citar ubicacion curricular cuando contextualice: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion: no eliminar reglas utiles previas."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar desarrollo en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Evitar entregas solo descriptivas; incluir postura argumentada propia.",
    "Relacionar conceptos, normas, doctrina o datos con el problema planteado.",
    "Sustentar afirmaciones relevantes con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No transferir conclusiones especificas desde actividades hermanas.",
    "Supuesto: si la consigna de Actividad 6 aborda interpretacion juridica, integrar hermeneutica y argumentacion juridica."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar aguas abajo.",
    "Revisar que no exista respuesta no estructurada reutilizada sin normalizacion.",
    "Confirmar trazabilidad: cada afirmacion relevante debe tener fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Revisar que la conclusion derive del analisis y no sea decorativa."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de automatizar nombres.",
    "Supuesto: archivo .bib canonico esperado por Slug es filosofia-del-derecho.bib; confirmar localmente."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas oficiales o academicas.",
    "Registrar fuentes especificas de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, editorial o nota, URL cuando exista.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a toda actividad; su alcance indica Semana 7."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables, no redaccion literal ni conclusiones puntuales.",
    "Aplicar union-dedupe lossless para evitar duplicados sin recortar reglas utiles.",
    "Mantener advertencia historica sobre salidas no parseables heredadas de ciclos tempranos.",
    "Etiquetar reglas de baja confianza como provisionales hasta verificacion local.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas, no contenido inventado."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6 y producto requerido final.",
    "Confirmar rubrica especifica de evaluacion para calibrar profundidad argumentativa.",
    "Confirmar nombre canonico final del .bib de asignatura por coexistencia con clean.bib y token Slug.",
    "Confirmar si Actividad 6 exige formato de citacion juridica adicional a BibTeX.",
    "Supuesto: validar si el corpus de interpretacion juridica de clean.bib es pertinente a Actividad 6."
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
        "Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y utiles para practica juridica.",
      "Asegurar coherencia entre identidad institucional, evidencia y argumentacion propia."
    ],
    "style_markers": [
      "Inicio con encuadre del problema.",
      "Secciones explicitas y ordenadas.",
      "Diferenciacion entre sintesis de fuentes y postura propia.",
      "Cierre con criterio juridico aplicable.",
      "Supuestos marcados de forma visible."
    ],
    "argumentative_patterns": [
      "Delimitar problema antes de teorizar.",
      "Anclar conceptos en norma, doctrina o evidencia.",
      "Contrastar fuentes y construir postura.",
      "Derivar conclusion desde el analisis.",
      "Evitar afirmaciones sin respaldo verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermenueutica juridica [supuesto condicional por consigna]",
        "Argumentacion juridica [supuesto condicional por consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/filosofia-del-derecho.bib",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y consistencia formal."
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
          "source": "Marco conceptual-normativo",
          "target": "Analisis propio",
          "kind": "supports",
          "justification": "Los conceptos y normas sostienen la postura juridica."
        },
        {
          "source": "Hermenueutica juridica [supuesto condicional por consigna]",
          "target": "Argumentacion juridica [supuesto condicional por consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico confirma cinco ejes de trabajo recurrentes.",
        "Memoria origen confirma regla de normalizacion previa a propagacion.",
        "clean.bib declara alcance especifico para actividad de interpretacion juridica (Semana 7)."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: deduplicacion de reglas repetidas en identidad, estructura, calidad y LaTeX.",
      "Ciclo 13: se conserva regla historica de bloqueo por JSON no parseable.",
      "Ciclo 13: se refuerza separacion entre hechos confirmados y supuestos.",
      "Ciclo 13: se evita traslado de contenido exclusivo de Actividad 1; solo patrones reutilizables.",
      "Ciclo 13: se mantiene continuidad institucional y curricular entre nodos hermanos."
    ]
  }
}