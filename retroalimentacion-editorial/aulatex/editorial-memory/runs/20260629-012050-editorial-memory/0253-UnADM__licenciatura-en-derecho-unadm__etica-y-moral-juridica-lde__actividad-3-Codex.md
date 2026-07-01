{
  "summary": [
    "Se refuerza memoria lateral con patrones reutilizables entre asignaturas sin copiar contenido específico.",
    "Se conserva identidad UnADM, ubicación curricular y pauta editorial canónica del nodo destino.",
    "Se consolida compresión lossless por deduplicación semántica y textual sin recorte de reglas útiles.",
    "Se mantiene bloqueo de propagación ante salidas no JSON parseables y normalización previa obligatoria.",
    "Se preservan ejes editoriales comunes: problema, conceptos, evidencia, análisis propio y conclusión jurídica transferible.",
    "Se añade control explícito de fuentes provisionales y marcado de [Supuesto] cuando falte consigna local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Vincular toda actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 créditos.",
    "Usar carpeta de la asignatura destino como entrada canónica.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Conservar referencia explícita de origen-destino y ciclo en metadatos editoriales."
  ],
  "structure_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Abrir con encuadre breve del problema jurídico o social.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final a la consigna real de Actividad 3.",
    "Cerrar con conclusión jurídica transferible a la práctica profesional.",
    "Si falta consigna textual, usar estructura base y evitar inventar formato final."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Integrar los cinco ejes del programa analítico en el desarrollo.",
    "Transferir solo patrones editoriales entre nodos laterales, no redacción literal ni conclusiones hermanas.",
    "Mantener trazabilidad de cambios entre ciclos de consolidación."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Escalar a revisión humana si persisten fallas de parseo en ciclos consecutivos."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables y deduplicar por equivalencia verificable.",
    "Evitar comandos o paquetes no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Verificar nombres de archivos definidos en README antes de referenciarlos.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico.",
    "[Supuesto] Corregir líneas con caracteres truncados en README antes de automatizar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales jurídicos verificables.",
    "Registrar fuentes específicas de actividad en etica-y-moral-juridica.bib.",
    "No inventar referencias ni completar metadatos sin evidencia documental.",
    "Conservar metadatos mínimos: autor o editor, título, año y fuente editorial o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Marcar y corregir entradas incompletas antes de citarlas.",
    "Mantener trazabilidad de fusión cuando existan claves duplicadas de la misma obra."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Reusar reglas institucionales de calidad sin perder especificidad local del destino.",
    "Aplicar analogía controlada: transferir marco argumentativo, no contenidos temáticos cerrados.",
    "Preservar historial de incidentes de parseo para prevenir regresiones.",
    "Si falta dato local, propagar plantilla base y abrir pregunta en lugar de inferir contenido."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 3 en Ética y Moral Jurídica.",
    "Confirmar tipo de producto requerido en la semana: reporte, presentación u otro.",
    "Confirmar rúbrica de evaluación específica para calibrar profundidad argumentativa.",
    "Definir criterio operativo final para fusionar claves BibTeX duplicadas.",
    "Corregir y completar entrada truncada sierraUniversidadNacional1910 en el .bib local.",
    "Confirmar si existen fuentes obligatorias adicionales a la bibliografía base. [Supuesto]"
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
        "Normalización estructurada antes de propagación."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 créditos.",
        "Asignatura destino: Ética y Moral Jurídica."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en entregables académicos con rigor jurídico y postura propia.",
      "Garantizar consistencia editorial transversal entre actividades de la suite UnADM."
    ],
    "style_markers": [
      "Apertura con objetivo y problema.",
      "Desarrollo por secciones funcionales.",
      "Cierre aplicado a práctica jurídica.",
      "Marcado explícito de [Supuesto] cuando falte evidencia."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> análisis propio -> conclusión aplicada.",
      "Afirmación -> evidencia -> interpretación jurídica -> postura personal.",
      "Comparación ética/moral/derecho con criterios de pertinencia al caso."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalización JSON",
        "Integridad académica",
        "Ejes editoriales comunes",
        "Ética jurídica",
        "Moral jurídica",
        "Conclusión jurídica transferible"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Normalización JSON",
          "target": "Propagación recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo válido no hay transferencia segura."
        },
        {
          "source": "Ejes editoriales comunes",
          "target": "Conclusión jurídica transferible",
          "kind": "develops",
          "justification": "La secuencia editorial conduce a aplicabilidad profesional."
        },
        {
          "source": "Ética jurídica",
          "target": "Moral jurídica",
          "kind": "contrasts",
          "justification": "Distinguir planos mejora precisión argumentativa."
        }
      ],
      "evidence": [
        "README local define identidad y pauta editorial.",
        "Programa analítico local define propósito y cinco ejes.",
        "Memoria origen aporta patrón estructural transversal reutilizable.",
        "Historial local confirma necesidad de compuerta JSON estricta."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se integran reglas transferibles del origen con deduplicación lossless.",
      "Ciclo 2: se elimina supuesto inválido de 'sin reglas parseables en origen' por nueva evidencia disponible.",
      "Ciclo 2: se refuerza separación entre patrones transferibles y contenido específico no transferible.",
      "Ciclo 2: se mantiene control de calidad por parseo JSON y normalización previa."
    ]
  }
}