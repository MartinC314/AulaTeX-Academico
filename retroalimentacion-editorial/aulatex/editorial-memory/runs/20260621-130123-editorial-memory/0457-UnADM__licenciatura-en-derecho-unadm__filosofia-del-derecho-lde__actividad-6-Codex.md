{
  "summary": [
    "Se refuerza memoria lateral entre actividades hermanas con deduplicación sin pérdida.",
    "Se preserva identidad UnADM, ubicación curricular y ejes editoriales comunes.",
    "Se mantiene regla crítica de normalizar antes de propagar.",
    "Se evita transferir conclusiones o bibliografía exclusiva de una actividad a otra.",
    "Se consolidan patrones reutilizables para Actividad 6 con control de supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, Filosofía del Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar toda fuente heredada no verificada como provisional hasta validación local.",
    "Conservar regla de no regresión editorial en cada ciclo."
  ],
  "structure_rules": [
    "Entregar JSON válido y parseable en tareas de consolidación.",
    "Usar exactamente el esquema solicitado sin claves extra.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica derivada del desarrollo."
  ],
  "activity_rules": [
    "Definir objetivo puntual de la actividad antes del desarrollo.",
    "Relacionar conceptos y normas con el problema planteado.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir síntesis de fuentes frente a postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Supuesto: si Actividad 6 aborda interpretación jurídica, integrar hermenéutica y argumentación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "No eliminar reglas útiles previas durante consolidación.",
    "Verificar trazabilidad de afirmaciones relevantes a fuente o supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar que la conclusión no sea decorativa y derive del análisis."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre archivos .tex y .bib.",
    "No cambiar claves BibTeX ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Usar codificación y acentos correctos en español.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica automáticamente a Actividad 6."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacción literal ni conclusiones específicas.",
    "Aplicar unión-deduplicación lossless en cada ciclo.",
    "Preservar advertencias históricas sobre salidas no estructuradas.",
    "Propagar identidad curricular verificada a nodos hermanos de la asignatura.",
    "Cuando falten datos locales, mantener plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rúbrica específica de evaluación para Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentación o ambos.",
    "Confirmar nombre canónico final del .bib por coexistencia de archivos y token Slug sin resolver.",
    "Confirmar si las fuentes de interpretación jurídica son obligatorias o solo opcionales en Actividad 6.",
    "Confirmar si se requiere formato de citación jurídica adicional a BibTeX."
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
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Asegurar fundamento jurídico, evidencia verificable y transferencia profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve del problema.",
      "Secciones explícitas y ordenadas.",
      "Diferenciación clara entre fuente y postura propia.",
      "Cierre con utilidad jurídica práctica.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Exponer marco conceptual-normativo.",
      "Contrastar fuentes relevantes.",
      "Tomar postura fundamentada.",
      "Concluir en clave profesional transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Problema jurídico o social",
        "Marco conceptual-normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización estructurada",
        "Hermenéutica jurídica",
        "Argumentación jurídica"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "La postura argumentada requiere un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión válida deriva del desarrollo argumentativo."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "No se debe propagar salida no parseable."
        },
        {
          "source": "Hermenéutica jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "Patrón reusable cuando la consigna trate interpretación."
        }
      ],
      "evidence": [
        "README: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: cinco ejes de trabajo.",
        "Regla histórica consolidada: bloquear propagación sin JSON parseable.",
        "Token Slug sin resolver detectado en README y programa analítico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se consolidan reglas transversales sin recortar reglas útiles previas.",
      "Ciclo 5: se refuerza transferencia lateral por analogía controlada entre actividades hermanas.",
      "Ciclo 5: se mantiene separación entre hechos confirmados y supuestos locales.",
      "Ciclo 5: se evita trasladar bibliografía o conclusiones específicas de Actividad 1 a Actividad 6."
    ]
  }
}