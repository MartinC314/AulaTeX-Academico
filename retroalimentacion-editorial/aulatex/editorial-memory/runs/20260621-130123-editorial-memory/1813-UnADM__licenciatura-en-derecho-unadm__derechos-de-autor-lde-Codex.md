{
  "summary": [
    "Se consolida memoria transversal minima para Derechos de autor con identidad UnADM.",
    "Se preserva normalizacion estructurada obligatoria antes de cualquier propagacion.",
    "Se refuerzan ejes estables: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene compresion lossless por union y deduplicacion sin recorte.",
    "Se marca como provisional toda herencia no verificada localmente (Codex, GPT-Pro)."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, portada y metadatos.",
    "Alinear entregables con Licenciatura en Derecho, semestre 5, bloque 1, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Usar malla-curricular-derecho-unadm.pdf como soporte curricular institucional."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear formato final al producto solicitado por la planeacion semanal.",
    "Corregir tokens de plantilla sin resolver en README y programa analitico.",
    "Corregir nombres de archivo corruptos antes de publicar."
  ],
  "activity_rules": [
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante, no solo resumen.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar fuentes especificas por actividad al .bib local.",
    "No asumir que fuentes de otras semanas aplican automaticamente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Auditar README y programa analitico por marcadores de plantilla y caracteres anómalos.",
    "Marcar y retener como provisional cualquier herencia externa no verificada."
  ],
  "latex_rules": [
    "Mantener codificacion y acentos correctos en español en .tex y .bib.",
    "Declarar metadatos antes de \\input{template} si la plantilla lo exige.",
    "Mover paquetes al preambulo efectivo y evitar cargas truncadas.",
    "Nunca dejar \\usepackage sin argumento.",
    "Compilar sin errores criticos, referencias rotas ni comandos incompletos.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "bibliography_rules": [
    "No inventar referencias; usar solo fuentes consultables y verificables.",
    "Priorizar fuentes institucionales UnADM y material juridico pertinente.",
    "Conservar metadatos minimos: autor, titulo, año y fuente o URL.",
    "Incluir fecha de consulta en fuentes web.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Usar derechos-de-autor.bib como repositorio canonico local."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validacion de JSON y estructura.",
    "Transferir a nodos laterales solo abstracciones editoriales estables.",
    "Evitar transferencia de redaccion literal entre materias no equivalentes.",
    "Mantener sin regresion reglas utiles previamente consolidadas.",
    "Conservar bandera de normalizacion manual para herencia de ciclos tempranos."
  ],
  "open_questions": [
    "Confirmar oficialmente si LDE-S5B1 es clave curricular canonica. [supuesto]",
    "Definir nombre de figura docente para eliminar marcador pendiente.",
    "Confirmar si Roma Norte, Ciudad de Mexico debe permanecer fijo en plantilla. [supuesto]",
    "Validar orden definitivo entre \\input{template} y paquetes en la plantilla local.",
    "Confirmar retiro o continuidad de herencia provisional Codex/GPT-Pro tras validacion local."
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
        "Semestre 5, bloque 1, obligatoria, 8 creditos.",
        "Asignatura: Derechos de autor."
      ]
    },
    "essence": [
      "Problema juridico delimitado.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica aplicable."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos trazables.",
      "Sostener coherencia entre identidad institucional, estructura y evidencia.",
      "Permitir propagacion segura de reglas estables en la suite."
    ],
    "style_markers": [
      "Declarar supuestos de forma explicita.",
      "Mantener secciones funcionales y trazables.",
      "Evitar ambiguedad en fuentes y metadatos.",
      "Cerrar con utilidad juridica profesional."
    ],
    "argumentative_patterns": [
      "Problema inicial breve.",
      "Marco conceptual y normativo.",
      "Analisis con postura propia.",
      "Cierre con implicacion practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Evidencia verificable",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Integridad bibliografica"
      ],
      "citations": [
        "unadmSitioWeb",
        "unadmMallaDerecho2024"
      ],
      "relations": [
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion segura",
          "kind": "supports",
          "justification": "Evita heredar salidas no parseables."
        },
        {
          "source": "Evidencia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "Toda afirmacion requiere respaldo trazable."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La postura argumentada habilita cierre profesional util."
        },
        {
          "source": "Identidad institucional UnADM",
          "target": "Coherencia editorial de materia",
          "kind": "depends_on",
          "justification": "Portada, metadatos y tono deben alinearse."
        }
      ],
      "evidence": [
        "README de Derechos de autor fija identidad y ubicacion curricular.",
        "Programa analitico define ejes problema-conceptos-producto-analisis-cierre.",
        "derechos-de-autor.bib contiene fuentes institucionales base.",
        "reporte-derechos-de-autor.tex evidencia necesidad de saneamiento de preambulo."
      ]
    },
    "reinforcement_log": [
      "Se conserva regla de bloqueo por JSON no parseable.",
      "Se integra patron argumentativo estable desde nodo transversal sin literalidad.",
      "Se refuerza control de supuestos y herencia provisional.",
      "Se añade gate tecnico LaTeX por \\usepackage incompleto detectado localmente.",
      "Se mantiene estrategia conservadora: solo abstracciones estables transferidas."
    ]
  }
}