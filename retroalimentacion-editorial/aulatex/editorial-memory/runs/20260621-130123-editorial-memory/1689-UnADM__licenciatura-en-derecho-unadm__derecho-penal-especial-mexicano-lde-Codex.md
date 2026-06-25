{
  "summary": [
    "Se consolida sincronizacion transversal conservadora entre nodos no equivalentes.",
    "Se preservan reglas estables: identidad UnADM, cinco ejes, normalizacion estructurada y cierre juridico propio.",
    "Se mantiene transferencia por abstracciones editoriales; no se migra contenido tematico de Filosofia del Derecho.",
    "Se refuerza control tecnico local: placeholders de slug y campo truncado en TeX deben corregirse antes de cierre.",
    "Se aplica compresion lossless por union y deduplicacion sin regresion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono, formato y trazabilidad.",
    "Usar contexto curricular verificado del destino: semestre 2, bloque 2, obligatoria, 8 creditos.",
    "Tomar la carpeta de la materia como entrada canonica.",
    "Marcar como [supuesto] todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar autoria real del estudiante y validar matricula y figura docente antes de entrega."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Estructurar por secciones: conceptos clave, marco normativo/doctrinal, analisis propio y cierre.",
    "Alinear el formato final al producto pedido por la planeacion semanal.",
    "Sincronizar README, programa analitico, .tex y .bib por actividad.",
    "Mantener consistencia de nombres de archivo y slug canonico de la materia."
  ],
  "activity_rules": [
    "Mapear cada actividad a un problema penal concreto.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Agregar al .bib solo fuentes especificas de la actividad con datos verificables.",
    "No trasladar doctrina o casos de Filosofia del Derecho sin evidencia local pertinente."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Normalizar manualmente todo insumo desestructurado antes de reutilizar.",
    "Confirmar estructura minima completa antes de aplicar aguas abajo.",
    "Exigir respaldo o marca [supuesto] en toda afirmacion sensible.",
    "Validar correspondencia 1:1 entre citas en texto y entradas del .bib.",
    "Detectar y corregir placeholders/tokens sin resolver antes de compilar.",
    "Compilar LaTeX sin errores criticos ni referencias rotas."
  ],
  "latex_rules": [
    "Conservar plantilla article en espanol y letterpaper.",
    "Completar metadatos documentales antes de salida final.",
    "Corregir token de slug sin resolver en README y programa analitico.",
    "Usar derecho-penal-especial-mexicano.bib como archivo bibliografico canonico local.",
    "Corregir campo truncado Tipo/Creditos en authortable.",
    "Evitar macros, rutas o expresiones de plantilla sin expansion."
  ],
  "bibliography_rules": [
    "Usar el .bib local como fuente unica de referencias del entregable.",
    "Conservar fuentes base institucionales verificables ya presentes.",
    "No inventar referencias ni completar metadatos por inferencia.",
    "Registrar fecha de consulta en recursos web variables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Mantener claves BibTeX estables para evitar rupturas de compilacion."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas validadas y no contradictorias.",
    "Priorizar identidad, estructura reusable, gates de calidad y grafo conceptual.",
    "Transferir solo abstracciones estables entre materias no equivalentes.",
    "Evitar redaccion literal y evitar transferencia tematica sin insumo local.",
    "Mantener bandera activa de normalizacion manual para herencias no estructuradas.",
    "Propagar a laterales correcciones de placeholders y campos truncados cuando aparezcan."
  ],
  "open_questions": [
    "[supuesto] Confirmar si LDE-S2B2 se fija como codigo oficial global de la materia.",
    "Confirmar nombre real de figura docente para plantillas.",
    "Confirmar si autor y matricula visibles siguen vigentes para nuevas entregas.",
    "Confirmar si cada actividad exige reporte, presentacion u otro producto.",
    "Verificar que no queden rutas o nombres con caracteres anómalos en archivos locales."
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
      "Marco conceptual y normativo pertinente.",
      "Producto alineado a consigna.",
      "Analisis propio con postura.",
      "Cierre juridico transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en entregables juridicos claros, verificables y utiles para practica profesional.",
      "Sostener continuidad editorial institucional sin perder especificidad local por actividad."
    ],
    "style_markers": [
      "Apertura con problema y objetivo.",
      "Desarrollo por bloques funcionales.",
      "Citas verificables y consistentes con .bib.",
      "Marcado explicito de [supuesto].",
      "Conclusiones con aplicabilidad juridica."
    ],
    "argumentative_patterns": [
      "Problema -> norma/doctrina -> analisis -> conclusion.",
      "Afirmacion -> evidencia -> inferencia juridica.",
      "Consigna -> criterios de cumplimiento verificable."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Cinco ejes editoriales",
        "Integridad bibliografica",
        "Conclusion juridica transferible",
        "Sincronizacion documental README-programa-.tex-.bib"
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
          "justification": "Requiere citas verificables y correspondencia 1:1 con .bib."
        },
        {
          "source": "Filosofia del Derecho",
          "target": "Derecho penal especial mexicano",
          "kind": "contrasts",
          "justification": "Transferencia transversal limitada a reglas editoriales estables."
        },
        {
          "source": "Sincronizacion documental README-programa-.tex-.bib",
          "target": "Consistencia operativa del nodo",
          "kind": "supports",
          "justification": "Reduce errores de plantilla, slug y compilacion."
        }
      ],
      "evidence": [
        "README local confirma contexto curricular y pauta editorial.",
        "Programa analitico local explicita cinco ejes de trabajo.",
        "Bib local contiene base institucional verificable.",
        "Plantilla TeX local muestra campo truncado pendiente de correccion.",
        "Se detectan tokens de slug sin resolver en documentos locales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 5: se preserva memoria previa sin recortes y se deduplica semanticamente.",
      "Ciclo 5: se refuerzan gates de parseo JSON, supuestos y consistencia cita-bibliografia.",
      "Ciclo 5: se mantiene estrategia conservadora de no migrar contenido disciplinar entre nodos no equivalentes.",
      "Ciclo 5: se agrega refuerzo operativo sobre correccion de placeholders y campo truncado."
    ]
  }
}