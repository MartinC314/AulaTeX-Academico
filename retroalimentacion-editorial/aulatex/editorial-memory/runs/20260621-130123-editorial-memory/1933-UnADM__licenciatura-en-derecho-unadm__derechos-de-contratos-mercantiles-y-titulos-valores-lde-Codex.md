{
  "summary": [
    "Se consolida sincronización transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa y control de calidad JSON.",
    "Se refuerza compresión lossless por unión y deduplicación sin recorte semántico.",
    "Se mantiene separación entre abstracciones transferibles y contenido temático local de cada materia.",
    "Se mantiene contexto local verificable del destino: semestre 6, bloque 2, obligatoria, 8 créditos."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables a Licenciatura en Derecho y a la materia destino.",
    "Conservar tono jurídico-formal, claro y con criterio propio.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local.",
    "Usar carpeta de materia como entrada canónica."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener consistencia entre README, programa analítico, .tex y .bib."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Distinguir evidencia citada de interpretación propia.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "No asumir fuentes de otras semanas sin validación local.",
    "Adaptar profundidad argumentativa a rúbrica vigente cuando exista."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Validar estructura mínima completa antes de aplicar aguas abajo.",
    "Confirmar trazabilidad entre afirmaciones y fuentes.",
    "Verificar ausencia de fuentes inventadas.",
    "Revisar no regresión de reglas útiles previas."
  ],
  "latex_rules": [
    "Usar español con acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables.",
    "Evitar comandos no estándar sin justificación editorial.",
    "Compilar sin errores críticos ni referencias rotas.",
    "Corregir nombres truncados y tokens de slug sin expandir en README y programa.",
    "Corregir macro truncada de plantilla antes de uso productivo [supuesto: sigue pendiente]."
  ],
  "bibliography_rules": [
    "Usar el .bib local confirmado de la materia destino.",
    "Priorizar fuentes institucionales UnADM y jurídicas verificables.",
    "Registrar fuentes específicas por actividad en el .bib local.",
    "No inventar referencias; usar solo obras consultables.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Agregar fecha de consulta en recursos web.",
    "Distinguir bibliografía base de bibliografía específica de actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables en relación transversal.",
    "No transferir redacción literal ni contenido temático de Filosofía del Derecho.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Mantener estrategia progresiva y conservadora en cada ciclo.",
    "Aplicar unión-dedupe lossless en cada fusión recursiva.",
    "Mantener alerta histórica de normalización manual hasta cierre verificado."
  ],
  "open_questions": [
    "Confirmar corrección definitiva de nombres truncados en README del destino.",
    "Confirmar resolución de placeholders de slug en README y programa analítico.",
    "Confirmar estado final de macro truncada en plantilla .tex.",
    "Confirmar si la incidencia de salidas no JSON parseable ya quedó cerrada en flujos actuales.",
    "Confirmar plantilla oficial de presentación si difiere del reporte.",
    "Confirmar criterio institucional sobre year fijo vs solo fecha de consulta en sitio UnADM."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal académico.",
        "Jurídicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineación explícita con UnADM.",
        "Integridad académica con citas verificables.",
        "Normalización estructurada obligatoria antes de propagar.",
        "Carpeta canónica como punto de entrada."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Materia destino en semestre 6, bloque 2, obligatoria, 8 créditos.",
        "Enfoque profesional transferible."
      ]
    },
    "essence": [
      "Problema delimitado.",
      "Marco conceptual y normativo.",
      "Evidencia verificable.",
      "Análisis propio.",
      "Conclusión jurídica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeación semanal en productos académicos sólidos y trazables.",
      "Asegurar consistencia editorial entre documentos de materia.",
      "Garantizar calidad formal y jurídica en propagación recursiva."
    ],
    "style_markers": [
      "Inicio breve con problema.",
      "Secciones explícitas y ordenadas.",
      "Supuestos etiquetados cuando falte evidencia.",
      "Cierre con implicación profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos y normas -> evidencia -> análisis propio -> conclusión.",
      "Afirmación jurídica siempre respaldada por fuente verificable.",
      "Contraste entre evidencia y postura personal, sin resumen plano."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad académica",
        "Normalización estructurada",
        "JSON parseable",
        "Problema jurídico delimitado",
        "Marco normativo o doctrinal",
        "Evidencia verificable",
        "Análisis propio",
        "Conclusión transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalización estructurada",
          "target": "JSON parseable",
          "kind": "depends_on",
          "justification": "La propagación segura requiere formato válido."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad académica",
          "kind": "supports",
          "justification": "La identidad exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema jurídico delimitado",
          "target": "Análisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitación no hay argumentación pertinente."
        },
        {
          "source": "Marco normativo o doctrinal",
          "target": "Conclusión transferible",
          "kind": "supports",
          "justification": "El cierre profesional requiere base jurídica explícita."
        },
        {
          "source": "Evidencia verificable",
          "target": "Análisis propio",
          "kind": "develops",
          "justification": "La interpretación se fortalece con respaldo documental."
        }
      ],
      "evidence": [
        "README y programa analítico del destino confirman ejes y contexto curricular.",
        "Bibliografía local existente confirma base institucional mínima.",
        "Histórico de incidencias confirma necesidad de gate JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 22: deduplicación semántica aplicada sin pérdida de reglas útiles.",
      "Ciclo 22: se reforzó transferencia transversal de abstracciones estables.",
      "Ciclo 22: se evitó migrar contenido temático específico del nodo origen.",
      "Ciclo 22: se preservaron alertas de normalización y calidad institucional."
    ]
  }
}