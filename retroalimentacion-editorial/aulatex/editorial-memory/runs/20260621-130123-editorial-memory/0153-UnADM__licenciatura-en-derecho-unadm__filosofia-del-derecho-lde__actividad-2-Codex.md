{
  "summary": [
    "Se refuerza memoria de actividad-2 con transferencia lateral controlada desde actividad-1.",
    "Se conserva identidad UnADM y ubicación curricular verificable sin copiar contenido exclusivo del hermano.",
    "Se mantiene compresión lossless por unión y deduplicación; sin recorte de reglas útiles.",
    "Se consolida normalización obligatoria de salidas no estructuradas antes de propagación recursiva.",
    "Se preservan ejes editoriales troncales: problema, conceptos, evidencia, análisis propio y conclusión jurídica."
  ],
  "identity_rules": [
    "Mantener tono formal académico-jurídico UnADM.",
    "Vincular explícitamente la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Conservar cierre con criterio jurídico propio."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto pedido en la planeación semanal.",
    "Diferenciar postura propia, cita textual y paráfrasis.",
    "Cerrar con conclusión transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Ajustar actividad-2 a la instrucción docente disponible.",
    "No asumir tema, semana o formato sin evidencia local.",
    "Sustentar cada afirmación sustantiva con fuente verificable o marca de supuesto.",
    "Evitar entregas solo descriptivas; incluir postura argumentada del estudiante.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Transferir solo patrones reutilizables; no copiar conclusiones específicas de actividad-1."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas heredadas antes de reutilizarlas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "No eliminar reglas útiles previas; solo unir y deduplicar."
  ],
  "latex_rules": [
    "Usar acentos y codificación española correctos en .tex y .bib.",
    "Mantener estabilidad de claves BibTeX ya citadas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar rutas y nombres canónicos en README antes de referenciar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico [supuesto: aún persisten]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y malla curricular de Derecho para contexto.",
    "Agregar fuentes específicas de actividad en el .bib canónico de la asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como complemento temático, no reemplazo automático [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Aplicar unión-dedupe lossless en cada ciclo.",
    "Reusar reglas institucionales validadas sin bajar especificidad local.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener registro histórico de fuentes provisionales sin elevarlas a canónicas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-2: tema, semana y producto.",
    "Confirmar si existe plantilla obligatoria de secciones definida por docente.",
    "Confirmar estilo de citación institucional obligatorio [supuesto: no confirmado].",
    "Confirmar nombre canónico final del .bib de asignatura frente a tokens Slug.",
    "Confirmar si actividad-2 requiere bibliografía propia o reutiliza parte de la existente."
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
      "Problema jurídico o social.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos trazables.",
      "Asegurar coherencia entre consigna, desarrollo y cierre.",
      "Garantizar transferencia profesional del razonamiento jurídico."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones funcionales y trazables.",
      "Marcado explícito de supuestos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> análisis -> conclusión.",
      "Afirmación jurídica -> respaldo verificable -> interpretación propia.",
      "Consigna local -> adecuación de formato -> verificación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización estructurada",
        "Ejes editoriales troncales",
        "Integridad académica",
        "Trazabilidad cita-bibliografía",
        "Transferencia lateral controlada"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "Transferencia lateral controlada",
          "kind": "depends_on",
          "justification": "Sin JSON válido no hay propagación segura."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales troncales",
          "kind": "supports",
          "justification": "Define tono, propósito y criterios de cierre."
        },
        {
          "source": "Trazabilidad cita-bibliografía",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Permite auditar respaldo de afirmaciones."
        },
        {
          "source": "Ejes editoriales troncales",
          "target": "Actividad-2",
          "kind": "develops",
          "justification": "Son patrones reutilizables entre nodos hermanos."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica.",
        "Programa analítico: propósito y ejes de trabajo transferibles.",
        "Regla consolidada: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se deduplican reglas repetidas y se preserva cobertura útil completa.",
      "Ciclo 17: se refuerza transferencia por patrones, no por contenido específico de actividad-1.",
      "Ciclo 17: se mantiene estado provisional de fuentes no verificadas localmente."
    ]
  }
}