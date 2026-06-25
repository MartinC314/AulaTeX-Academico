{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 6 con unión y deduplicación sin pérdida.",
    "Se preserva identidad UnADM, ubicación curricular y ejes editoriales base de Filosofía del Derecho.",
    "Se mantiene regla crítica: no propagar contenido no estructurado; normalizar antes de reutilizar.",
    "Se conserva separación entre reglas verificadas y supuestos marcados.",
    "Se agrega control de transferencia entre hermanos: reutilizar patrones, no conclusiones ni bibliografía exclusiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, Filosofía del Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Conservar regla de no regresión en consolidaciones."
  ],
  "structure_rules": [
    "Entregar JSON válido y parseable en tareas de memoria editorial.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Estructurar productos con: problema, conceptos o marco normativo, desarrollo, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear formato final al producto solicitado en la planeación semanal."
  ],
  "activity_rules": [
    "Adaptar redacción al objetivo específico de Actividad 6 sin romper ejes de asignatura.",
    "Explicitar el problema jurídico o social desde el inicio.",
    "Sustentar afirmaciones relevantes con fuentes verificables.",
    "Distinguir síntesis de fuentes frente a postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Supuesto: si la consigna aborda interpretación jurídica, vincular hermenéutica, argumentación y aplicación normativa."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Validar consistencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas útiles previas durante consolidación."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad entre .tex y .bib sin cambiar claves citadas.",
    "Comprobar que toda clave citada exista en el bibliográfico activo.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Marcar como supuesto el nombre canónico de .bib mientras exista ambigüedad documental."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas verificables.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No transferir bibliografía exclusiva de una actividad hermana sin validación de consigna local.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a interpretación jurídica (Semana 7) y su reutilización depende de la consigna de Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar en hermanos solo patrones estables: identidad, estructura, calidad, conceptos y relaciones.",
    "No copiar redacción literal ni conclusiones específicas entre actividades hermanas.",
    "Etiquetar reglas de baja confianza como provisionales hasta confirmación local.",
    "Aplicar compresión lossless por unión y deduplicación, no por recorte.",
    "Conservar advertencias históricas de no-JSON parseable para prevenir regresiones."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica de evaluación para ajustar profundidad argumentativa.",
    "Confirmar si Actividad 6 exige reporte, presentación o ambos.",
    "Confirmar nombre canónico final del archivo .bib por token Slug sin resolver en README.",
    "Confirmar si las fuentes de hermenéutica y SCJN son obligatorias o solo opcionales en Actividad 6.",
    "Confirmar si se exige formato de citación jurídica adicional a BibTeX institucional."
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
        "Asignatura: Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto de planeación semanal.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar fundamento jurídico, evidencia verificable y cierre argumentativo profesional."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explícitas y ordenadas.",
      "Diferenciación visible entre fuente y postura propia.",
      "Cierre con utilidad profesional jurídica.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual y normativo.",
      "Analizar con postura propia sustentada.",
      "Derivar conclusión desde el análisis, no decorativa."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Problema jurídico o social",
        "Marco conceptual-normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Hermenéutica jurídica",
        "Argumentación jurídica",
        "Normalización estructurada"
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
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis parte de una delimitación explícita del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión válida debe derivar del razonamiento presentado."
        },
        {
          "source": "Hermenéutica jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "En actividades de interpretación, la hermenéutica fundamenta la argumentación."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON parseable no hay transferencia confiable entre nodos."
        }
      ],
      "evidence": [
        "README de asignatura: identidad, pauta editorial y ubicación curricular.",
        "Programa analítico: cinco ejes de trabajo.",
        "Regla histórica consolidada: bloquear propagación sin JSON parseable.",
        "Existencia de token Slug sin resolver en README y programa analítico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 21: se refuerzan patrones reutilizables entre hermanos sin copiar contenido específico.",
      "Ciclo 21: se mantiene deduplicación lossless y no regresión de reglas útiles.",
      "Ciclo 21: se preserva separación entre hechos verificados y supuestos."
    ]
  }
}