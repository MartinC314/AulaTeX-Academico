{
  "summary": [
    "Se refuerza transferencia lateral desde Filosofía del Derecho hacia Ética y Moral jurídica con reglas reutilizables.",
    "Se preservan reglas válidas previas y se deduplican sin recorte.",
    "Se mantiene normalización estructurada obligatoria antes de propagación recursiva.",
    "Se consolidan ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica.",
    "Se agrega mejora verificable local: resolver tokens Slug sin expandir en README y programa analítico.",
    "Se agrega mejora verificable local: marcar entrada .bib truncada como bloqueo de compilación hasta corregir."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y cierre jurídico.",
    "Vincular cada producto a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como punto de entrada canónico.",
    "Mantener referencia explícita a la asignatura destino: Ética y Moral jurídica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Registrar ruta origen-destino y ciclo en cada fusión editorial."
  ],
  "structure_rules": [
    "Responder siempre en JSON válido y parseable.",
    "Usar el esquema canónico completo sin omitir secciones.",
    "Aplicar compresión lossless por unión y deduplicación.",
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeación semanal.",
    "Marcar explícitamente supuestos cuando falte evidencia."
  ],
  "activity_rules": [
    "Alinear cada entrega al problema jurídico o social de la actividad.",
    "Integrar conceptos, normas o doctrina pertinentes antes de concluir.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Cerrar con conclusión transferible a la práctica jurídica.",
    "No asumir fuentes de otras semanas sin validación en la consigna local.",
    "Si falta consigna textual, usar estructura base y abrir preguntas de validación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar ausencia de afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar ausencia de duplicados semánticos antes de guardar memoria.",
    "No eliminar reglas útiles previas durante la fusión.",
    "Aceptar solo mejoras verificables contra archivos locales o memoria previa.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Bloquear compilación si existe entrada .bib truncada sin corregir."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos del README antes de referenciarlos.",
    "Corregir caracteres anómalos en rutas o nombres antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "Mantener consistencia de nombres .tex y .bib según slug de la materia."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de la actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias; usar solo obras realmente consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Evitar claves BibTeX duplicadas para la misma obra.",
    "Registrar duplicados históricos como alias trazables antes de normalizar.",
    "Marcar como supuesto cualquier incidencia bibliográfica no confirmada."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Transferir solo patrones reutilizables, no redacción ni conclusiones específicas.",
    "Evitar copiar bibliografía exclusiva del nodo hermano.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Mantener bandera de normalización manual en ciclos con salidas no estructuradas.",
    "Priorizar refuerzo lateral de identidad, estructura, calidad y patrones argumentativos."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 8 y producto solicitado.",
    "Confirmar rúbrica específica para calibrar profundidad argumentativa.",
    "Supuesto: la entrada sierraUniversidadNacional1910 está truncada; confirmar campos faltantes.",
    "Confirmar política local para unificar claves duplicadas en el .bib sin perder trazabilidad.",
    "Confirmar si README debe corregir líneas con caracteres iniciales truncados en nombres de archivo."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Claro y jurídicamente preciso.",
        "Argumentativo con criterio propio.",
        "Ético con rigor jurídico."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Carpeta de asignatura como entrada canónica.",
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2.",
        "Asignatura obligatoria de 8 créditos.",
        "Asignatura destino: Ética y Moral jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y verificables.",
      "Asegurar coherencia entre identidad institucional, contenido y calidad formal.",
      "Sostener memoria editorial persistente sin pérdida de reglas útiles."
    ],
    "style_markers": [
      "Frases breves y accionables.",
      "Supuestos explícitos.",
      "Trazabilidad por ruta y ciclo.",
      "Cero invención de fuentes."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo al inicio.",
      "Construir marco conceptual y normativo antes del análisis.",
      "Contrastar postura propia con evidencia.",
      "Cerrar con implicación práctica jurídica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Ejes editoriales de actividad",
        "Integridad académica",
        "Trazabilidad bibliográfica",
        "Ética y Moral jurídica"
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
          "target": "Ejes editoriales de actividad",
          "kind": "supports",
          "justification": "La pauta institucional fija estructura y criterios de entrega."
        },
        {
          "source": "Normalización JSON",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Permite trazabilidad y control de calidad en memoria persistente."
        },
        {
          "source": "Trazabilidad bibliográfica",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "Claves estables y metadatos completos hacen verificable el sustento."
        },
        {
          "source": "Ejes editoriales de actividad",
          "target": "Ética y Moral jurídica",
          "kind": "develops",
          "justification": "El patrón de cinco ejes se adapta al contenido ético-jurídico local."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia segura entre nodos."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y ubicación curricular.",
        "Programa analítico local confirma propósito y cinco ejes de trabajo.",
        "Archivo .bib local muestra duplicados y una entrada truncada verificable.",
        "Memoria origen aporta patrón reusable de estructura, calidad y argumentación."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: se consolida refuerzo lateral sin copiar contenido específico del hermano.",
      "Ciclo 11: se preservan reglas útiles previas y se deduplican.",
      "Ciclo 11: se añade bloqueo de compilación por entrada .bib truncada como mejora verificable.",
      "Ciclo 11: se mantiene obligatoriedad de normalización JSON para propagación recursiva."
    ]
  }
}