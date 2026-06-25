{
  "summary": [
    "Sincronización transversal aplicada con estrategia conservadora y sin regresión.",
    "Se preservan reglas institucionales UnADM y ejes metodológicos reutilizables.",
    "Se transfiere solo abstracción estable desde actividad origen a materia destino.",
    "Se mantiene compresión lossless por unión y deduplicación.",
    "Se refuerzan gates: JSON válido, supuestos marcados y trazabilidad de fuentes.",
    "Supuesto: no hay consigna local de actividad específica en este ciclo."
  ],
  "identity_rules": [
    "Mantener identidad UnADM en tono, portada y metadatos.",
    "Usar contexto curricular verificado del destino: semestre 6, bloque 1, obligatoria, 8 créditos.",
    "Usar la carpeta de asignatura como entrada canónica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validación local.",
    "Verificar datos personales y figura docente antes de entrega final."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto a la planeación semanal y consigna vigente.",
    "Mantener separación entre reporte .tex, presentación .tex y .bib local.",
    "Corregir rutas y nombres rotos en README y programa analítico antes de publicar."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Evitar entregas meramente descriptivas.",
    "Vincular análisis fiscal-tributario con aplicación profesional concreta.",
    "Cerrar con conclusión jurídica transferible."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Verificar correspondencia entre producto entregable y consigna local."
  ],
  "latex_rules": [
    "Usar codificación y acentos correctos en español en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos y sin referencias rotas.",
    "Cerrar correctamente entornos truncados en portada y tablas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analítico."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y normas jurídicas verificables.",
    "Registrar fuentes específicas por actividad en derecho-fiscal-y-tributario.bib.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica de actividad.",
    "Usar malla curricular solo para soporte de datos curriculares."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo después de validar JSON y estructura.",
    "Compartir a nodos laterales solo reglas generales y estables.",
    "Evitar transferir redacción literal o bibliografía temática no equivalente.",
    "Aplicar normalización manual si reaparecen salidas no estructuradas.",
    "Mantener política de no regresión en ciclos siguientes.",
    "Priorizar identidad, gates de calidad y grafo conceptual común."
  ],
  "open_questions": [
    "Confirmar formato de citación requerido por la asignatura.",
    "Confirmar si plantilla debe conservar autor y matrícula en repositorios compartidos.",
    "Confirmar nombre de figura docente en portada.",
    "Confirmar si el .bib local único aplica a todas las actividades.",
    "Resolver definitivamente rutas truncadas en README (reporte/referencias).",
    "Supuesto: aún no existe consigna local detallada para una actividad concreta."
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
        "Trazabilidad de supuestos y fuentes."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia: Derecho fiscal y tributario.",
        "Semestre 6, bloque 1, obligatoria, 8 créditos."
      ]
    },
    "essence": [
      "Problema jurídico inicial claro.",
      "Marco conceptual y normativo pertinente.",
      "Análisis propio sustentado.",
      "Cierre con transferencia profesional.",
      "Consistencia técnica entre .tex y .bib."
    ],
    "reason_for_being": [
      "Convertir la planeación semanal en entregables sólidos y verificables.",
      "Asegurar coherencia entre identidad institucional, método jurídico y evidencia.",
      "Permitir propagación segura entre nodos sin pérdida editorial."
    ],
    "style_markers": [
      "Supuestos siempre etiquetados.",
      "Sin afirmaciones sin fuente.",
      "Estructura funcional estable.",
      "Cierre jurídico aplicable."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo.",
      "Exponer conceptos y norma aplicable.",
      "Contrastar fuentes con postura propia.",
      "Concluir con implicación práctica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Problema jurídico",
        "Marco normativo",
        "Análisis propio",
        "Conclusión transferible",
        "Normalización JSON",
        "Consistencia .tex/.bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Problema jurídico",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación del problema no hay argumentación útil."
        },
        {
          "source": "Marco normativo",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "La conclusión jurídica requiere fundamento explícito."
        },
        {
          "source": "Normalización JSON",
          "target": "Consistencia .tex/.bib",
          "kind": "develops",
          "justification": "La estructura formal habilita control de calidad técnico-editorial."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Análisis propio",
          "kind": "supports",
          "justification": "La pauta institucional exige criterio personal con evidencia."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicación curricular.",
        "Programa analítico: propósito y ejes de trabajo.",
        "derecho-fiscal-y-tributario.bib: base institucional verificable.",
        "Supuesto: transferencia transversal limitada a patrones metodológicos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 20: deduplicación completa sin recorte semántico.",
      "Ciclo 20: reforzada regla de supuestos explícitos en datos no visibles.",
      "Ciclo 20: reforzada prioridad de calidad estructural antes de propagación.",
      "Ciclo 20: consolidado núcleo argumentativo reusable entre materias no equivalentes."
    ]
  }
}