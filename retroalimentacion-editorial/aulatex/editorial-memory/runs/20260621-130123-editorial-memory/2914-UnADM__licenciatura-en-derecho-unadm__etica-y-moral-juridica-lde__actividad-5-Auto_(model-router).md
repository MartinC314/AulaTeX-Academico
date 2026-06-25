{
  "summary": [
    "Se consolida memoria editorial para Actividad 5 de Ética y Moral jurídica.",
    "Se preserva identidad UnADM y Licenciatura en Derecho.",
    "Se refuerza transferencia lateral desde Filosofía del Derecho solo con patrones reutilizables.",
    "Se evita copiar contenido temático exclusivo del nodo origen.",
    "Se mantiene normalización obligatoria a JSON parseable.",
    "Se conserva historial de incidencias por salidas no parseables.",
    "Se aplica compresión lossless por unión y deduplicación.",
    "Se refuerzan ejes editoriales: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se incorporan verificaciones locales sobre README, programa analítico y archivo .bib.",
    "Supuesto: la consigna textual exacta de Actividad 5 aún no está disponible."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular la actividad a la Licenciatura en Derecho.",
    "Alinear la actividad a Ética y Moral jurídica.",
    "Usar semestre 1, bloque 2, obligatoria, 8 créditos según README local.",
    "Citar la malla curricular como fuente de ubicación curricular.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Registrar ruta origen y destino de cada injerto de memoria.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "No promover reglas provisionales a canon sin validación manual.",
    "Conservar integridad académica con citas verificables.",
    "Evitar arrastrar conclusiones temáticas de Filosofía del Derecho sin justificación local."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido y parseable cuando se consolide memoria.",
    "Usar frases cortas, accionables y sin duplicados.",
    "Conservar secciones existentes y agregar solo mejoras verificables.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Definir objetivo puntual antes del desarrollo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Mantener estructura mínima: introducción, desarrollo, postura personal y conclusión cuando la consigna no especifique otra."
  ],
  "activity_rules": [
    "Verificar consigna textual exacta de Actividad 5 antes de redactar.",
    "Confirmar tipo de producto final solicitado.",
    "Alinear el producto a la pauta editorial de la asignatura.",
    "Incluir problema, conceptos, evidencia, análisis propio y conclusión.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Distinguir entre reflexión ética, moral profesional y análisis jurídico.",
    "Conectar dilemas ético-jurídicos con práctica profesional verificable.",
    "No asumir fuentes obligatorias de semanas posteriores sin confirmación local.",
    "No copiar redacción, conclusiones ni bibliografía exclusiva del nodo origen."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de propagar.",
    "Revisar manualmente respuestas no estructuradas antes de consolidar memoria.",
    "Confirmar que no se eliminen reglas útiles previas al fusionar.",
    "Validar ausencia de duplicados semánticos tras la fusión.",
    "Confirmar respaldo o marca de supuesto en cada afirmación no evidente.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Validar integridad sintáctica de archivos .bib tras cada edición.",
    "Verificar que el producto corresponda a la consigna de Actividad 5.",
    "Marcar para revisión manual incidencias locales detectadas en README y .bib.",
    "Unificar incidencias repetidas por ciclo en una plantilla única.",
    "Bloquear promoción de reglas provisionales si provienen de salidas no parseables."
  ],
  "latex_rules": [
    "Mantener compatibilidad con reportes y presentaciones LaTeX de la asignatura.",
    "Usar codificación y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas de compilación.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir nombres y rutas con caracteres anómalos antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Usar etica-y-moral-juridica.bib como archivo .bib local mientras se confirme el nombre canónico.",
    "No copiar preámbulos LaTeX completos en memoria editorial.",
    "Registrar solo reglas técnicas reutilizables, no bloques LaTeX extensos."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos bibliográficos.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "Conservar trazabilidad entre citas en texto y entradas .bib.",
    "Conservar metadatos mínimos: autor o editor, título, año, editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Marcar para revisión manual entradas potencialmente duplicadas por autor, título y año.",
    "Deduplicar claves bibliográficas duplicadas solo con validación manual previa.",
    "Verificar cierre correcto de cada entrada BibTeX antes de compilar.",
    "Confirmar si el truncamiento visible del .bib existe en el archivo real.",
    "No importar bibliografía exclusiva de Filosofía del Derecho salvo necesidad justificada por la consigna local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables entre asignaturas laterales.",
    "Aplicar analogía controlada sin copiar contenido específico del nodo origen.",
    "Conservar identidad institucional, calidad, estructura y patrones argumentativos comunes.",
    "Mantener especificidad local de Ética y Moral jurídica.",
    "Usar normalización manual si se detecta salida no estructurada en nodos vecinos.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Agrupar ciclos con fallo de parseo bajo una regla de incidencia deduplicada.",
    "Registrar ciclos con fallo como trazabilidad, no como contenido temático.",
    "Revisar Ciclos 1 a 11 antes de reutilizar incidencias históricas.",
    "No propagar conclusiones locales sin consigna verificable.",
    "Propagar reglas generales cuando falte consigna textual."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 5.",
    "Confirmar tipo de producto final solicitado.",
    "Confirmar rúbrica específica de evaluación.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si Actividad 5 requiere reporte, presentación, cuadro, caso o producto visual.",
    "Confirmar nombre canónico final del archivo .bib local.",
    "Confirmar si etica-y-moral-juridica.bib está truncado en el archivo real.",
    "Confirmar política local para depurar claves BibTeX duplicadas sin perder trazabilidad.",
    "Confirmar si se desea bloqueo automático tras N fallos consecutivos de parseo.",
    "Confirmar si las fuentes citadas en el .tex corresponden exactamente a Actividad 5.",
    "Confirmar si la actividad exige enfoque comparativo entre moral, ética y derecho.",
    "Confirmar alcance esperado de la postura personal."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Institucional sin rigidez excesiva.",
        "Reflexivo ante dilemas ético-jurídicos.",
        "Crítico sin perder respeto académico."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Trazabilidad de fuentes y memoria editorial.",
        "Respeto a consigna y rúbrica local.",
        "Ubicación curricular respaldada por malla curricular."
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
      "Conceptos éticos, morales, jurídicos y doctrinales pertinentes.",
      "Producto solicitado por la planeación.",
      "Evidencia verificable y citas explícitas.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Distinción entre ética, moral y derecho.",
      "Responsabilidad profesional del jurista.",
      "Dilema ético-jurídico contextualizado.",
      "Normalización editorial antes de propagar."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros y verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico con sensibilidad ética y moral.",
      "Conectar reflexión ética con práctica profesional del derecho.",
      "Evitar productos meramente descriptivos.",
      "Sostener la postura personal con evidencia consultable.",
      "Preservar memoria editorial útil para actividades futuras.",
      "Asegurar propagación confiable mediante JSON parseable."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Encuadre breve del problema.",
      "Secciones explícitas y ordenadas.",
      "Conceptos operativos definidos.",
      "Citas verificables en afirmaciones sustantivas.",
      "Marcado explícito de supuestos.",
      "Postura personal argumentada.",
      "Cierre con criterio jurídico propio.",
      "Lenguaje académico en español claro.",
      "Trazabilidad de fuentes locales.",
      "Sin bibliografía inventada.",
      "Sin conclusiones importadas de otra asignatura."
    ],
    "argumentative_patterns": [
      "Plantear problema y alcance.",
      "Definir conceptos operativos.",
      "Distinguir dimensión ética, moral y jurídica.",
      "Vincular marco normativo o doctrinal pertinente.",
      "Contrastar deber ser ético con práctica jurídica.",
      "Sustentar con fuentes verificables.",
      "Desarrollar análisis crítico propio.",
      "Evaluar implicaciones profesionales.",
      "Cerrar con conclusión jurídica transferible.",
      "Alinear respuesta a consigna y rúbrica.",
      "Marcar supuestos cuando falten datos locales.",
      "Evitar resumen sin postura."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral jurídica",
        "Integridad académica",
        "Evidencia verificable",
        "Análisis propio",
        "Postura argumentada",
        "Conclusión jurídica transferible",
        "Problema jurídico o social",
        "Conceptos éticos y jurídicos",
        "Marco normativo o doctrinal",
        "Práctica profesional del jurista",
        "Dilema ético-jurídico",
        "Normalización JSON",
        "Deduplicación lossless",
        "Propagación recursiva",
        "Analogía controlada",
        "Etica con los clásicos",
        "Ética general y profesional",
        "Compendio de ética",
        "En favor de los clásicos: una ética para el siglo XXI",
        "100 Técnicas Didácticas de Enseñanza y Aprendizaje",
        "Oración cívica",
        "Discurso en la inauguración de la Universidad Nacional",
        "La raza cósmica",
        "El perfil del hombre y la cultura en México",
        "El poder y el valor",
        "El ethos, destino del hombre",
        "Planificación de actividades S5",
        "Moral y Derecho en el ámbito jurídico mexicano"
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
        "sierraUniversidadNacional1910",
        "constitucionCPEUM2026",
        "cndhMarcoNormativo"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige identidad UnADM, citas verificables y criterio propio."
        },
        {
          "source": "Integridad académica",
          "target": "Evidencia verificable",
          "kind": "depends_on",
          "justification": "Las afirmaciones sustantivas requieren fuentes consultables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La postura del estudiante debe sostenerse en fuentes explícitas."
        },
        {
          "source": "Análisis propio",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "El cierre profesional deriva del razonamiento argumentado."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Conceptos éticos y jurídicos",
          "kind": "develops",
          "justification": "El encuadre del problema determina los conceptos que deben definirse."
        },
        {
          "source": "Conceptos éticos y jurídicos",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Los conceptos orientan la selección de doctrina, normas y datos pertinentes."
        },
        {
          "source": "Ética y Moral jurídica",
          "target": "Práctica profesional del jurista",
          "kind": "develops",
          "justification": "La asignatura conecta reflexión ética con conducta profesional."
        },
        {
          "source": "Dilema ético-jurídico",
          "target": "Postura argumentada",
          "kind": "supports",
          "justification": "El dilema permite construir una respuesta crítica con criterio propio."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Deduplicación lossless",
          "target": "Memoria editorial persistente",
          "kind": "supports",
          "justification": "La unión sin duplicados conserva reglas útiles sin recorte."
        },
        {
          "source": "Analogía controlada",
          "target": "Transferencia lateral",
          "kind": "supports",
          "justification": "Permite reutilizar patrones comunes sin copiar contenido exclusivo del origen."
        },
        {
          "source": "Bibliografía local",
          "target": "Actividad 5",
          "kind": "supports",
          "justification": "Las fuentes específicas deben registrarse en el .bib de la asignatura."
        }
      ],
      "evidence": [
        "README local: Materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: fuente curricular UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf.",
        "README local: la carpeta funciona como punto de entrada canónico.",
        "README local: cada actividad debe conservar identidad UnADM, integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: orientar productos académicos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: transformar planeación semanal en reportes, presentaciones y productos visuales.",
        "Programa analítico local: ejes de trabajo problema, conceptos, producto, análisis propio y conclusión.",
        "Programa analítico local: fuentes específicas deben agregarse en el .bib de la asignatura.",
        "Contexto local: README y programa contienen token Slug sin expandir.",
        "Contexto local: README muestra nombres de archivo con caracteres anómalos.",
        "Contexto local: etica-y-moral-juridica.bib muestra entradas duplicadas potenciales por autor, título y año.",
        "Contexto local: captura del .bib termina en entrada incompleta; requiere verificación en archivo real.",
        "Memoria destino: existen salidas no parseables previas desde Codex, Auto, Claude Foundry y GPT-Pro.",
        "Memoria destino: Actividad 5 usa reporte-etica-y-moral-juridica-Actividad-5.tex como artefacto primario.",
        "Memoria destino: claves citadas en .tex incluyen constitucionCPEUM2026, cndhMarcoNormativo, ronquilloarmasEticaGeneralProfesional2018 y singerCompendioEtica1995.",
        "Memoria origen: se transfieren solo patrones generales de problema, conceptos, evidencia, análisis propio y conclusión jurídica."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3 refuerza identidad UnADM sin importar contenido exclusivo de Filosofía del Derecho.",
      "Ciclo 3 consolida estructura base para Actividad 5 con analogía controlada.",
      "Ciclo 3 preserva incidencias históricas de parseo como control de calidad.",
      "Ciclo 3 deduplica reglas repetidas de estructura, bibliografía y LaTeX.",
      "Ciclo 3 mantiene preguntas abiertas por falta de consigna textual local.",
      "Ciclo 3 agrega verificación local de tokens Slug sin expandir.",
      "Ciclo 3 agrega revisión manual de duplicados BibTeX locales.",
      "Ciclo 3 conserva patrón argumentativo problema-conceptos-marco-análisis-cierre.",
      "Ciclo 3 refuerza distinción local entre ética, moral y derecho.",
      "Ciclo 3 bloquea transferencia de conclusiones y bibliografía exclusivas del nodo origen."
    ]
  }
}