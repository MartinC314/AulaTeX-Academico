{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofía del Derecho con transferencia solo de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto local verificado para Derecho a la Seguridad Social.",
    "Se mantiene compresión lossless por deduplicación y unión sin recorte útil.",
    "Se fija secuencia editorial estable: problema, fundamento, análisis, evidencia, postura y cierre.",
    "Se mantiene bloqueo de propagación ante salida no estructurada o JSON inválido."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho y a Derecho a la Seguridad Social.",
    "Basar ubicación curricular en semestre 2, bloque 1, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Usar README y programa analítico locales como fuentes primarias.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto pedido en la consigna semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Adaptar salida a reporte, presentación u otro formato permitido por consigna."
  ],
  "activity_rules": [
    "Sustentar cada afirmación con fuente verificable y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Confirmar correspondencia exacta con consigna de Actividad 1.",
    "No asumir fuentes de otras semanas sin validación local."
  ],
  "quality_gates": [
    "Bloquear propagación si no hay JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Rechazar afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Normalizar respuestas no estructuradas antes de reutilizar.",
    "Verificar ajuste del producto a consigna local de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres canónicos de archivo según README local.",
    "Usar derecho-a-la-seguridad-social.bib como base canónica local.",
    "Corregir rutas o caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir en nombres de archivo si aparecieran [supuesto]."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normatividad vigente verificable.",
    "Registrar fuentes específicas de actividad en el .bib local.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar cpeum2026, lss2026 y lissste2026 cuando la consigna lo requiera."
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
    "Confirmar rúbrica específica de evaluación para calibrar profundidad.",
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
        "Carpeta de asignatura como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Derecho a la Seguridad Social.",
        "Semestre 2, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Fundamento normativo verificable.",
      "Análisis propio con postura.",
      "Evidencia trazable.",
      "Cierre profesional transferible."
    ],
    "reason_for_being": [
      "Transformar cada consigna en producto jurídico verificable.",
      "Asegurar trazabilidad entre consigna, fuentes, argumento y conclusión.",
      "Sostener continuidad editorial sin perder especificidad local."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones claras y trazables.",
      "Supuestos marcados explícitamente.",
      "Conclusión no descriptiva, sino argumentada."
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
          "justification": "Define el fundamento superior del derecho en la actividad."
        },
        {
          "source": "Ley del Seguro Social",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Operativiza cobertura y prestaciones del régimen aplicable."
        },
        {
          "source": "Ley del ISSSTE",
          "target": "Derecho a la seguridad social",
          "kind": "develops",
          "justification": "Regula protección social de personas servidoras públicas."
        },
        {
          "source": "Universalidad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Sirve para evaluar alcance real y barreras de acceso."
        },
        {
          "source": "Progresividad",
          "target": "Acceso, cobertura y justiciabilidad",
          "kind": "supports",
          "justification": "Permite analizar avances y posibles retrocesos normativos."
        }
      ],
      "evidence": [
        "README local: estructura canónica y control editorial.",
        "Programa analítico local: propósito y ejes de trabajo.",
        "derecho-a-la-seguridad-social.bib: base verificable de citas."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas de identidad, estructura, actividad y calidad.",
      "Se preservaron reglas útiles previas sin eliminación regresiva.",
      "Se reforzó transferencia lateral por patrones, sin copiar contenido temático exclusivo del origen.",
      "Se mantuvo política de supuestos y verificación local como control de riesgo editorial."
    ]
  }
}