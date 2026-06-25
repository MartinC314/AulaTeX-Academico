{
  "summary": [
    "Memoria de Actividad 7 consolidada para Ética y Moral jurídica.",
    "Transferencia lateral desde Filosofía del Derecho aplicada solo como patrón reutilizable.",
    "Se preserva identidad UnADM y ubicación curricular verificable del destino.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se bloquea propagación si la salida no es JSON parseable.",
    "Se conservan alertas por salidas no estructuradas previas.",
    "Se agregan preguntas abiertas donde falta consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en cada entrega.",
    "Usar tono académico-jurídico formal.",
    "Alinear la actividad con Licenciatura en Derecho.",
    "Alinear la actividad con Ética y Moral jurídica.",
    "Usar semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Sustentar ubicación curricular con malla-curricular-derecho-unadm.pdf.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Conservar trazabilidad de fuentes provisionales.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Registrar fuente provisional del ciclo cuando no exista JSON válido del origen. [Supuesto]"
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Integrar el producto solicitado por la planeación semanal.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Incluir problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Alinear la estructura con la pauta editorial local de la asignatura.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Preparar salida en JSON parseable antes de propagar memoria."
  ],
  "activity_rules": [
    "Confirmar que el producto corresponda a la consigna de Actividad 7.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Mantener integridad académica en citas y referencias.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar afirmaciones sin respaldo documental.",
    "Evitar asumir fuentes de semanas o materias distintas sin validación.",
    "Relacionar ética, moral y práctica jurídica cuando la consigna lo permita.",
    "Distinguir análisis conceptual de valoración normativa.",
    "Cerrar con utilidad para el ejercicio profesional jurídico."
  ],
  "quality_gates": [
    "Validar JSON estricto antes de guardar.",
    "Validar esquema requerido completo antes de propagar.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuesta no estructurada antes de aplicarla aguas abajo.",
    "Confirmar que no se eliminen reglas útiles previas.",
    "Aplicar propagación recursiva solo si pasan las compuertas de calidad.",
    "Marcar supuestos explícitos cuando falten datos locales.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Confirmar correspondencia del producto con la consigna de Actividad 7.",
    "Revisar estructura mínima completa antes de reutilizar reglas."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reporte, presentación y .bib de la materia.",
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Conservar consistencia entre archivos .tex y bibliografía local.",
    "Mantener claves BibTeX estables.",
    "Evitar renombres arbitrarios que rompan citas existentes.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Corregir caracteres anómalos en rutas y nombres de archivo antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "No copiar LaTeX completo en memoria editorial."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de Actividad 7 en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias ni metadatos bibliográficos.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Deduplicar entradas bibliográficas equivalentes sin perder trazabilidad.",
    "Mantener una clave canónica y mapear alias cuando existan duplicados de la misma obra. [Supuesto]",
    "Verificar integridad sintáctica del .bib antes de propagar cambios. [Supuesto]",
    "No normalizar entradas si el .bib está truncado; abrir incidencia primero. [Supuesto]",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre nodos laterales.",
    "No copiar redacción literal de actividades hermanas.",
    "No copiar conclusiones específicas de Filosofía del Derecho.",
    "No copiar bibliografía exclusiva de Filosofía del Derecho.",
    "Usar analogía controlada entre fundamentos filosóficos y ética jurídica.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Aplicar normalización manual si se detecta salida no estructurada.",
    "Ciclo 1 requiere normalización manual si la entrada no es parseable.",
    "Ciclo 2 requiere normalización manual si la entrada no es parseable.",
    "Ciclo 3 requiere normalización manual si la entrada no es parseable.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar consigna exacta de Actividad 7.",
    "Confirmar tipo de producto solicitado en Actividad 7.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana de Ética y Moral jurídica.",
    "Confirmar si Actividad 7 requiere reporte, presentación o producto visual.",
    "Confirmar política local de alias de claves BibTeX para duplicados existentes.",
    "Confirmar si las claves duplicadas actuales del .bib deben mantenerse por retrocompatibilidad. [Supuesto]",
    "Confirmar si se corrige el .bib local truncado antes de nuevas propagaciones. [Supuesto]",
    "Definir criterio operativo final para duplicados .bib con claves distintas y metadatos iguales.",
    "Confirmar si caso Ayotzinapa, CPEUM, LGV y LGMDFP pertenecen a la consigna local de Actividad 7.",
    "Confirmar si el documento local conserva documenttitle y documentsubtitle heredados de otra actividad. [Supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Sobrio y verificable.",
        "Argumentativo con criterio propio.",
        "Orientado a práctica profesional."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Respeto a la planeación semanal.",
        "Trazabilidad de fuentes y supuestos.",
        "Validación estructural antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Ética y Moral jurídica.",
        "Semestre 1.",
        "Bloque 2.",
        "Obligatoria.",
        "8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos éticos, morales, normativos y doctrinales pertinentes.",
      "Producto solicitado por la planeación.",
      "Evidencia verificable.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Integridad académica.",
      "Distinción entre ética y moral.",
      "Vínculo entre moral, derecho y ejercicio profesional."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros y verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico con base ética y moral.",
      "Conectar reflexión conceptual con práctica profesional.",
      "Evitar productos descriptivos sin postura.",
      "Preservar trazabilidad editorial en LaTeX y bibliografía."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Objetivo explícito.",
      "Secciones claras y trazables.",
      "Citas explícitas y verificables.",
      "Supuestos etiquetados.",
      "Contraste conceptual controlado.",
      "Postura personal argumentada.",
      "Cierre con utilidad profesional jurídica.",
      "Lenguaje académico sin grandilocuencia.",
      "Normalización antes de propagación."
    ],
    "argumentative_patterns": [
      "Delimitar el problema jurídico o social.",
      "Definir conceptos éticos y morales clave.",
      "Ubicar marco normativo o doctrinal verificable.",
      "Contrastar posturas con evidencia.",
      "Distinguir descripción, valoración y conclusión jurídica.",
      "Construir postura del estudiante desde fuentes verificables.",
      "Conectar ética y moral con responsabilidad profesional.",
      "Cerrar con consecuencia práctica para el ejercicio jurídico.",
      "Marcar supuestos cuando falte información local.",
      "Evitar extrapolación de fuentes de otra asignatura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral jurídica",
        "Integridad académica",
        "Problema jurídico o social",
        "Conceptos clave",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Ética",
        "Moral",
        "Derecho",
        "Práctica jurídica",
        "Responsabilidad profesional",
        "Planeación semanal",
        "Actividad 7",
        "etica-y-moral-juridica.bib",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib",
        "huertaEticaConClasicos2000",
        "huerta2000etica",
        "ronquilloarmasEticaGeneralProfesional2018",
        "ronquillo2018etica",
        "singerCompendioEtica1995",
        "singer1995compendio",
        "prieto2009favor",
        "lopezmartinezTecnicasDidacticas2023",
        "barredaOracionCivica1867",
        "sierraUniversidadNacional1910",
        "constitucionCPEUM2026",
        "casoAyotzinapaCNDH2024",
        "lgv2026",
        "lgmdfp2026",
        "clave",
        "clave1",
        "clave2"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige citas verificables y conclusión con criterio propio."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "develops",
          "justification": "La asignatura pertenece al trayecto curricular jurídico del destino."
        },
        {
          "source": "malla-curricular-derecho-unadm.pdf",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local la identifica como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "depends_on",
          "justification": "El programa analítico indica transformar la planeación en productos académicos."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El análisis parte de un problema delimitado."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Los conceptos ordenan la lectura de normas, doctrina y datos."
        },
        {
          "source": "Evidencia verificable",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura debe sustentarse en fuentes explícitas."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "El cierre debe derivar del razonamiento desarrollado."
        },
        {
          "source": "Ética",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distinción conceptual es base recurrente de la materia."
        },
        {
          "source": "Moral",
          "target": "Derecho",
          "kind": "contrasts",
          "justification": "La asignatura requiere diferenciar valoración moral y regulación jurídica."
        },
        {
          "source": "Ética",
          "target": "Responsabilidad profesional",
          "kind": "develops",
          "justification": "La ética orienta criterios de actuación profesional."
        },
        {
          "source": "Responsabilidad profesional",
          "target": "Práctica jurídica",
          "kind": "supports",
          "justification": "La valoración ética mejora la toma de decisiones jurídicas."
        },
        {
          "source": "etica-y-moral-juridica.bib",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "El archivo bibliográfico local conserva fuentes base y específicas."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "supports",
          "justification": "La transferencia lateral aporta patrón de problema, conceptos, evidencia, análisis y cierre sin copiar contenido exclusivo."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: identidad UnADM, integridad académica y citas verificables.",
        "README local: conclusión jurídica con criterio propio.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: planeación semanal transformada en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de problema, conceptos, fuentes, análisis propio y cierre.",
        "Bibliografía local: etica-y-moral-juridica.bib contiene fuentes de ética general, ética clásica y materiales UnADM.",
        "Bibliografía local: existen claves duplicadas observables para obras equivalentes.",
        "Memoria destino: Actividad 7 usa reporte-etica-y-moral-juridica-Actividad-7.tex como artefacto primario.",
        "Memoria destino: citas locales incluyen constitucionCPEUM2026, casoAyotzinapaCNDH2024, lgv2026, lgmdfp2026, ronquilloarmasEticaGeneralProfesional2018 y singerCompendioEtica1995.",
        "Transferencia lateral: se reutilizan patrones editoriales, no bibliografía exclusiva ni conclusiones de Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3 consolida reglas parseables para Actividad 7.",
      "Se deduplican reglas repetidas sin eliminar contenido útil.",
      "Se preservan advertencias por salidas no JSON de Codex, Auto, Claude Foundry y GPT-Pro.",
      "Se refuerza validación JSON estricta antes de propagación recursiva.",
      "Se conserva identidad UnADM y contexto curricular local.",
      "Se transfiere desde Filosofía del Derecho solo el patrón estructural y argumentativo.",
      "Se evita copiar fuentes exclusivas del nodo origen.",
      "Se mantiene control de supuestos para consigna faltante.",
      "Se conserva alerta por posible .bib truncado.",
      "Se refuerza la relación ética-moral-derecho-práctica profesional."
    ]
  }
}