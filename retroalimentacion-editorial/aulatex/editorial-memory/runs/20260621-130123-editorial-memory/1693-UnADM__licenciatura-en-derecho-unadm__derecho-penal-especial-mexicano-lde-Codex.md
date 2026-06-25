{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes editoriales y normalizacion estructurada.",
    "Se refuerza control de calidad parseable, trazabilidad de supuestos y consistencia cita-bibliografia.",
    "Se evita transferir contenido tematico de Filosofia del Derecho al destino penal sin evidencia local.",
    "Se mantiene compresion lossless por union-dedupe sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de materia como entrada canonica editorial.",
    "Marcar como supuesto todo dato no visible en consigna o fuente local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Vincular el problema con normas, conceptos o doctrina penal aplicable.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Agregar fuentes especificas de la actividad al .bib local antes de version final.",
    "No trasladar contenido disciplinar del origen sin evidencia verificable en el destino."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente todo insumo desestructurado antes de reutilizar.",
    "Validar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Exigir correspondencia 1:1 entre citas en texto y entradas del .bib.",
    "Verificar coherencia entre README, programa analitico y plantillas TeX.",
    "Detectar y corregir placeholders o campos truncados antes de compilar.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla article en español y letterpaper.",
    "Completar metadatos del documento antes de salida final.",
    "Corregir placeholders de slug sin resolver en README y programa analitico.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliografico canonico local.",
    "Corregir nombres corruptos de archivos mostrados en README.",
    "Completar campo truncado Tipo/Creditos en authortable [supuesto: 'Obligatoria / 8'].",
    "Evitar macros, rutas o tokens de plantilla sin expandir."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar entradas institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Registrar metadatos minimos: autor, titulo, año y fuente/editorial o URL.",
    "Registrar fecha de consulta cuando aplique a recursos web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas editoriales estables y no tematicas.",
    "Priorizar identidad, estructura reusable y quality gates sobre contenido de materia origen.",
    "Mantener bandera activa de normalizacion manual para salidas heredadas no parseables.",
    "Aplicar deduplicacion semantica sin recorte de reglas utiles.",
    "Propagar correcciones de placeholders y campos truncados a nodos laterales similares.",
    "Si falta contexto local, mantener cerebro minimo y abrir vacios como preguntas."
  ],
  "open_questions": [
    "Confirmar nombre real de figura docente en plantillas del destino.",
    "Confirmar si coursecode LDE-S2B2 queda fijo como regla global de materia.",
    "Confirmar cierre exacto del campo truncado Tipo/Creditos en .tex.",
    "Verificar correccion final de rutas con caracteres anómalos en README.",
    "Definir primeras fuentes penales especificas por actividad para poblar .bib local."
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
      "Problema juridico + fundamento normativo + analisis propio + conclusion transferible.",
      "Calidad estructural y bibliografica como condicion de validez editorial.",
      "Transferencia transversal conservadora entre nodos no equivalentes."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos consistentes, verificables y utiles para la practica juridica.",
      "Preservar continuidad editorial institucional sin contaminar disciplina destino con contenido no verificado."
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
          "justification": "Evita reutilizar salidas no parseables."
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
          "justification": "Exige citas verificables y .bib consistente."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Solo se transfieren abstracciones editoriales estables."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Sincronizacion transversal",
          "kind": "develops",
          "justification": "Permite continuidad estilistica entre materias."
        }
      ],
      "evidence": [
        "README destino valida ubicacion curricular y pauta editorial.",
        "Programa analitico destino define cinco ejes de trabajo.",
        "Bib local contiene base institucional verificable.",
        "Plantilla .tex muestra campo truncado y figura docente pendiente."
      ]
    },
    "reinforcement_log": [
      "Ciclo 6: se deduplican reglas repetidas y se preserva cobertura funcional completa.",
      "Ciclo 6: se refuerza gate JSON parseable como bloqueo duro de propagacion.",
      "Ciclo 6: se mantiene estrategia conservadora de no transferir contenido tematico entre disciplinas.",
      "Ciclo 6: se formaliza correccion de placeholders y truncamientos como deuda tecnica editorial prioritaria."
    ]
  }
}