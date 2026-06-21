{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reusable desde Actividad 1.",
    "Se mantiene identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se preserva normalización obligatoria: sin JSON parseable no hay propagación.",
    "Se refuerzan ejes editoriales estables: problema, conceptos y fuentes, análisis propio, conclusión jurídica.",
    "Se aplica deduplicación lossless sin eliminar reglas útiles previas.",
    "Se restringe transferencia a patrones generales; sin copiar conclusiones ni bibliografía exclusiva del nodo hermano."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en toda salida.",
    "Vincular actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto pedido en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad hermana.",
    "No copiar redacción literal ni conclusiones específicas de Actividad 1.",
    "Incluir postura argumentada del estudiante; evitar resumen descriptivo puro.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, tema o formato de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado si la salida no es JSON parseable.",
    "Validar esquema completo antes de propagar recursivamente.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Confirmar trazabilidad entre afirmaciones, citas y .bib.",
    "Marcar afirmaciones no verificadas como [supuesto].",
    "Distinguir fuentes académicas y normativas de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como [supuesto] que el .bib canónico es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo fuentes realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar al .bib solo entradas citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente o URL.",
    "No trasladar bibliografía exclusiva de una actividad hermana sin validación local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos reglas institucionales y de calidad comunes.",
    "No propagar supuestos como hechos confirmados.",
    "Cuando falte dato local, propagar plantilla base y preguntas abiertas.",
    "Mantener compresión por unión y deduplicación lossless.",
    "Registrar en bitácora cada refuerzo lateral aplicado en ciclo."
  ],
  "open_questions": [
    "[supuesto] Falta consigna textual exacta de Actividad 3.",
    "Confirmar formato requerido: reporte, presentación u otro.",
    "Confirmar rúbrica específica para ajustar profundidad argumentativa.",
    "Confirmar bibliografía obligatoria propia de Actividad 3.",
    "Confirmar si la bibliografía depurada de Semana 7 aplica o no a Actividad 3.",
    "Confirmar archivo .tex principal canónico para esta actividad."
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
      "Problema jurídico o social como detonante.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en entregables académicos sólidos.",
      "Asegurar claridad, fundamento jurídico, evidencia y transferencia profesional."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicación condicionada]"
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
          "target": "Integridad académica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay trazabilidad editorial confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis se construye desde un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La verificabilidad evita invención y fortalece el rigor."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica propia.",
        "Programa analítico: propósito y ejes de trabajo de la asignatura.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 87: refuerzo lateral aplicado desde Actividad 1 hacia Actividad 3.",
      "Se consolidaron reglas comunes sin copiar contenido específico de hermano.",
      "Se deduplicaron variantes ortográficas y de acentuación sin pérdida semántica.",
      "Se mantuvo política de [supuesto] para vacíos de consigna local.",
      "Se preservó no regresión en identidad, estructura, calidad, LaTeX y bibliografía."
    ]
  }
}