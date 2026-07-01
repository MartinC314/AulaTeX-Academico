{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofía del Derecho hacia Ética y Moral Jurídica con deduplicación lossless.",
    "Se preservan reglas institucionales, estructurales y de calidad reutilizables entre asignaturas hermanas.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se incorporan mejoras verificables del contexto local: corrección de tokens Slug y rutas con caracteres anómalos.",
    "Se evita transferir redacción literal, conclusiones específicas y bibliografía exclusiva del nodo origen."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura destino como punto de entrada canónico.",
    "Marcar como [Supuesto] cualquier dato no visible en la consigna local de Actividad 1.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Registrar trazabilidad de consolidación con ruta origen, destino, relación y ciclo."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido y parseable conforme al esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Aplicar compresión lossless por unión y deduplicación, no por recorte.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear la entrega al producto solicitado por la planeación semanal."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Verificar correspondencia exacta del producto con la consigna de Actividad 1.",
    "No asumir fuentes de semanas posteriores sin confirmación local.",
    "Integrar fundamento jurídico, evidencia y transferencia profesional en cada producto."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresiones: no eliminar reglas útiles previas durante consolidación."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar etica-y-moral-juridica.bib como archivo canónico local tras resolver Slug. [Supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Deduplicar claves bibliográficas duplicadas sin perder trazabilidad de citas existentes."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No transferir bibliografía exclusiva ni conclusiones temáticas del nodo hermano.",
    "Si falta consigna textual local, propagar estructura base y abrir preguntas en lugar de inventar contenido.",
    "Mantener bitácora de supuestos por ciclo para auditoría editorial."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Ética y Moral Jurídica.",
    "Confirmar formato solicitado: reporte, presentación u otro producto.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Confirmar criterio canónico para conservar una sola clave por obra duplicada en etica-y-moral-juridica.bib.",
    "Confirmar si las claves citadas en .tex migrarán a claves normalizadas o se mantendrán alias de compatibilidad."
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
        "Trazabilidad de fuentes y supuestos."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura destino: Ética y Moral Jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social bien delimitado.",
      "Conceptos y marco normativo o doctrinal pertinentes.",
      "Análisis propio sustentado en evidencia verificable.",
      "Conclusión jurídica transferible a la práctica.",
      "Disciplina editorial: estructura, trazabilidad y calidad técnica."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos académicos sólidos y verificables.",
      "Garantizar continuidad editorial entre nodos laterales sin perder identidad local.",
      "Preservar memoria útil mediante deduplicación semántica y control de supuestos."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secuencia argumentativa estable problema-marco-análisis-cierre.",
      "Diferenciación clara entre síntesis y postura personal.",
      "Cierre con implicación jurídica práctica.",
      "Etiquetado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema inicial breve -> conceptos clave -> fundamento normativo/doctrinal -> análisis propio -> conclusión transferible.",
      "Afirmación jurídica -> evidencia verificable -> interpretación razonada -> implicación práctica.",
      "Comparación de posturas éticas -> criterio jurídico aplicado -> toma de posición argumentada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Deduplicación bibliográfica",
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
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta delimitada."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión profesional exige fundamento verificable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura."
        },
        {
          "source": "Deduplicación bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Reduce ambigüedad de citas sin pérdida de información."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicación curricular.",
        "Programa analítico local define propósito y ejes de trabajo.",
        "Memoria origen aporta reglas reutilizables de estructura, calidad y propagación.",
        "Bibliografía local evidencia duplicidad de claves que requiere política de deduplicación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: se refuerzan reglas comunes de identidad, estructura y calidad desde nodo lateral.",
      "Ciclo 1: se mantiene bloqueo por JSON no parseable como compuerta obligatoria.",
      "Ciclo 1: se agrega mejora verificable local sobre resolución de tokens Slug y rutas anómalas.",
      "Ciclo 1: se preserva no transferencia de bibliografía exclusiva del origen."
    ]
  }
}