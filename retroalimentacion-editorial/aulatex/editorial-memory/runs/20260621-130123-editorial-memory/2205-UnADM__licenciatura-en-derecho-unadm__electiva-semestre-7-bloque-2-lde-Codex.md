{
  "summary": [
    "Se sincroniza transversalmente un nucleo editorial estable desde actividad a materia sin trasladar contenido tematico especifico.",
    "Se conserva identidad UnADM, estructura canonica y validacion estructurada previa a propagacion.",
    "Se refuerza compresion lossless por union-dedupe con estrategia progresiva y conservadora en ciclo 2.",
    "Se mantiene el destino como cerebro editorial minimo ampliable por actividad local."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar encuadre curricular local del destino: Licenciatura en Derecho, semestre 7, bloque 2, electiva.",
    "Usar la carpeta de materia como punto de entrada canonico.",
    "No mezclar identidad de otras carreras en productos de Derecho.",
    "Marcar como supuesto todo dato no visible en consigna, rubrica o malla.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada entrega al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Registrar fuentes especificas de cada actividad en el .bib local.",
    "No asumir que bibliografia de otra asignatura o semana aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Marcar y aislar insumos no estructurados para normalizacion manual.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Corregir placeholders y tokens sin expandir en README, programa y rutas antes de reutilizar."
  ],
  "latex_rules": [
    "Usar plantilla .tex local de la materia como base.",
    "Mantener metadatos del curso LDE-S7B2 y portada academica completa.",
    "Usar article con spanish, letterpaper y oneside salvo instruccion contraria.",
    "No compilar con tokens tipo $(@{...}) ni rutas rotas.",
    "Mantener acentos y codificacion correcta en .tex y .bib.",
    "Compilar sin errores criticos, sin referencias ni citas rotas."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes verificables y consultables.",
    "Priorizar fuentes institucionales UnADM y normativas pertinentes al encargo.",
    "Centralizar referencias en electiva-semestre-7-bloque-2.bib.",
    "Conservar claves BibTeX estables para evitar quiebres de compilacion.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener metadatos minimos: autor, titulo, anio, fuente/editorial o URL."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal o contenido tematico de Filosofia del Derecho.",
    "Mantener bandera de normalizacion manual para memorias heredadas no parseables.",
    "Aplicar union-dedupe sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Supuesto: falta nombre oficial final de la electiva en malla curricular; confirmar.",
    "Supuesto: creditos de la electiva estan vacios en README/portada; confirmar dato oficial.",
    "Confirmar reemplazo de placeholders en README y programa analitico.",
    "Confirmar figura docente en plantilla base.",
    "Confirmar politica local de year vs fecha de consulta para fuentes web institucionales."
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
      "Problema juridico.",
      "Conceptos y normas pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, sustentados y utiles para la practica."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones trazables.",
      "Supuestos etiquetados.",
      "Cierre con implicacion practica."
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
          "justification": "La identidad delimita forma y alcance del entregable."
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
          "justification": "El analisis propio habilita un cierre util en practica."
        }
      ],
      "evidence": [
        "README local confirma identidad y carpeta canonica.",
        "Programa analitico local confirma ejes de trabajo reutilizables.",
        "Bibliografia local confirma base institucional minima en .bib."
      ]
    },
    "reinforcement_log": [
      "Ciclo 2: se consolida transferencia transversal de reglas estables sin arrastre tematico.",
      "Ciclo 2: se mantiene bloqueo por JSON no parseable y normalizacion manual obligatoria.",
      "Ciclo 2: se refuerza union-dedupe sin regresion de reglas utiles previas."
    ]
  }
}