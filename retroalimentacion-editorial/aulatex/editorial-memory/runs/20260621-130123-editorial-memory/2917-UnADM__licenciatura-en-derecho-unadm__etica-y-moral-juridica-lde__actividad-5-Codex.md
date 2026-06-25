{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofía del Derecho a Ética y Moral jurídica con patrones reutilizables.",
    "Se preserva identidad UnADM, estructura base y control de calidad sin copiar contenido temático específico del origen.",
    "Se consolida compresión lossless por deduplicación semántica y normalización JSON obligatoria.",
    "Se mantiene regla de marcar supuestos cuando falte consigna local verificable.",
    "Se integra trazabilidad de incidencias técnicas locales: tokens Slug sin expandir y posible truncamiento en .bib [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular toda entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Alinear actividad al contexto de Ética y Moral jurídica sin importar patrones de otra materia.",
    "Marcar como supuesto cualquier dato no visible en consigna o rúbrica local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Registrar ruta origen-destino en cada injerto de memoria editorial."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido y parseable según esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Aplicar compresión lossless por unión y deduplicación, sin recorte.",
    "Definir objetivo puntual antes del desarrollo.",
    "Mantener secuencia editorial: problema, conceptos, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por planeación semanal."
  ],
  "activity_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No arrastrar conclusiones específicas de Filosofía del Derecho a Ética y Moral jurídica.",
    "Verificar consigna textual exacta de Actividad 5 antes de fijar alcance final."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de propagar.",
    "Confirmar que no se eliminen reglas útiles previas al fusionar.",
    "Validar ausencia de duplicados semánticos después de fusionar.",
    "Confirmar respaldo o marca de supuesto en afirmaciones no evidentes.",
    "Validar correspondencia entre citas en texto y entradas del .bib.",
    "Normalizar manualmente cualquier salida no estructurada antes de reutilizar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir rutas o nombres con caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor o editor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Marcar para revisión manual entradas potencialmente duplicadas por autor+título+año.",
    "Supuesto: el archivo .bib local puede estar truncado; validar archivo real antes de editar."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura completa.",
    "Transferir patrones editoriales generales, no redacción literal ni conclusiones de la materia origen.",
    "Mantener analogía controlada: forma y calidad sí, contenido temático específico no.",
    "Reducir repetición de incidencias por ciclo con una regla plantilla única.",
    "Escalar a validación manual si persisten fallos de parseo en ciclos consecutivos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar tipo de producto final requerido en la semana.",
    "Confirmar política local de depuración de claves BibTeX duplicadas sin perder trazabilidad.",
    "Confirmar si el truncamiento observado en etica-y-moral-juridica.bib existe en el archivo real [supuesto]."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Reflexivo ante dilemas ético-jurídicos."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad de memoria editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura destino: Ética y Moral jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos.",
      "Asegurar coherencia entre forma, evidencia y argumentación.",
      "Preservar continuidad editorial entre nodos sin contaminación temática."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones explícitas y ordenadas.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explícito de supuestos.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Conectar marco normativo o doctrinal.",
      "Desarrollar análisis crítico propio.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Deduplicación lossless",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Analogía controlada entre asignaturas"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Normalización JSON",
          "target": "Deduplicación lossless",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay consolidación confiable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere respaldo documental."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión profesional emerge del razonamiento crítico."
        },
        {
          "source": "Analogía controlada entre asignaturas",
          "target": "Conclusión jurídica transferible",
          "kind": "contrasts",
          "justification": "Se transfieren patrones formales, no conclusiones temáticas del origen."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y conclusión jurídica con criterio propio.",
        "Programa analítico: ejes problema-conceptos-producto-análisis-conclusión.",
        "README/programa: token Slug sin expandir visible.",
        "Bib local: duplicados de claves por misma obra y posible truncamiento final [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: se refuerza estructura editorial transversal sin copiar contenido específico de Filosofía del Derecho.",
      "Ciclo 4: se conserva regla de bloqueo por JSON no parseable.",
      "Ciclo 4: se consolida deduplicación semántica en reglas repetidas.",
      "Ciclo 4: se mantiene trazabilidad de supuestos e incidencias técnicas locales."
    ]
  }
}