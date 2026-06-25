{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica con transferencia de patrones reutilizables.",
    "Se preserva identidad UnADM y contexto curricular verificable del nodo destino.",
    "Se mantiene normalizacion estructurada obligatoria y bloqueo por JSON no parseable.",
    "Se refuerzan ejes editoriales comunes: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se evita copiar conclusiones o bibliografia exclusiva del origen; solo se transfieren reglas generales.",
    "Se mantiene compresion lossless por union y deduplicacion."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Citar malla-curricular-derecho-unadm.pdf como sustento de ubicacion curricular."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Incluir evidencia verificable dentro del desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el producto final a la consigna de Actividad 7 y a la planeacion semanal."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de semanas o materias distintas sin validacion local.",
    "Confirmar tipo de producto solicitado antes de redactar version final."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "Confirmar no eliminacion de reglas utiles previas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca [Supuesto].",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Propagar recursivamente solo despues de pasar compuertas de calidad."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas por renombre arbitrario.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir caracteres anomalos en rutas o nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos bibliograficos.",
    "Conservar metadatos minimos: autor o editor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Deduplicar entradas equivalentes sin perder trazabilidad de claves usadas."
  ],
  "propagation_hints": [
    "Propagar lateral y recursivamente solo reglas generales verificadas.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Aplicar analogia controlada: conservar estructura y calidad; adaptar contenido al tema local.",
    "Si falta consigna local, mantener plantilla base y abrir preguntas en lugar de inventar.",
    "Registrar ciclos con incidencias de parseo para auditoria editorial."
  ],
  "open_questions": [
    "Confirmar consigna exacta y tipo de producto requerido en Actividad 7.",
    "Confirmar rubrica de evaluacion para ajustar profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana para Actividad 7.",
    "Definir politica local de alias BibTeX para duplicados existentes en etica-y-moral-juridica.bib. [Supuesto]",
    "Confirmar si se normalizaran entradas truncadas del .bib antes de nuevas propagaciones. [Supuesto]"
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
        "Carpeta de asignatura como entrada canonica.",
        "Validacion estructural previa a propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Actividad destino: Actividad 7."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo o doctrinal.",
      "Evidencia verificable.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos trazables y utiles para la practica juridica.",
      "Garantizar coherencia entre identidad institucional, estructura argumentativa y soporte bibliografico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones claras y trazables.",
      "Supuestos etiquetados.",
      "Citas explicitas y verificables.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Definir objetivo.",
      "Exponer conceptos y marco.",
      "Contrastar posturas con evidencia.",
      "Fijar posicion propia.",
      "Concluir con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco normativo o doctrinal",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Normalizacion JSON",
        "Trazabilidad bibliografica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de etica-y-moral-juridica-lde",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El razonamiento parte del problema para construir postura."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion valida deriva de analisis y evidencia."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Propagacion recursiva",
          "kind": "depends_on",
          "justification": "Sin salida parseable no se autoriza transferencia de memoria."
        },
        {
          "source": "Trazabilidad bibliografica",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La consistencia entre citas y .bib evita afirmaciones sin respaldo."
        }
      ],
      "evidence": [
        "README local confirma identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico local define proposito y ejes de trabajo reutilizables.",
        "Memoria origen aporta reglas generales de estructura, calidad y normalizacion.",
        "Regla transversal vigente: no inventar fuentes y marcar supuestos cuando falten datos."
      ]
    },
    "reinforcement_log": [
      "Ciclo 15: se incorpora transferencia lateral controlada de patrones editoriales generales.",
      "Ciclo 15: se deduplican reglas equivalentes y se conserva cobertura funcional completa.",
      "Ciclo 15: se mantiene bloqueo por JSON no parseable como compuerta dura.",
      "Ciclo 15: se refuerza separacion entre reglas transferibles y contenido especifico no transferible."
    ]
  }
}