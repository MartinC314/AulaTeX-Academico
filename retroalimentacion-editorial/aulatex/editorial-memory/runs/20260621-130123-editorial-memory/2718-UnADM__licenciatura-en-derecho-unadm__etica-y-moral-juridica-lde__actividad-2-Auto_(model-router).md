{
  "summary": [
    "Se consolida memoria editorial de Actividad 2 en Ética y Moral jurídica.",
    "Se refuerza transferencia lateral desde Filosofía del Derecho solo con patrones reutilizables.",
    "Se preservan reglas útiles previas mediante deduplicación semántica.",
    "Se mantiene identidad UnADM y Licenciatura en Derecho.",
    "Se fija eje editorial común: problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Se conserva bloqueo ante salidas no parseables.",
    "Se integra evidencia local del README, programa analítico y archivo .bib.",
    "Supuesto: falta consigna textual exacta de Actividad 2.",
    "Supuesto: el producto esperado puede ser cuadro comparativo, según memoria previa.",
    "Ciclo 20 refuerza estructura, calidad, trazabilidad y analogía controlada."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Conservar enfoque de Licenciatura en Derecho.",
    "Conservar enfoque de la asignatura Ética y Moral jurídica.",
    "Alinear la actividad a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Citar la malla curricular UnADM para ubicación curricular cuando se use ese dato.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Registrar ruta de origen y destino en cada propagación.",
    "No reemplazar reglas previas útiles; anexar o deduplicar.",
    "Mantener tono formal, académico y jurídicamente preciso.",
    "Evitar grandilocuencia; privilegiar sobriedad verificable."
  ],
  "structure_rules": [
    "Entregar memoria en JSON válido y parseable.",
    "Usar el esquema requerido completo.",
    "No agregar campos fuera del esquema solicitado.",
    "Redactar reglas en frases cortas y accionables.",
    "Eliminar duplicados sin perder significado útil.",
    "Iniciar la actividad con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener trazabilidad de cambios por ciclo."
  ],
  "activity_rules": [
    "Alinear cada actividad a problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Ajustar el producto al formato solicitado por la planeación semanal.",
    "Orientar el desarrollo a claridad, fundamento jurídico, evidencia y transferencia profesional.",
    "Evitar asumir fuentes de semanas distintas sin validación local.",
    "Distinguir ética, moral y derecho cuando la consigna lo permita.",
    "Relacionar escuelas éticas con criterios de decisión jurídica cuando aplique.",
    "Supuesto: si el producto es cuadro comparativo, comparar escuelas con criterios homogéneos.",
    "Supuesto: si el tema es escuelas contemporáneas, incluir utilidad jurídica de cada corriente."
  ],
  "quality_gates": [
    "Validar sintaxis JSON antes de guardar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Aplicar compresión por unión y deduplicación lossless.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna de Actividad 2.",
    "Verificar consistencia con README y programa analítico locales.",
    "Revisar integridad académica antes de publicar.",
    "Conservar trazabilidad de fuentes provisionales.",
    "Bloquear uso automático de reglas exclusivas de otra asignatura."
  ],
  "latex_rules": [
    "Mantener compatibilidad con la suite LaTeX de la asignatura.",
    "Usar UTF-8 y acentos correctos en .tex y .bib.",
    "Conservar entradas canónicas: reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Registrar Actividad 2 en archivo propio cuando exista producto individual.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Separar contenido, citas y bibliografía para compilación estable.",
    "Corregir caracteres anómalos en rutas y nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar etica-y-moral-juridica.bib como archivo bibliográfico local verificable.",
    "No copiar LaTeX completo en memoria editorial."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos bibliográficos.",
    "Usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM cuando apliquen al encuadre.",
    "Agregar referencias verificables en etica-y-moral-juridica.bib.",
    "Conservar metadatos mínimos: autor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Deduplicar obras equivalentes con distinta clave sin perder trazabilidad.",
    "Conservar temporalmente claves duplicadas hasta definir política de alias.",
    "Validar citas en texto contra claves existentes en .bib.",
    "No transferir bibliografía exclusiva de Filosofía del Derecho a Ética y Moral jurídica.",
    "Supuesto: existen duplicados locales verificables por metadatos coincidentes.",
    "Supuesto: falta política final de fusión de claves BibTeX duplicadas."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas parseables y verificadas.",
    "Propagar laterales solo por analogía controlada.",
    "Transferir identidad institucional, estructura, calidad y patrones argumentativos.",
    "No copiar conclusiones específicas de nodos hermanos.",
    "No copiar bibliografía exclusiva de nodos hermanos.",
    "Reutilizar ejes editoriales comunes de Licenciatura en Derecho.",
    "Conservar especificidad local de Ética y Moral jurídica.",
    "Aplicar normalización manual si aparece salida no estructurada.",
    "Mantener trazabilidad de origen y destino en futuras corridas.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclos 1 a 11 registran salidas no parseables y requieren cautela.",
    "Ciclo 20 refuerza validación local antes de propagación aguas abajo."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 2.",
    "Confirmar si Actividad 2 requiere reporte, presentación, cuadro comparativo u otro formato.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si el tema local es escuelas clásicas o contemporáneas de la ética.",
    "Confirmar criterios de comparación exigidos para el producto final.",
    "Definir política editorial para alias y fusión de claves BibTeX duplicadas.",
    "Definir umbral de bloqueo tras ciclos consecutivos sin JSON parseable.",
    "Confirmar formato de trazabilidad de fuentes provisionales por modelo.",
    "Confirmar si las claves genéricas clave, clave1 y clave2 deben eliminarse o reemplazarse.",
    "Confirmar recuperación de memoria estructurada previa de Actividad 1 local.",
    "Confirmar nombre canónico final de productos individuales por actividad."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable.",
        "Institucional sin grandilocuencia."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Normalización estructurada antes de propagar.",
        "Respeto a la planeación semanal.",
        "Trazabilidad de reglas y decisiones editoriales."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Asignatura: Ética y Moral jurídica.",
        "Semestre 1.",
        "Bloque 2.",
        "Asignatura obligatoria.",
        "8 créditos.",
        "Actividad 2.",
        "Relación lateral-transversal con Filosofía del Derecho."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Ética y moral como criterios de orientación profesional.",
      "Escuelas éticas como marcos de decisión.",
      "Integridad académica como condición editorial.",
      "Comparación conceptual con utilidad jurídica.",
      "Transferencia profesional del razonamiento ético-jurídico."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico con base ética y moral.",
      "Evitar productos meramente descriptivos.",
      "Asegurar evidencia, citas y trazabilidad.",
      "Conectar teoría ética con práctica jurídica.",
      "Sostener conclusiones útiles para el ejercicio profesional."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explícitos ante falta de evidencia.",
      "Citas verificables.",
      "Trazabilidad de fuentes y decisiones.",
      "Cierre con criterio jurídico propio.",
      "Comparaciones con criterios homogéneos.",
      "Distinción entre dato local y regla transferida.",
      "Evitar redacción literal heredada de nodos hermanos."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo al inicio.",
      "Definir conceptos antes de valorar.",
      "Relacionar ética, moral y derecho con precisión.",
      "Contrastar corrientes éticas mediante criterios comunes.",
      "Vincular marco doctrinal con práctica jurídica.",
      "Sostener postura propia con evidencia.",
      "Explicar implicaciones profesionales de cada postura.",
      "Cerrar con conclusión jurídica transferible.",
      "Distinguir descripción, comparación y valoración.",
      "Evitar saltos argumentales sin fuente o supuesto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral jurídica",
        "Actividad 2",
        "Problema jurídico o social",
        "Conceptos clave",
        "Marco normativo o doctrinal",
        "Fuentes verificables",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Deduplicación bibliográfica con trazabilidad",
        "Escuelas contemporáneas de la ética",
        "Utilitarismo",
        "Ética del cuidado",
        "Neopositivismo",
        "Relativismo",
        "Neokantismo",
        "Marxismo",
        "Ética con los clásicos",
        "Ética general y profesional",
        "Compendio de ética",
        "Técnicas didácticas de enseñanza y aprendizaje"
      ],
      "citations": [
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
        "sierraUniversidadNacional1910",
        "clave",
        "clave1",
        "clave2"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Licenciatura en Derecho",
          "kind": "supports",
          "justification": "El README local ubica la materia dentro de la Licenciatura en Derecho de la UnADM."
        },
        {
          "source": "Licenciatura en Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "supports",
          "justification": "La asignatura pertenece al programa curricular indicado por el README local."
        },
        {
          "source": "Programa analítico local",
          "target": "Ejes editoriales de actividad",
          "kind": "develops",
          "justification": "El programa define problema, conceptos, fuentes, análisis propio y cierre argumentativo."
        },
        {
          "source": "Ejes editoriales de actividad",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La secuencia editorial culmina en una conclusión aplicable a la práctica jurídica."
        },
        {
          "source": "Fuentes verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta editorial local exige citas verificables e integridad académica."
        },
        {
          "source": "Integridad académica",
          "target": "Deduplicación bibliográfica con trazabilidad",
          "kind": "depends_on",
          "justification": "El control de claves y metadatos evita citas ambiguas o duplicadas."
        },
        {
          "source": "etica-y-moral-juridica.bib",
          "target": "Deduplicación bibliográfica con trazabilidad",
          "kind": "supports",
          "justification": "El archivo local contiene obras equivalentes con claves distintas."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "supports",
          "justification": "La relación lateral-transversal permite transferir patrones generales de argumentación jurídica."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Bibliografía local de Ética y Moral jurídica",
          "kind": "contrasts",
          "justification": "Las fuentes exclusivas de Filosofía no deben copiarse al destino sin validación local."
        },
        {
          "source": "Escuelas contemporáneas de la ética",
          "target": "Criterios de decisión jurídica",
          "kind": "develops",
          "justification": "Las corrientes éticas pueden organizar la comparación de posturas con utilidad profesional."
        },
        {
          "source": "Análisis propio",
          "target": "Postura académica",
          "kind": "develops",
          "justification": "La actividad exige criterio del estudiante y no solo resumen descriptivo."
        },
        {
          "source": "Citas en texto",
          "target": "Archivo .bib local",
          "kind": "depends_on",
          "justification": "La compilación estable requiere correspondencia entre citas y claves BibTeX."
        }
      ],
      "evidence": [
        "README local: materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: productos académicos con problema, conceptos, fuentes, análisis propio y cierre.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib local.",
        "etica-y-moral-juridica.bib: contiene huertaEticaConClasicos2000 y huerta2000etica para la misma obra.",
        "etica-y-moral-juridica.bib: contiene ronquilloarmasEticaGeneralProfesional2018 y ronquillo2018etica para la misma obra.",
        "etica-y-moral-juridica.bib: contiene singerCompendioEtica1995 y singer1995compendio para la misma obra.",
        "Memoria previa: Actividad 2 registra intentos no parseables desde varios modelos.",
        "Memoria previa: documento local cita huertaEticaConClasicos2000, ronquilloarmasEticaGeneralProfesional2018, singerCompendioEtica1995 y lopezmartinezTecnicasDidacticas2023."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20 preserva normalización obligatoria antes de propagar.",
      "Ciclo 20 deduplica reglas repetidas sin eliminar contenido útil.",
      "Ciclo 20 limita transferencia desde Filosofía a patrones reutilizables.",
      "Ciclo 20 evita copiar bibliografía exclusiva del nodo origen.",
      "Ciclo 20 refuerza eje problema-conceptos-fuentes-análisis-cierre.",
      "Ciclo 20 incorpora evidencia local de README, programa y .bib.",
      "Ciclo 20 conserva alerta por salidas no parseables anteriores.",
      "Ciclo 20 marca como supuesto la falta de consigna textual exacta.",
      "Ciclo 20 mantiene política de citas verificables.",
      "Ciclo 20 refuerza deduplicación bibliográfica con trazabilidad."
    ]
  }
}