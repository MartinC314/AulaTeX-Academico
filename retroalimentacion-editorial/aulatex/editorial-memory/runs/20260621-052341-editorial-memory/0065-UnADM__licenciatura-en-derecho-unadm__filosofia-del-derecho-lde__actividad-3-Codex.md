{
  "summary": [
    "Se consolida memoria de actividad-3 con transferencia lateral reutilizable desde actividad-1.",
    "Se preservan reglas institucionales UnADM, estructura base y control de calidad sin regresión.",
    "Se deduplica de forma lossless y se mantiene normalización JSON obligatoria antes de propagar.",
    "Se refuerza política de supuestos para datos no visibles en la consigna local.",
    "Se evita copiar conclusiones específicas o bibliografía exclusiva de un hermano."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como [supuesto] cualquier dato no confirmado en la consigna local.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedente provisional, no como fuente académica.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear el documento al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar patrones válidos de actividad-1 sin copiar redacción literal.",
    "No trasladar conclusiones específicas entre actividades hermanas.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Validar esquema mínimo completo antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Validar consistencia entre citas en texto y .bib.",
    "Normalizar manualmente cualquier memoria no estructurada antes de reutilizar.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir rutas y nombres solo con verificación local.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como [supuesto] bib canónico filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar en .bib solo entradas realmente citadas en la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No usar memoria editorial como bibliografía académica.",
    "Tratar filosofia-del-derecho-clean.bib como [supuesto] de uso condicionado por coincidencia temática."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones estables.",
    "No propagar supuestos como hechos confirmados.",
    "Aplicar unión+deduplicación lossless en cada ciclo.",
    "Propagar reglas específicas de Filosofía del Derecho solo dentro de la misma asignatura.",
    "Mantener bandera de riesgo cuando exista historial de salida no estructurada."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato requerido de entrega en actividad-3 (reporte, presentación u otro).",
    "Confirmar rúbrica de evaluación específica para actividad-3.",
    "Confirmar bibliografía obligatoria de actividad-3.",
    "Confirmar si actividad-3 corresponde a interpretación jurídica u otra unidad.",
    "Confirmar archivo .tex principal y nombre canónico final del .bib."
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
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Normalización estructurada antes de propagación."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Garantizar coherencia entre identidad institucional, método argumentativo y trazabilidad de fuentes."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explícitas con orden lógico.",
      "Afirmación respaldada por cita verificable.",
      "Supuestos marcados de forma visible.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo explícito -> desarrollo coherente -> cierre consistente."
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
        "filosofia-del-derecho-clean.bib [supuesto condicionado]"
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
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "Sin estructura válida no hay memoria confiable ni trazabilidad editorial."
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
        },
        {
          "source": "Bibliografía verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La verificación de fuentes evita afirmaciones no respaldadas."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, citas verificables y cierre jurídico propio.",
        "Programa analítico: ejes de trabajo y propósito editorial.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Regla persistente: deduplicación lossless y no regresión."
      ]
    },
    "reinforcement_log": [
      "Ciclo 65: se transfieren patrones laterales reutilizables desde actividad-1 a actividad-3.",
      "Ciclo 65: se conserva normalización estructurada obligatoria.",
      "Ciclo 65: se refuerza política de supuestos y se evita invención de fuentes.",
      "Ciclo 65: se mantiene separación entre bibliografía base y bibliografía específica.",
      "Ciclo 65: sin eliminación de reglas útiles previas."
    ]
  }
}