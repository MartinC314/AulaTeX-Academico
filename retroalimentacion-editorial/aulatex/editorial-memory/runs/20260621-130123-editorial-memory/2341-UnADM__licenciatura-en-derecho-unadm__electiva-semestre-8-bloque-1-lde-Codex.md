{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia Electiva S8 B1 con enfoque conservador.",
    "Se preservan reglas estables: identidad UnADM, estructura argumentativa, trazabilidad de fuentes y conclusion juridica transferible.",
    "Se mantiene gate duro de normalizacion JSON parseable antes de propagacion recursiva.",
    "Se refuerza deduplicacion lossless por union semantica sin recorte de reglas utiles.",
    "Se incorporan mejoras verificables del destino: correccion de placeholders Slug y literales corruptos en README/programa."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y formato.",
    "Usar tono juridico formal, claro, verificable y sobrio en inferencias.",
    "Conservar contexto curricular del destino: Licenciatura en Derecho, semestre 8, bloque 1, tipo Electiva.",
    "No renombrar asignatura ni codigo provisional sin confirmacion oficial.",
    "Conservar autor y matricula de plantilla mientras no exista instruccion institucional en contrario.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Marcar como supuesto todo dato no visible o no confirmado en consigna local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Declarar objetivo puntual antes del desarrollo.",
    "Organizar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto solicitado por planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Usar carpeta de materia como entrada canonica.",
    "Conservar README, programa analitico, plantillas TeX y .bib como base minima."
  ],
  "activity_rules": [
    "Vincular cada producto con al menos un problema juridico o social delimitado.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Diferenciar resumen de fuentes frente a postura propia del estudiante.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No extrapolar contenido tematico de nodos no equivalentes sin evidencia local.",
    "No asumir fuentes de semanas posteriores como aplicables por defecto."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizacion aguas abajo.",
    "Validar consistencia entre portada, metadatos y nombre de asignatura.",
    "Confirmar trazabilidad de afirmaciones con respaldo o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de entrega.",
    "Confirmar que rutas de fuentes locales existan."
  ],
  "latex_rules": [
    "Mantener plantilla base de reporte y presentacion con metadatos consistentes.",
    "Usar codificacion y paquetes compatibles con espanol academico.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Mantener claves BibTeX estables.",
    "Resolver tokens tipo $(@{...}.Slug) en README, programa y referencias cruzadas.",
    "Corregir nombres de archivo corruptos en README (supuesto: faltan letras iniciales en reporte/referencias)."
  ],
  "bibliography_rules": [
    "Usar electiva-semestre-8-bloque-1.bib como archivo local canonico mientras no haya cambio verificado.",
    "Registrar en .bib solo fuentes consultadas y verificables.",
    "No inventar referencias.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base institucional de bibliografia especifica por actividad.",
    "Priorizar fuentes institucionales UnADM para contexto curricular.",
    "Agregar doctrina, norma o jurisprudencia solo cuando la consigna lo requiera."
  ],
  "propagation_hints": [
    "Propagar transversalmente solo abstracciones editoriales estables.",
    "No propagar metadatos especificos de una actividad a nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Aplicar union-dedupe lossless en cada ciclo para evitar regresiones.",
    "Registrar supuestos explicitamente cuando falte contexto local.",
    "Si aparece salida no estructurada, normalizar manualmente antes de propagar."
  ],
  "open_questions": [
    "Confirmar creditos oficiales de la electiva para portada y README.",
    "Confirmar nombre oficial de la electiva y codigo de curso definitivo.",
    "Confirmar figura docente para completar plantilla.",
    "Confirmar si hay consigna local que exija artefacto distinto de reporte/presentacion.",
    "Supuesto: los literales '\\neporte' y '\\neferencias' en README son errores de texto; validar correccion final.",
    "Confirmar si existe bibliografia obligatoria adicional para esta materia."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico",
        "Claro y juridicamente preciso",
        "Verificable y sobrio",
        "Argumentativo con criterio propio"
      ],
      "institutional": [
        "Alineacion explicita con UnADM",
        "Integridad academica con citas verificables",
        "Entrada canonica por carpeta de materia",
        "Supuestos etiquetados sin ambiguedad"
      ],
      "curricular": [
        "Licenciatura en Derecho",
        "Semestre 8, bloque 1, tipo Electiva",
        "Transferencia profesional como criterio de cierre"
      ]
    },
    "essence": [
      "Problema juridico o social",
      "Conceptos y fuentes pertinentes",
      "Producto alineado a planeacion",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables academicos con fundamento juridico y evidencia.",
      "Preservar consistencia editorial institucional entre actividades y materia.",
      "Garantizar calidad tecnica y trazabilidad antes de propagacion recursiva."
    ],
    "style_markers": [
      "Objetivo explicito al inicio",
      "Secciones estables reutilizables",
      "Postura propia sustentada",
      "Cierre practico profesional",
      "Supuestos declarados"
    ],
    "argumentative_patterns": [
      "Problema -> conceptos/fuentes -> analisis -> conclusion",
      "Afirmacion -> evidencia -> inferencia juridica",
      "Descripcion breve -> posicion critica -> implicacion practica"
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Estructura argumentativa juridica",
        "Trazabilidad de fuentes",
        "Normalizacion JSON",
        "Control de placeholders editoriales"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Define tono, formato y criterio de cierre."
        },
        {
          "source": "Trazabilidad de fuentes",
          "target": "Estructura argumentativa juridica",
          "kind": "supports",
          "justification": "Sostiene afirmaciones y evita descripcion vacia."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin parseo valido no hay reutilizacion confiable."
        },
        {
          "source": "Control de placeholders editoriales",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Reduce errores por tokens y rutas corruptas."
        },
        {
          "source": "Estructura argumentativa juridica",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "Conduce de problema a aplicacion profesional."
        }
      ],
      "evidence": [
        "README destino con token Slug sin expandir.",
        "README destino con literales de archivo corruptos.",
        "Programa analitico del destino con ejes editoriales estables.",
        "Archivo .bib local con claves institucionales existentes.",
        "Regla heredada de bloqueo por salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 14: deduplicacion semantica aplicada sin eliminar reglas utiles previas.",
      "Ciclo 14: se reforzaron gates de JSON parseable y trazabilidad.",
      "Ciclo 14: se transfirieron solo abstracciones estables entre nodos no equivalentes.",
      "Ciclo 14: se mantuvieron vacios locales abiertos como supuestos verificables."
    ]
  }
}