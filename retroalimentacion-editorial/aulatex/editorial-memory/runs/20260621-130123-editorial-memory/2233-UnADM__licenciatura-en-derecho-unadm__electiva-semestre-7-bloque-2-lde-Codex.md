{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe y sin regresion.",
    "Se conservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se transfiere solo abstraccion reusable desde actividad no equivalente.",
    "Se evita importar contenido tematico especifico de Filosofia del Derecho.",
    "Se refuerza normalizacion obligatoria de entradas no parseables antes de propagacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre curricular local del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar carpeta de materia como entrada canonica.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra asignatura aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente insumos no estructurados antes de reutilizarlos.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir en README y programa analitico."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 y portada academica completa.",
    "Usar article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "No compilar con placeholders tipo $(@{...}) sin resolver.",
    "Mantener claves BibTeX estables y referencias sin roturas.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativa pertinente al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente/URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables, validadas y no duplicadas.",
    "Separar reglas institucionales de reglas tematicas al transferir transversalmente.",
    "Mantener bandera de normalizacion manual para ciclos con herencia no estructurada.",
    "Aplicar compresion lossless por deduplicacion, no por recorte."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales faltantes en README y portada.",
    "Confirmar figura docente en plantilla base.",
    "Resolver nombres de archivo con placeholder en README y programa analitico.",
    "Supuesto: year 2026 en unadmSitioWeb se mantiene hasta criterio institucional de fechado."
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Produccion orientada a planeacion semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, sustentados y utiles para practica profesional."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados cuando falte contexto.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion propia.",
      "Consigna -> objetivo -> verificacion final de coherencia."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalizacion estructurada",
        "evidencia verificable",
        "postura argumentada",
        "alineacion con consigna",
        "conclusion transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional",
          "target": "alineacion con consigna",
          "kind": "supports",
          "justification": "Define limites formales y curriculares del entregable."
        },
        {
          "source": "normalizacion estructurada",
          "target": "evidencia verificable",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay trazabilidad de respaldo."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere sustento documental."
        },
        {
          "source": "postura argumentada",
          "target": "conclusion transferible",
          "kind": "develops",
          "justification": "El analisis propio habilita cierre aplicable a practica juridica."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y carpeta canonica.",
        "Programa analitico local: ejes problema-conceptos-producto-analisis-cierre.",
        "Bib local: base institucional unadmSitioWeb y unadmMallaDerecho2024.",
        "Regla heredada consolidada: bloquear propagacion sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 9: se integran abstracciones estables de actividad origen sin arrastre tematico.",
      "Ciclo 9: se conserva ADN editorial del destino y se refuerzan quality gates.",
      "Ciclo 9: se mantiene estrategia progresiva y conservadora con union-dedupe."
    ]
  }
}