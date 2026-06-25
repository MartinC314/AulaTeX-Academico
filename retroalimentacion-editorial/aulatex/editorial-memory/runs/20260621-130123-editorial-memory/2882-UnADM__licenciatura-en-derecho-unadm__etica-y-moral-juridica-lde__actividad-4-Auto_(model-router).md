{
  "summary": [
    "Se consolida Actividad 4 de Ética y Moral Jurídica con identidad UnADM.",
    "Se aplica transferencia lateral desde Filosofía del Derecho solo como patrón reutilizable.",
    "Se preserva estructura común: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se corrige el supuesto previo de falta de JSON válido del origen.",
    "Se mantiene historial de fallas de parseo JSON en ciclos previos.",
    "Se refuerza normalización obligatoria antes de propagar.",
    "Se conserva compresión por unión y deduplicación sin pérdida útil.",
    "Se evita copiar conclusiones, redacción o bibliografía exclusiva del nodo hermano.",
    "Se agregan controles locales verificables desde README, programa analítico y archivo .bib.",
    "Se mantiene encuadre curricular verificado: Derecho UnADM, semestre 1, bloque 2, obligatoria, 8 créditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular la actividad a la Licenciatura en Derecho.",
    "Ubicar la asignatura en semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Marcar como supuesto cualquier dato ausente en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Etiquetar como provisional toda regla derivada de salidas no parseables.",
    "Conservar trazabilidad de fuente, ciclo y propagación.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: Auto model-router desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1.",
    "Fuente provisional: GPT-Pro desde Actividad 1.",
    "Adaptar el contenido al campo de Ética y Moral Jurídica.",
    "No trasladar identidad temática de Filosofía del Derecho como si fuera local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones funcionales.",
    "Usar estructura base: problema, conceptos y fuentes, análisis propio, conclusión jurídica.",
    "Incluir marco normativo o doctrinal cuando la consigna lo requiera.",
    "Integrar el producto solicitado por la planeación semanal.",
    "Alinear el producto al formato solicitado por la consigna.",
    "Transformar la planeación en reporte, presentación o producto visual según corresponda.",
    "Asegurar coherencia entre actividad, reporte y presentación cuando coexistan.",
    "Evitar secciones vacías en memoria persistente.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Alinear la estructura con los ejes del programa analítico local."
  ],
  "activity_rules": [
    "Adaptar la Actividad 4 al encuadre de Ética y Moral Jurídica.",
    "Vincular el producto con un problema jurídico o social concreto.",
    "Explicar relación operativa entre ética, moral y norma jurídica cuando la consigna lo pida.",
    "Contrastar moral personal, moral social y moral ideal si aplica.",
    "Diferenciar validez jurídica y valoración moral cuando sea pertinente.",
    "Incluir postura propia sustentada.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otra actividad como obligatorias para Actividad 4.",
    "No copiar redacción literal de nodos hermanos.",
    "No transferir conclusiones específicas de Filosofía del Derecho.",
    "Ajustar profundidad y formato a la rúbrica local pendiente."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar respuestas no estructuradas antes de reutilizarlas.",
    "Normalizar manualmente ciclos con fallas de parseo.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Validar deduplicación sin pérdida de reglas útiles.",
    "Confirmar que toda afirmación tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar integridad sintáctica del archivo .bib antes de citar.",
    "Registrar y corregir entradas BibTeX truncadas antes de compilación final.",
    "Verificar correspondencia del producto con la consigna de Actividad 4.",
    "Verificar nombres de archivo del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres.",
    "Resolver tokens sin expandir antes de compilar.",
    "No propagar reglas laterales sin adaptación local."
  ],
  "latex_rules": [
    "Redactar entregables en LaTeX con estructura académica clara.",
    "Usar codificación y acentos correctos en español.",
    "Mantener compatibilidad con archivos canónicos de la materia.",
    "Usar claves BibTeX existentes y verificadas.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos.",
    "Compilar sin referencias rotas.",
    "Sincronizar reporte y presentación cuando ambos existan.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analítico.",
    "Corregir nombres anómalos como rutas truncadas en README.",
    "Usar como supuesto local el archivo etica-y-moral-juridica.bib hasta confirmación."
  ],
  "bibliography_rules": [
    "Usar bibliografía local de la asignatura como base inicial.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "No inventar fuentes.",
    "No inventar metadatos bibliográficos.",
    "Usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año, fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Depurar duplicados BibTeX equivalentes cuando se edite.",
    "Preferir una clave canónica por obra.",
    "Mantener alias solo si existe dependencia técnica.",
    "Marcar entradas truncadas o incompletas para corrección antes de citar.",
    "No importar bibliografía exclusiva de Filosofía del Derecho sin uso local verificado."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Transferir laterales solo como patrones, no como contenido final.",
    "Aplicar analogía controlada entre Filosofía del Derecho y Ética y Moral Jurídica.",
    "Preservar identidad UnADM, integridad académica y conclusión jurídica.",
    "Mantener nota de normalización manual mientras existan ciclos no parseables.",
    "Ciclos 1 a 11 requieren normalización manual si se reutilizan.",
    "Ciclo 17 consolida refuerzo lateral con fuente origen parseable.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Propagar solo reglas generales cuando falte consigna textual.",
    "No propagar bibliografía temática de un hermano como obligatoria.",
    "Mantener deduplicación por equivalencia semántica verificable."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar si el entregable principal es reporte, presentación u otro formato.",
    "Confirmar producto solicitado por la planeación semanal.",
    "Confirmar si debe elaborarse mapa conceptual, cuadro comparativo u otro recurso.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar plantilla LaTeX oficial de actividad.",
    "Confirmar nombre canónico final del archivo .bib local.",
    "Confirmar política formal de deduplicación BibTeX por clave canónica.",
    "Confirmar y reparar la entrada BibTeX truncada al final del archivo .bib.",
    "Confirmar si los alias BibTeX actuales tienen dependencias técnicas.",
    "Confirmar si las claves genéricas clave, clave1 y clave2 deben reemplazarse."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Prudente ante datos no verificados.",
        "Institucional sin perder análisis crítico."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad de fuente, ciclo y propagación.",
        "Normalización obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria.",
        "8 créditos.",
        "Asignatura destino: Ética y Moral Jurídica.",
        "Nodo de trabajo: Actividad 4."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Relación entre moral y Derecho en el ámbito jurídico mexicano.",
      "Ética como reflexión crítica de la conducta.",
      "Moral como práctica valorativa individual o social.",
      "Norma jurídica como regla obligatoria institucionalizada.",
      "Obligación como deber exigible.",
      "Sanción estatal como coacción legítima.",
      "Validez jurídica no idéntica a aprobación moral."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico con responsabilidad ética.",
      "Distinguir descripción moral, juicio ético y consecuencia jurídica.",
      "Conectar el aprendizaje con práctica profesional transferible.",
      "Evitar productos meramente expositivos.",
      "Proteger integridad académica mediante citas y trazabilidad."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Secciones funcionales y no ornamentales.",
      "Citas verificables en afirmaciones fuertes.",
      "Postura personal argumentada.",
      "Conclusión jurídica con implicación práctica.",
      "Supuestos marcados de forma visible.",
      "Fuentes provisionales etiquetadas.",
      "Lenguaje académico sobrio.",
      "Analogía controlada entre asignaturas.",
      "Adaptación local sin copia literal."
    ],
    "argumentative_patterns": [
      "Delimitar problema -> definir conceptos -> aplicar marco -> argumentar postura -> concluir.",
      "Distinguir ética, moral y Derecho antes de valorar un caso.",
      "Contrastar moral y norma jurídica cuando exista tensión.",
      "Relacionar doctrina con consecuencia práctica.",
      "Usar evidencia antes de emitir juicio conclusivo.",
      "Evitar resumen pasivo; priorizar inferencia justificada.",
      "Cerrar con criterio profesional transferible.",
      "Alinear pregunta guía, desarrollo y conclusión.",
      "Separar afirmaciones verificadas de supuestos.",
      "No convertir bibliografía base en prueba automática."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Trazabilidad editorial",
        "Problema jurídico o social",
        "Planeación semanal",
        "Producto académico",
        "Evidencia verificable",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Ética",
        "Moral",
        "Derecho",
        "Norma jurídica",
        "Moral personal",
        "Moral social",
        "Moral ideal",
        "Obligación jurídica",
        "Sanción estatal",
        "Validez jurídica",
        "Valoración moral",
        "Actividad 4",
        "etica-y-moral-juridica.bib",
        "programa-analitico-etica-y-moral-juridica.md",
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
        "garciaMaynezEtica",
        "cndhMarcoNormativo2026",
        "sanchezVazquezEtica1969",
        "villoroPoderValor1997",
        "gonzalezEthosDestino1996",
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
          "source": "Carpeta de asignatura",
          "target": "Trazabilidad editorial",
          "kind": "supports",
          "justification": "El README la define como punto de entrada canónico."
        },
        {
          "source": "Planeación semanal",
          "target": "Producto académico",
          "kind": "develops",
          "justification": "El programa analítico ordena transformar la planeación en productos."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o caso delimitado."
        },
        {
          "source": "Conceptos y fuentes",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "Los conceptos y fuentes sostienen la inferencia jurídica."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La conclusión debe derivar del razonamiento y la evidencia."
        },
        {
          "source": "Ética",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "Se relacionan, pero cumplen funciones conceptuales distintas."
        },
        {
          "source": "Moral",
          "target": "Norma jurídica",
          "kind": "contrasts",
          "justification": "La valoración moral no equivale automáticamente a validez jurídica."
        },
        {
          "source": "Norma jurídica",
          "target": "Sanción estatal",
          "kind": "depends_on",
          "justification": "La coercibilidad distingue la regla jurídica en el análisis local."
        },
        {
          "source": "Ética y Moral Jurídica",
          "target": "Filosofía del Derecho",
          "kind": "contrasts",
          "justification": "La relación lateral permite patrones comunes, no copia temática."
        },
        {
          "source": "Bibliografía local",
          "target": "Evidencia verificable",
          "kind": "supports",
          "justification": "El archivo .bib local contiene la base inicial de consulta."
        },
        {
          "source": "Entradas BibTeX duplicadas",
          "target": "Clave canónica",
          "kind": "depends_on",
          "justification": "La depuración requiere elegir una clave estable por obra."
        },
        {
          "source": "Entrada BibTeX truncada",
          "target": "Compilación final",
          "kind": "contrasts",
          "justification": "Una entrada incompleta puede romper referencias y debe corregirse."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular malla-curricular-derecho-unadm.pdf.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: propósito de transformar planeación en productos académicos.",
        "Programa analítico local: ejes de problema, conceptos, producto, análisis y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la asignatura.",
        "Archivo etica-y-moral-juridica.bib: existen entradas duplicadas equivalentes.",
        "Archivo etica-y-moral-juridica.bib: entrada sierraUniversidadNacional1910 aparece truncada.",
        "Memoria destino: fallas previas de parseo JSON en Actividad 4.",
        "Memoria origen: patrón reutilizable de problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
        "Regla de salto lateral: no copiar redacción, conclusiones ni bibliografía exclusiva del hermano."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se consolida transferencia lateral-transversal.",
      "Se refuerza identidad UnADM sin cambiar asignatura destino.",
      "Se conserva ubicación curricular verificada por contexto local.",
      "Se deduplican reglas repetidas de tono, estructura y calidad.",
      "Se preserva historial de normalización manual por fallas de parseo.",
      "Se integra regla del origen sobre bloqueo de salidas no JSON.",
      "Se integra patrón de conclusión jurídica transferible.",
      "Se evita importar bibliografía exclusiva de Filosofía del Derecho.",
      "Se eleva la relación ética-moral-Derecho como núcleo local.",
      "Se marca como pendiente la consigna exacta de Actividad 4.",
      "Se detecta necesidad de reparar BibTeX truncado.",
      "Se mantiene compresión lossless por deduplicación editorial."
    ]
  }
}