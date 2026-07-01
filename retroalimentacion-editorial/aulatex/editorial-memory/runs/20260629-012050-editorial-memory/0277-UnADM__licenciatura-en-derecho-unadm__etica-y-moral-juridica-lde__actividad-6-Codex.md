{
  "summary": [
    "Se refuerza memoria lateral con patrones reutilizables entre Filosofía del Derecho y Ética y Moral jurídica.",
    "Se mantiene compresión lossless por deduplicación semántica sin recorte de reglas útiles.",
    "Se preserva identidad UnADM, estructura por ejes y control de calidad parseable.",
    "Se agregan mejoras verificables desde README, programa analítico y .bib local de destino.",
    "Se conserva trazabilidad de fallas históricas de parseo como contexto no operativo."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como punto de entrada canónico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Usar tono académico-jurídico claro y cerrar con criterio propio argumentado."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar solo resumen descriptivo.",
    "Verificar correspondencia entre consigna de Actividad 6 y producto final.",
    "Traducir el análisis a implicaciones de práctica jurídica cuando proceda.",
    "Evitar afirmaciones sin respaldo o sin marca [Supuesto].",
    "No transferir conclusiones específicas de actividades hermanas."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalización manual.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas útiles previas en cada fusión.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Validar consistencia entre objetivo, estructura y cierre argumentativo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener secciones claras y estables para compilación y reutilización.",
    "Evitar paquetes o comandos no justificados por la consigna.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres de archivo con caracteres anómalos detectados en README."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni completar metadatos sin respaldo.",
    "Conservar metadatos mínimos: autor/editor, título, año y fuente editorial o URL.",
    "Deduplicar obras equivalentes por clave canónica sin perder trazabilidad.",
    "Bloquear cita operativa de entradas truncadas hasta completar campos mínimos."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir solo patrones generales: identidad, estructura, calidad y método argumentativo.",
    "Evitar copiar redacción literal y bibliografía exclusiva de nodo hermano.",
    "Aplicar analogía controlada: mantener forma editorial y adaptar contenido a consigna local.",
    "Conservar trazabilidad de supuestos y fuentes provisionales en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar formato principal requerido: reporte, presentación u otro.",
    "Confirmar rúbrica específica de evaluación para calibrar profundidad argumentativa.",
    "Definir clave canónica oficial para deduplicación .bib en la asignatura.",
    "[Supuesto] Confirmar y reparar entrada truncada sierraUniversidadNacional1910 en .bib local."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Orientado a evidencia verificable."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Ética y Moral jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo/doctrinal pertinente.",
      "Análisis propio con evidencia.",
      "Conclusión jurídica transferible.",
      "Control de calidad estructural y bibliográfico."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos trazables.",
      "Mantener coherencia entre identidad institucional y rigor argumentativo.",
      "Garantizar propagación segura de memoria editorial entre nodos."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y trazables.",
      "Postura personal argumentada.",
      "Marca [Supuesto] ante vacíos.",
      "Cierre aplicable a práctica jurídica."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco.",
      "Sustentar con fuentes verificables.",
      "Analizar con criterio propio.",
      "Concluir con implicación práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Cita verificable",
        "Normalización estructurada",
        "Deduplicación bibliográfica",
        "Problema jurídico o social",
        "Análisis propio",
        "Conclusión transferible",
        "Ética y moral jurídica"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "etica-y-moral-juridica.bib",
        "programa-analitico-etica-y-moral-juridica.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono académico-jurídico",
          "kind": "supports",
          "justification": "La pauta editorial exige consistencia institucional."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "Los ejes de trabajo ordenan este flujo argumentativo."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión transferible",
          "kind": "depends_on",
          "justification": "La conclusión válida deriva del análisis sustentado."
        },
        {
          "source": "Integridad académica",
          "target": "Cita verificable",
          "kind": "depends_on",
          "justification": "No hay validez editorial sin soporte trazable."
        },
        {
          "source": "Normalización estructurada",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Solo memoria parseable debe propagarse."
        },
        {
          "source": "Deduplicación bibliográfica",
          "target": "Calidad de citación",
          "kind": "supports",
          "justification": "Reduce ambigüedad y errores de claves."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión con criterio propio.",
        "Programa analítico local: ejes problema-conceptos-producto-análisis-conclusión.",
        ".bib local: duplicados verificables y entrada truncada detectable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se transfieren patrones transversales de Filosofía del Derecho sin copiar contenido específico.",
      "Se deduplican reglas repetidas y se conservan todas las útiles.",
      "Se refuerza gate de JSON parseable como condición de propagación recursiva.",
      "Se consolida regla de [Supuesto] para vacíos de consigna.",
      "Se mantiene foco en calidad bibliográfica con deduplicación y bloqueo de entradas truncadas."
    ]
  }
}