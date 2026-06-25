{
  "summary": [
    "Se sincroniza transversalmente un nucleo editorial estable desde actividad de Filosofia del Derecho hacia materia electiva sin transferir contenido tematico literal.",
    "Se conserva identidad UnADM y encuadre curricular local del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Se refuerzan ejes reutilizables: problema, conceptos o normas, evidencia, analisis propio y conclusion juridica transferible.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se preserva estrategia progresiva y conservadora con compresion lossless por union-dedupe."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre curricular del destino y no heredar metadatos curriculares del origen no equivalente.",
    "Usar la carpeta de materia como entrada canonica para plantillas y referencias.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica, README o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "No mezclar identidad de otras carreras o asignaturas en productos de Derecho."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre consigna, desarrollo y conclusion."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, objetivo, analisis y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra semana o asignatura aplica automaticamente.",
    "Etiquetar supuestos cuando falten instrucciones locales."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin etiqueta de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Comprobar que rutas y nombres de archivos existan en el repositorio."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener codificacion y acentos correctos en .tex y .bib.",
    "No compilar con placeholders o tokens sin expandir.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Conservar metadatos de portada solo con datos confirmados; marcar como supuesto lo faltante."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Centralizar referencias en el .bib canonico de la materia.",
    "No trasladar bibliografia tematica del origen sin verificacion documental local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo abstracciones estables: identidad, estructura, gates y grafo conceptual.",
    "Evitar transferir redaccion literal o temas propios de una actividad no equivalente.",
    "Mantener union-dedupe y sin regresion en cada ciclo.",
    "Separar reglas institucionales de reglas tematicas antes de propagar lateralmente.",
    "Si aparece salida no estructurada, activar normalizacion manual y no bloquear memoria valida previa."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular institucional.",
    "Confirmar creditos oficiales para README y portada.",
    "Corregir placeholders en README y programa analitico para nombre canonico del .bib.",
    "Definir si el year del sitio UnADM se mantiene fijo o se gestiona por fecha de consulta.",
    "Confirmar figura docente en plantilla base.",
    "Supuesto: aun no hay consigna local de actividad especifica dentro de la electiva."
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
        "Normalizacion estructurada obligatoria antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Produccion orientada a planeacion semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la actividad.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Evidencia verificable con cita.",
      "Analisis propio y postura argumentada.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Estandarizar productos academicos con calidad juridica verificable.",
      "Asegurar continuidad editorial entre nodos no equivalentes sin perder identidad local.",
      "Permitir propagacion segura basada en estructura y no en texto literal."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados cuando falte informacion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma o doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion propia.",
      "Consigna -> objetivo -> verificacion de coherencia final."
    ],
    "knowledge_graph": {
      "concepts": [
        "identidad institucional",
        "normalizacion estructurada",
        "alineacion con consigna",
        "evidencia verificable",
        "postura argumentada",
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
          "kind": "supports",
          "justification": "Evita ruido y mejora trazabilidad de respaldo."
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
        },
        {
          "source": "alineacion con consigna",
          "target": "conclusion transferible",
          "kind": "depends_on",
          "justification": "La transferencia practica exige responder al producto solicitado."
        }
      ],
      "evidence": [
        "README local de la materia como punto de entrada canonico.",
        "Programa analitico local con ejes problema-conceptos-producto-analisis-cierre.",
        "Bibliografia base local en electiva-semestre-7-bloque-2.bib.",
        "Regla historica conservada: bloquear propagacion ante salida no JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 17: se consolidan abstracciones estables del origen sin importar tema especifico de Filosofia del Derecho.",
      "Ciclo 17: se mantiene compresion lossless por deduplicacion y sin regresion.",
      "Ciclo 17: se refuerzan gates de parseabilidad JSON, estructura minima y control de supuestos.",
      "Ciclo 17: se preserva base institucional UnADM y encuadre curricular del destino."
    ]
  }
}