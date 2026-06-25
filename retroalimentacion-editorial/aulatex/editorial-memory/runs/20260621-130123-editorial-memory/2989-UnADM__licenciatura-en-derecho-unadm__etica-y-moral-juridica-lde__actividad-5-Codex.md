{
  "summary": [
    "Se refuerza transferencia lateral con patrones reutilizables y sin copiar contenido temático de Filosofía del Derecho.",
    "Se conserva la identidad UnADM y el marco curricular de Derecho como regla estable.",
    "Se consolida normalización obligatoria: solo JSON parseable, deduplicación lossless y trazabilidad de supuestos.",
    "Se mantienen ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se integra mejora verificable local: controlar tokens Slug sin expandir en README y programa analítico.",
    "Se integra mejora verificable local: tratar el .bib como fuente activa con revisión de duplicados y truncamientos [supuesto]."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular cada entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no parseables como provisionales hasta validación manual.",
    "No promover reglas provisionales a canon sin evidencia local."
  ],
  "structure_rules": [
    "Responder en JSON válido y parseable según esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar reglas útiles previas y agregar solo mejoras verificables.",
    "Aplicar compresión lossless por unión y deduplicación, sin recorte.",
    "Estructurar actividades en: objetivo, problema, conceptos, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "No arrastrar conclusiones específicas de otra asignatura sin justificación local."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de propagar recursivamente.",
    "Confirmar que no se eliminen reglas útiles previas al fusionar.",
    "Validar ausencia de duplicados semánticos tras la fusión.",
    "Confirmar respaldo o marca [supuesto] en afirmaciones no evidentes.",
    "Validar correspondencia entre citas en texto y entradas .bib."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Corregir rutas o nombres con caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor/editor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Marcar para revisión manual entradas potencialmente duplicadas por autor+título+año.",
    "Verificar truncamientos y cierre de entradas BibTeX antes de compilar [supuesto]."
  ],
  "propagation_hints": [
    "Propagar solo patrones generales reutilizables en saltos laterales.",
    "Evitar copiar redacción literal, conclusiones específicas o bibliografía exclusiva de nodos hermanos.",
    "Mantener trazabilidad de origen y destino por ciclo.",
    "Aplicar normalización manual cuando un nodo entregue salida no estructurada.",
    "Usar analogía controlada: transferir método, no contenido temático cerrado."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica específica para calibrar profundidad argumentativa.",
    "Confirmar tipo de producto final (reporte, presentación u otro).",
    "Confirmar política local para depurar claves BibTeX duplicadas sin perder trazabilidad.",
    "Confirmar si el truncamiento en etica-y-moral-juridica.bib existe en archivo real [supuesto]."
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
        "Trazabilidad de memoria editorial y fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura destino: Ética y Moral jurídica.",
        "Actividad destino: Actividad 5."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo/doctrinal pertinente.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos jurídicos con calidad verificable.",
      "Preservar continuidad editorial entre actividades sin contaminar contenidos específicos.",
      "Garantizar salidas reutilizables por estructura, no por improvisación."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones ordenadas y consistentes.",
      "Citas explícitas en afirmaciones sustantivas.",
      "Marcado explícito de [supuesto] cuando falten datos.",
      "Cierre con criterio jurídico propio y aplicable."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Relacionar marco normativo o doctrinal.",
      "Desarrollar análisis crítico propio.",
      "Concluir con implicación jurídica práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Normalización JSON",
        "Deduplicación lossless",
        "Trazabilidad de supuestos"
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
          "justification": "La pauta institucional exige evidencia y trazabilidad."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura argumentada requiere respaldo consultable."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión práctica deriva del razonamiento."
        },
        {
          "source": "Normalización JSON",
          "target": "Deduplicación lossless",
          "kind": "depends_on",
          "justification": "La compresión segura exige estructura parseable."
        },
        {
          "source": "Trazabilidad de supuestos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Distinguir hechos de supuestos evita sobreafirmaciones."
        }
      ],
      "evidence": [
        "README local establece identidad UnADM, integridad académica y conclusión jurídica.",
        "Programa analítico local define ejes problema-conceptos-producto-análisis-conclusión.",
        "README y programa muestran token Slug sin expandir, mejora técnica verificable.",
        "Archivo .bib local contiene duplicados de obras y posible truncamiento final [supuesto]."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: se reforzó transferencia lateral por método editorial común.",
      "Ciclo 22: se preservaron reglas útiles previas sin eliminación.",
      "Ciclo 22: se deduplicaron reglas redundantes en una versión canónica.",
      "Ciclo 22: se añadieron controles verificables de Slug y .bib local."
    ]
  }
}