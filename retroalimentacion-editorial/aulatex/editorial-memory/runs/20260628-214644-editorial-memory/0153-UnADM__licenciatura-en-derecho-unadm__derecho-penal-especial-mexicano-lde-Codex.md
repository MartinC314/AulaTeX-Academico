{
  "summary": [
    "Se consolida memoria transversal minima para Derecho penal especial mexicano con identidad UnADM.",
    "Se preservan reglas estables de normalizacion estructurada, integridad academica y compresion union-dedupe sin perdida.",
    "Se transfiere solo abstraccion reusable: ejes editoriales, gates de calidad, disciplina de citas y cierre juridico propio.",
    "Se evita traslado tematico literal de Filosofia del Derecho por no equivalencia disciplinar.",
    "Se refuerza correccion de placeholders y campos truncados detectados en README, programa analitico y plantilla TeX."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en todo entregable.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula antes de entrega."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear cada producto a la consigna semanal real.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Sincronizar coherencia entre README, programa analitico, TeX y .bib."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada propia, no solo resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No asumir que bibliografia de otra materia aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Exigir estructura minima completa del esquema editorial.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Detectar y corregir placeholders o tokens sin expandir antes de compilar.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener codificacion correcta para espanol y acentos en .tex y .bib.",
    "Conservar clase y formato institucional ya definidos salvo consigna en contrario.",
    "Completar metadatos del documento antes de salida final.",
    "Corregir campo truncado de Tipo/Creditos en authortable.",
    "Resolver tokens tipo $(@{...}.Slug) en README y programa analitico.",
    "Usar nombre canonico del .bib local consistente con slug de materia.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar entradas institucionales base existentes.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Registrar fecha de consulta cuando aplique a recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar abstracciones estables sobre contenido tematico literal.",
    "Mantener estrategia conservadora: reforzar sin borrar reglas utiles previas.",
    "Aplicar deduplicacion semantica lossless en cada ciclo.",
    "Propagar a nodos laterales las correcciones de placeholders y normalizacion JSON."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantilla del destino.",
    "Confirmar si LDE-S2B2 es codigo oficial o supuesto operativo.",
    "Confirmar consigna concreta de la proxima actividad para ajustar tipo de producto.",
    "Verificar que autor y matricula visibles sean datos vigentes. [supuesto]",
    "Confirmar que no existan mas campos truncados en plantillas derivadas."
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
        "Destino: semestre 2, bloque 2, obligatoria, 8 creditos. [verificado en contexto local]",
        "Usar malla curricular institucional como respaldo de ubicacion."
      ]
    },
    "essence": [
      "Problema juridico o social como punto de partida.",
      "Conceptos, normas y doctrina pertinentes.",
      "Analisis propio con evidencia.",
      "Conclusion juridica aplicable.",
      "Disciplina tecnica de consistencia editorial y bibliografica."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos claros, fundados y transferibles.",
      "Asegurar trazabilidad entre consigna, argumento, evidencia y cierre.",
      "Sostener una memoria editorial reutilizable sin perdida de reglas utiles."
    ],
    "style_markers": [
      "Frases directas y verificables.",
      "Marcado explicito de supuestos.",
      "Separacion clara entre dato verificado y dato provisional.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion.",
      "Afirmacion -> evidencia -> interpretacion -> implicacion practica.",
      "Control de coherencia entre objetivo, desarrollo y resultado."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion JSON",
        "Ejes editoriales de cinco pasos",
        "Integridad bibliografica 1:1",
        "Conclusion juridica transferible",
        "Consistencia README-programa-TeX-bib"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay transferencia confiable."
        },
        {
          "source": "Ejes editoriales de cinco pasos",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordenan el desarrollo y evitan entregas descriptivas."
        },
        {
          "source": "Integridad bibliografica 1:1",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Asegura respaldo verificable de afirmaciones."
        },
        {
          "source": "Correccion de placeholders",
          "target": "Compilacion LaTeX estable",
          "kind": "supports",
          "justification": "Evita errores tecnicos y rutas invalidas."
        }
      ],
      "evidence": [
        "README local confirma ubicacion curricular del destino.",
        "Programa analitico local explicita ejes de trabajo y proposito editorial.",
        "Plantilla TeX local muestra campo truncado y figura docente pendiente.",
        "Bib local contiene base institucional verificable."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin recorte semantico.",
      "Se conservaron gates criticos heredados: JSON parseable y normalizacion manual.",
      "Se reforzo separacion entre abstraccion transversal y contenido disciplinar local.",
      "Se mantuvo bandera de fuentes provisionales no verificadas.",
      "Se creo cerebro editorial minimo util para destino con vacios abiertos."
    ]
  }
}