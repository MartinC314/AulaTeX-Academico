{
  "summary": [
    "Se consolida sincronizacion transversal conservadora para Derecho penal especial mexicano.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y cierre juridico propio.",
    "Se refuerza deduplicacion lossless por union semantica sin recorte de reglas utiles.",
    "Se mantiene bloqueo de propagacion ante salidas no JSON parseables.",
    "Se agrega control de placeholders y campos truncados detectados en README, programa y plantilla TeX."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado en la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Corregir nombres corruptos y placeholders sin cambiar el slug canonico."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar texto solo descriptivo.",
    "Vincular problema con normas, conceptos o doctrina penal aplicable.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "No transferir contenido tematico de Filosofia del Derecho sin evidencia local verificable."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente todo insumo desestructurado antes de reutilizar.",
    "Verificar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir marca de supuesto o respaldo para cada afirmacion sensible.",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Detectar y corregir placeholders o campos truncados antes de compilar."
  ],
  "latex_rules": [
    "Mantener plantilla article en español y letterpaper.",
    "Completar metadatos institucionales antes de salida final.",
    "Usar archivo bib local canonico derecho-penal-especial-mexicano.bib.",
    "Evitar tokens sin expandir tipo $(@{...}.Slug) en rutas y nombres.",
    "Corregir campo truncado Tipo/Creditos en authortable.",
    "Compilar sin errores criticos ni referencias rotas."
  ],
  "bibliography_rules": [
    "Usar el .bib local como fuente unica del entregable.",
    "Conservar fuentes institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "Agregar entradas por actividad solo con datos verificables.",
    "No inventar fuentes ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, año, fuente o URL.",
    "Registrar fecha de consulta en recursos web cuando aplique."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y no tematicas.",
    "Priorizar identidad, estructura reusable, quality gates y grafo conceptual.",
    "Aplicar deduplicacion semantica sin eliminar reglas utiles previas.",
    "Mantener bandera de normalizacion manual para herencias no estructuradas.",
    "Transferir correcciones de placeholders a nodos laterales similares."
  ],
  "open_questions": [
    "Confirmar figura docente real en plantillas del destino.",
    "Confirmar si coursecode LDE-S2B2 queda fijo como regla global. [Supuesto]",
    "Corregir definitivamente entradas corruptas en README (eporte/eferencias).",
    "Confirmar que matricula visible corresponde al estudiante real. [Supuesto]",
    "Definir consignas locales por actividad para activar memoria tematica penal especifica."
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
      "Calidad juridica basada en problema, evidencia y conclusion transferible.",
      "Transferencia transversal conservadora: forma estable, no contenido disciplinar ajeno."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos verificables y utiles para practica juridica.",
      "Asegurar coherencia entre identidad institucional, estructura argumentativa y trazabilidad bibliografica."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Cierre con posicion juridica propia.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis -> conclusion.",
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
          "justification": "Evita reutilizar salidas no parseables."
        },
        {
          "source": "Cinco ejes editoriales",
          "target": "Calidad argumentativa",
          "kind": "supports",
          "justification": "Ordena problema, conceptos, evidencia, analisis y cierre."
        },
        {
          "source": "Integridad bibliografica",
          "target": "Validez academica",
          "kind": "depends_on",
          "justification": "Exige trazabilidad cita-bibliografia."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Solo se transfieren abstracciones editoriales estables."
        },
        {
          "source": "Control de placeholders y campos truncados",
          "target": "Compilacion LaTeX confiable",
          "kind": "supports",
          "justification": "Reduce fallos de build y errores de ruta."
        }
      ],
      "evidence": [
        "README de destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico explicita cinco ejes de trabajo.",
        "Bib local contiene base institucional verificable.",
        "Plantilla TeX muestra campo truncado y dato docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: deduplicacion semantica aplicada sin perdida.",
      "Ciclo 15: se preservan reglas institucionales heredadas validas.",
      "Ciclo 15: se refuerzan gates de JSON parseable y normalizacion manual.",
      "Ciclo 15: se mantiene estrategia transversal conservadora entre nodos no equivalentes."
    ]
  }
}