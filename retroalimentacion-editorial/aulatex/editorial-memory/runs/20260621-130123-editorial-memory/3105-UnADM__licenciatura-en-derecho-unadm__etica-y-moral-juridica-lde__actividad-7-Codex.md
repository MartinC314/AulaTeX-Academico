{
  "summary": [
    "Se consolida refuerzo lateral desde Filosofia del Derecho hacia Etica y Moral juridica sin copiar contenidos especificos.",
    "Se preservan reglas utiles previas y se aplica deduplicacion lossless.",
    "Se refuerza el nucleo editorial comun: problema, conceptos, evidencia, analisis propio y conclusion juridica.",
    "Se mantiene validacion JSON estricta y esquema completo antes de propagacion recursiva.",
    "Se integra control explicito de supuestos para datos no visibles en la consigna."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear la actividad a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como [Supuesto] cualquier dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar trazabilidad de origen y ciclo en cada propagacion."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Integrar evidencia verificable en el desarrollo.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Alinear el producto final a la consigna real de Actividad 7."
  ],
  "activity_rules": [
    "Incluir postura argumentada del estudiante y evitar solo resumen.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar mezclar fuentes de otras semanas o materias sin justificacion.",
    "Confirmar tipo de entrega exigido por la actividad antes de redactar.",
    "Mantener enfoque etico-juridico aplicado al ejercicio profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar esquema requerido completo antes de guardar memoria.",
    "No eliminar reglas utiles previas; solo fusionar y deduplicar.",
    "Confirmar que toda afirmacion tenga respaldo o marca [Supuesto].",
    "Validar consistencia entre citas en texto y claves del .bib.",
    "Permitir propagacion recursiva solo si pasa todas las compuertas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar rupturas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Corregir rutas o nombres con caracteres anomalos antes de compilar."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales UnADM y materiales juridicos verificables.",
    "Registrar fuentes especificas de Actividad 7 en etica-y-moral-juridica.bib.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Gestionar duplicados por deduplicacion controlada sin romper citas existentes. [Supuesto]"
  ],
  "propagation_hints": [
    "Propagar lateral y recursivo solo despues de validar JSON y esquema.",
    "Transferir patrones reutilizables, no redaccion ni conclusiones de otra materia.",
    "Reforzar identidad, estructura, calidad y trazabilidad en nodos hermanos.",
    "Si falta consigna local, propagar estructura base y abrir preguntas.",
    "Mantener historial de refuerzos por ciclo para prevenir regresiones."
  ],
  "open_questions": [
    "Confirmar consigna exacta y tipo de producto solicitado en Actividad 7.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad.",
    "Confirmar politica local para aliases de claves BibTeX duplicadas. [Supuesto]",
    "Confirmar si los duplicados actuales del .bib se conservan por retrocompatibilidad. [Supuesto]",
    "Confirmar cierre correcto de entradas truncadas en etica-y-moral-juridica.bib. [Supuesto]"
  ],
  "editorial_dna": {
    "identity": {
      "tone": [
        "Formal academico.",
        "Claro y juridicamente preciso.",
        "Argumentativo con criterio propio.",
        "Sobrio y verificable."
      ],
      "institutional": [
        "Alineacion explicita con UnADM.",
        "Integridad academica con citas verificables.",
        "Carpeta de asignatura como entrada canonica.",
        "Validacion estructural antes de propagacion."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo pertinentes.",
      "Evidencia verificable.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir la planeacion semanal en productos academicos trazables y utiles para practica juridica.",
      "Asegurar coherencia entre identidad institucional, argumentacion y evidencia."
    ],
    "style_markers": [
      "Encuadre breve inicial.",
      "Secciones claras y trazables.",
      "Citas explicitas.",
      "Supuestos etiquetados.",
      "Cierre con utilidad profesional."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Presentar marco conceptual y normativo.",
      "Contrastar posturas con evidencia.",
      "Fijar posicion propia.",
      "Concluir con aplicacion juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Etica",
        "Moral",
        "Practica profesional"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "programa-analitico-etica-y-moral-juridica.md",
        "etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige verificabilidad y trazabilidad."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de una delimitacion clara del problema."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion debe derivar del razonamiento sustentado."
        },
        {
          "source": "Etica",
          "target": "Moral",
          "kind": "contrasts",
          "justification": "La distincion conceptual es recurrente en la materia."
        },
        {
          "source": "Moral",
          "target": "Practica profesional",
          "kind": "depends_on",
          "justification": "Los criterios morales impactan la actuacion juridica."
        }
      ],
      "evidence": [
        "README de la asignatura: identidad, ubicacion curricular y pauta editorial.",
        "Programa analitico: proposito y ejes de trabajo.",
        "Bibliografia local: base de fuentes y necesidad de control de duplicados."
      ]
    },
    "reinforcement_log": [
      "Ciclo 7: refuerzo lateral aplicado con transferencia de patrones reutilizables.",
      "Ciclo 7: deduplicacion lossless ejecutada sin eliminar reglas vigentes.",
      "Ciclo 7: se mantiene bloqueo por falta de estructura parseable en futuros saltos."
    ]
  }
}