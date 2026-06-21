{
  "summary": [
    "Consolidar memoria de materia de Filosofía del Derecho con abstracción ascendente desde actividad-1.",
    "Preservar reglas válidas previas sin regresión y aplicar deduplicación lossless por unión.",
    "Mantener identidad UnADM, trazabilidad curricular y normalización estructurada obligatoria.",
    "Fijar patrón editorial transferible: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Registrar riesgos de ingesta por salidas no JSON parseable sin perder contenido útil."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios académicos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Usar malla-curricular-derecho-unadm.pdf como fuente curricular verificada.",
    "Marcar como [supuesto] todo dato no visible en consigna o documento local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local. [supuesto]",
    "Conservar referencias provisionales históricas (Codex, GPT-Pro) solo como traza de riesgo. [supuesto]"
  ],
  "structure_rules": [
    "Abrir cada producto con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear formato final al producto solicitado por planeación semanal.",
    "Mantener trazabilidad entre actividad, archivo .tex y archivo .bib de la materia.",
    "Separar artefactos por tipo: reporte y presentación en archivos dedicados."
  ],
  "activity_rules": [
    "Delimitar problema y pregunta guía al inicio de cada actividad.",
    "Sustentar afirmaciones sustantivas con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre objetivo, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores como obligatorias para actividad-1. [supuesto]",
    "Confirmar que el entregable corresponde exactamente a la consigna de la actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no se eliminen reglas útiles heredadas en cada ciclo.",
    "Validar correspondencia entre producto entregado y consigna.",
    "Validar consistencia entre citas en .tex y entradas en .bib.",
    "Exigir respaldo o marca [supuesto] en afirmaciones no verificadas."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos y tokens sin expandir en rutas y nombres antes de compilar.",
    "No adoptar nombres con placeholders como canónicos hasta resolverlos localmente. [supuesto]",
    "Mantener separación de archivos por tipo de entrega para evitar colisiones."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar bibliografía específica de actividad en el .bib de la asignatura.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Preservar claves jurídicas recurrentes ya verificables (UNAM, IIJ, SCJN).",
    "No completar entradas truncadas sin verificación local de campos. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON, estructura y trazabilidad.",
    "Elevar al ancestro reglas generales reutilizables, no redacción literal de una actividad.",
    "Reusar puertas de calidad institucional como filtro previo en nodos vecinos.",
    "Evitar propagar nombres de archivo anómalos hasta corrección local.",
    "Cuando falte consigna textual, propagar solo reglas generales y marcar [supuesto].",
    "Mantener etiqueta operativa: compresión lossless por unión-deduplicación."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de actividad-1 para cerrar reglas de formato.",
    "Confirmar nombre canónico final del .bib de la materia.",
    "Resolver placeholders tipo $(@{...}.Slug) en README y programa analítico.",
    "Confirmar si bibliografía depurada de Semana 7 aplica o no a actividad-1. [supuesto]",
    "Verificar integridad completa de la entrada scjnIncapacidadResistencia2019."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como disparador.",
      "Conceptos, normas, doctrina y evidencia verificable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable a práctica profesional.",
      "Trazabilidad editorial entre consigna, texto y bibliografía."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos rigurosos y útiles.",
      "Estandarizar calidad editorial sin perder contexto jurídico.",
      "Permitir propagación segura de reglas entre actividades y niveles."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado explícito y estable.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer marco conceptual y normativo.",
      "Contrastar fuentes y sostener tesis propia.",
      "Concluir con implicación jurídica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Problema-conceptos-evidencia-análisis-conclusión"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación aporta criterios para construir argumentos jurídicos sólidos."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación permite evaluar validez, razones y consecuencias normativas."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "La materia integra el debate entre validez normativa y contenido axiológico."
        },
        {
          "source": "Marco normativo/doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión requiere sustento normativo verificable."
        }
      ],
      "evidence": [
        "README de materia: identidad, ubicación curricular y pauta editorial.",
        "Programa analítico: propósito y cinco ejes de trabajo.",
        "Archivos .bib locales: claves recurrentes y trazables.",
        "Memoria de actividad-1: patrón editorial estable transferible."
      ]
    },
    "reinforcement_log": [
      "Se reforzó normalización obligatoria previa a propagación.",
      "Se consolidó patrón argumentativo común de la asignatura.",
      "Se preservaron reglas útiles previas sin recorte semántico.",
      "Se depuraron duplicados y variantes ortográficas sin pérdida de contenido.",
      "Se mantuvo trazabilidad de riesgos por fuentes provisionales. [supuesto]"
    ]
  }
}