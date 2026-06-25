{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre actividad de origen y materia destino.",
    "Se preservan reglas utiles previas por union-dedupe sin recorte.",
    "Se transfiere solo marco editorial estable y reusable entre nodos no equivalentes.",
    "Se refuerzan ejes comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene bloqueo de propagacion para salidas no JSON parseable.",
    "Se mantiene alerta local por tokens Slug sin expandir y nombres de archivo con artefactos.",
    "Supuesto: no se transfiere doctrina especifica de Filosofia del Derecho al destino por diferencia disciplinar."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Usar nombre oficial de la materia destino en todos los artefactos.",
    "Usar Licenciatura en Derecho como programa academico.",
    "Respetar contexto curricular local confirmado: semestre 6, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no confirmado por consigna o archivo local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar desarrollo en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el entregable al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Conservar correspondencia entre README, .tex, presentacion y .bib.",
    "Resolver placeholders y tokens de plantilla antes de cerrar version."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Identificar el problema que activa la actividad antes de argumentar.",
    "Conectar la conclusion con aplicacion practica en contexto profesional.",
    "Registrar en .bib solo fuentes usadas por la actividad."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar memoria.",
    "No eliminar reglas utiles previas durante fusion editorial.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Revisar y normalizar respuestas no estructuradas antes de propagacion recursiva.",
    "Verificar que README liste archivos reales y rutas existentes."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Actualizar documenttitle y documentsubtitle por actividad.",
    "Corregir tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir nombres de archivo con artefactos de salto antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y materiales juridicos pertinentes al destino.",
    "Distinguir bibliografia base de materia y bibliografia especifica por actividad.",
    "Conservar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "No citar fuentes no agregadas al .bib local.",
    "Mantener trazabilidad entre cita en texto y entrada BibTeX."
  ],
  "propagation_hints": [
    "Propagar lateral y ascendente solo tras validacion de JSON y estructura.",
    "Propagar solo abstracciones editoriales estables en nodos no equivalentes.",
    "No propagar contenido doctrinal especifico de Filosofia del Derecho al destino.",
    "Reutilizar gates institucionales de calidad sin perder contexto local.",
    "Mantener estrategia progresiva y conservadora para evitar regresiones.",
    "Si falta consigna local, propagar solo reglas generales y abrir vacios en preguntas."
  ],
  "open_questions": [
    "Confirmar valor final del Slug en README y programa analitico local.",
    "Confirmar correccion de nombres de archivo con artefactos de salto en README.",
    "Confirmar si documentauthor debe parametrizarse por actividad.",
    "Confirmar si year=2026 en unadmSitioWeb se usa como anio bibliografico o solo consulta.",
    "Supuesto: destino aun no define guia de citacion juridica especifica distinta a plantilla general."
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
        "Integridad academica con trazabilidad bibliografica.",
        "Entrada canonica por carpeta de materia."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 6, bloque 2, obligatoria, 8 creditos.",
        "Transferencia profesional como criterio de cierre."
      ]
    },
    "essence": [
      "Problema juridico bien delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable y trazable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible a practica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y aplicables.",
      "Sostener consistencia editorial institucional entre actividades y artefactos LaTeX.",
      "Proteger calidad mediante validaciones estructurales y bibliograficas."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Supuestos marcados explicitamente.",
      "Sin afirmaciones sin fuente.",
      "Cierre con transferencia profesional."
    ],
    "argumentative_patterns": [
      "Problema -> conceptos -> evidencia -> analisis propio -> conclusion.",
      "Marco normativo como soporte del criterio personal.",
      "Coherencia estricta entre consigna, desarrollo y cierre."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Problema juridico",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Control de supuestos",
        "Integridad bibliografica",
        "Correccion de tokens Slug"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin JSON valido no hay transferencia segura."
        },
        {
          "source": "Evidencia verificable",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion exige sustento normativo y documental."
        },
        {
          "source": "Control de supuestos",
          "target": "Integridad argumentativa",
          "kind": "supports",
          "justification": "Diferencia datos confirmados de inferencias provisionales."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Estructura de entregables",
          "kind": "supports",
          "justification": "Fija tono, formato y trazabilidad comun."
        },
        {
          "source": "Correccion de tokens Slug",
          "target": "Compilacion LaTeX estable",
          "kind": "depends_on",
          "justification": "Evita rutas invalidas y referencias rotas."
        }
      ],
      "evidence": [
        "README local de la materia.",
        "Programa analitico local.",
        "Archivo .bib local.",
        "Memoria origen con ejes editoriales estables y gates de calidad."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se preservan reglas utiles previas sin regresion.",
      "Ciclo 15: se deduplican variantes repetidas y se normaliza redaccion accionable.",
      "Ciclo 15: se transfiere marco reusable transversal; se excluye doctrina no equivalente.",
      "Ciclo 15: se refuerza control de JSON, supuestos, citas y compilacion."
    ]
  }
}