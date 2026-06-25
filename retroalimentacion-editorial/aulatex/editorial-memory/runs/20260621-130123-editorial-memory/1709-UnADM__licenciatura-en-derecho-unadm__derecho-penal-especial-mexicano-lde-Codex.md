{
  "summary": [
    "Se consolida memoria transversal estable para Derecho penal especial mexicano con identidad UnADM.",
    "Se preservan reglas utiles previas sin regresion y con deduplicacion semantica.",
    "Se refuerza normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se mantienen cinco ejes editoriales como patron reusable entre actividades.",
    "Se confirma estrategia conservadora: transferir metodo editorial, no contenido tematico de Filosofia del Derecho."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna o fuentes locales.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir placeholders y nombres corruptos sin cambiar slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Vincular afirmaciones con normas, doctrina o datos verificables.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Agregar fuentes especificas de actividad al .bib local antes de version final.",
    "No trasladar contenido disciplinar de Filosofia del Derecho sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marca de supuesto en toda afirmacion.",
    "Verificar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Compilar LaTeX sin errores criticos ni referencias rotas.",
    "Detectar y resolver campos truncados y tokens sin expandir antes de entrega."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y letterpaper.",
    "Completar metadatos institucionales antes de salida final.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliografico canonico local.",
    "Resolver token $(@{...}.Slug) en README y programa analitico.",
    "Corregir campo truncado Tipo/Creditos en authortable. [supuesto: sigue incompleto]",
    "Evitar macros o rutas con expresiones de plantilla sin resolver."
  ],
  "bibliography_rules": [
    "Usar solo fuentes realmente consultables y verificables.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Registrar fecha de consulta en recursos web variables.",
    "Mantener entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y no contradictorias.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Evitar transferencia de redaccion literal entre nodos no equivalentes.",
    "Mantener bandera de normalizacion manual para insumos heredados no estructurados.",
    "Propagar correcciones de placeholders y campos truncados a nodos laterales similares.",
    "Aplicar union-dedupe sin perdida y sin eliminar reglas utiles previas."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantillas.",
    "Confirmar si LDE-S2B2 debe fijarse como regla global permanente.",
    "Validar autor y matricula visibles contra datos oficiales. [supuesto: pendientes]",
    "Verificar cierre completo del campo Tipo/Creditos en .tex.",
    "Confirmar consignas y rubricas de actividades para ajustar profundidad argumentativa.",
    "Confirmar si existe bibliografia penal obligatoria adicional por semana."
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
      "Cinco ejes editoriales como columna vertebral reusable.",
      "Cierre juridico propio como sello de producto academico.",
      "Rigor de evidencia y trazabilidad bibliografica.",
      "Transferencia transversal por metodo, no por tema."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, sustentados y transferibles.",
      "Asegurar continuidad editorial entre actividades con calidad verificable.",
      "Reducir errores de forma que comprometen validez academica."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Inferencias juridicas explicitas desde evidencia.",
      "Marcado visible de supuestos cuando falte dato."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Consigna -> checklist de cumplimiento -> entrega."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliografica",
        "Conclusion juridica transferible",
        "Control de placeholders y campos truncados"
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
          "justification": "Evita reutilizar salidas no parseables y mantiene consistencia."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena problema, evidencia, analisis propio y cierre."
        },
        {
          "source": "Integridad bibliografica",
          "target": "Validez academica",
          "kind": "depends_on",
          "justification": "Exige trazabilidad entre citas y .bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "La transferencia valida es metodologica, no tematica."
        },
        {
          "source": "Control de placeholders y campos truncados",
          "target": "Confiabilidad del entregable",
          "kind": "supports",
          "justification": "Previene errores formales en README, .tex y programa analitico."
        }
      ],
      "evidence": [
        "README local confirma ubicacion curricular y pauta editorial.",
        "Programa analitico local confirma cinco ejes de trabajo.",
        ".bib local contiene base institucional verificable.",
        "Plantilla .tex muestra campo truncado Tipo/Creditos. [supuesto: sigue vigente hasta correccion]"
      ]
    },
    "reinforcement_log": [
      "Ciclo 10: deduplicacion semantica aplicada sin perdida de reglas utiles.",
      "Ciclo 10: se refuerza gate de JSON parseable para toda propagacion.",
      "Ciclo 10: se mantiene estrategia transversal conservadora entre nodos no equivalentes.",
      "Ciclo 10: se prioriza identidad, estructura reusable y grafo conceptual sobre literalidad."
    ]
  }
}