{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se preserva identidad UnADM, contexto curricular y ejes editoriales sin regresión.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se aplica deduplicación lossless y se eliminan variantes repetidas de forma, no de fondo.",
    "Se conserva política de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como supuesto todo dato no confirmado en consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente académica.",
    "Citar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado en la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar reglas válidas de actividad-1 sin copiar redacción literal ni conclusiones específicas.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, formato o bibliografía específica de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado o propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar manualmente respuestas no estructuradas antes de reutilizar.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y no renombrarlas sin necesidad verificada.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos en rutas y nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Supuesto: .bib canónico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Registrar en .bib solo fuentes efectivamente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "No usar memoria editorial como bibliografía académica.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a actividad temática distinta; confirmar aplicabilidad en actividad-3."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones recurrentes.",
    "No propagar conclusiones específicas ni bibliografía exclusiva entre hermanos.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Conservar bandera de riesgo cuando exista antecedente de parseo fallido.",
    "Aplicar compresión por unión y deduplicación lossless en cada ciclo."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido en actividad-3: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para profundidad argumentativa.",
    "Confirmar bibliografía obligatoria de la semana de actividad-3.",
    "Confirmar si actividad-3 reutiliza bibliografía depurada o requiere .bib propio.",
    "Confirmar archivo .tex principal canónico de actividad-3."
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
      "Producto alineado a planeación semanal.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos con fundamento jurídico y evidencia.",
      "Garantizar trazabilidad entre afirmaciones, citas y cierre argumentativo.",
      "Sostener continuidad editorial entre actividades sin perder validez local."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Supuestos marcados cuando falte evidencia local.",
      "Citas verificables en afirmaciones relevantes.",
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
        "filosofia-del-derecho-clean.bib [supuesto de uso condicionado]"
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
        "README: identidad UnADM, integridad académica y conclusión jurídica propia.",
        "Programa analítico: propósito y ejes de trabajo editoriales.",
        "Regla persistente: bloquear propagación sin JSON parseable.",
        "Contexto local: tokens Slug sin expandir en README/programa analítico."
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicación integral aplicada sin pérdida semántica.",
      "Ciclo 10: se reforzó transferencia lateral por patrones, no por contenido específico.",
      "Ciclo 10: se mantuvo no regresión en reglas de calidad, LaTeX y bibliografía.",
      "Ciclo 10: se mantuvieron supuestos explícitos donde faltan datos locales verificables."
    ]
  }
}