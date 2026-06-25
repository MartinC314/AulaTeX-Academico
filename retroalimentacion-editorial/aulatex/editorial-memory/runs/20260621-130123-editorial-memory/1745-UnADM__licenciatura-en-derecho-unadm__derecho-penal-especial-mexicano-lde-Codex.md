{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre Filosofia del Derecho y Derecho penal especial mexicano.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales, normalizacion estructurada y cierre juridico propio.",
    "Se mantiene transferencia por abstracciones reutilizables; no se transfiere contenido tematico disciplinar sin evidencia local.",
    "Se refuerza control tecnico: JSON parseable, deduplicacion lossless y consistencia README-programa-.tex-.bib.",
    "Se confirman pendientes locales del destino: placeholders de slug, campos truncados y figura docente por definir."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local.",
    "Conservar autoria real del estudiante y validar matricula antes de entrega.",
    "No inventar figuras docentes ni datos administrativos."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Organizar por secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Mantener consistencia de nombres de archivo y slug canonico de la materia."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Agregar fuentes especificas de cada actividad al .bib local antes de version final.",
    "No asumir que bibliografia de otras materias o semanas aplica automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizacion aguas abajo.",
    "Normalizar manualmente todo insumo desestructurado heredado.",
    "Validar que cada afirmacion tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas del .bib.",
    "Verificar coherencia entre README, programa analitico y plantillas TeX.",
    "Detectar placeholders, tokens sin expandir y campos truncados antes de compilar.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla article en espanol y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Corregir token de slug sin expandir a derecho-penal-especial-mexicano.bib en README y programa.",
    "Corregir campo truncado Tipo/Creditos en authortable. [Supuesto: valor esperado 'Obligatoria / 8']",
    "Mantener acentos y codificacion correcta en .tex y .bib.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver rutas o nombres con caracteres anommalos antes de compilar."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar fuentes institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos faltantes.",
    "Registrar autor, titulo, anio y fuente o URL como minimo.",
    "Registrar fecha de consulta cuando la fuente sea web o variable.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No usar contenido bibliografico heredado de Filosofia del Derecho sin verificacion local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas estables y no contradictorias.",
    "Priorizar identidad institucional, estructura reusable y gates de calidad.",
    "Aplicar deduplicacion semantica sin recortar informacion util.",
    "No transferir redaccion literal entre nodos no equivalentes.",
    "Mantener bandera activa de normalizacion manual para insumos historicamente no parseables (Codex/GPT-Pro).",
    "Propagar correcciones tecnicas de placeholders y campos truncados a nodos laterales similares."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantillas de la materia.",
    "Confirmar si LDE-S2B2 debe fijarse como regla global inmutable.",
    "Confirmar que matricula visible corresponde al estudiante real. [Supuesto actual: ES2611202040]",
    "Verificar si existen consignas activas por actividad que exijan tipo de producto especifico adicional.",
    "Validar que no queden tokens de plantilla sin resolver en archivos markdown y tex."
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
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio sustentado.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y profesionalmente utiles.",
      "Mantener continuidad editorial entre actividades sin perder rigor tecnico."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Uso explicito de evidencia verificable.",
      "Marcado explicito de supuestos.",
      "Cierre con posicion juridica propia."
    ],
    "argumentative_patterns": [
      "Problema -> marco normativo/doctrinal -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Consigna -> trazabilidad de cumplimiento del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliografica",
        "Conclusion juridica transferible",
        "Sincronizacion transversal conservadora"
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
          "justification": "Reduce reutilizacion de salidas no parseables."
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
          "justification": "Exige citas verificables y consistencia con .bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Transferencia permitida solo en reglas editoriales estables, no en contenido tematico."
        },
        {
          "source": "Sincronizacion transversal conservadora",
          "target": "Identidad institucional UnADM",
          "kind": "develops",
          "justification": "Asegura continuidad de estilo y criterios de calidad entre nodos."
        }
      ],
      "evidence": [
        "README destino: pauta editorial e informacion curricular verificable.",
        "Programa analitico destino: cinco ejes de trabajo.",
        "Bib local: base institucional existente.",
        "Plantilla TeX: evidencia de campo truncado y figura docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 19: deduplicacion lossless aplicada sin eliminar reglas utiles previas.",
      "Ciclo 19: se refuerza gate de JSON parseable y normalizacion manual obligatoria.",
      "Ciclo 19: se mantiene politica de no transferir contenido tematico entre nodos no equivalentes.",
      "Ciclo 19: se agregan correcciones tecnicas verificables de placeholders y truncamientos locales."
    ]
  }
}