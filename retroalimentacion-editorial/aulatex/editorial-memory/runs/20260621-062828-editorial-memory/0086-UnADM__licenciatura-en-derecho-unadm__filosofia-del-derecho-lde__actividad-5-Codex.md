{
  "summary": [
    "Se consolida memoria lateral de Actividad 5 con deduplicación lossless y sin recorte de reglas útiles.",
    "Se preserva identidad UnADM y encuadre curricular de Filosofía del Derecho en Licenciatura en Derecho.",
    "Se mantiene el núcleo editorial: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se refuerza la regla de propagación: solo patrones reutilizables; sin copiar conclusiones ni bibliografía exclusiva entre actividades hermanas.",
    "Se confirma riesgo histórico de parseo y se mantiene compuerta estricta de JSON antes de propagación recursiva.",
    "Supuesto: falta consigna local completa de Actividad 5; se conserva estructura base y preguntas abiertas."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y encuadre.",
    "Alinear la actividad con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar enfoque jurídico-académico con claridad, fundamento y transferencia profesional.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas de modelos como provisionales hasta verificación local.",
    "No usar trazas de memoria de modelos como fuentes académicas citables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Distinguir en cada tramo: afirmación, evidencia y conclusión.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica aplicable a práctica profesional.",
    "Adaptar la forma final a reporte, presentación o recurso visual según consigna."
  ],
  "activity_rules": [
    "Adaptar el contenido al enunciado real de Actividad 5 sin romper reglas troncales de asignatura.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No arrastrar bibliografía de otra semana sin confirmar pertinencia.",
    "Mantener trazabilidad entre instrucción, desarrollo y criterio de evaluación.",
    "Si hay ambigüedad de alcance, registrar supuesto operativo y continuar con consistencia."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar respaldo o marca de supuesto en cada afirmación relevante.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar coherencia jurídica mínima entre premisas y conclusión.",
    "Revisar manualmente memoria con incidentes históricos de parseo antes de reutilizar."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables ya citadas en .tex.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Verificar nombres reales de archivos cuando README muestre tokens sin expandir.",
    "Resolver tokens tipo $(@{...}.Slug) antes de fijar rutas y nombre canónico de .bib.",
    "Supuesto: el .bib canónico esperado es filosofia-del-derecho.bib, pendiente de confirmación local final."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar en .bib solo fuentes realmente usadas en la actividad.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Tratar filosofia-del-derecho-clean.bib como set temático potencialmente de otra semana hasta confirmar pertinencia en Actividad 5.",
    "Conservar claves existentes para evitar ruptura de compilación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Aplicar unión y deduplicación; evitar regresiones de reglas previas útiles.",
    "Transferir entre hermanos solo identidad, estructura, calidad y patrones argumentativos reutilizables.",
    "No transferir redacción literal, conclusiones específicas ni bibliografía exclusiva.",
    "Mantener bandera de riesgo por salidas no parseables en ciclos previos.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar rúbrica de evaluación específica de Actividad 5.",
    "Confirmar tipo de producto requerido en Actividad 5: reporte, presentación o recurso visual.",
    "Confirmar si Actividad 5 reutiliza bibliografía existente o requiere curaduría nueva.",
    "Confirmar nombre canónico final del .bib de asignatura tras resolver token Slug en README."
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
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Análisis propio no meramente descriptivo.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos rigurosos.",
      "Asegurar trazabilidad entre consigna, evidencia y postura.",
      "Sostener continuidad editorial institucional entre actividades."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones funcionales y claras.",
      "Postura propia sustentada.",
      "Supuestos explícitos cuando falte dato.",
      "Cierre con aplicabilidad profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> inferencia jurídica.",
      "Contraste doctrinal breve -> toma de postura.",
      "Cierre con transferencia a práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalización JSON",
        "Problema jurídico",
        "Marco normativo/doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible",
        "Consistencia cita-.bib",
        "Bibliografía base vs bibliografía específica"
      ],
      "citations": [
        "README.md",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Estructura de actividad",
          "kind": "supports",
          "justification": "Define tono, rigor y forma del entregable."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación del problema no hay análisis pertinente."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica válida exige respaldo trazable."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo estable no hay transferencia confiable."
        },
        {
          "source": "Bibliografía base vs bibliografía específica",
          "target": "Pertinencia de fuentes por actividad",
          "kind": "develops",
          "justification": "Evita arrastre automático de fuentes entre semanas."
        }
      ],
      "evidence": [
        "README fija identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico fija ejes problema-conceptos-fuentes-análisis-cierre.",
        "Historial reporta incidentes de salida no parseable y exige compuerta de estructura.",
        "Contexto local muestra token Slug sin expandir; requiere validación de nombre .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 86: deduplicación integral de reglas repetidas en destino.",
      "Ciclo 86: refuerzo lateral de patrones reutilizables desde hermano Actividad 1.",
      "Ciclo 86: preservación explícita de no transferencia de conclusiones y bibliografía exclusiva.",
      "Ciclo 86: mantenimiento de compuertas de calidad por riesgo histórico de parseo.",
      "Ciclo 86: conservación de supuestos abiertos por falta de consigna local completa."
    ]
  }
}