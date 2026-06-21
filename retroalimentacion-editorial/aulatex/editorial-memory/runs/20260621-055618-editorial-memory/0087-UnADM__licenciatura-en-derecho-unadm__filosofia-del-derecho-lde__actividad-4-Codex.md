{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 4 con deduplicación lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se mantiene validación JSON estricta por antecedentes de salidas no parseables.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni bibliografía exclusiva del hermano.",
    "Supuesto: la consigna específica de Actividad 4 no está completa en el contexto visible."
  ],
  "identity_rules": [
    "Mantener tono formal académico UnADM.",
    "Alinear contenido con Licenciatura en Derecho y Filosofía del Derecho.",
    "Sostener postura jurídica propia con respaldo verificable.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Vincular ubicación curricular a semestre 1, bloque 2, obligatoria, 8 créditos con fuente institucional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Alinear el formato final al producto pedido en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analítico.",
    "Incluir problema, conceptos, evidencia y análisis propio de forma explícita.",
    "Evitar entrega solo descriptiva o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar que fuentes usadas correspondan a la semana y consigna reales.",
    "No asumir reutilización automática de bibliografía de otras semanas."
  ],
  "quality_gates": [
    "Bloquear propagación si salida no es JSON parseable.",
    "Exigir estructura mínima completa antes de reutilizar.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Validar que toda afirmación tenga fuente o marca de supuesto.",
    "Validar correspondencia entre producto entregado y consigna de Actividad 4.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Citar solo claves existentes en .bib.",
    "No renombrar claves BibTeX activas sin migración controlada.",
    "Compilar sin errores críticos, citas rotas ni referencias faltantes.",
    "Verificar nombres reales de archivos en README por tokens sin resolver.",
    "Corregir rutas o nombres con caracteres dañados antes de compilar.",
    "No introducir comandos no estándar sin justificación editorial."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y jurídicas verificables.",
    "Registrar en .bib de asignatura solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a interpretación jurídica; confirmar aplicabilidad a Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Mantener unión-dedupe sin regresiones de reglas útiles.",
    "Transferir patrones generales cuando falte consigna textual local.",
    "Preservar bandera de normalización manual en ciclos con salida no estructurada.",
    "Reforzar conexiones entre identidad, estructura, calidad y argumentación en nodos hermanos."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 4: producto, extensión y rúbrica.",
    "Confirmar si Actividad 4 requiere reporte, presentación u otro formato.",
    "Confirmar fuentes obligatorias específicas de la semana.",
    "Confirmar nombre canónico final del .bib por token Slug no resuelto en README.",
    "Confirmar si se usa .bib incremental propio o el .bib general de asignatura."
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
        "Normalización obligatoria antes de propagar.",
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo pertinente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y criterio propio.",
      "Asegurar trazabilidad entre problema, fuentes, análisis y cierre argumentativo."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y jerárquicas.",
      "Cita explícita en afirmaciones sustantivas.",
      "Supuestos etiquetados cuando falte evidencia local."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y normas.",
      "Contrastar evidencia.",
      "Sostener postura personal argumentada.",
      "Concluir con aplicabilidad jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofía del Derecho",
        "Normalización estructurada",
        "Validación JSON estricta",
        "Integridad académica y verificabilidad",
        "Relación problema-evidencia-conclusión"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y formato académico."
        },
        {
          "source": "Ejes editoriales de Filosofía del Derecho",
          "target": "Relación problema-evidencia-conclusión",
          "kind": "develops",
          "justification": "Los ejes ordenan el argumento desde el problema hasta el cierre jurídico."
        },
        {
          "source": "Normalización estructurada",
          "target": "Validación JSON estricta",
          "kind": "depends_on",
          "justification": "La propagación segura requiere estructura parseable."
        },
        {
          "source": "Integridad académica y verificabilidad",
          "target": "Relación problema-evidencia-conclusión",
          "kind": "supports",
          "justification": "La conclusión jurídica válida depende de evidencia comprobable."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y conclusión jurídica propia.",
        "Programa analítico: cinco ejes de trabajo reutilizables.",
        "Historial de ciclos: salidas no parseables justifican gate técnico estricto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 87: deduplicación de reglas repetidas y normalización semántica sin pérdida.",
      "Ciclo 87: refuerzo lateral de patrones de estructura y calidad desde nodo hermano.",
      "Ciclo 87: se evita transferir contenido específico o bibliografía exclusiva de Actividad 1.",
      "Ciclo 87: se mantienen supuestos abiertos donde falta consigna local verificable."
    ]
  }
}