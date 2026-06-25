{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular verificado en README y programa analítico.",
    "Se refuerzan ejes estables: problema, conceptos/fuentes, análisis propio y conclusión jurídica.",
    "Se mantiene normalización JSON obligatoria antes de propagación recursiva.",
    "Se aplica deduplicación lossless sin recorte ni regresión de reglas útiles.",
    "Se mantiene política de supuestos para datos no confirmados de actividad-3."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] todo dato no visible en la consigna local.",
    "Tratar memorias Codex/GPT-Pro como antecedente editorial provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal.",
    "No transferir conclusiones específicas de un hermano a otro.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de reutilizar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Marcar afirmaciones sin respaldo como [supuesto] o retirarlas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar regla de no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación correcta de español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir rutas y nombres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar reporte o presentación según consigna confirmada."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Agregar al .bib solo entradas realmente citadas.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la actividad [supuesto condicionado].",
    "No usar memoria editorial como bibliografía académica."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir a hermanos solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar contenido temático específico no confirmado localmente.",
    "Conservar bandera de riesgo cuando exista antecedente de parseo fallido.",
    "Aplicar unión + deduplicación lossless en cada ciclo.",
    "Escalar preguntas abiertas cuando falte consigna oficial."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega de actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica de actividad-3.",
    "Confirmar bibliografía obligatoria de la semana de actividad-3.",
    "Confirmar si filosofia-del-derecho-clean.bib aplica a actividad-3 [supuesto].",
    "Confirmar nombre canónico final del .bib de asignatura tras resolver Slug."
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
      "Problema jurídico o social delimitado.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto alineado a planeación semanal.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Asegurar fundamento jurídico, evidencia y transferencia profesional.",
      "Estandarizar calidad editorial entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
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
        "Bibliografía verificable",
        "Supuestos explícitos"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
      ],
      "relations": [
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no hay transferencia confiable."
        },
        {
          "source": "Identidad UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
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
        "README: identidad UnADM, integridad académica y conclusión jurídica.",
        "Programa analítico: ejes problema-conceptos-producto-análisis-conclusión.",
        "Regla persistente: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicación completa de reglas repetidas con conservación total.",
      "Ciclo 14: se refuerza transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 14: se preserva política de supuestos para evitar invención de consigna o fuentes.",
      "Ciclo 14: se mantiene no regresión sobre calidad, LaTeX y bibliografía."
    ]
  }
}