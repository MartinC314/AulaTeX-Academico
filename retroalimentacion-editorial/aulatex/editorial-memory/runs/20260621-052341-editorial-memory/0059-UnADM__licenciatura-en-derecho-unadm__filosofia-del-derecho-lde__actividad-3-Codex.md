{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con patrones reutilizables de actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, análisis propio, conclusión jurídica.",
    "Se aplica deduplicación lossless sin recorte de reglas útiles.",
    "Supuesto: la consigna específica de actividad-3 sigue no visible localmente."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias Codex o GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Registrar incidencias de parseo como metadato técnico, no como evidencia disciplinar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas entre actividades hermanas sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva sin evidencia local.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin confirmación local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir fuentes académicas, normativas, jurisprudenciales y antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad verificada.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar al .bib solo fuentes realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Semana 7 y requiere validación para actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir a nodos hermanos solo patrones generales reutilizables.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión y deduplicación lossless en cada ciclo.",
    "Preservar banderas de riesgo por antecedentes de salida no estructurada.",
    "Reforzar reglas institucionales sin perder especificidad local."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica específica para calibrar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de actividad-3.",
    "Confirmar si aplica bibliografía de interpretación jurídica o se requiere .bib propio.",
    "Confirmar nombre canónico final del archivo .bib en la asignatura."
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
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y transferencia profesional.",
      "Convertir consigna en estructura argumentativa verificable y evaluable.",
      "Mantener continuidad editorial entre actividades sin pérdida de calidad."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas con orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y marco -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo consistente -> cierre transferible."
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
          "justification": "La pauta institucional exige trazabilidad de fuentes y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay auditoría editorial confiable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de una delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La verificabilidad evita invención de fuentes."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: ejes de trabajo y propósito editorial.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Contexto local: token Slug sin expandir detectado en README y programa."
      ]
    },
    "reinforcement_log": [
      "Ciclo 59: refuerzo lateral aplicado por analogía controlada entre hermanos.",
      "Se conservaron reglas previas útiles y se eliminaron duplicados semánticos.",
      "Se añadió control explícito de no transferencia de conclusiones o bibliografía exclusiva.",
      "Se mantuvo política de supuestos para datos no visibles.",
      "Se reforzó compatibilidad LaTeX y trazabilidad bibliográfica sin inventar fuentes."
    ]
  }
}