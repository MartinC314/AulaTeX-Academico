{
  "summary": [
    "Se consolida refuerzo lateral desde actividad-1 a actividad-3 con deduplicación lossless.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se mantienen ejes editoriales estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene bloqueo de propagación sin JSON parseable y normalización previa obligatoria.",
    "Se evita transferencia de conclusiones específicas o bibliografía exclusiva del nodo hermano.",
    "Se agrega control de supuestos para datos no confirmados de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Registrar incidencias de parseo solo como metadato técnico."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Usar secuencia base: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar patrones válidos de actividad-1 sin copiar redacción literal.",
    "No transferir conclusiones específicas de actividad-1 a actividad-3.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas.",
    "Distinguir evidencia académica de antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir rutas y nombres solo con verificación local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README/programa y fijar nombre canónico.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Agregar al .bib solo entradas realmente citadas en actividad-3.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No reutilizar automáticamente bibliografía depurada de otra semana sin confirmar aplicabilidad.",
    "Conservar claves SCJN/UNAM solo si están efectivamente citadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar a nodos hermanos solo reglas reutilizables de identidad, estructura y calidad.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar compresión por unión y deduplicación sin pérdida semántica.",
    "Conservar bandera de riesgo cuando haya antecedentes de salida no estructurada.",
    "Si falta evidencia local, transferir plantilla base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido (reporte, presentación u otro).",
    "Confirmar rúbrica específica de evaluación para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de actividad-3.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-3 [supuesto].",
    "Confirmar nombre canónico final del .bib tras resolver token Slug."
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
      "Problema jurídico delimitado.",
      "Conceptos y marco normativo/doctrinal pertinente.",
      "Evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos trazables y útiles.",
      "Estandarizar calidad editorial sin perder especificidad por actividad.",
      "Garantizar propagación segura entre nodos mediante estructura validable."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas en orden lógico.",
      "Afirmación con evidencia y cita.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre profesional aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Problema jurídico",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Bibliografía verificable",
        "Política de supuestos"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
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
          "justification": "El análisis parte de una delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica con criterio propio.",
        "Programa analítico: ejes de trabajo y propósito de transformación del producto.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 97: deduplicación completa de reglas repetidas en destino.",
      "Ciclo 97: se refuerza transferencia lateral solo de patrones reutilizables.",
      "Ciclo 97: se excluye copia de conclusiones y bibliografía exclusiva del hermano.",
      "Ciclo 97: se mantiene no regresión y política de supuestos."
    ]
  }
}