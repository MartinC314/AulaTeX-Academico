{
  "summary": [
    "Se conserva identidad UnADM y ubicación curricular verificada para Actividad 6.",
    "Se refuerza normalización obligatoria: no propagar salidas no estructuradas.",
    "Se mantienen ejes editoriales estables: problema, conceptos, producto, análisis propio y conclusión jurídica.",
    "Se aplica compresión lossless por unión y deduplicación sin eliminar reglas útiles.",
    "Se transfiere solo patrón reusable desde hermano: estructura, calidad, trazabilidad y control de supuestos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Licenciatura en Derecho, Filosofía del Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar como provisionales las fuentes heredadas no verificadas.",
    "Conservar regla de no regresión en consolidaciones editoriales."
  ],
  "structure_rules": [
    "Entregar JSON válido y parseable en tareas de memoria.",
    "Usar exactamente el esquema solicitado sin claves extra.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto final con la planeación semanal de Actividad 6."
  ],
  "activity_rules": [
    "Adaptar la redacción al objetivo específico de Actividad 6.",
    "No romper los cinco ejes del programa analítico.",
    "Distinguir síntesis de fuentes y postura propia.",
    "Sustentar afirmaciones con fuentes verificables disponibles.",
    "Evitar generalizaciones filosóficas sin anclaje jurídico.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Supuesto: si la consigna trata interpretación jurídica, vincular hermenéutica, argumentación y aplicación normativa."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Separar reglas confirmadas de supuestos marcados.",
    "Verificar coherencia entre problema, desarrollo y conclusión.",
    "Validar correspondencia entre citas en texto y archivo .bib activo.",
    "No eliminar reglas útiles previas durante consolidación."
  ],
  "latex_rules": [
    "Mantener compatibilidad entre .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Usar codificación correcta en español en .tex y .bib.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Marcar como supuesto el nombre canónico de .bib mientras exista ambigüedad entre filosofia-del-derecho.bib y filosofia-del-derecho-clean.bib."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y fuentes jurídicas oficiales o académicas.",
    "Registrar fuentes específicas de actividad en el .bib de la asignatura.",
    "Conservar metadatos mínimos: autor, título, año, editorial o nota, URL cuando exista.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a actividad temática de interpretación jurídica y no sustituye automáticamente el .bib general."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo tras validar JSON y estructura.",
    "Transferir patrones generales, no conclusiones ni bibliografía exclusiva de un hermano.",
    "Preservar advertencia histórica de salidas no parseables para nodos con herencia Codex/GPT-Pro.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "Si falta consigna local, propagar estructura base y abrir preguntas en lugar de inventar contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar rúbrica de evaluación específica de Actividad 6.",
    "Confirmar formato principal exigido: reporte, presentación u otro.",
    "Confirmar nombre canónico final del .bib de la asignatura.",
    "Confirmar si Actividad 6 exige fuentes obligatorias distintas a las ya disponibles.",
    "Confirmar si requiere formato de citación jurídica adicional a BibTeX."
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
      "Producto alineado a planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos con fundamento jurídico, evidencia y criterio propio.",
      "Asegurar continuidad editorial entre actividades hermanas sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Inicio con delimitación del problema.",
      "Secciones explícitas y orden lógico.",
      "Diferenciación clara entre fuente y postura personal.",
      "Cierre con utilidad profesional jurídica.",
      "Supuestos siempre marcados."
    ],
    "argumentative_patterns": [
      "Problema delimitado -> marco conceptual/normativo -> análisis propio -> conclusión derivada.",
      "Afirmación relevante -> evidencia verificable o supuesto explícito.",
      "Adaptación a consigna local sin romper ejes troncales."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Trazabilidad de fuentes"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
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
          "justification": "El análisis requiere un problema previamente delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "develops",
          "justification": "La conclusión válida debe derivar del razonamiento expuesto."
        },
        {
          "source": "Normalización JSON",
          "target": "Trazabilidad de fuentes",
          "kind": "supports",
          "justification": "La estructura parseable permite validar reglas, supuestos y citas."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicación curricular y pauta editorial.",
        "Programa analítico: cinco ejes de trabajo.",
        "Historial: regla persistente de bloquear propagación de salida no estructurada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 74: se consolidan reglas hermanas reutilizables sin copiar conclusiones específicas.",
      "Ciclo 74: se mantiene deduplicación lossless y no regresión de calidad.",
      "Ciclo 74: se refuerza control de supuestos ante ambigüedad de archivo .bib canónico."
    ]
  }
}