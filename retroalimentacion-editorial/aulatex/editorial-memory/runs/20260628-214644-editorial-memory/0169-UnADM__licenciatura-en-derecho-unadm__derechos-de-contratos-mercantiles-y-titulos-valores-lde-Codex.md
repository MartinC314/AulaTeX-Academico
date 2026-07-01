{
  "summary": [
    "Se consolida memoria transversal mínima para materia destino con identidad UnADM.",
    "Se preservan ejes editoriales estables: problema, conceptos o normas, evidencia, análisis propio y conclusión jurídica.",
    "Se mantiene regla crítica: no propagar contenido no estructurado sin normalización previa.",
    "Se confirma contexto local: semestre 6, bloque 2, obligatoria, 8 créditos.",
    "Se detectan placeholders y nombres truncados en README/programa; se marcan para saneamiento editorial."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, metadatos y presentación.",
    "Alinear todo entregable a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono jurídico-formal con postura académica propia.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Usar carpeta de materia como entrada canónica de README, programa, .tex y .bib.",
    "Abrir cada actividad con encuadre breve del problema jurídico o social.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear el producto final a la planeación semanal y a la consigna específica.",
    "Cerrar con conclusión jurídica transferible a práctica profesional."
  ],
  "activity_rules": [
    "Definir objetivo puntual antes del desarrollo.",
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir evidencia citada de interpretación propia.",
    "Evitar entregas meramente descriptivas.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones, citas en texto y archivo .bib.",
    "Evitar regresión de reglas útiles ya consolidadas."
  ],
  "latex_rules": [
    "Mantener codificación correcta para español en .tex y .bib.",
    "Corregir macros truncadas antes de compilar.",
    "Resolver placeholders de slug en README y programa analítico.",
    "Usar nomenclatura consistente de archivos de reporte y presentación.",
    "Compilar sin errores críticos, referencias rotas ni claves BibTeX inestables."
  ],
  "bibliography_rules": [
    "Usar como base el .bib local confirmado de la materia destino.",
    "Priorizar fuentes institucionales UnADM y normativas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables por ser nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "No transferir redacción literal ni contenido temático propio de Filosofía del Derecho.",
    "Mantener estrategia progresiva y conservadora en ciclos iniciales.",
    "Si falta contexto local, conservar cerebro mínimo y abrir vacíos explícitos."
  ],
  "open_questions": [
    "Confirmar rúbricas y consignas reales de actividades de la materia destino.",
    "Confirmar plantilla oficial de presentación si difiere del reporte.",
    "Confirmar corrección final de nombres truncados en README.",
    "Confirmar resolución de placeholder slug en README y programa.",
    "Supuesto: persiste alerta institucional por salidas no JSON parseables en historial."
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
        "Carpeta de materia como entrada canónica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 créditos.",
        "Asignatura: Derechos de contratos mercantiles y títulos valores."
      ]
    },
    "essence": [
      "Problema jurídico o social.",
      "Conceptos y normas pertinentes.",
      "Producto alineado a planeación.",
      "Análisis propio.",
      "Conclusión jurídica transferible."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos verificables.",
      "Asegurar fundamento jurídico, evidencia y postura propia.",
      "Garantizar transferencia profesional en el cierre."
    ],
    "style_markers": [
      "Afirmaciones con respaldo verificable.",
      "Supuestos marcados de forma explícita.",
      "Secciones claras y orden argumentativo estable.",
      "Cierre con criterio jurídico propio."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar evidencia.",
      "Emitir análisis propio.",
      "Concluir con aplicabilidad profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional UnADM",
        "integridad académica",
        "trazabilidad de fuentes",
        "problema jurídico",
        "análisis propio",
        "conclusión jurídica transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional UnADM",
          "target": "integridad académica",
          "kind": "supports",
          "justification": "La pauta local exige citas verificables y formato institucional."
        },
        {
          "source": "problema jurídico",
          "target": "análisis propio",
          "kind": "develops",
          "justification": "La estructura editorial parte del problema y culmina en postura razonada."
        },
        {
          "source": "trazabilidad de fuentes",
          "target": "conclusión jurídica transferible",
          "kind": "supports",
          "justification": "La conclusión gana validez cuando deriva de evidencia verificable."
        }
      ],
      "evidence": [
        "README de materia: pauta editorial y ubicación curricular.",
        "Programa analítico: ejes de trabajo y propósito de realización.",
        ".bib local: entradas institucionales confirmadas."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin pérdida funcional.",
      "Se preservaron gates institucionales de JSON y normalización.",
      "Se agregó saneamiento de placeholders y truncamientos por evidencia local.",
      "Se evitó transferir contenido doctrinal específico no transversal del origen."
    ]
  }
}