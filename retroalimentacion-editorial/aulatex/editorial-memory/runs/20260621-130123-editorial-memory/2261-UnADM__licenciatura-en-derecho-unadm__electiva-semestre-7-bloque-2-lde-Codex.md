{
  "summary": [
    "Sincronizacion transversal consolidada desde actividad no equivalente hacia materia electiva con transferencia de abstracciones estables.",
    "Se preserva identidad UnADM y encuadre curricular local del destino.",
    "Se refuerza normalizacion estructurada obligatoria antes de toda propagacion recursiva.",
    "Se mantiene compresion lossless por union-dedupe sin recorte de reglas utiles.",
    "Se priorizan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre de Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No mezclar identidad de otras carreras en productos de Derecho."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra semana o asignatura aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y nombres rotos en README y programa antes de reutilizar plantillas."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 y portada academica completa.",
    "Usar article con spanish, letterpaper y oneside salvo instruccion distinta.",
    "No compilar con tokens sin expandir tipo $(@{...}.Slug).",
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, generales y no duplicadas.",
    "Compartir entre nodos no equivalentes solo abstracciones editoriales estables.",
    "No propagar contenido tematico especifico de Filosofia del Derecho a la electiva sin verificacion local.",
    "Mantener estrategia progresiva y conservadora para evitar regresiones.",
    "Conservar alerta de normalizacion manual en ciclos con salidas no estructuradas heredadas."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales faltantes en README y portada.",
    "Confirmar figura docente para sustituir placeholder.",
    "Confirmar si year del sitio UnADM se mantiene o se prioriza solo fecha de consulta.",
    "Supuesto: falta consigna local de actividades especificas de la electiva para ajustar granularidad."
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
      "Problema juridico o social",
      "Conceptos y marco normativo",
      "Evidencia verificable",
      "Analisis propio",
      "Conclusion juridica transferible"
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables y utiles.",
      "Asegurar calidad institucional y coherencia argumentativa en cada entrega."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados cuando falte informacion.",
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
        "conclusion transferible",
        "alineacion con consigna"
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
          "justification": "Sin estructura valida no hay control de trazabilidad."
        },
        {
          "source": "evidencia verificable",
          "target": "postura argumentada",
          "kind": "supports",
          "justification": "La postura propia requiere respaldo documental."
        },
        {
          "source": "postura argumentada",
          "target": "conclusion transferible",
          "kind": "develops",
          "justification": "El analisis propio habilita cierre aplicable."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y punto de entrada canonico.",
        "Programa analitico local confirma ejes de problema, conceptos, producto, analisis y cierre.",
        "Bibliografia local confirma base institucional en electiva-semestre-7-bloque-2.bib.",
        "Supuesto: transferencia transversal desde actividad origen solo aporta reglas estables, no contenido tematico local."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 16: se conserva gate de JSON parseable como bloqueo duro de propagacion.",
      "Ciclo 16: se agrega control explicito de placeholders en README/programa/LaTeX.",
      "Ciclo 16: se mantiene frontera transversal para no contaminar tema de electiva con doctrina especifica del origen."
    ]
  }
}