{
  "summary": [
    "Se consolida memoria lateral de Actividad 3 con transferencia reusable desde Actividad 1.",
    "Se preservan reglas institucionales UnADM, estructura editorial y control de calidad sin regresión.",
    "Se mantiene deduplicación lossless y se corrigen duplicados semánticos y ortográficos.",
    "Se refuerza regla crítica: no propagar sin JSON parseable ni sin normalización previa.",
    "Se mantiene política de supuestos para datos no visibles en la consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no confirmado en la consigna de Actividad 3.",
    "Tratar memorias editoriales Codex/GPT-Pro como antecedentes técnicos provisionales, no como fuentes académicas.",
    "Usar malla-curricular-derecho-unadm.pdf solo para ubicación curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna local, usar estructura base y marcar [supuesto]."
  ],
  "activity_rules": [
    "Heredar reglas válidas de Actividad 1 sin copiar redacción literal ni conclusiones específicas.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir semana, tema o formato de Actividad 3 sin evidencia local.",
    "Registrar diferencias de Actividad 3 como [supuesto] hasta confirmar guía oficial."
  ],
  "quality_gates": [
    "Bloquear guardado y propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes citadas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Distinguir fuentes académicas y normativas de antecedentes editoriales.",
    "Aplicar no regresión: no eliminar reglas útiles previas."
  ],
  "latex_rules": [
    "Usar acentos y codificación correcta en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrarlas sin necesidad verificada.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos y rutas antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Tomar como [supuesto] el .bib canónico filosofia-del-derecho.bib hasta confirmación local."
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Agregar al .bib solo entradas realmente citadas por la actividad.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 3 [supuesto condicionado]."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables: identidad, estructura, calidad, conceptos y relaciones.",
    "No propagar conclusiones ni bibliografía exclusiva de un hermano.",
    "Aplicar unión+deduplicación lossless en cada ciclo.",
    "Mantener bandera de riesgo cuando exista antecedente de parseo fallido.",
    "Si faltan datos locales, propagar plantilla base con preguntas abiertas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 3.",
    "Confirmar formato de entrega requerido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para nivel de profundidad.",
    "Confirmar bibliografía obligatoria de la semana de Actividad 3.",
    "Confirmar si aplica la bibliografía depurada de Interpretación jurídica (Semana 7) [supuesto].",
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
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible.",
      "Rigor de fuentes y trazabilidad."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en producto académico con fundamento jurídico.",
      "Garantizar consistencia editorial y calidad técnica de entregables LaTeX.",
      "Preservar memoria institucional reusable entre actividades hermanas."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y orden lógico.",
      "Afirmación con cita verificable.",
      "Supuestos etiquetados cuando falte evidencia local.",
      "Cierre jurídico aplicable a práctica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación -> postura.",
      "Objetivo inicial -> desarrollo coherente -> cierre consistente."
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
          "justification": "El análisis se construye sobre delimitación clara del problema."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión válida depende de argumentación sustentada."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad académica, conclusión jurídica propia.",
        "Programa analítico: ejes de trabajo y propósito de transformación editorial.",
        "Memoria previa: bloqueo por salida no JSON parseable y necesidad de normalización."
      ]
    },
    "reinforcement_log": [
      "Ciclo 18: deduplicación semántica y ortográfica sin pérdida.",
      "Ciclo 18: refuerzo de reglas transversales reutilizables entre hermanos.",
      "Ciclo 18: preservación de no regresión y política de supuestos.",
      "Ciclo 18: se evita transferencia de conclusiones y bibliografía exclusiva no verificada."
    ]
  }
}