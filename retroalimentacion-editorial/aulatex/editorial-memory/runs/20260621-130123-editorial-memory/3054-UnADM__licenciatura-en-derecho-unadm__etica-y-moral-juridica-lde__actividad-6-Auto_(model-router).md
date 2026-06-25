{
  "summary": [
    "Se consolida memoria editorial de Actividad 6 en Ética y Moral jurídica.",
    "Se preserva historial de fallas de JSON parseable como contexto de calidad.",
    "Se refuerza identidad UnADM desde README y programa analítico local.",
    "Se integra transferencia lateral solo de patrones reutilizables.",
    "Se evita copiar contenido específico de Filosofía del Derecho.",
    "Se mantiene compresión lossless por deduplicación.",
    "Se conservan ejes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se agregan controles locales de bibliografía duplicada y entrada truncada.",
    "Ciclo 16 refuerza analogía controlada entre asignaturas jurídicas de primer semestre."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Alinear contenido con Licenciatura en Derecho.",
    "Usar ubicación curricular local: semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Tomar la carpeta de Ética y Moral jurídica como punto de entrada canónico.",
    "Usar tono académico-jurídico claro.",
    "Cerrar con criterio propio y aplicabilidad jurídica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna.",
    "Tratar salidas heredadas de Codex, Auto, Claude Foundry y GPT-Pro como provisionales.",
    "[Supuesto] Actividad 6 pertenece formalmente a Ética y Moral jurídica hasta confirmar consigna textual."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Ajustar secciones al producto solicitado por la planeación semanal.",
    "Mantener coherencia entre objetivo, desarrollo y conclusión.",
    "Usar secciones reutilizables para reporte o presentación.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Evitar estructura genérica si la consigna exige cuadro, mapa, presentación u otro producto."
  ],
  "activity_rules": [
    "Verificar correspondencia con la consigna de Actividad 6.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entrega solo descriptiva o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir afirmaciones verificadas de supuestos.",
    "Traducir el análisis a aplicación profesional jurídica cuando proceda.",
    "Relacionar ética, moral y derecho solo con fuentes locales o verificadas.",
    "No usar bibliografía exclusiva de otra asignatura sin verificación local.",
    "No asumir fuentes de semanas posteriores como obligatorias para Actividad 6."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "No propagar salidas no estructuradas sin normalización manual.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no se eliminen reglas útiles previas.",
    "Validar consistencia entre consigna, objetivo, desarrollo y conclusión.",
    "Confirmar respaldo o marca de [Supuesto] en afirmaciones sustantivas.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar entradas .bib truncadas antes de citar.",
    "Revisar duplicados bibliográficos antes de compilar.",
    "Bloquear citas operativas con claves inexistentes o incompletas."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reporte-etica-y-moral-juridica.tex.",
    "Mantener compatibilidad con presentacion-etica-y-moral-juridica.tex.",
    "Usar codificación y acentos correctos en español.",
    "Usar secciones claras y estables.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Compilar sin errores críticos.",
    "Compilar sin referencias rotas.",
    "Mantener consistencia terminológica entre .tex, README y programa analítico.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Verificar nombres de archivos antes de referenciarlos.",
    "[Supuesto] El .bib canónico local es etica-y-moral-juridica.bib por Slug del README."
  ],
  "bibliography_rules": [
    "Registrar fuentes específicas de Actividad 6 en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM y bibliografía base local.",
    "No inventar fuentes.",
    "No completar datos bibliográficos sin respaldo.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Deduplicar entradas equivalentes por clave canónica sin perder trazabilidad.",
    "Resolver duplicados huertaEticaConClasicos2000 y huerta2000etica.",
    "Resolver duplicados ronquilloarmasEticaGeneralProfesional2018 y ronquillo2018etica.",
    "Resolver duplicados singerCompendioEtica1995 y singer1995compendio.",
    "Marcar entradas incompletas para curación editorial antes de citar.",
    "[Supuesto] La entrada sierraUniversidadNacional1910 está truncada por campo final incompleto."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir identidad institucional, estructura, calidad y patrones argumentativos.",
    "No transferir conclusiones específicas de asignaturas hermanas.",
    "No transferir bibliografía exclusiva de Filosofía del Derecho.",
    "Usar analogía controlada entre ética jurídica y filosofía jurídica.",
    "Mantener especificidad local de Ética y Moral jurídica.",
    "Reutilizar compuertas de calidad institucional sin reducir reglas locales.",
    "Normalizar manualmente memorias no estructuradas antes de reutilizarlas.",
    "Ciclos 1 a 11 conservan historial de normalización pendiente si se reabren.",
    "Evitar regresiones respecto de reglas útiles previas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar formato de entrega exigido: reporte, presentación, cuadro u otro.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si Actividad 6 requiere bibliografía propia o solo base local.",
    "Confirmar clave canónica para cada par duplicado del .bib.",
    "Completar y validar sierraUniversidadNacional1910 en el .bib local.",
    "Confirmar si las claves clave, clave1 y clave2 son marcadores temporales.",
    "Confirmar uso operativo de constitucionCPEUM2026 y cndhMarcoNormativo en Actividad 6."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Reflexivo en ética y moral jurídica."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Normalización estructurada obligatoria antes de propagación.",
        "Ubicación curricular sustentada en malla institucional."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1.",
        "Bloque 2.",
        "Asignatura obligatoria.",
        "8 créditos.",
        "Asignatura: Ética y Moral jurídica.",
        "[Supuesto] Actividad 6 pendiente de confirmación por consigna textual."
      ]
    },
    "essence": [
      "Identidad institucional UnADM.",
      "Integridad académica.",
      "Problema jurídico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Marco normativo o doctrinal.",
      "Análisis propio y postura académica.",
      "Conclusión jurídica transferible.",
      "Producto solicitado por la planeación.",
      "Ética y moral jurídica como eje local.",
      "Aplicación profesional del razonamiento ético-jurídico."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en producto académico verificable.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico con base ética y responsabilidad profesional.",
      "Evitar respuestas descriptivas sin postura.",
      "Asegurar transferencia del aprendizaje a la práctica jurídica.",
      "Conservar trazabilidad editorial para reutilización segura."
    ],
    "style_markers": [
      "Encuadre inicial breve y preciso.",
      "Objetivo explícito antes del desarrollo.",
      "Secciones ordenadas y reutilizables.",
      "Citas verificables en afirmaciones sustantivas.",
      "Supuestos marcados de forma visible.",
      "Cierre con criterio jurídico propio.",
      "Aplicabilidad profesional explícita.",
      "Terminología coherente con programa analítico local.",
      "Sin fuentes inventadas.",
      "Sin contenido exclusivo de asignatura hermana."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> marco -> análisis propio -> conclusión transferible.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación jurídica.",
      "Consigna -> objetivo -> producto -> validación final.",
      "Concepto ético -> relevancia jurídica -> aplicación profesional.",
      "Norma o doctrina -> caso o problema -> postura razonada.",
      "Fuente local -> paráfrasis fiel -> comentario crítico.",
      "Supuesto -> límite de validez -> pregunta abierta."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Ética y Moral jurídica",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Normalización JSON parseable",
        "Deduplicación bibliográfica canónica",
        "Actividad 6",
        "Planeación semanal",
        "Producto académico",
        "Ética con los clásicos",
        "Ética general y profesional",
        "Compendio de ética",
        "En favor de los clásicos: una ética para el siglo XXI",
        "100 Técnicas Didácticas de Enseñanza y Aprendizaje",
        "Oración cívica",
        "Discurso en la inauguración de la Universidad Nacional",
        "Entrada .bib truncada"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
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
        "cndhMarcoNormativo",
        "clave",
        "clave1",
        "clave2"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono académico-jurídico",
          "kind": "supports",
          "justification": "El README local exige identidad UnADM e integridad académica."
        },
        {
          "source": "Malla curricular de Derecho",
          "target": "Ubicación curricular",
          "kind": "supports",
          "justification": "El README local la declara como fuente de semestre, bloque, tipo y créditos."
        },
        {
          "source": "Programa analítico local",
          "target": "Estructura problema-conceptos-fuentes-análisis-cierre",
          "kind": "develops",
          "justification": "El programa analítico enumera esos ejes de trabajo."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El problema funciona como disparador del razonamiento."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión debe derivar del razonamiento y no de un resumen."
        },
        {
          "source": "Citas verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta editorial local exige fuentes verificables."
        },
        {
          "source": "Normalización JSON parseable",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "La memoria no estructurada debe bloquearse antes de reutilizarse."
        },
        {
          "source": "Deduplicación bibliográfica canónica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Evita claves duplicadas, citas rotas y pérdida de trazabilidad."
        },
        {
          "source": "Entrada .bib truncada",
          "target": "Cita operativa",
          "kind": "contrasts",
          "justification": "Una entrada incompleta no debe citarse hasta ser curada."
        },
        {
          "source": "Patrones de Filosofía del Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "supports",
          "justification": "Solo se transfieren reglas generales de identidad, estructura y calidad."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: propósito de reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la asignatura.",
        ".bib local: duplicados huertaEticaConClasicos2000 y huerta2000etica.",
        ".bib local: duplicados ronquilloarmasEticaGeneralProfesional2018 y ronquillo2018etica.",
        ".bib local: duplicados singerCompendioEtica1995 y singer1995compendio.",
        ".bib local: sierraUniversidadNacional1910 aparece truncada.",
        "Memoria previa: fallas de JSON parseable desde Codex, Auto, Claude Foundry y GPT-Pro.",
        "Transferencia lateral: se conservan patrones reutilizables y no contenido específico de Filosofía del Derecho."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16 aplica refuerzo lateral-transversal desde Filosofía del Derecho.",
      "Se conserva solo lo reutilizable: identidad, estructura, calidad y argumentación.",
      "Se descarta transferencia de bibliografía exclusiva del origen.",
      "Se refuerza normalización JSON como compuerta obligatoria.",
      "Se preserva trazabilidad de fallas históricas sin hacerlas operativas.",
      "Se consolida punto de entrada canónico local.",
      "Se preserva regla de marcar supuestos.",
      "Se fortalecen controles de .bib local.",
      "Se mantiene objetivo de conclusión jurídica transferible.",
      "Se evita regresión de reglas útiles previas."
    ]
  }
}