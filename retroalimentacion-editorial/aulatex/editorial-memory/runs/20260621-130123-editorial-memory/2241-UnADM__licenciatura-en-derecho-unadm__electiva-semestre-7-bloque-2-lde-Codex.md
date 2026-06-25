{
  "summary": [
    "Sincronizacion transversal aplicada con union-dedupe y sin regresion.",
    "Se preservan reglas estables de identidad UnADM, estructura argumentativa y control de calidad.",
    "Se transfieren solo abstracciones reutilizables; no se transfiere contenido tematico de Filosofia del Derecho.",
    "Se mantiene normalizacion estructurada obligatoria antes de toda propagacion recursiva.",
    "Se refuerza cerebro editorial minimo de materia para semestre 7 bloque 2 electiva."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar encuadre curricular local: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar la carpeta de materia como entrada canonica.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar resumen solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra asignatura aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir antes de publicar plantilla."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 salvo confirmacion oficial distinta.",
    "Conservar portada con datos academicos completos cuando aplique.",
    "No compilar con tokens sin expandir tipo $(@{...}.Slug).",
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar transversal y recursivo solo reglas validadas y no duplicadas.",
    "Transferir abstracciones editoriales, no redaccion literal ni temas de otra materia.",
    "Mantener estrategia progresiva y conservadora en cada ciclo.",
    "Preservar alertas de normalizacion manual para ciclos con memoria no estructurada.",
    "Priorizar identidad, gates de calidad y grafo conceptual en saltos no equivalentes."
  ],
  "open_questions": [
    "Supuesto: faltan creditos oficiales en README y portada; confirmar en malla.",
    "Confirmar nombre oficial final de la electiva en semestre 7 bloque 2.",
    "Confirmar figura docente para reemplazar placeholder.",
    "Confirmar politica local para year vs fecha de consulta en fuentes web institucionales."
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
        "Normalizacion estructurada previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 7, bloque 2, electiva.",
        "Produccion orientada a planeacion semanal y transferencia profesional."
      ]
    },
    "essence": [
      "Problema, conceptos, evidencia, analisis propio y conclusion juridica.",
      "Trazabilidad estructural antes de reutilizacion.",
      "Transferencia transversal por abstracciones estables."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles.",
      "Asegurar coherencia entre consigna, evidencia y cierre juridico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y trazables.",
      "Supuestos etiquetados cuando falte contexto.",
      "Cierre con implicacion practica juridica."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion propia.",
      "Consigna -> objetivo -> verificacion final."
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
          "justification": "El analisis propio habilita cierre util para practica."
        }
      ],
      "evidence": [
        "README local: entrada canonica e identidad UnADM.",
        "Programa analitico local: ejes editoriales de trabajo.",
        "Bibliografia local: base institucional en .bib de materia.",
        "Supuesto: transferencia tematica desde Filosofia del Derecho no aplica por no equivalencia de nodo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 11: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 11: se conservaron gates criticos de parseo JSON y normalizacion manual.",
      "Ciclo 11: se reforzo patron argumentativo reusable sin importar tema de origen.",
      "Ciclo 11: se mantuvieron alertas de placeholders y tokens sin expandir."
    ]
  }
}