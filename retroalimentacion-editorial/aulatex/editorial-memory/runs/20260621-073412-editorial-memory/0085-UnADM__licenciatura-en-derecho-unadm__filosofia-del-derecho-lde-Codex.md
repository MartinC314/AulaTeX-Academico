{
  "summary": [
    "Consolidar memoria de materia con abstracción ascendente desde actividad-1.",
    "Preservar reglas útiles previas sin regresión y con deduplicación lossless.",
    "Mantener normalización obligatoria de insumos no estructurados antes de propagar.",
    "Fijar eje editorial transversal: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Reforzar trazabilidad entre consigna, producto .tex y bibliografía .bib."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y criterios académicos.",
    "Alinear entregables a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como entrada canónica editorial y operativa.",
    "Marcar como [supuesto] todo dato no visible en consigna o documentos locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Usar malla-curricular-derecho-unadm.pdf como respaldo curricular verificado."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener trazabilidad entre actividad, sección argumentativa y evidencia citada."
  ],
  "activity_rules": [
    "Evitar entregas solo descriptivas o de resumen.",
    "Incluir postura argumentada del estudiante en cada actividad.",
    "Sustentar afirmaciones sustantivas con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir que fuentes de semanas posteriores aplican a actividad-1.",
    "Confirmar correspondencia entre consigna específica y tipo de producto entregado."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar que no existan afirmaciones sin respaldo o sin marca de [supuesto].",
    "Validar consistencia entre citas en texto y entradas en .bib.",
    "Confirmar no eliminación de reglas útiles heredadas en cada ciclo."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Compilar sin errores críticos, citas rotas ni referencias huérfanas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres/rutas anómalos antes de declarar canon de archivos."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura con trazabilidad.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente/editorial o URL.",
    "No completar entradas truncadas sin verificación local. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas verificadas por README, programa analítico y .bib local.",
    "Elevar patrones reutilizables de actividad a materia sin copiar redacción literal.",
    "Mantener etiqueta de compresión union-dedupe lossless en cada salto.",
    "Registrar incidencias de ingesta no parseable como riesgo, sin perder contenido útil.",
    "Reusar puertas de calidad institucionales en nodos laterales y superiores."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de actividad-1 para fijar producto exacto. [supuesto]",
    "Confirmar nombre canónico final del archivo .bib de la materia. [supuesto]",
    "Definir si filosofia-del-derecho-clean.bib es auxiliar o canónico. [supuesto]",
    "Verificar integridad de la entrada scjnIncapacidadResistencia2019 truncada. [supuesto]",
    "Sustituir referencias de fuente provisional heredada por evidencia local verificada. [supuesto]"
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
      "Problema jurídico o social delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Estandarizar calidad editorial sin perder especificidad de cada actividad.",
      "Conectar formación teórica con transferencia a práctica jurídica."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Seccionado explícito y estable.",
      "Cierre con criterio jurídico propio.",
      "Marcado explícito de [supuesto] cuando aplique."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis crítico -> conclusión.",
      "Afirmación sustantiva -> evidencia citada -> interpretación propia.",
      "Consigna -> tipo de producto -> verificación de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Conclusión jurídica transferible"
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
          "justification": "La interpretación sostiene la construcción de razones jurídicas."
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "Permite evaluar normas, hechos y consecuencias."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión válida requiere soporte normativo verificable."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra el debate axiológico y de validez."
        }
      ],
      "evidence": [
        "README de materia: identidad y pauta editorial.",
        "Programa analítico: propósito y ejes de trabajo.",
        "Bibliografía local .bib/.clean.bib: claves citables y trazables.",
        "Regla persistente: normalizar insumos no JSON parseable antes de propagación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 85: se elevan patrones de actividad-1 a materia sin pérdida de reglas.",
      "Se deduplican variantes textuales manteniendo semántica operativa.",
      "Se conserva control de calidad heredado de Codex/GPT-Pro como riesgo de ingesta.",
      "Se refuerza trazabilidad consigna-producto-cita como núcleo editorial."
    ]
  }
}