{
  "summary": [
    "Se refuerza memoria editorial de Actividad 6 con transferencia lateral reusable desde Filosofía del Derecho.",
    "Se conserva compresión lossless por deduplicación y trazabilidad de fallas históricas de parseo.",
    "Se mantienen ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se preserva regla crítica: no propagar salidas no estructuradas sin normalización previa.",
    "Se agregan mejoras verificables del contexto local: token Slug sin expandir en README/programa y entrada .bib truncada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Usar tono académico-jurídico claro y preciso.",
    "Cerrar con criterio propio y aplicabilidad jurídica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Mantener coherencia entre objetivo, desarrollo y conclusión.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Evitar afirmaciones sin respaldo o sin marca de [Supuesto].",
    "Verificar correspondencia entre consigna de Actividad 6 y tipo de producto entregado.",
    "Traducir el análisis a aplicación profesional jurídica cuando proceda."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "No propagar salidas no estructuradas sin normalización manual.",
    "Confirmar que no se eliminen reglas útiles previas durante cada fusión.",
    "Validar consistencia entre consigna, estructura, evidencia y conclusión.",
    "Validar consistencia entre citas en texto y archivo .bib."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener compatibilidad con reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni completar datos sin respaldo.",
    "Conservar metadatos mínimos: autor/editor, título, año y fuente/editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Deduplicar entradas equivalentes por clave canónica sin perder trazabilidad.",
    "Resolver duplicados evidentes: huertaEticaConClasicos2000/huerta2000etica, ronquilloarmasEticaGeneralProfesional2018/ronquillo2018etica, singerCompendioEtica1995/singer1995compendio.",
    "Bloquear uso operativo de entradas truncadas hasta completar campos mínimos.",
    "[Supuesto] La entrada sierraUniversidadNacional1910 está truncada y requiere curación."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y parseables.",
    "Transferir solo patrones reutilizables, no redacción ni conclusiones específicas.",
    "Aplicar analogía controlada: conservar marco institucional y compuertas de calidad.",
    "Evitar regresiones frente a reglas útiles previas.",
    "Cuando falte consigna local, propagar estructura base y abrir preguntas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 6.",
    "Confirmar formato de entrega exigido: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación para ajustar profundidad argumentativa.",
    "Definir política local de clave canónica para deduplicación .bib.",
    "Confirmar cierre correcto del campo final en sierraUniversidadNacional1910."
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
        "Normalización estructurada obligatoria antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Ética y Moral jurídica.",
        "[Supuesto] Actividad 6 pendiente de confirmación por consigna textual."
      ]
    },
    "essence": [
      "Problema jurídico o social como disparador.",
      "Conceptos y marco normativo o doctrinal pertinentes.",
      "Evidencia verificable y trazable.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Transformar planeación semanal en productos académicos con fundamento jurídico y transferencia profesional.",
      "Asegurar calidad editorial persistente y reutilizable entre nodos laterales."
    ],
    "style_markers": [
      "Encuadre inicial breve.",
      "Secciones explícitas y ordenadas.",
      "Citas en afirmaciones sustantivas.",
      "Cierre con implicación jurídica práctica.",
      "Marcado explícito de [Supuesto] ante vacíos."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/marco -> análisis propio -> conclusión transferible.",
      "Afirmación -> evidencia verificable -> interpretación -> implicación jurídica.",
      "Consigna -> objetivo puntual -> desarrollo coherente -> validación final."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Problema jurídico o social",
        "Marco normativo o doctrinal",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Normalización JSON parseable",
        "Deduplicación bibliográfica canónica"
      ],
      "citations": [
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib",
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El programa analítico define el problema como eje de desarrollo."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "depends_on",
          "justification": "La conclusión debe derivar del razonamiento y evidencia."
        },
        {
          "source": "Normalización JSON parseable",
          "target": "Deduplicación bibliográfica canónica",
          "kind": "supports",
          "justification": "La estructura validada permite control de calidad y trazabilidad."
        }
      ],
      "evidence": [
        "README local: identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: ejes problema, conceptos, producto, análisis y cierre argumentativo.",
        "README/programa: token Slug sin expandir en referencia al .bib.",
        ".bib local: duplicados verificables y entrada sierraUniversidadNacional1910 truncada."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se consolidan patrones transversales sin copiar contenido específico del nodo origen.",
      "Se deduplican reglas repetidas y se preservan todas las reglas útiles previas.",
      "Se fortalece puerta de calidad de parseabilidad JSON para propagación recursiva.",
      "Se mantiene política de supuestos explícitos ante datos no visibles."
    ]
  }
}