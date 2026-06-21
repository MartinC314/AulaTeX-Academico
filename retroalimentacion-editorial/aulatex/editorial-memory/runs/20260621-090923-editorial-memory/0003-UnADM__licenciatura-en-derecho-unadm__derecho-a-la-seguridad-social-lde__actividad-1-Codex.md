{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofía del Derecho con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto local de Derecho a la Seguridad Social.",
    "Se mantiene secuencia editorial estable: problema, fundamento, análisis, evidencia, postura y cierre.",
    "Se conserva regla de normalización estricta: bloquear salidas no estructuradas o JSON inválido.",
    "Se aplica compresión lossless por deduplicación sin recorte de reglas útiles."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM, formal y jurídico.",
    "Vincular la actividad a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Basar ubicación curricular en semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar README y programa analítico locales como fuente primaria.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato al producto exacto pedido en la planeación.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Sustentar cada afirmación con fuente verificable y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Validar que el producto coincide con la consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin confirmar pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si no hay JSON parseable.",
    "Validar estructura mínima completa antes de reutilizar.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y .bib.",
    "Normalizar respuestas no estructuradas antes de propagar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres canónicos de archivos según README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canónica local.",
    "Corregir rutas o caracteres anómalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes específicas de actividad en el .bib local.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar cpeum2026, lss2026 y lissste2026 solo cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad y patrones argumentativos.",
    "No copiar redacción literal, conclusiones ni bibliografía exclusiva entre nodos hermanos.",
    "Aplicar analogía controlada: primero calidad e identidad, luego estructura y conceptos.",
    "Preservar reglas previas útiles y agregar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si el formato requerido es reporte, presentación o mixto.",
    "Confirmar rúbrica específica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana.",
    "Confirmar si se exige jurisprudencia específica en esta actividad."
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
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Producto jurídico verificable centrado en problema, fundamento y análisis.",
      "Uso de marco constitucional, legal e institucional de seguridad social.",
      "Postura propia sustentada y cierre profesional transferible."
    ],
    "reason_for_being": [
      "Convertir consignas semanales en entregables sólidos, verificables y útiles para práctica jurídica.",
      "Asegurar trazabilidad entre consigna, fuentes, análisis y conclusión."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones claras y auditables.",
      "Supuestos marcados de forma visible.",
      "Conclusión no descriptiva, con implicación jurídica."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> análisis -> evidencia -> conclusión.",
      "Regla general -> contraste contextual -> postura -> implicación práctica.",
      "Pregunta guía -> criterios jurídicos -> inferencia razonada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho a la seguridad social",
        "Marco constitucional",
        "Ley del Seguro Social",
        "Ley del ISSSTE",
        "Universalidad",
        "Progresividad",
        "Igualdad y no discriminación",
        "Acceso, cobertura y justiciabilidad"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024",
        "cpeum2026",
        "lss2026",
        "lissste2026"
      ],
      "relations": [
        {
          "source": "Marco constitucional",
          "target": "Derecho a la seguridad social",
          "kind": "supports",
          "justification": "Define fundamento de validez y exigibilidad del derecho."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Operativiza prestaciones y mecanismos institucionales."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula cobertura para personas servidoras públicas."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar alcance real del derecho."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite analizar avances y no regresividad."
        }
      ],
      "evidence": [
        "README local de la asignatura.",
        "Programa analítico local.",
        "derecho-a-la-seguridad-social.bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se deduplican reglas repetidas y se conservan todas las válidas.",
      "Ciclo 3: se mantiene bloqueo por JSON inválido como puerta de calidad crítica.",
      "Ciclo 3: se refuerza transferencia lateral sin arrastre temático exclusivo de Filosofía del Derecho.",
      "Ciclo 3: se preserva base bibliográfica local y uso condicionado por consigna."
    ]
  }
}