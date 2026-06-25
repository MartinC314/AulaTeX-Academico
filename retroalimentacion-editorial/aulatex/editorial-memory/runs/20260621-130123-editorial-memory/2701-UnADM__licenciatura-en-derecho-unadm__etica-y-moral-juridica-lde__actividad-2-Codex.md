{
  "summary": [
    "Se refuerza memoria lateral de Actividad 2 con patrones reutilizables de Actividad 1.",
    "Se preserva identidad UnADM y contexto curricular compartido.",
    "Se consolida estructura editorial comun: problema, conceptos, evidencia, analisis propio y cierre juridico.",
    "Se mantiene normalizacion obligatoria antes de propagacion recursiva.",
    "Se integra evidencia local verificable de README, programa analitico y .bib del destino.",
    "Supuesto: falta consigna textual de Actividad 2; se conserva estructura base sin inventar producto especifico."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Vincular toda entrega a Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como punto de entrada canonico.",
    "Conservar enfoque de la asignatura Etica y Moral juridica en el nodo destino.",
    "Marcar como supuesto cualquier dato no visible en la consigna.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Registrar origen y destino en propagaciones laterales."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Entregar memoria en JSON valido y parseable con esquema completo."
  ],
  "activity_rules": [
    "Estructurar cada actividad en problema, conceptos, fuentes, analisis propio y conclusion juridica.",
    "Incluir postura argumentada del estudiante, no solo resumen descriptivo.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Evitar asumir fuentes de semanas distintas sin validacion local.",
    "Mantener claridad, fundamento juridico, evidencia y transferencia profesional."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Aplicar compresion lossless por union y deduplicacion; no recortar contenido valido."
  ],
  "latex_rules": [
    "Usar UTF-8 y acentos correctos en .tex y .bib.",
    "Mantener claves BibTeX estables para evitar compilaciones rotas.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Corregir caracteres anomalos en rutas y nombres de archivo.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Conservar entradas canonicas: reporte-etica-y-moral-juridica.tex y presentacion-etica-y-moral-juridica.tex."
  ],
  "bibliography_rules": [
    "No inventar fuentes ni metadatos bibliograficos.",
    "Usar solo obras realmente consultables y verificables.",
    "Priorizar fuentes institucionales UnADM cuando apliquen al encuadre curricular.",
    "Registrar fuentes especificas de la actividad en etica-y-moral-juridica.bib.",
    "Conservar metadatos minimos: autor o editor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: existen claves duplicadas para la misma obra; mantener trazabilidad mientras se define politica de alias."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir a nodos laterales solo patrones generales reutilizables.",
    "No transferir redaccion literal ni conclusiones especificas entre actividades hermanas.",
    "Reutilizar reglas institucionales de calidad sin perder especificidad local.",
    "Evitar regresiones: no eliminar reglas utiles previas; solo deduplicar y reforzar."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 2 y producto final requerido.",
    "Confirmar rubrica de evaluacion especifica para calibrar profundidad argumentativa.",
    "Definir politica editorial final para alias y fusion de claves BibTeX duplicadas.",
    "Confirmar si se debe mantener doble clave legacy en .bib o migrar a clave canonica unica."
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
        "Normalizacion estructurada obligatoria antes de propagar."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura destino: Etica y Moral juridica.",
        "Relacion lateral-transversal con Filosofia del Derecho."
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
      "Transformar planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Asegurar coherencia entre estructura argumentativa, citas y cierre profesional.",
      "Preservar memoria editorial reutilizable sin perdida semantica."
    ],
    "style_markers": [
      "Frases cortas y accionables.",
      "Supuestos explicitos cuando falte evidencia.",
      "Trazabilidad de decisiones y fuentes.",
      "Cierre con implicacion juridica practica."
    ],
    "argumentative_patterns": [
      "Delimitar problema y objetivo al inicio.",
      "Desarrollar conceptos y marco normativo con respaldo verificable.",
      "Contrastar fuentes y sostener postura propia.",
      "Concluir con criterio juridico transferible."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de actividad",
        "Integridad academica",
        "Postura argumentada del estudiante",
        "Conclusion juridica transferible",
        "Normalizacion estructurada",
        "Deduplicacion bibliografica con trazabilidad"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/programa-analitico-etica-y-moral-juridica.md",
        "UnADM/licenciatura-en-derecho-unadm/etica-y-moral-juridica-lde/etica-y-moral-juridica.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Ejes editoriales de actividad",
          "kind": "supports",
          "justification": "El marco institucional fija tono, formato y criterio academico."
        },
        {
          "source": "Ejes editoriales de actividad",
          "target": "Conclusion juridica transferible",
          "kind": "develops",
          "justification": "La secuencia problema-conceptos-evidencia-analisis conduce a cierre profesional."
        },
        {
          "source": "Integridad academica",
          "target": "Deduplicacion bibliografica con trazabilidad",
          "kind": "depends_on",
          "justification": "La calidad de citacion exige control de claves y metadatos consistentes."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva",
          "kind": "supports",
          "justification": "Sin JSON parseable no hay transferencia segura entre nodos."
        }
      ],
      "evidence": [
        "README local define identidad UnADM y ubicacion curricular.",
        "Programa analitico local define proposito y ejes de trabajo.",
        ".bib local muestra duplicados verificables por metadatos equivalentes.",
        "Regla persistente: bloquear propagacion cuando no haya JSON parseable."
      ]
    },
    "reinforcement_log": [
      "Ciclo 16: se transfieren patrones reutilizables desde Filosofia del Derecho Actividad 1 a Etica y Moral juridica Actividad 2.",
      "Ciclo 16: se mantiene deduplicacion lossless sin eliminar reglas utiles previas.",
      "Ciclo 16: se refuerzan reglas de calidad, estructura y trazabilidad para propagacion lateral recursiva."
    ]
  }
}