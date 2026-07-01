{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con base reusable de Actividad 1.",
    "Se preservan reglas institucionales UnADM, estructura mínima y control de calidad.",
    "Se aplica deduplicación lossless sin recorte de reglas útiles previas.",
    "Se mantiene normalización obligatoria de salidas antes de propagación recursiva.",
    "Se refuerza política de supuestos cuando falte consigna local verificable."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente académica.",
    "Registrar incidencias de parseo como trazabilidad técnica, no como evidencia disciplinar.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas del nodo hermano sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva del hermano.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante, evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, tema o formato de Actividad 3 sin evidencia local.",
    "Registrar diferencias específicas de Actividad 3 como supuestos hasta confirmación oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Aplicar regla de no regresión: no eliminar reglas útiles previas.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas.",
    "Distinguir fuentes académicas, normativas, jurisprudenciales y antecedentes editoriales."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin justificación verificable.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Verificar nombres de archivo del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No asumir que filosofia-del-derecho-clean.bib aplica a Actividad 3 sin confirmación.",
    "Supuesto: filosofia-del-derecho-clean.bib está orientado a Interpretación jurídica (Semana 7)."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad y relaciones recurrentes.",
    "Evitar propagar contenido específico no confirmado localmente.",
    "Conservar bandera de riesgo cuando exista historial de salida no estructurada.",
    "Aplicar compresión por unión y deduplicación lossless en cada ciclo.",
    "Propagar reglas de Filosofía del Derecho solo a nodos de la misma asignatura.",
    "No propagar supuestos como hechos confirmados."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 3.",
    "Confirmar si Actividad 3 corresponde a interpretación jurídica o a otro tema.",
    "Confirmar archivo .tex principal de Actividad 3.",
    "Confirmar nombre canónico final del .bib de la asignatura."
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
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por planeación.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico verificable.",
      "Garantizar trazabilidad entre afirmaciones, fuentes y cierre jurídico.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminación de contenido específico."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas con orden lógico.",
      "Citas verificables en afirmaciones relevantes.",
      "Supuestos marcados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión jurídica.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Estructura mínima de actividad",
        "Supuestos explícitos",
        "Bibliografía verificable",
        "No regresión editorial"
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
          "source": "Estructura mínima de actividad",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre sólido depende de problema, marco y análisis previo."
        },
        {
          "source": "Supuestos explícitos",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita inventar datos cuando falta evidencia local."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Sostiene trazabilidad de afirmaciones."
        }
      ],
      "evidence": [
        "README establece identidad UnADM, integridad académica y conclusión jurídica.",
        "Programa analítico define ejes: problema, conceptos, producto, análisis y conclusión.",
        "Historial técnico confirma necesidad de normalización por salidas no parseables.",
        "Token Slug sin expandir en README/programa requiere saneamiento previo."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas equivalentes con conservación semántica.",
      "Se preservaron reglas útiles de Actividad 1 y del destino sin regresión.",
      "Se reforzó separación entre memoria editorial y evidencia académica.",
      "Se añadió control explícito de transferencia lateral: reutilizar patrón, no contenido específico.",
      "Se mantuvieron supuestos abiertos donde faltan datos locales verificables."
    ]
  }
}