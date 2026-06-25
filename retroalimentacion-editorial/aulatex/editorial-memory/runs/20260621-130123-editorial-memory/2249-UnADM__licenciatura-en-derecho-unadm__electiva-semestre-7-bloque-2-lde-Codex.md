{
  "summary": [
    "Sincronización transversal aplicada con estrategia progresiva y conservadora.",
    "Se preservan reglas válidas del destino y del origen sin regresión.",
    "Se transfieren solo abstracciones estables: identidad, estructura, calidad y método argumentativo.",
    "Se mantiene normalización estructurada obligatoria antes de cualquier propagación.",
    "Se conserva compresión lossless por unión y deduplicación.",
    "Se detectan placeholders en README y programa analítico; queda regla activa de corrección previa.",
    "Supuesto: faltan datos locales de créditos y nombre oficial final de la electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre local: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Usar carpeta de materia como punto de entrada canónico.",
    "Conservar autoría y matrícula en portada cuando aplique.",
    "Marcar como supuesto todo dato no visible en consigna, rúbrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmación local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema jurídico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar en: conceptos clave, marco normativo o doctrinal, análisis propio y cierre.",
    "Alinear cada entregable al producto pedido por la planeación semanal.",
    "Cerrar con conclusión jurídica transferible a práctica profesional.",
    "Mantener claridad, fundamento jurídico, evidencia y utilidad profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explícita.",
    "Incluir postura argumentada del estudiante; evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guía, desarrollo y conclusión.",
    "Registrar fuentes específicas de cada actividad en el .bib local.",
    "No asumir que bibliografía de otra asignatura o semana aplica automáticamente.",
    "Vincular cada actividad con el problema jurídico o social que la activa."
  ],
  "quality_gates": [
    "Bloquear propagación si la salida no es JSON parseable.",
    "Revisar estructura mínima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalización manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia del producto con la consigna vigente.",
    "Corregir placeholders y nombres rotos en README y programa analítico antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 salvo confirmación oficial distinta.",
    "Usar article con spanish, letterpaper y oneside salvo instrucción contraria.",
    "Mantener portada con tabla de identificación académica completa.",
    "Sustituir \"Actividad X\" por el nombre real del entregable.",
    "No compilar con tokens sin expandir tipo $(@{...}.Slug).",
    "Mantener codificación y acentos correctos en .tex y .bib.",
    "Compilar sin errores críticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar claves BibTeX estables para evitar roturas.",
    "Conservar metadatos mínimos: autor, título, año y fuente o URL.",
    "Distinguir bibliografía base de bibliografía específica por actividad.",
    "Verificar fecha de consulta y disponibilidad en fuentes web."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y deduplicadas.",
    "Transferir a nodos no equivalentes solo abstracciones editoriales estables.",
    "Separar reglas institucionales de reglas temáticas al propagar lateralmente.",
    "No propagar redacción literal ni contenido temático específico sin verificación local.",
    "Conservar alertas de ciclos con normalización manual pendiente."
  ],
  "open_questions": [
    "Confirmar créditos oficiales de la electiva para README y portada.",
    "Confirmar nombre oficial de la materia en malla curricular.",
    "Corregir tokens placeholder en README y programa analítico.",
    "Confirmar si \"Nombre por definir\" de figura docente ya puede sustituirse.",
    "Definir política local de year vs fecha de consulta para sitio UnADM."
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
        "Normalización estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Producción orientada a planeación semanal y transferencia profesional."
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
      "Convertir planeación semanal en entregables académicos sólidos y verificables.",
      "Asegurar trazabilidad editorial entre consigna, evidencia y cierre argumentativo."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explícitas y trazables.",
      "Supuestos etiquetados cuando falte información.",
      "Cierre con implicación jurídica práctica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> análisis -> conclusión.",
      "Afirmación -> evidencia -> interpretación propia.",
      "Consigna -> objetivo -> validación de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalización estructurada",
        "alineación con consigna",
        "evidencia verificable",
        "postura argumentada",
        "conclusión transferible"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "identidad institucional",
          "target": "alineación con consigna",
          "kind": "supports",
          "justification": "Define límites formales y curriculares del entregable."
        },
        {
          "source": "normalización estructurada",
          "target": "evidencia verificable",
          "kind": "supports",
          "justification": "Evita ruido heredado y mejora trazabilidad."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia exige sustento documental."
        },
        {
          "source": "postura argumentada",
          "target": "conclusión transferible",
          "kind": "develops",
          "justification": "El análisis propio permite cierre útil para práctica jurídica."
        }
      ],
      "evidence": [
        "README local: identidad UnADM y punto de entrada canónico.",
        "Programa analítico local: ejes problema-conceptos-producto-análisis-cierre.",
        "Bib local: base institucional verificable.",
        "Regla heredada estable: bloquear propagación sin JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: consolidada transferencia transversal sin importar redacción literal.",
      "Ciclo 13: reforzada regla de normalización estructurada previa a propagación.",
      "Ciclo 13: mantenidos ejes editoriales universales de Derecho UnADM.",
      "Ciclo 13: preservadas alertas por placeholders y campos curriculares incompletos."
    ]
  }
}