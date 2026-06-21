{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con deduplicación lossless y sin recortes.",
    "Se preserva ADN UnADM: identidad institucional, integridad académica y cierre jurídico con criterio propio.",
    "Se refuerza regla crítica: no propagar sin JSON parseable y estructura mínima completa.",
    "Se mantienen ejes editoriales recurrentes: problema, conceptos y fuentes, análisis propio, conclusión jurídica.",
    "Se conserva política de supuestos para datos no confirmados de la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables desde actividad-1.",
    "No copiar redacción literal ni conclusiones específicas entre nodos hermanos.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Validar esquema completo antes de aplicar aguas abajo.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [supuesto].",
    "Distinguir fuentes académicas y normativas de antecedentes editoriales.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como [supuesto] el .bib canónico filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo entradas efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como [supuesto] de uso condicionado por coincidencia temática."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos reglas de identidad, estructura, calidad y trazabilidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresión por unión y deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo en nodos con historial de salida no estructurada.",
    "Si falta consigna textual, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega de actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica específica de evaluación para actividad-3.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica o a otra unidad.",
    "Confirmar nombre canónico final del archivo .bib de la asignatura."
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
        "Filosofía del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Sostener argumentación jurídica con evidencia y criterio propio.",
      "Garantizar continuidad editorial entre actividades sin perder calidad."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas y orden lógico.",
      "Trazabilidad afirmación-cita.",
      "Supuestos etiquetados.",
      "Cierre profesional aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad académica",
        "Normalización JSON",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable",
        "Política de supuestos"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis surge de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README fija identidad UnADM e integridad académica.",
        "Programa analítico define propósito y ejes de trabajo.",
        "Historial local confirma necesidad de normalización previa por parseo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: deduplicación total de reglas repetidas sin pérdida semántica.",
      "Ciclo 9: se conserva no regresión y bloqueo por JSON inválido.",
      "Ciclo 9: se refuerza transferencia lateral por patrones, no por contenido literal.",
      "Ciclo 9: se mantienen supuestos abiertos donde faltan datos locales."
    ]
  }
}