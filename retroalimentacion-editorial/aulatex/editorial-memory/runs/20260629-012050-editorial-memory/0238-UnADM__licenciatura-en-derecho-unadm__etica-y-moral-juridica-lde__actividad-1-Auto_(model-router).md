{
  "summary": [
    "Se consolida memoria lateral desde Filosofía del Derecho hacia Ética y Moral Jurídica.",
    "Se transfieren solo patrones reutilizables y verificables.",
    "Se preserva identidad UnADM y contexto curricular local.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene contingencia histórica por salidas previas no parseables.",
    "Se corrige supuesto previo: sí existen reglas académicas transferibles desde el origen validado.",
    "Se evita copiar bibliografía exclusiva de Filosofía del Derecho.",
    "Se prioriza normalización JSON antes de propagación recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Mantener contexto de Licenciatura en Derecho.",
    "Ubicar la asignatura en semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura destino como entrada canónica.",
    "Registrar fuente de cada consolidación con ruta origen y destino.",
    "Etiquetar toda regla importada con origen y ciclo cuando aplique.",
    "Conservar trazabilidad de incidencias de parseo por modelo y actividad.",
    "Mantener fuentes provisionales por modelo si no hubo JSON verificable.",
    "Marcar como [Supuesto] cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas localmente como provisionales.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular cuando se declare contexto."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido conforme al esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Aplicar compresión lossless por deduplicación.",
    "No eliminar reglas útiles previas.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Marcar supuestos explícitamente con etiqueta [Supuesto]."
  ],
  "activity_rules": [
    "Alinear cada entrega a la pauta local: problema, conceptos, análisis propio y conclusión jurídica.",
    "Verificar que el producto corresponda a la consigna específica de Actividad 1.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Integrar fundamento jurídico, evidencia y transferencia profesional.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de semanas posteriores sin confirmación local.",
    "Distinguir síntesis conceptual de valoración ética y jurídica.",
    "Relacionar escuelas éticas con dilemas jurídicos solo si la consigna lo permite.",
    "Ajustar profundidad argumentativa a la rúbrica confirmada."
  ],
  "quality_gates": [
    "Validar parseo JSON antes de guardar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Bloquear propagación aguas abajo si no cumple esquema.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Registrar incidencias de formato como resumen operativo.",
    "Verificar deduplicación semántica sin perder reglas válidas.",
    "Confirmar que toda afirmación tenga respaldo o marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Evitar regresiones durante consolidación.",
    "Verificar correspondencia exacta con la consigna de Actividad 1."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar etica-y-moral-juridica.bib como archivo bibliográfico local verificado.",
    "Mantener consistencia editorial entre reporte y presentación de la asignatura.",
    "No agregar reglas LaTeX no verificadas por artefactos locales. [Supuesto]"
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Conservar trazabilidad entre citas en texto y entradas .bib.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Revisar y deduplicar claves bibliográficas duplicadas sin perder información.",
    "No importar bibliografía exclusiva de Filosofía del Derecho sin uso local verificado.",
    "No asumir que fuentes de semanas posteriores correspondan a Actividad 1.",
    "Resolver duplicados locales antes de fijar claves canónicas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales de calidad sin reducir especificidad local.",
    "Propagar solo patrones generales cuando falte consigna textual.",
    "Aplicar analogía controlada entre asignaturas laterales.",
    "No copiar conclusiones específicas de una asignatura hermana.",
    "No copiar bibliografía exclusiva de una asignatura hermana.",
    "Mantener trazabilidad de origen, destino y ciclo.",
    "Normalizar incidencias repetidas en una regla general deduplicada.",
    "Ciclo 2 requiere normalización manual si se reutiliza.",
    "Preservar reglas locales verificadas sobre Ética y Moral Jurídica."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1 en Ética y Moral Jurídica.",
    "Confirmar formato solicitado: reporte, presentación, cuadro comparativo u otro producto.",
    "Confirmar rúbrica de evaluación específica de Actividad 1.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si Actividad 1 corresponde a escuelas éticas clásicas o a otro tema.",
    "Definir formato canónico único para registro de errores de parseo por modelo.",
    "Definir criterio canónico para conservar una sola clave por obra duplicada en etica-y-moral-juridica.bib.",
    "Confirmar si se deben conservar claves human-readable o claves heredadas cortas.",
    "Confirmar si el README debe corregir nombres con caracteres anómalos.",
    "Confirmar si el curso comparte código 030 con Filosofía del Derecho o si es dato heredado. [Supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Reflexivo ante dilemas ético-jurídicos."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad de fuentes y supuestos.",
        "Respeto a la planeación semanal.",
        "Normalización estructurada antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura destino: Ética y Moral Jurídica.",
        "Semestre 1.",
        "Bloque 2.",
        "Asignatura obligatoria.",
        "8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos éticos y jurídicos pertinentes.",
      "Normas, doctrina o datos verificables.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Integridad académica.",
      "Normalización JSON.",
      "Deduplicación bibliográfica.",
      "Analogía controlada entre materias jurídicas básicas."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio ético-jurídico aplicable a la práctica profesional.",
      "Conectar teoría ética con responsabilidad jurídica cuando la consigna lo permita.",
      "Producir entregas verificables, trazables y compilables."
    ],
    "style_markers": [
      "Explicitar objetivo de actividad antes del desarrollo.",
      "Separar marco conceptual y marco normativo o doctrinal.",
      "Diferenciar síntesis de postura personal argumentada.",
      "Evitar resumen sin valoración crítica.",
      "Cerrar con conclusión jurídica aplicable.",
      "Marcar supuestos de forma visible.",
      "Usar citas verificables y consistentes.",
      "Mantener lenguaje académico sobrio.",
      "Evitar traslado literal desde asignaturas hermanas.",
      "Usar analogías solo si preservan especificidad local."
    ],
    "argumentative_patterns": [
      "Problema inicial breve -> conceptos éticos y jurídicos -> soporte doctrinal o normativo -> análisis propio -> conclusión.",
      "Afirmación jurídica -> evidencia verificable -> interpretación razonada -> implicación práctica.",
      "Escuela ética -> criterio moral -> consecuencia jurídica -> valoración profesional.",
      "Dilema ético -> conflicto de valores -> marco jurídico -> postura argumentada.",
      "Consigna -> producto requerido -> evidencia -> cierre transferible.",
      "Fuente local -> concepto aplicable -> análisis del estudiante -> conclusión."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral Jurídica",
        "Problema jurídico o social",
        "Conceptos éticos",
        "Conceptos jurídicos",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Normalización JSON",
        "Propagación recursiva",
        "Deduplicación bibliográfica",
        "Escuelas éticas clásicas",
        "Ética general y profesional",
        "Ética con los clásicos",
        "Compendio de ética",
        "Cuadro comparativo",
        "Planeación semanal"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib",
        "huertaEticaConClasicos2000",
        "huerta2000etica",
        "ronquilloarmasEticaGeneralProfesional2018",
        "ronquillo2018etica",
        "singerCompendioEtica1995",
        "singer1995compendio",
        "prieto2009favor",
        "lopezmartinezTecnicasDidacticas2023",
        "barredaOracionCivica1867",
        "sierraUniversidadNacional1910"
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
          "target": "Ética y Moral Jurídica",
          "kind": "develops",
          "justification": "La asignatura pertenece al trayecto jurídico inicial de la carrera."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere un problema delimitado para evitar exposición genérica."
        },
        {
          "source": "Conceptos éticos",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "La postura necesita categorías éticas claras para argumentar."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión profesional requiere fundamento verificable."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las citas explícitas reducen afirmaciones sin respaldo."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia segura de memoria."
        },
        {
          "source": "Deduplicación bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Reduce ambigüedad de citas sin perder información."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Ética y Moral Jurídica",
          "kind": "supports",
          "justification": "El origen aporta patrones editoriales comunes, no contenido específico."
        },
        {
          "source": "Escuelas éticas clásicas",
          "target": "Cuadro comparativo",
          "kind": "develops",
          "justification": "La memoria local registra secciones orientadas a comparación de escuelas."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto solicitado",
          "kind": "depends_on",
          "justification": "El formato final debe ajustarse a la consigna de la semana."
        },
        {
          "source": "Bibliografía local",
          "target": "Actividad 1",
          "kind": "supports",
          "justification": "Las fuentes específicas deben registrarse en etica-y-moral-juridica.bib."
        }
      ],
      "evidence": [
        "README local: Materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis propio y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la asignatura.",
        "Bib local: existen duplicados para Ética con los clásicos.",
        "Bib local: existen duplicados para Ética general y profesional.",
        "Bib local: existen duplicados para Compendio de ética.",
        "Memoria origen: estructura problema, conceptos, marco doctrinal, análisis propio y cierre.",
        "Memoria origen: bloqueo de propagación si no hay JSON parseable.",
        "Memoria origen: no inventar referencias.",
        "Memoria destino: actividad con artefacto reporte-etica-y-moral-juridica-Actividad-1.tex.",
        "Memoria destino: citas locales huerta2000etica, ronquillo2018etica y prieto2009favor."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 aplica refuerzo lateral-transversal por analogía controlada.",
      "Se preservan reglas locales verificadas de Ética y Moral Jurídica.",
      "Se consolidan reglas transferibles de estructura, calidad, LaTeX y bibliografía.",
      "Se excluyen fuentes exclusivas de Filosofía del Derecho salvo como patrón metodológico.",
      "Se normalizan duplicados semánticos sin recortar reglas útiles.",
      "Se sustituyen relaciones no canónicas por tipos permitidos.",
      "Se mantiene trazabilidad de contingencias por salidas no parseables.",
      "Se refuerza el ADN editorial como memoria persistente del nodo destino."
    ]
  }
}