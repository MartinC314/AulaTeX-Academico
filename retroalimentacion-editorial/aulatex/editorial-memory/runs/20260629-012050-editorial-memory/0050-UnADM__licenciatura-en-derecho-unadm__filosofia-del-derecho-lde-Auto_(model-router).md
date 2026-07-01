{
  "summary": [
    "Materia consolidada con identidad UnADM y cinco ejes editoriales transferidos desde Actividad 1.",
    "Compresión union-dedupe lossless; sin eliminación de reglas útiles previas.",
    "Trazabilidad entre actividad, archivos .tex y .bib de la materia asegurada.",
    "Normalización obligatoria de insumos no JSON parseable antes de propagar.",
    "Puertas de calidad activas: citas verificables, estructura mínima y compilación limpia.",
    "Se refuerzan patrones argumentativos: problema, conceptos, evidencia, análisis y conclusión jurídica.",
    "Se preservan fuentes provisionales marcadas como supuestos hasta verificación local.",
    "Propagación recursiva solo tras validar JSON, estructura y bibliografía."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en redacción, tono y formato.",
    "Alinear con Licenciatura en Derecho: semestre 1, bloque 2, obligatoria, 8 créditos (malla-curricular-derecho-unadm.pdf).",
    "Usar la carpeta de la materia como punto de entrada canónico para actividades y entregables.",
    "Marcar como supuesto cualquier dato no visible en consignas o documentos verificados.",
    "Tratar fuentes heredadas Codex y GPT-Pro como provisionales hasta confirmación local. [supuesto]",
    "Conservar trazabilidad curricular y documental entre README, programa analítico y productos .tex."
  ],
  "structure_rules": [
    "Abrir con encuadre breve y delimitado del problema jurídico o social.",
    "Definir un objetivo puntual del producto antes del desarrollo.",
    "Seccionar en: conceptos clave, marco normativo/doctrinal, análisis propio y cierre.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear el formato final al producto indicado por la planeación (reporte o presentación).",
    "Mantener correspondencia entre secciones, preguntas guía y conclusiones."
  ],
  "activity_rules": [
    "Verificar que el producto corresponda a la consigna específica de cada actividad.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada; evitar entregas solo descriptivas.",
    "No asumir fuentes de semanas posteriores para actividades iniciales. [supuesto]",
    "Integrar normas, doctrina, datos y casos relevantes al problema planteado.",
    "Registrar en el .bib de la materia las fuentes específicas usadas en cada actividad."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y entradas en el .bib.",
    "Compilar sin errores críticos ni referencias rotas antes de cierre.",
    "Registrar y normalizar insumos no estructurados previos a su reutilización."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrarlas sin migración completa.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar rutas y nombres canónicos de archivos antes de compilar.",
    "Compilar sin warnings bloqueantes y sin citas pendientes (?); corregir referencias rotas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM, IIJ-UNAM y SCJN cuando aplique.",
    "Distinguir bibliografía base de la materia y bibliografía específica por actividad.",
    "No inventar referencias; usar solo obras consultables con metadatos mínimos (autor, título, año, editorial/URL).",
    "Mantener claves ya citadas en .tex; deduplicar entradas sin pérdida de información.",
    "No asumir que filosofia-del-derecho-clean.bib corresponde a Actividad 1; documenta su orientación a Semana 7. [supuesto]",
    "Completar entradas truncadas solo tras verificación local (p. ej., scjnIncapacidadResistencia2019). [supuesto]"
  ],
  "propagation_hints": [
    "Propagar reglas a nivel licenciatura y a materias afines solo tras validar JSON, estructura y .bib.",
    "Aplicar normalización manual en ciclo 1 cuando existan insumos no estructurados.",
    "Reusar puertas de calidad institucional como filtro previo en nuevas actividades.",
    "Evitar propagar nombres de archivo anómalos hasta corregirlos localmente.",
    "Conservar trazabilidad entre actividad, .tex y .bib en todos los nodos descendentes.",
    "Propagación recursiva progresiva: primero materia, luego actividades y artefactos derivados."
  ],
  "open_questions": [
    "Confirmar nombre canónico del archivo .bib de la materia (¿filosofia-del-derecho.bib?).",
    "Determinar si filosofia-del-derecho-clean.bib sustituye al placeholder del README. [supuesto]",
    "Confirmar producto exacto solicitado por Actividad 1 y su rúbrica.",
    "Verificar integridad completa de scjnIncapacidadResistencia2019 en el .bib local. [supuesto]",
    "Aclarar si las fuentes de Semana 7 aplican a otras semanas o son acotadas. [supuesto]",
    "Definir plantilla mínima obligatoria para reporte vs presentación en esta materia."
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
        "Carpeta de la materia como entrada canónica editorial."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social como disparador analítico.",
      "Marco conceptual y normativo como soporte del argumento.",
      "Evidencia verificable y trazable.",
      "Análisis crítico con postura académica.",
      "Conclusión jurídica aplicable a la práctica.",
      "Hermenéutica e interpretación jurídica.",
      "Argumentación jurídica.",
      "Derecho y moral.",
      "Justicia."
    ],
    "reason_for_being": [
      "Transformar planeación en productos académicos con fundamento y transferencia profesional.",
      "Homologar estructura argumentativa para reportes y presentaciones.",
      "Garantizar trazabilidad entre consignas, desarrollo y bibliografía."
    ],
    "style_markers": [
      "Encuadre inicial breve y focalizado.",
      "Seccionado explícito y estable.",
      "Marcado de supuestos cuando falte evidencia.",
      "Conexión constante a fuentes verificables.",
      "Cierre con criterio jurídico propio y transferible."
    ],
    "argumentative_patterns": [
      "Delimitación del problema.",
      "Conceptos clave y marco normativo/doctrinal.",
      "Evidencia y casos aplicados.",
      "Análisis crítico con postura propia.",
      "Conclusión jurídica transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Filosofía del Derecho",
        "Hermenéutica e interpretación jurídica",
        "Argumentación jurídica",
        "Derecho y moral",
        "Justicia",
        "Conclusión jurídica transferible",
        "Constitución Política de los Estados Unidos Mexicanos (texto vigente)",
        "Ley General de Víctimas (texto vigente)",
        "Teoría pura del derecho",
        "Estudios de teoría del derecho natural"
      ],
      "citations": [
        "hernandezManriquezHermeneutica2019",
        "scjnMemoriaArgumentacion2008",
        "scjnViolenciaFisica2022",
        "scjnIncapacidadResistencia2019",
        "noauthor_constitucion_nodate",
        "de_victimas_ley_2013",
        "generales_ley_2021",
        "finnis_estudios_2017",
        "lovon_manual_2020",
        "ruiz_rodriguez_filosofia_derecho_2018",
        "ruiz_rodriguez_filosofia_derecho_2009",
        "gandara_ley_2015",
        "franzoni_acevedo_ley_2017"
      ],
      "relations": [
        {
          "source": "Hermenéutica e interpretación jurídica",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "La interpretación fundamenta la construcción de argumentos jurídicos aplicables.",
          "evidence": [
            "hernandezManriquezHermeneutica2019",
            "scjnMemoriaArgumentacion2008"
          ]
        },
        {
          "source": "Teoría pura del derecho",
          "target": "Derecho y moral",
          "kind": "contrasts",
          "justification": "Distingue validez normativa de juicios morales en el análisis jurídico.",
          "evidence": [
            "ruiz_rodriguez_filosofia_derecho_2009"
          ]
        },
        {
          "source": "Estudios de teoría del derecho natural",
          "target": "Justicia",
          "kind": "develops",
          "justification": "Aporta criterios axiológicos para evaluar la justicia de normas.",
          "evidence": [
            "finnis_estudios_2017"
          ]
        },
        {
          "source": "Constitución Política de los Estados Unidos Mexicanos (texto vigente)",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión aplicable requiere soporte constitucional y legal verificable.",
          "evidence": [
            "noauthor_constitucion_nodate"
          ]
        },
        {
          "source": "Ley General de Víctimas (texto vigente)",
          "target": "Argumentación jurídica",
          "kind": "supports",
          "justification": "Aporta parámetros de protección y reparación en casos concretos.",
          "evidence": [
            "de_victimas_ley_2013"
          ]
        }
      ],
      "evidence": [
        "hernandezManriquezHermeneutica2019 :: Nociones de hermenéutica e interpretación jurídica en el contexto mexicano.",
        "scjnMemoriaArgumentacion2008 :: Memoria de seminarios de argumentación jurídica.",
        "scjnViolenciaFisica2022 :: Tesis sobre violencia física en tipo penal de violación (SJF).",
        "scjnIncapacidadResistencia2019 :: Tesis sobre incapacidad de resistencia como ausencia de consentimiento (SJF).",
        "noauthor_constitucion_nodate :: Texto vigente de la CPEUM.",
        "de_victimas_ley_2013 :: Ley General de Víctimas.",
        "generales_ley_2021 :: Referencias generales a normativa complementaria. [supuesto]",
        "finnis_estudios_2017 :: Estudios de teoría del derecho natural.",
        "lovon_manual_2020 :: Manual práctico de filosofía del derecho.",
        "ruiz_rodriguez_filosofia_derecho_2009 :: Referente doctrinal de filosofía del derecho.",
        "ruiz_rodriguez_filosofia_derecho_2018 :: Actualizaciones doctrinales. [supuesto]",
        "gandara_ley_2015 :: Análisis sobre LGAMVLV.",
        "franzoni_acevedo_ley_2017 :: Desarrollo normativo en violencia de género."
      ]
    },
    "reinforcement_log": [
      "Ciclo 1: Se elevan patrones y ejes editoriales desde Actividad 1 a la materia.",
      "Se consolidan puertas de calidad: JSON parseable, estructura mínima, citas verificables y compilación limpia.",
      "Se marcan como provisionales las fuentes heredadas Codex y GPT-Pro hasta verificación local.",
      "Se refuerza trazabilidad entre README, programa analítico, .tex y .bib.",
      "Se normalizan tokens $(@{...}.Slug) como pendiente de corrección editorial.",
      "Se preserva compresión union-dedupe sin eliminar reglas previas útiles."
    ]
  }
}