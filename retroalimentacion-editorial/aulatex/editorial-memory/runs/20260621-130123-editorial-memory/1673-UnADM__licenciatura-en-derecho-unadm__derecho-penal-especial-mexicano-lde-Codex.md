{
  "summary": [
    "Se consolida memoria transversal minima para Derecho penal especial mexicano con identidad UnADM.",
    "Se preservan reglas estables: normalizacion estructurada, cinco ejes editoriales y cierre juridico propio.",
    "Se refuerza control de calidad: JSON parseable, trazabilidad de supuestos y consistencia cita-bibliografia.",
    "Se mantiene estrategia conservadora: no transferir contenido tematico de Filosofia del Derecho sin evidencia local verificable."
  ],
  "identity_rules": [
    "Mantener tono institucional UnADM en todo entregable.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de la materia como entrada canonica.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Agregar al .bib solo fuentes realmente consultables de la actividad.",
    "No trasladar doctrina de otra materia sin justificacion y evidencia local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente cualquier insumo desestructurado antes de reutilizar.",
    "Confirmar estructura minima completa antes de aplicar aguas abajo.",
    "Validar que toda afirmacion tenga respaldo o marca de supuesto.",
    "Validar correspondencia 1:1 entre citas en texto y entradas .bib.",
    "Detectar y corregir placeholders o campos truncados antes de compilar.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Mantener plantilla article en espanol y letterpaper.",
    "Completar metadatos academicos antes de salida final.",
    "Corregir token de slug sin expandir en README y programa analitico.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliografico canonico local.",
    "Completar campo truncado Tipo/Creditos en authortable.",
    "Evitar comandos no estandar sin justificacion editorial."
  ],
  "bibliography_rules": [
    "Usar el .bib local de la materia como fuente unica del entregable.",
    "Conservar fuentes institucionales base: unadmSitioWeb y unadmMallaDerecho2024.",
    "No inventar referencias ni metadatos.",
    "Registrar metadatos minimos: autor, titulo, anio y fuente o URL.",
    "Registrar fecha de consulta cuando la fuente sea web o variable.",
    "Distinguir bibliografia base de bibliografia especifica por actividad."
  ],
  "propagation_hints": [
    "Propagar solo abstracciones editoriales estables entre nodos no equivalentes.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Evitar transferencia de redaccion literal entre materias.",
    "Mantener deduplicacion semantica sin recorte de reglas utiles.",
    "Aplicar propagacion recursiva solo tras validar JSON y estructura."
  ],
  "open_questions": [
    "Confirmar nombre definitivo de figura docente en plantillas.",
    "Confirmar si LDE-S2B2 queda como codigo oficial fijo. [supuesto]",
    "Confirmar consigna concreta de la primera actividad local de la materia.",
    "Confirmar si existe rubrica especifica para profundidad argumentativa.",
    "Verificar que autor y matricula visibles sean datos vigentes."
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
        "Materia destino: Derecho penal especial mexicano.",
        "Semestre 2, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas y doctrina pertinentes.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos solidos y verificables.",
      "Asegurar trazabilidad editorial desde consigna hasta conclusion juridica."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por secciones funcionales.",
      "Cierre con posicion juridica propia.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Consigna -> cumplimiento verificable del producto."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliografica",
        "Conclusion juridica transferible"
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
          "justification": "Solo se transfieren reglas editoriales estables, no contenido tematico."
        }
      ],
      "evidence": [
        "README de destino confirma ubicacion curricular y pauta editorial.",
        "Programa analitico de destino explicita cinco ejes de trabajo.",
        "Archivo .bib local contiene base institucional verificable.",
        "Plantilla .tex exhibe placeholder y campo truncado a corregir."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas sin perder contenido util.",
      "Se preservo gate de JSON parseable como bloqueo fuerte.",
      "Se reforzo marcado de supuestos para datos no visibles.",
      "Se consolidaron reglas transversales de estructura y calidad.",
      "Se abrieron vacios locales del destino sin inventar fuentes."
    ]
  }
}