{
  "summary": [
    "Se sincroniza memoria transversal desde actividad de Filosofia del Derecho hacia materia electiva con transferencia de abstracciones estables.",
    "Se conserva identidad institucional UnADM y normalizacion estructurada obligatoria antes de propagar.",
    "Se refuerzan ejes reutilizables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene estrategia progresiva y conservadora con compresion lossless por union-dedupe.",
    "Se preserva regla de bloquear propagacion ante salidas no JSON parseable y aislar insumos no estructurados."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar encuadre local del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "Conservar autoria, matricula y datos academicos en portada cuando aplique.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Marcar como supuesto cualquier dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Mantener trazabilidad entre consigna, desarrollo, evidencia y conclusion."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local de la materia.",
    "No asumir que bibliografia de otra semana o asignatura aplica automaticamente.",
    "Registrar supuestos cuando falten instrucciones completas."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y nombres rotos en README o programa antes de reutilizar plantillas.",
    "Comprobar que las rutas citadas existan en el repositorio local."
  ],
  "latex_rules": [
    "Usar la plantilla .tex local como base y mantener article, spanish, letterpaper, oneside salvo instruccion distinta.",
    "Mantener metadatos del curso LDE-S7B2 y portada con identificacion academica.",
    "Sustituir 'Actividad X' por nombre real del producto antes de cierre.",
    "No compilar con placeholders tipo $(@{...}) sin normalizacion.",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas juridicas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL y nota de consulta cuando aplique.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No trasladar bibliografia tematica de Filosofia del Derecho sin verificacion documental y pertinencia local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas, generales y no duplicadas.",
    "Separar reglas institucionales de reglas tematicas al propagar lateralmente.",
    "Mantener bandera de normalizacion manual para ciclos con insumo no estructurado.",
    "Evitar regresiones: nunca eliminar reglas utiles previas ya verificadas.",
    "Si falta contexto del destino, mantener cerebro editorial minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar nombre oficial de la electiva en malla curricular.",
    "Confirmar creditos oficiales para README y portada.",
    "Confirmar nombre de figura docente en plantilla base.",
    "Corregir placeholders de .bib en README y programa analitico.",
    "Supuesto: year 2026 en unadmSitioWeb es valido; confirmar politica entre year y fecha de consulta.",
    "Confirmar si existe consigna local de actividades para ajustar tipos de producto por semana."
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
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio y postura argumentada.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables, fundamentados y utiles para practica juridica.",
      "Sostener coherencia editorial transversal entre actividades y materia sin mezclar contenido no equivalente."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden argumental estable.",
      "Supuestos etiquetados cuando falte informacion.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
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
        "conclusion transferible",
        "control de supuestos"
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
          "justification": "La postura propia requiere fundamento documentado."
        },
        {
          "source": "postura argumentada",
          "target": "conclusion transferible",
          "kind": "develops",
          "justification": "El analisis propio habilita cierre aplicable."
        },
        {
          "source": "control de supuestos",
          "target": "alineacion con consigna",
          "kind": "supports",
          "justification": "Evita afirmar datos no confirmados."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM y carpeta como entrada canonica.",
        "Programa analitico local define ejes problema-conceptos-producto-analisis-cierre.",
        "Bibliografia local contiene base institucional verificable.",
        "Regla heredada valida: bloquear propagacion cuando no hay JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 3: se deduplican reglas repetidas y se conservan todas las utiles.",
      "Ciclo 3: se transfieren solo abstracciones estables por relacion transversal.",
      "Ciclo 3: no se importa redaccion literal ni contenido tematico especifico de Filosofia del Derecho.",
      "Ciclo 3: se mantiene cerebro editorial minimo del destino y se registran vacios locales como preguntas."
    ]
  }
}