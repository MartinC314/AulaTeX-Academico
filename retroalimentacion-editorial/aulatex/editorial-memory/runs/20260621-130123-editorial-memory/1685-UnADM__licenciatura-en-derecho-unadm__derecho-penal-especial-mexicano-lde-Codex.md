{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables de identidad UnADM, estructura reusable y control de calidad.",
    "Se transfiere solo abstraccion editorial; no se transfiere contenido tematico de Filosofia del Derecho.",
    "Se refuerza normalizacion obligatoria de insumos no parseables antes de propagacion recursiva.",
    "Se mantiene compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna o evidencia local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto solicitado en planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir placeholders de slug y nombres corruptos sin alterar el slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto y verificable.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "No usar la actividad origen como base disciplinar si no aporta evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marca de supuesto para toda afirmacion.",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Detectar y corregir campos truncados y placeholders antes de compilar."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y letterpaper salvo consigna contraria.",
    "Usar acentos y codificacion consistentes en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar roturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni tokens sin expandir.",
    "Completar metadatos y tabla academica antes de salida final."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar fuentes institucionales base verificadas del destino.",
    "Agregar fuentes por actividad solo con datos consultables.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, estructura reusable, gates y grafo conceptual.",
    "Mantener estrategia conservadora en saltos transversales entre materias.",
    "Evitar transferencia de redaccion literal o contenido tematico no verificable.",
    "Propagar correcciones tecnicas comunes: JSON, placeholders, truncamientos, cita-bib.",
    "Mantener bandera de normalizacion manual para herencias de Codex/GPT-Pro no estructuradas."
  ],
  "open_questions": [
    "Confirmar figura docente real en plantillas del destino.",
    "Confirmar si LDE-S2B2 queda fijo como regla global de materia. [supuesto]",
    "Cerrar campo truncado Tipo/Creditos en reporte .tex del destino.",
    "Verificar si existen mas rutas con caracteres anomales en README/estructura.",
    "Confirmar rubricas locales de actividades para ajustar profundidad argumentativa.",
    "Confirmar fuentes penales obligatorias por unidad para enriquecer .bib local."
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
        "Materia: Derecho penal especial mexicano.",
        "Semestre 2, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico activo.",
      "Conceptos y norma aplicable.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos validos y utiles para practica juridica.",
      "Sostener continuidad editorial entre actividades sin perder rigor ni trazabilidad."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Secciones funcionales y ordenadas.",
      "Marcado explicito de supuestos.",
      "Cierre con posicion juridica propia.",
      "Consistencia entre README, programa, .tex y .bib."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/conceptual -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Consigna -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliografica",
        "Conclusion juridica transferible",
        "No transferencia tematica sin evidencia local"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "supports",
          "justification": "Reduce errores por insumos no parseables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena problema, evidencia, analisis y cierre."
        },
        {
          "source": "Integridad bibliografica",
          "target": "Validez academica",
          "kind": "depends_on",
          "justification": "Exige trazabilidad de fuentes y correspondencia cita-bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "En salto transversal solo pasan abstracciones editoriales estables."
        }
      ],
      "evidence": [
        "README del destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico del destino define cinco ejes de trabajo.",
        ".bib local contiene base institucional verificable.",
        "Plantilla .tex muestra campo truncado y requiere correccion."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 4: reforzada regla de no transferir contenido tematico entre materias no equivalentes.",
      "Ciclo 4: reforzado gate JSON parseable y normalizacion manual previa.",
      "Ciclo 4: consolidada base minima persistente para sincronizacion transversal."
    ]
  }
}