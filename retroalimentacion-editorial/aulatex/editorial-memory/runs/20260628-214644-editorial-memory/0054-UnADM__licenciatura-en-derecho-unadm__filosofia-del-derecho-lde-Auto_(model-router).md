{
  "summary": [
    "Se consolida memoria editorial de la materia elevando patrones verificados desde Actividad 1.",
    "Se aplica compresión union-dedupe lossless sin eliminar reglas útiles.",
    "Se fija identidad UnADM y trazabilidad curricular (semestre 1, bloque 2, obligatoria, 8 créditos).",
    "Se normalizan insumos no JSON parseable antes de propagar.",
    "Se integra pauta estable: problema, conceptos y marco, evidencia, análisis propio, conclusión transferible.",
    "Se refuerzan puertas de calidad, bibliografía verificable y compatibilidad LaTeX-BibTeX.",
    "Se documenta grafo de conocimiento con citas recurrentes y relaciones reutilizables.",
    "Propagación recursiva controlada por validaciones en ciclo 2."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear con Licenciatura en Derecho: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de materia como punto de entrada canónico.",
    "Marcar como [supuesto] todo dato no visible en consignas o documentos locales.",
    "Citar malla-curricular-derecho-unadm.pdf como fuente curricular verificada.",
    "Tratar fuentes heredadas Codex y GPT-Pro como provisionales hasta verificación local. [supuesto]"
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo/doctrinal, análisis propio, cierre.",
    "Alinear el producto al tipo solicitado por la planeación.",
    "Cerrar con conclusión jurídica transferible a la práctica.",
    "Mantener trazabilidad entre actividad, .tex y .bib de la materia."
  ],
  "activity_rules": [
    "Delimitar el problema y el alcance de la actividad.",
    "Integrar normas, doctrina y datos pertinentes con citas verificables.",
    "Incluir postura argumentada del estudiante; evitar solo descripción.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otras semanas sin confirmación local.",
    "Asegurar que el producto corresponde a la consigna específica de la semana."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marcar [supuesto] en toda afirmación sustantiva.",
    "Validar correspondencia entre citas en texto y entradas en el .bib.",
    "Revisar y normalizar insumos no estructurados antes de reutilizarlos.",
    "Confirmar integridad de claves placeholder (p. ej., clave, clave1) antes de cierre. [supuesto]"
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar sin migración completa.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores ni referencias rotas.",
    "Verificar nombres en README antes de referenciarlos en .tex.",
    "Resolver tokens $(@{...}.Slug) en README y programa analítico antes de compilar. [supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM, SCJN e IIJ-UNAM verificables.",
    "Registrar fuentes específicas de cada actividad en el .bib de la materia.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de materia y bibliografía específica por actividad.",
    "Tratar filosofia-del-derecho-clean.bib como depurado provisional hasta confirmar .bib canónico. [supuesto]"
  ],
  "propagation_hints": [
    "Propagar reglas arriba y lateralmente solo tras validar JSON y estructura.",
    "Reusar puertas de calidad institucionales como filtro previo.",
    "Aplicar normalización manual cuando se detecten salidas no estructuradas.",
    "Propagar reglas generales cuando falte consigna textual local.",
    "En ciclo 2, propagar solo reglas verificadas por README, programa analítico y .bib local.",
    "Mantener compresión union-dedupe en cada salto recursivo."
  ],
  "open_questions": [
    "Confirmar consigna y tipo de producto de Actividad 1 (reporte, presentación u otro).",
    "Verificar rúbrica de evaluación para ajustar profundidad argumentativa.",
    "Definir nombre canónico del archivo .bib de la materia.",
    "Determinar si filosofia-del-derecho-clean.bib sustituye al placeholder del README. [supuesto]",
    "Confirmar fuentes obligatorias por semana y su reutilización entre actividades.",
    "Completar y verificar campos de scjnIncapacidadResistencia2019 en el .bib. [supuesto]"
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
        "Materia como punto de entrada canónico."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como disparador analítico.",
      "Marco conceptual y normativo pertinente.",
      "Evidencia y citas verificables.",
      "Análisis crítico con postura propia.",
      "Conclusión aplicable a la práctica jurídica."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en productos claros y sustentados.",
      "Asegurar trazabilidad académica entre actividad, .tex y .bib.",
      "Fortalecer competencias de interpretación y argumentación jurídica."
    ],
    "style_markers": [
      "Encuadre breve y focalizado.",
      "Seccionado estable y legible.",
      "Marcado explícito de supuestos.",
      "Cierre con criterio jurídico transferible."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Conceptos clave y marco normativo/doctrinal.",
      "Análisis crítico con contraste de posturas.",
      "Síntesis y conclusión normativamente respaldada."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Análisis crítico del fenómeno jurídico",
        "Conclusión jurídica transferible",
        "Marco normativo",
        "Constitución Política de los Estados Unidos Mexicanos",
        "Ley General de Víctimas"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "rojas_gonzalez_filosofia_derecho_2018",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "generales_ley_2021",
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "franzoni_acevedo_ley_2017",
        "gandara_ley_2015",
        "ruizrodriguezFilosofiaDerecho2009",
        "clave",
        "clave1",
        "clave2",
        "claveFuente"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación fundamenta la construcción argumentativa en casos y normas.",
          "evidence": [
            "hernandezManriquezHermeneutica2019",
            "scjnMemoriaArgumentacion2008"
          ]
        },
        {
          "source": "Argumentación jurídica",
          "target": "Análisis crítico del fenómeno jurídico",
          "kind": "develops",
          "justification": "La argumentación estructura razones, pondera normas y consecuencias.",
          "evidence": [
            "scjnMemoriaArgumentacion2008"
          ]
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Derecho y moral",
          "kind": "develops",
          "justification": "Integra debate axiológico y validez normativa.",
          "evidence": [
            "ruiz_rodriguez_filosofia_derecho_2009",
            "rojas_gonzalez_filosofia_derecho_2018",
            "finnis_estudios_2017"
          ]
        },
        {
          "source": "Conclusión jurídica transferible",
          "target": "Marco normativo",
          "kind": "depends_on",
          "justification": "La aplicabilidad profesional exige soporte normativo verificable.",
          "evidence": [
            "noauthor_constitucion_nodate",
            "de_victimas_ley_2013",
            "generales_ley_2021"
          ]
        },
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "Las reglas interpretativas orientan la determinación del sentido aplicable.",
          "evidence": [
            "hernandezManriquezHermeneutica2019",
            "scjnViolenciaFisica2022",
            "scjnIncapacidadResistencia2019"
          ]
        }
      ],
      "evidence": [
        "hernandezManriquezHermeneutica2019 :: Nociones de hermenéutica e interpretación jurídica en México (IIJ-UNAM).",
        "scjnMemoriaArgumentacion2008 :: Seminarios de argumentación jurídica (IIJ-UNAM).",
        "scjnViolenciaFisica2022 :: Criterio SCJN sobre violencia física en violación (Registro 2025574).",
        "scjnIncapacidadResistencia2019 :: Criterio SCJN sobre incapacidad de resistencia. [verificar campos] [supuesto]",
        "noauthor_constitucion_nodate :: Texto vigente CPEUM.",
        "de_victimas_ley_2013 :: Ley General de Víctimas.",
        "generales_ley_2021 :: Ley General aplicable citada en los .tex locales.",
        "ruiz_rodriguez_filosofia_derecho_2009 :: Obra de referencia en Filosofía del Derecho.",
        "rojas_gonzalez_filosofia_derecho_2018 :: Manual/esquema de Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Elevados ejes editoriales problema-conceptos-evidencia-análisis-conclusión desde Actividad 1.",
      "Unificada identidad UnADM y trazabilidad curricular en la materia.",
      "Dedupe de reglas duplicadas y preservación de todas las útiles.",
      "Mejorada dirección relacional: la conclusión depende del marco normativo.",
      "Asegurada compatibilidad LaTeX-BibTeX y control de tokens de README.",
      "Conservadas claves bibliográficas recurrentes y marcados placeholders como [supuesto].",
      "Instalada puerta de calidad de JSON parseable para toda propagación recursiva."
    ]
  }
}