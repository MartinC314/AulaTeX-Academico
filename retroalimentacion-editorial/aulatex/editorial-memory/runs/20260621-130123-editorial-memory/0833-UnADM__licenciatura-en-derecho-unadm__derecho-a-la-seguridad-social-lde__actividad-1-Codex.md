{
  "summary": [
    "Se consolida refuerzo lateral ciclo 11 con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto local verificado en README y programa analítico.",
    "Se mantiene compresión lossless por deduplicación, sin recorte de reglas útiles.",
    "Se refuerza secuencia editorial estable: problema, fundamento, análisis, evidencia, postura y cierre.",
    "Se mantiene bloqueo de propagación para salidas no estructuradas o JSON inválido."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Basar ubicación curricular en semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar README y programa analítico locales como fuentes primarias de identidad.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato y extensión al producto solicitado en la consigna semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Adaptar salida a reporte, presentación o formato mixto solo si la consigna lo permite."
  ],
  "activity_rules": [
    "Sustentar cada afirmación con fuente verificable y cita explícita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Verificar correspondencia exacta del producto con la consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validación de pertinencia local."
  ],
  "quality_gates": [
    "Bloquear propagación si no hay JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Validar ajuste del producto a la consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres canónicos de archivo según README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canónica local.",
    "Corregir rutas o caracteres anómalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes específicas de actividad en el .bib local.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Usar cpeum2026, lss2026 y lissste2026 cuando la consigna los requiera."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir lateralmente solo identidad, estructura, calidad y patrones argumentativos.",
    "No copiar redacción literal, conclusiones ni bibliografía exclusiva entre nodos hermanos.",
    "Aplicar analogía controlada: primero reglas institucionales y calidad, luego estructura y conceptos.",
    "Preservar reglas útiles previas y sumar solo mejoras verificables."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 1; confirmar entregable exacto.",
    "Confirmar si el formato requerido es reporte, presentación o mixto.",
    "Confirmar rúbrica específica de evaluación para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana en planeación local.",
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
        "Control editorial desde la carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social contextualizado.",
      "Fundamento constitucional y legal verificable.",
      "Análisis propio con postura sustentada.",
      "Evidencia trazable en citas y .bib.",
      "Cierre profesional transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar cada consigna en un producto jurídico verificable.",
      "Conservar coherencia entre identidad institucional, calidad técnica y valor argumentativo.",
      "Garantizar transferencia lateral sin contaminación temática entre asignaturas."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Marcado explícito de supuestos.",
      "Postura personal sustentada.",
      "Conclusión jurídica no descriptiva."
    ],
    "argumentative_patterns": [
      "Problema -> fundamento normativo -> análisis -> evidencia -> conclusión.",
      "Regla general -> contraste con contexto -> postura -> implicación práctica.",
      "Pregunta guía -> criterios jurídicos -> inferencia razonada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Derecho a la seguridad social",
        "Marco constitucional en México",
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
          "source": "Marco constitucional en México",
          "target": "Derecho a la seguridad social",
          "kind": "supports",
          "justification": "Define el fundamento superior del derecho y sus límites de interpretación."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Operativiza prestaciones, sujetos y mecanismos de protección."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula cobertura y prestaciones para personas servidoras públicas."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite evaluar exclusiones y brechas de acceso."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite valorar avances y prohibición de retrocesos."
        }
      ],
      "evidence": [
        "README local: estructura canónica y control editorial.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "derecho-a-la-seguridad-social.bib: base verificable vigente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicación integral de reglas repetidas sin pérdida semántica.",
      "Ciclo 11: se preservan puertas de calidad y bloqueo por JSON inválido.",
      "Ciclo 11: se mantiene transferencia lateral controlada sin copiar contenido exclusivo del nodo origen.",
      "Ciclo 11: se conserva trazabilidad de fuentes locales y marcación de supuestos."
    ]
  }
}