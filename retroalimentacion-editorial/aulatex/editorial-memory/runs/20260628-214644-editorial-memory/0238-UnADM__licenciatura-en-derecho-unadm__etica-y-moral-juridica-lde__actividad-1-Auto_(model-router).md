{
  "summary": [
    "Se consolida memoria lateral desde Filosofía del Derecho hacia Ética y Moral Jurídica.",
    "Se transfieren solo patrones reutilizables y verificables.",
    "Se preserva identidad UnADM y contexto de Licenciatura en Derecho.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene contingencia histórica por salidas previas no parseables.",
    "Se corrige supuesto previo: sí existen reglas académicas transferibles desde el origen.",
    "Se evita copiar bibliografía exclusiva de Filosofía del Derecho.",
    "Se conserva pauta local de Ética y Moral Jurídica.",
    "Se aplica compresión lossless por deduplicación.",
    "Se exige normalización JSON antes de propagación recursiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM.",
    "Mantener contexto de Licenciatura en Derecho.",
    "Mantener asignatura destino: Ética y Moral Jurídica.",
    "Vincular la asignatura a semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura destino como entrada canónica.",
    "Citar malla-curricular-derecho-unadm.pdf para ubicación curricular.",
    "Marcar como [Supuesto] cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales.",
    "Registrar ruta origen y destino en cada consolidación.",
    "Etiquetar reglas importadas con origen y ciclo cuando aplique.",
    "Conservar trazabilidad de incidencias de parseo por modelo.",
    "Mantener fuente provisional: Codex desde Actividad 1.",
    "Mantener fuente provisional: Auto model-router desde Actividad 1.",
    "Mantener fuente provisional: Claude Foundry desde Actividad 1.",
    "Mantener fuente provisional: GPT-Pro desde Actividad 1."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido conforme al esquema requerido.",
    "Usar frases cortas, accionables y sin duplicados.",
    "No eliminar reglas útiles previas.",
    "Unir y deduplicar reglas equivalentes.",
    "Aplicar compresión lossless por deduplicación.",
    "Marcar supuestos con etiqueta [Supuesto].",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar conceptos clave y marco normativo o doctrinal.",
    "Distinguir síntesis de postura personal argumentada.",
    "Cerrar con conclusión jurídica aplicable.",
    "Alinear la estructura al producto solicitado por la planeación semanal.",
    "Transformar la planeación en reporte, presentación o producto visual según consigna."
  ],
  "activity_rules": [
    "Alinear cada entrega a la pauta local de Ética y Moral Jurídica.",
    "Verificar que el producto corresponda a Actividad 1.",
    "Confirmar consigna textual antes de fijar formato final.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Integrar fundamento jurídico, evidencia y transferencia profesional.",
    "No asumir fuentes de semanas posteriores sin confirmación local.",
    "No copiar conclusiones específicas de asignaturas hermanas.",
    "No importar bibliografía exclusiva de Filosofía del Derecho sin uso local verificable.",
    "Relacionar ética, moral y práctica jurídica cuando la consigna lo permita.",
    "Diferenciar conceptos éticos, morales y jurídicos con precisión."
  ],
  "quality_gates": [
    "Validar parseo JSON antes de guardar memoria.",
    "Bloquear propagación si la salida no es JSON parseable.",
    "Bloquear propagación si no cumple el esquema requerido.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Registrar incidencias de formato como resumen operativo.",
    "Verificar deduplicación semántica sin perder reglas válidas.",
    "Evitar regresiones durante consolidación.",
    "Confirmar que toda afirmación tenga respaldo o marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia exacta con la consigna de Actividad 1.",
    "Revisar que las reglas importadas sean reutilizables y no específicas del origen."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos.",
    "Compilar sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug).",
    "Resolver token local hacia etica-y-moral-juridica.bib cuando corresponda.",
    "Revisar anomalías locales del README: eporte y eferencias.",
    "Mantener consistencia editorial entre reporte y presentación.",
    "No agregar reglas LaTeX no verificadas por artefactos locales. [Supuesto]"
  ],
  "bibliography_rules": [
    "No inventar fuentes.",
    "Usar solo referencias verificables disponibles.",
    "Priorizar fuentes institucionales UnADM.",
    "Priorizar materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Conservar trazabilidad entre citas en texto y entradas .bib.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Revisar claves bibliográficas duplicadas.",
    "Deduplicar claves sin perder información.",
    "Definir una clave canónica por obra duplicada.",
    "No asumir bibliografía de Filosofía del Derecho como fuente local.",
    "Validar que cada cita usada aparezca en el .bib local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Propagar lateralmente solo patrones generales reutilizables.",
    "No propagar redacción literal de actividades hermanas.",
    "No propagar conclusiones específicas de nodos hermanos.",
    "No propagar bibliografía exclusiva sin verificación local.",
    "Reutilizar reglas institucionales sin reducir especificidad local.",
    "Normalizar incidencias repetidas en una sola regla general.",
    "Aplicar analogía controlada entre Filosofía del Derecho y Ética y Moral Jurídica.",
    "Mantener trazabilidad de ciclo 2.",
    "Ciclos previos con salidas no parseables requieren normalización manual si se reutilizan.",
    "Cuando falten datos locales, dejar pregunta abierta.",
    "Propagar arriba y laterales solo reglas validadas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 1.",
    "Confirmar formato solicitado: reporte, presentación, cuadro comparativo u otro.",
    "Confirmar rúbrica de evaluación específica.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si Actividad 1 corresponde a escuelas éticas clásicas. [Supuesto]",
    "Confirmar si el documento local titulado Actividad 2 aplica a Actividad 1. [Supuesto]",
    "Definir criterio canónico para claves duplicadas en etica-y-moral-juridica.bib.",
    "Confirmar clave canónica para Ética con los clásicos.",
    "Confirmar clave canónica para Ética general y profesional.",
    "Confirmar clave canónica para Compendio de ética.",
    "Definir formato único para registro de errores de parseo por modelo.",
    "Confirmar si existen instrucciones locales adicionales no visibles."
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
        "Respeto a la planeación semanal."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1.",
        "Bloque 2.",
        "Asignatura obligatoria.",
        "8 créditos.",
        "Asignatura destino: Ética y Moral Jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social que activa la asignatura.",
      "Conceptos éticos, morales y jurídicos pertinentes.",
      "Fuentes verificables y citas explícitas.",
      "Marco normativo o doctrinal cuando corresponda.",
      "Análisis propio con postura académica.",
      "Conclusión jurídica transferible a la práctica profesional.",
      "Integridad académica como eje transversal.",
      "Analogía controlada con Filosofía del Derecho.",
      "Diferenciación entre ética, moral y derecho.",
      "Reflexión sobre responsabilidad profesional jurídica."
    ],
    "reason_for_being": [
      "Transformar la planeación semanal en productos académicos verificables.",
      "Integrar problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
      "Formar criterio jurídico con base ética.",
      "Evitar resúmenes sin postura crítica.",
      "Asegurar transferencia profesional de la conclusión.",
      "Normalizar memoria editorial para propagación segura.",
      "Preservar identidad institucional UnADM.",
      "Conectar reflexión moral con práctica jurídica."
    ],
    "style_markers": [
      "Objetivo explícito al inicio.",
      "Problema delimitado antes del desarrollo.",
      "Conceptos definidos con precisión.",
      "Marco doctrinal separado del análisis propio.",
      "Citas verificables en afirmaciones sustantivas.",
      "Postura personal argumentada.",
      "Conclusión breve y aplicable.",
      "Supuestos marcados con [Supuesto].",
      "Sin bibliografía inventada.",
      "Sin redacción copiada de nodos hermanos.",
      "Uso estable de claves BibTeX.",
      "Revisión de tokens sin expandir."
    ],
    "argumentative_patterns": [
      "Problema inicial -> conceptos clave -> soporte doctrinal -> análisis propio -> conclusión.",
      "Afirmación ética -> fuente verificable -> interpretación jurídica -> implicación profesional.",
      "Concepto moral -> contraste con norma jurídica -> consecuencia práctica.",
      "Escuela ética -> criterio central -> aplicación al ámbito jurídico.",
      "Dilema jurídico -> valores en tensión -> postura razonada -> cierre aplicable.",
      "Fuente institucional -> ubicación curricular -> pauta editorial.",
      "Cita en texto -> entrada .bib -> consistencia final.",
      "Consigna local -> formato requerido -> estructura de entrega."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Licenciatura en Derecho",
        "Ética y Moral Jurídica",
        "Problema jurídico o social",
        "Conceptos clave",
        "Ética",
        "Moral",
        "Moral jurídica",
        "Derecho",
        "Marco normativo o doctrinal",
        "Escuelas éticas clásicas",
        "Análisis propio",
        "Postura académica",
        "Conclusión jurídica transferible",
        "Integridad académica",
        "Citas verificables",
        "Normalización JSON",
        "Deduplicación bibliográfica",
        "Propagación recursiva",
        "Analogía controlada"
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
        "lopezmartinezTecnicasDidacticas2023"
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
          "justification": "La asignatura pertenece al plan curricular de Derecho."
        },
        {
          "source": "Problema jurídico o social",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "El análisis requiere una pregunta o problema delimitado."
        },
        {
          "source": "Conceptos clave",
          "target": "Marco normativo o doctrinal",
          "kind": "supports",
          "justification": "Las definiciones ordenan el uso de normas, doctrina y fuentes."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión necesita fundamento verificable para ser aplicable."
        },
        {
          "source": "Ética",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La actividad debe distinguir reflexión ética y pautas morales cuando corresponda."
        },
        {
          "source": "Moral jurídica",
          "target": "Derecho",
          "kind": "supports",
          "justification": "La moral jurídica orienta criterios de valoración en la práctica legal."
        },
        {
          "source": "Escuelas éticas clásicas",
          "target": "Postura académica",
          "kind": "supports",
          "justification": "Las escuelas ofrecen criterios para argumentar una posición."
        },
        {
          "source": "Citas verificables",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Las fuentes explícitas reducen afirmaciones sin respaldo."
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
          "justification": "Una clave canónica por obra reduce ambigüedad de citas."
        },
        {
          "source": "Analogía controlada",
          "target": "Ética y Moral Jurídica",
          "kind": "supports",
          "justification": "Permite reutilizar patrones de Filosofía del Derecho sin copiar contenido específico."
        }
      ],
      "evidence": [
        "README local: materia de Licenciatura en Derecho de la UnADM.",
        "README local: semestre 1, bloque 2, obligatoria, 8 créditos.",
        "README local: carpeta como punto de entrada canónico.",
        "README local: integridad académica, citas verificables y conclusión jurídica.",
        "Programa analítico local: productos con claridad, fundamento jurídico, evidencia y transferencia profesional.",
        "Programa analítico local: problema, conceptos, fuentes, análisis propio y cierre argumentativo.",
        "Programa analítico local: fuentes específicas deben agregarse al .bib de la asignatura.",
        "Bib local: existen duplicados para Ética con los clásicos.",
        "Bib local: existen duplicados para Ética general y profesional.",
        "Bib local: existen duplicados para Compendio de ética.",
        "Memoria origen: estructura problema, conceptos, marco, análisis propio y cierre.",
        "Memoria origen: bloqueo de propagación si no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2 lateral-transversal aplicado desde Filosofía del Derecho.",
      "Se preservaron reglas locales de contingencia por parseo.",
      "Se reforzó pauta común de problema, conceptos, evidencia, análisis y conclusión.",
      "Se mantuvo especificidad local de Ética y Moral Jurídica.",
      "Se excluyó bibliografía exclusiva de Filosofía del Derecho.",
      "Se conservaron citas locales verificables del .bib destino.",
      "Se integró regla de deduplicación bibliográfica por obras duplicadas locales.",
      "Se incorporó revisión de tokens sin expandir del README local.",
      "Se conservaron preguntas abiertas por falta de consigna textual.",
      "Se normalizaron relaciones del grafo a tipos permitidos."
    ]
  }
}