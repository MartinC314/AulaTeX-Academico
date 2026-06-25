{
  "summary": [
    "Consolidación lateral desde Actividad 1 hacia Actividad 6 con unión y deduplicación sin pérdida.",
    "Se refuerza identidad UnADM, pauta editorial y cinco ejes del programa analítico.",
    "Se mantiene regla crítica: no propagar salidas no estructuradas; normalizar antes de reutilizar.",
    "Se transfieren patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones generales.",
    "Se marcan supuestos cuando falte consigna local o archivos canónicos.",
    "Se controla token Slug sin resolver en README y ambigüedad del .bib canónico.",
    "Se preserva trazabilidad entre citas en texto y .bib local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular a Licenciatura en Derecho: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente de ubicación curricular.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Etiquetar memoria Codex/GPT previa como provisional hasta validación.",
    "No propagar redacción ni conclusiones específicas entre actividades hermanas."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Separar: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato exigido por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a la práctica profesional.",
    "Cuando la tarea sea de consolidación, entregar JSON válido usando el esquema requerido.",
    "No añadir claves fuera del esquema solicitado."
  ],
  "activity_rules": [
    "Adaptar la redacción al objetivo específico de la Actividad 6 sin romper los ejes base.",
    "Explicitar el problema que activa la respuesta y su alcance.",
    "Relacionar conceptos, normas y doctrina con el problema planteado.",
    "Sustentar afirmaciones con fuentes verificables disponibles en el .bib local.",
    "Distinguir síntesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas; incluir argumentación.",
    "Verificar coherencia entre preguntas guía, desarrollo y conclusión.",
    "Supuesto: si la Actividad 6 trata interpretación jurídica, integrar hermenéutica y argumentación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de propagar.",
    "Validar consistencia entre citas en texto y entradas en el .bib activo.",
    "Separar reglas verificadas de supuestos marcados.",
    "Verificar que la conclusión derive del análisis y no sea decorativa.",
    "Aplicar deduplicación por unión sin eliminar reglas útiles previas.",
    "Controlar tokens Slug sin resolver en README y referencias.",
    "Registrar trazabilidad de modificaciones en la memoria editorial."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres de archivos y rutas antes de compilar.",
    "Resolver tokens sin expandir del tipo $(@{...}.Slug) en README y programa analítico.",
    "Marcar como supuesto el nombre canónico del .bib hasta confirmarlo."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar materiales realmente consultables.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No citar entradas locales depuradas si no se usan efectivamente.",
    "Validar textos jurídicos en repositorios oficiales o académicos.",
    "Supuesto: confirmar .bib canónico (filosofia-del-derecho.bib vs filosofia-del-derecho-clean.bib) antes de agregar nuevas entradas."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo tras validar JSON y estructura.",
    "Reutilizar patrones generales de identidad, estructura y calidad; evitar contenido específico.",
    "Marcar reglas heredadas de baja confianza como provisionales hasta confirmar localmente.",
    "No degradar reglas útiles previas; solo agregar mejoras verificables.",
    "Normalizar manualmente nodos con historial de salida no estructurada.",
    "No propagar supuestos como hechos; documentar pendientes.",
    "Registrar cambios en refuerzo lateral para trazabilidad."
  ],
  "open_questions": [
    "Confirmar la consigna exacta y el producto requerido para la Actividad 6.",
    "Confirmar la rúbrica de evaluación específica de la Actividad 6.",
    "Definir si la Actividad 6 aborda interpretación jurídica u otro eje del programa.",
    "Confirmar el .bib canónico de la asignatura para la Actividad 6.",
    "Determinar si se exige estilo de citación adicional al BibTeX institucional.",
    "Identificar fuentes obligatorias de la semana correspondiente a la Actividad 6.",
    "Verificar si deben usarse las fuentes locales sobre hermenéutica y tesis SCJN en esta actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como punto de partida.",
      "Conceptos y marco normativo pertinentes.",
      "Producto alineado a la planeación.",
      "Análisis propio con postura argumentada.",
      "Conclusión transferible a la práctica.",
      "Control de calidad editorial y normalización."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos claros, fundamentados y útiles.",
      "Preservar identidad institucional y rigor académico.",
      "Asegurar coherencia entre problema, análisis y conclusión.",
      "Facilitar reutilización de patrones editoriales en actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explícitas y ordenadas.",
      "Citas verificables; postura personal diferenciada.",
      "Cierre con utilidad profesional.",
      "Supuestos marcados cuando falte información local."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Marco conceptual-normativo.",
      "Contraste de fuentes y criterios.",
      "Toma de postura fundamentada.",
      "Conclusión derivada del análisis.",
      "Validación de coherencia interna y de fuentes."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Ejes editoriales: problema, conceptos, producto, análisis, conclusión",
        "Hermenéutica jurídica",
        "Argumentación jurídica",
        "Tokens Slug sin resolver",
        "Claves BibTeX estables",
        "Compilación sin errores"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Ejes editoriales: problema, conceptos, producto, análisis, conclusión",
          "target": "Conclusión derivada del análisis",
          "kind": "depends_on",
          "justification": "El cierre requiere desarrollo argumentativo previo."
        },
        {
          "source": "Hermenéutica jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación fundamenta la construcción de argumentos."
        },
        {
          "source": "Tokens Slug sin resolver",
          "target": "Claves BibTeX estables",
          "kind": "contrasts",
          "justification": "Los tokens sin expandir generan inestabilidad en rutas y referencias."
        },
        {
          "source": "Claves BibTeX estables",
          "target": "Compilación sin errores",
          "kind": "supports",
          "justification": "La consistencia de claves evita referencias rotas."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: cinco ejes de trabajo.",
        "clean.bib: corpus local sobre hermenéutica e interpretación jurídica.",
        "Historial: coexistencia de filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib.",
        "Incidencia: token Slug sin resolver en README y programa analítico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: Unión y deduplicación de reglas desde Actividad 1 a 6.",
      "Se consolidan ejes editoriales y controles de calidad.",
      "Se agregan controles sobre tokens Slug y .bib canónico (supuesto).",
      "Se mantiene separación entre patrones generales y contenidos específicos.",
      "Se registran preguntas abiertas para completar datos locales de Actividad 6."
    ]
  }
}