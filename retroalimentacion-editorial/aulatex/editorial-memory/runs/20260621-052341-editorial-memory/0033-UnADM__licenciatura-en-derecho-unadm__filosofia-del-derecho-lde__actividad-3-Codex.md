{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se aplica compresión lossless por unión y deduplicación sin recorte útil.",
    "Se marcan como supuesto los datos locales no confirmados de la consigna de actividad-3."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda entrega.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar memorias Codex o GPT-Pro como antecedente editorial provisional, no fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal.",
    "No transferir conclusiones específicas entre nodos hermanos.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de reutilización aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación sensible.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar regla de no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir rutas o nombres solo con verificación local.",
    "Usar reporte o presentación según consigna confirmada."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar en .bib solo entradas realmente citadas.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con tema de actividad-3 [supuesto]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validación JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar bibliografía exclusiva ni conclusiones particulares de otra actividad.",
    "Propagar supuestos como supuestos, nunca como hechos.",
    "Mantener bandera de riesgo por antecedentes de parseo no estructurado.",
    "Aplicar unión-dedupe lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica específica para profundidad argumentativa.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica u otro tema.",
    "Confirmar archivo .tex principal canónico de actividad-3.",
    "Confirmar si la bibliografía depurada de Semana 7 aplica o se requiere .bib propio."
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
      "Problema jurídico o social bien delimitado.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a la planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Asegurar trazabilidad entre afirmaciones, fuentes y cierre argumentativo.",
      "Sostener una memoria editorial reutilizable sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas con orden lógico.",
      "Afirmaciones con cita verificable.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico transferible."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual y normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
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
        "Supuestos explícitos"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicabilidad]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica con criterio propio.",
        "Programa analítico: propósito y ejes de trabajo estables.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 33: deduplicación completa de reglas repetidas en origen y destino.",
      "Ciclo 33: se refuerza transferencia lateral sin copiar contenido específico de hermano.",
      "Ciclo 33: se conserva política de supuestos y no invención de fuentes.",
      "Ciclo 33: se mantiene no regresión y compresión lossless por unión."
    ]
  }
}