{
  "summary": [
    "Se consolida memoria lateral de actividad-3 con transferencia reusable desde actividad-1.",
    "Se preserva identidad UnADM y contexto curricular confirmado en README y programa analitico.",
    "Se mantiene normalizacion estructurada obligatoria antes de propagacion recursiva.",
    "Se refuerzan ejes editoriales estables: problema, conceptos/fuentes, analisis propio y conclusion juridica.",
    "Se aplica compresion lossless por union y deduplicacion sin recorte semantico.",
    "Supuesto: la consigna especifica de actividad-3 no esta visible en el contexto entregado."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular actividad-3 a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Marcar como supuesto cualquier dato no visible en la consigna local.",
    "Tratar memorias editoriales heredadas como antecedente provisional, no como fuente academica.",
    "Registrar incidencias de parseo como metadato tecnico, no como evidencia disciplinar."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear la entrega al producto solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Si falta consigna local, usar estructura base y marcar supuestos."
  ],
  "activity_rules": [
    "Heredar solo patrones reutilizables de actividad-1, sin copiar redaccion literal.",
    "No transferir conclusiones especificas ni bibliografia exclusiva de un hermano a otro.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante y evitar entrega solo descriptiva.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir semana, formato o tema de actividad-3 sin evidencia local."
  ],
  "quality_gates": [
    "Bloquear guardado y propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Aplicar no regresion: no eliminar reglas utiles previas.",
    "Validar trazabilidad entre citas en texto y archivo .bib.",
    "Normalizar manualmente memorias con incidencias de parseo antes de reutilizarlas."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar recompilaciones rotas.",
    "No renombrar claves bibliograficas ya usadas en documentos.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM, normativas y jurisprudenciales segun consigna.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib corresponde a Interpretacion juridica (Semana 7) y su uso en actividad-3 debe confirmarse."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Propagar lateralmente reglas institucionales y de calidad como nucleo estable.",
    "Propagar conceptos y relaciones recurrentes, no contenido puntual de una actividad hermana.",
    "Mantener compresion lossless por union-dedupe en cada ciclo.",
    "Conservar bandera de riesgo cuando existan antecedentes de salida no estructurada.",
    "Escalar preguntas abiertas cuando falte consigna textual local."
  ],
  "open_questions": [
    "Confirmar consigna exacta de actividad-3.",
    "Confirmar formato de entrega requerido: reporte, presentacion u otro.",
    "Confirmar rubrica de evaluacion especifica para profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana correspondiente.",
    "Confirmar si actividad-3 reutiliza bibliografia existente o requiere .bib propio.",
    "Confirmar nombre canonico final del archivo .bib de la asignatura."
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
        "Carpeta de asignatura como entrada canonica."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social que activa la asignatura.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto solicitado por la planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion transferible a la practica juridica."
    ],
    "reason_for_being": [
      "Transformar la planeacion semanal en productos academicos claros, fundados y transferibles.",
      "Garantizar evidencia verificable y criterio juridico propio en cada actividad.",
      "Sostener coherencia editorial entre actividades hermanas sin contaminacion de contenido especifico."
    ],
    "style_markers": [
      "Encuadre breve al inicio.",
      "Secciones explicitas y orden logico.",
      "Afirmaciones con respaldo verificable.",
      "Supuestos marcados de forma visible.",
      "Cierre juridico aplicable a practica profesional."
    ],
    "argumentative_patterns": [
      "Problema -> marco conceptual/normativo -> analisis propio -> conclusion juridica.",
      "Afirmacion -> evidencia -> interpretacion -> postura.",
      "Objetivo declarado -> desarrollo coherente -> cierre consistente."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad UnADM",
        "Normalizacion JSON",
        "Integridad academica",
        "Problema juridico",
        "Analisis propio",
        "Conclusion juridica transferible",
        "Bibliografia verificable",
        "Politica de supuestos"
      ],
      "citations": [
        "README.md de la asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib [supuesto de aplicacion condicionada]"
      ],
      "relations": [
        {
          "source": "Identidad UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y criterio propio."
        },
        {
          "source": "Normalizacion JSON",
          "target": "Politica de supuestos",
          "kind": "supports",
          "justification": "La estructura valida facilita distinguir hechos confirmados de supuestos."
        },
        {
          "source": "Problema juridico",
          "target": "Analisis propio",
          "kind": "develops",
          "justification": "El analisis parte de un problema delimitado y evita descripcion vacia."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion juridica transferible",
          "kind": "supports",
          "justification": "La conclusion depende de argumentacion sustentada."
        },
        {
          "source": "Bibliografia verificable",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La verificabilidad de fuentes sostiene la calidad academica."
        }
      ],
      "evidence": [
        "README: identidad UnADM, integridad academica, citas verificables y conclusion juridica propia.",
        "Programa analitico: ejes de trabajo y proposito de transformacion de productos.",
        "Regla persistente: bloquear propagacion sin JSON parseable.",
        "Nota local: bibliografia clean orientada a Semana 7; uso en actividad-3 queda como supuesto."
      ]
    },
    "reinforcement_log": [
      "Ciclo 4: deduplicacion integral de reglas repetidas en destino y origen.",
      "Ciclo 4: refuerzo lateral de estructura argumentativa comun sin copiar contenido especifico.",
      "Ciclo 4: mantenimiento de no regresion y normalizacion previa a propagacion.",
      "Ciclo 4: conservacion de supuestos abiertos por falta de consigna local verificable."
    ]
  }
}