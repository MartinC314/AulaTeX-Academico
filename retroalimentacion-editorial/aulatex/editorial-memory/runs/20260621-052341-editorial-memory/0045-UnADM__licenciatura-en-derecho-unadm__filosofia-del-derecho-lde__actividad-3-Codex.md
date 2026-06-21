{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reutilizable desde Actividad 1.",
    "Se preserva identidad UnADM, contexto curricular y pauta editorial sin regresiones.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se refuerzan ejes estables: problema, conceptos y fuentes, análisis propio y conclusión jurídica.",
    "Se conserva política de supuestos para datos no confirmados en consigna local.",
    "Se deduplican reglas por unión lossless, sin recorte de reglas útiles."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas del nodo hermano sin copiar redacción literal.",
    "No transferir conclusiones específicas ni bibliografía exclusiva no confirmada localmente.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, tema o formato de Actividad 3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Validar trazabilidad entre afirmaciones y fuentes.",
    "Confirmar marca de supuesto en todo dato no verificado.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir rutas o nombres de archivo solo con verificación local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: archivo .bib canónico esperado es filosofia-del-derecho.bib por Slug."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas, doctrinales y jurisprudenciales verificables.",
    "Registrar en .bib solo fuentes citadas en la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a actividad temática distinta; aplicar solo si coincide la consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validación JSON y estructura.",
    "Transferir patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar supuestos como hechos confirmados.",
    "Mantener compresión lossless por unión y deduplicación.",
    "Aplicar normalización manual en nodos con incidencias de parseo.",
    "Propagar reglas específicas de Filosofía del Derecho solo a nodos de la misma asignatura."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 3.",
    "Confirmar formato requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana de Actividad 3.",
    "Confirmar si aplica bibliografía depurada de interpretación jurídica.",
    "Confirmar archivo .tex principal canónico para Actividad 3."
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
      "Conceptos y fuentes pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Trazabilidad entre argumento y evidencia."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos.",
      "Garantizar claridad, fundamento jurídico, evidencia y transferencia profesional.",
      "Sostener continuidad editorial entre actividades hermanas sin contaminar contenidos específicos."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Afirmación con cita verificable.",
      "Supuestos marcados de forma visible.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente.",
      "Cuando falte dato local: declarar supuesto y limitar alcance."
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
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Política de supuestos",
          "kind": "supports",
          "justification": "La estructura explícita obliga a marcar lo no verificado."
        },
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis deriva de un problema delimitado."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión depende de argumentación sustentada."
        },
        {
          "source": "Bibliografía verificable",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin fuentes verificables no hay sustento argumentativo."
        }
      ],
      "evidence": [
        "README: identidad UnADM, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico: ejes problema, conceptos/fuentes, análisis propio y cierre.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Bibliografía clean marcada para actividad de interpretación jurídica; uso condicionado por consigna."
      ]
    },
    "reinforcement_log": [
      "Ciclo 45: transferencia lateral controlada desde actividad-1 a actividad-3.",
      "Se conservaron reglas útiles previas sin eliminación.",
      "Se removió duplicidad textual por deduplicación semántica lossless.",
      "Se reforzó separación entre antecedente editorial y fuente académica.",
      "Se mantuvo compatibilidad con propagación recursiva y control de calidad."
    ]
  }
}