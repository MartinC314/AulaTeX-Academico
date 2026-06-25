{
  "summary": [
    "Se consolida memoria editorial de Actividad 2 para Ética y Moral jurídica.",
    "Se refuerza identidad UnADM desde transferencia lateral controlada.",
    "Se preservan reglas útiles previas con deduplicación semántica.",
    "Se transfieren solo patrones reutilizables desde Filosofía del Derecho.",
    "Se excluyen conclusiones y bibliografía exclusiva del nodo origen.",
    "Se conserva bloqueo ante salidas no parseables.",
    "Se integra evidencia local del README, programa analítico y .bib.",
    "Supuesto: falta consigna textual completa de Actividad 2."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en toda entrega.",
    "Conservar enfoque de Licenciatura en Derecho.",
    "Conservar enfoque de la asignatura Ética y Moral jurídica.",
    "Alinear la actividad a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Registrar ruta de origen y destino en cada propagación.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Citar la malla curricular solo para ubicación curricular.",
    "No reemplazar reglas útiles previas; anexar o deduplicar.",
    "Fuente provisional: Codex desde Actividad 1.",
    "Fuente provisional: Auto model-router desde Actividad 1.",
    "Fuente provisional: Claude Foundry desde Actividad 1.",
    "Fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Entregar memoria en JSON válido y parseable.",
    "Usar el esquema requerido completo.",
    "No agregar campos fuera del esquema solicitado.",
    "Redactar reglas en frases cortas y accionables.",
    "Evitar duplicados semánticos.",
    "Mantener trazabilidad de cambios por ciclo.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación, cuadro o producto visual según consigna.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional."
  ],
  "activity_rules": [
    "Estructurar la actividad en problema, conceptos, fuentes, análisis propio y conclusión jurídica.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Ajustar el producto al formato solicitado por Actividad 2.",
    "Orientar el desarrollo a claridad, fundamento jurídico, evidencia y transferencia profesional.",
    "Distinguir ética, moral y moral jurídica cuando la consigna lo requiera.",
    "Comparar escuelas éticas con criterios homogéneos cuando el producto sea cuadro comparativo.",
    "No asumir fuentes de semanas distintas sin validación local.",
    "No copiar conclusiones específicas de actividades hermanas.",
    "Usar analogía lateral solo para estructura y calidad editorial."
  ],
  "quality_gates": [
    "Validar sintaxis JSON antes de guardar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Aplicar compresión por unión y deduplicación lossless.",
    "No recortar contenido válido.",
    "Confirmar que toda afirmación tenga respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar consistencia con README local.",
    "Verificar consistencia con programa analítico local.",
    "Revisar integridad académica antes de publicar.",
    "Verificar que el producto corresponda a la consigna de Actividad 2.",
    "Revisar ciclos consecutivos sin JSON parseable antes de propagar."
  ],
  "latex_rules": [
    "Mantener compatibilidad con la suite LaTeX de la asignatura.",
    "Usar UTF-8 y acentos correctos en .tex y .bib.",
    "Conservar entradas canónicas: reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex.",
    "Usar reporte-etica-y-moral-juridica-Actividad-2.tex como artefacto de Actividad 2.",
    "Separar contenido, citas y bibliografía para compilación estable.",
    "Mantener claves BibTeX estables.",
    "Compilar sin errores críticos.",
    "Compilar sin referencias rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Corregir caracteres anómalos en rutas y nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Revisar entradas truncadas del README antes de referenciarlas.",
    "Revisar entrada BibTeX truncada antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos bibliográficos.",
    "Usar solo obras consultables y verificables.",
    "Agregar referencias verificables en etica-y-moral-juridica.bib.",
    "Priorizar fuentes institucionales UnADM cuando apliquen al encuadre.",
    "Citar UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Deduplicar obras equivalentes con distinta clave sin perder trazabilidad.",
    "Conservar temporalmente claves duplicadas hasta definir política de alias.",
    "Detectar duplicado visible: huertaEticaConClasicos2000 y huerta2000etica.",
    "Detectar duplicado visible: ronquilloarmasEticaGeneralProfesional2018 y ronquillo2018etica.",
    "Detectar duplicado visible: singerCompendioEtica1995 y singer1995compendio.",
    "Validar la entrada sierraUniversidadNacional1910 antes de citarla.",
    "No trasladar bibliografía exclusiva de Filosofía del Derecho al destino."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas parseables y verificadas.",
    "Propagar laterales solo después de validar JSON y estructura.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Transferir identidad, estructura, calidad y patrones argumentativos generales.",
    "No transferir redacción literal de conclusiones hermanas.",
    "No transferir bibliografía exclusiva del nodo origen.",
    "Conservar trazabilidad de origen y destino.",
    "Aplicar normalización manual si aparece salida no estructurada.",
    "Evitar regresiones respecto de reglas útiles previas.",
    "Ciclo 1 necesita normalización manual si se reutiliza.",
    "Ciclo 2 necesita normalización manual si se reutiliza.",
    "Ciclos 3 a 11 requieren revisión antes de reutilizarse."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 2.",
    "Confirmar si Actividad 2 requiere reporte, presentación, cuadro comparativo u otro formato.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si el título local es escuelas clásicas o escuelas contemporáneas de la ética.",
    "Definir política editorial para fusionar claves BibTeX duplicadas.",
    "Definir política editorial para alias de claves BibTeX históricas.",
    "Definir umbral de bloqueo tras ciclos consecutivos sin JSON parseable.",
    "Confirmar formato de trazabilidad de fuentes provisionales por modelo.",
    "Revisar el README local por nombres truncados de archivos y carpetas.",
    "Revisar la entrada sierraUniversidadNacional1910 por posible truncamiento.",
    "Confirmar si las fuentes locales visibles bastan para Actividad 2."
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
        "Trazabilidad de reglas propagadas.",
        "Respeto a la planeación semanal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1.",
        "Bloque 2.",
        "Asignatura obligatoria.",
        "8 créditos.",
        "Asignatura: Ética y Moral jurídica.",
        "Actividad 2."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeación.",
      "Análisis propio y postura académica.",
      "Conclusión transferible a la práctica jurídica.",
      "Ética.",
      "Moral.",
      "Moral jurídica.",
      "Escuelas de la ética.",
      "Criterios filosóficos para decidir.",
      "Utilitarismo.",
      "Ética del cuidado.",
      "Neopositivismo.",
      "Relativismo.",
      "Neokantismo.",
      "Marxismo.",
      "Integridad académica.",
      "Deduplicación bibliográfica con trazabilidad."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos claros.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico desde dilemas éticos verificables.",
      "Conectar teoría ética con práctica profesional del derecho.",
      "Garantizar memoria editorial parseable y reutilizable.",
      "Evitar propagación de contenido no estructurado.",
      "Preservar ADN UnADM en cada actividad."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explícitos cuando falte evidencia.",
      "Citas verificables.",
      "Trazabilidad de fuentes.",
      "Cierre con criterio jurídico propio.",
      "Comparación con criterios homogéneos.",
      "Distinción entre descripción y postura argumentada.",
      "Normalización antes de propagación.",
      "Deduplicación sin recorte semántico.",
      "Analogía controlada entre asignaturas."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo al inicio.",
      "Definir conceptos antes de aplicarlos.",
      "Presentar marco doctrinal o normativo pertinente.",
      "Comparar posturas con criterios homogéneos.",
      "Contrastar fuentes sin forzar equivalencias.",
      "Sostener postura propia con evidencia.",
      "Evitar resumen descriptivo como producto final.",
      "Conectar análisis ético con práctica jurídica.",
      "Cerrar con implicación profesional verificable.",
      "Marcar supuestos cuando falte consigna."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral jurídica",
        "Actividad 2",
        "Problema jurídico o social",
        "Conceptos clave",
        "Fuentes verificables",
        "Análisis propio",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "JSON parseable",
        "Normalización estructurada",
        "Deduplicación lossless",
        "Bibliografía local",
        "Claves BibTeX estables",
        "Ética",
        "Moral",
        "Moral jurídica",
        "Escuelas de la ética",
        "Cuadro comparativo",
        "Utilitarismo",
        "Ética del cuidado",
        "Neopositivismo",
        "Relativismo",
        "Neokantismo",
        "Marxismo"
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
        "sierraUniversidadNacional1910"
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
          "justification": "La asignatura pertenece al plan curricular indicado en el README local."
        },
        {
          "source": "Programa analítico local",
          "target": "Ejes editoriales de actividad",
          "kind": "develops",
          "justification": "El programa enumera problema, conceptos, producto, análisis y conclusión."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "El encuadre inicial activa la postura académica del estudiante."
        },
        {
          "source": "Conceptos clave",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión requiere conceptos definidos y aplicados con precisión."
        },
        {
          "source": "Fuentes verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las citas explícitas reducen afirmaciones sin respaldo."
        },
        {
          "source": "Integridad académica",
          "target": "Deduplicación bibliográfica con trazabilidad",
          "kind": "depends_on",
          "justification": "La calidad de citas exige controlar claves y metadatos equivalentes."
        },
        {
          "source": "JSON parseable",
          "target": "Propagación recursiva",
          "kind": "supports",
          "justification": "La memoria solo puede reutilizarse de forma segura si mantiene estructura válida."
        },
        {
          "source": "Normalización estructurada",
          "target": "Deduplicación lossless",
          "kind": "supports",
          "justification": "La normalización permite unir reglas sin eliminar contenido útil."
        },
        {
          "source": "Filosofía del Derecho",
          "target": "Ética y Moral jurídica",
          "kind": "supports",
          "justification": "La transferencia lateral refuerza patrones institucionales y argumentativos generales."
        },
        {
          "source": "Bibliografía exclusiva del origen",
          "target": "Bibliografía local del destino",
          "kind": "contrasts",
          "justification": "Las fuentes propias de Filosofía del Derecho no deben copiarse sin pertinencia local."
        },
        {
          "source": "Ética",
          "target": "Moral jurídica",
          "kind": "develops",
          "justification": "La asignatura exige conectar reflexión ética con práctica jurídica."
        },
        {
          "source": "Escuelas de la ética",
          "target": "Cuadro comparativo",
          "kind": "supports",
          "justification": "La comparación requiere criterios homogéneos entre escuelas."
        },
        {
          "source": "Claves BibTeX estables",
          "target": "Compilación LaTeX",
          "kind": "supports",
          "justification": "La estabilidad de claves evita referencias rotas."
        },
        {
          "source": "README local",
          "target": "Corrección de rutas",
          "kind": "supports",
          "justification": "El README muestra nombres truncados que deben verificarse antes de compilar."
        }
      ],
      "evidence": [
        "README local: Materia de la Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica con criterio propio.",
        "Programa analítico local: claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: fuentes específicas deben agregarse en el .bib de la asignatura.",
        ".bib local: huertaEticaConClasicos2000 y huerta2000etica describen la misma obra.",
        ".bib local: ronquilloarmasEticaGeneralProfesional2018 y ronquillo2018etica describen la misma obra.",
        ".bib local: singerCompendioEtica1995 y singer1995compendio describen la misma obra.",
        ".bib local visible: lopezmartinezTecnicasDidacticas2023 es fuente UnADM.",
        "Memoria previa: hubo salidas no parseables de varios modelos.",
        "Memoria previa: se requiere normalización antes de propagar.",
        "Memoria previa: Actividad 2 contiene reporte-etica-y-moral-juridica-Actividad-2.tex.",
        "Supuesto: falta consigna textual completa de Actividad 2."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 aplica refuerzo lateral desde Filosofía del Derecho.",
      "Se transfieren patrones institucionales y de calidad.",
      "Se preserva la especificidad local de Ética y Moral jurídica.",
      "Se excluyen fuentes exclusivas del nodo origen.",
      "Se consolidan reglas de JSON parseable y normalización.",
      "Se refuerza secuencia problema-conceptos-fuentes-análisis-conclusión.",
      "Se agregan controles LaTeX por tokens sin expandir.",
      "Se agregan controles por nombres truncados en README.",
      "Se agregan controles por duplicados BibTeX visibles.",
      "Se mantienen preguntas abiertas cuando falta consigna local."
    ]
  }
}