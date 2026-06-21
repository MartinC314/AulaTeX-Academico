{
  "summary": [
    "Se consolida refuerzo lateral para Actividad 4 con deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales comunes.",
    "Se mantiene regla de normalizacion estructurada previa a toda propagacion.",
    "Se refuerza validacion JSON estricta por antecedentes no parseables.",
    "Se transfieren solo patrones reutilizables; no se copian conclusiones ni redaccion de Actividad 1.",
    "Supuesto: la consigna especifica de Actividad 4 no esta visible y debe confirmarse."
  ],
  "identity_rules": [
    "Mantener tono formal academico con precision juridica.",
    "Alinear contenido con UnADM, Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Vincular contexto curricular a semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato pedido en la planeacion semanal.",
    "Separar hechos, conceptos, argumentos y postura personal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Integrar los cinco ejes: problema, conceptos, producto, analisis propio y conclusion.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Incluir postura argumentada del estudiante; evitar texto solo descriptivo.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin confirmar pertinencia para Actividad 4.",
    "Supuesto: confirmar si la consigna de Actividad 4 exige reporte, presentacion u otro formato."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de aplicar aguas abajo.",
    "Normalizar respuestas no estructuradas antes de reutilizarlas.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar correspondencia entre citas en texto y archivo .bib.",
    "Validar que el producto final coincida con la consigna local de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en espanol en .tex y .bib.",
    "Citar en .tex solo claves existentes en .bib.",
    "Mantener claves BibTeX estables; no renombrar claves activas sin migracion.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Verificar nombres reales de archivos en README antes de compilar.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: archivo .bib canonico esperado es filosofia-del-derecho.bib por slug visible."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar en .bib solo fuentes realmente consultables.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, ano y fuente/editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Usar filosofia-del-derecho-clean.bib solo si coincide con la consigna de Actividad 4.",
    "Supuesto: filosofia-del-derecho-clean.bib parece orientado a Semana 7; verificar aplicabilidad."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Reutilizar reglas institucionales sin perder especificidad local.",
    "Evitar regresiones: conservar reglas utiles previas ya verificadas.",
    "Aplicar union-dedupe para compresion lossless entre nodos hermanos.",
    "Transferir patrones, no contenido literal ni conclusiones especificas.",
    "Mantener bandera de normalizacion manual para ciclos con salidas heredadas defectuosas."
  ],
  "open_questions": [
    "Confirmar consigna textual exacta de Actividad 4.",
    "Confirmar formato requerido: reporte, presentacion o producto visual.",
    "Confirmar rubrica y criterios de evaluacion especificos.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico definitivo del .bib en repositorio.",
    "Confirmar si Actividad 4 reutiliza bibliografia existente o requiere .bib incremental."
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
      "Problema juridico o social activa el desarrollo.",
      "Conceptos y fuentes sostienen el argumento.",
      "Analisis propio evita resumen pasivo.",
      "Cierre juridico debe ser transferible.",
      "Estructura y verificabilidad gobiernan la calidad."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos solidos.",
      "Garantizar coherencia entre institucion, metodo y evidencia.",
      "Permitir propagacion segura entre actividades hermanas."
    ],
    "style_markers": [
      "Objetivo puntual al inicio.",
      "Secciones funcionales con logica juridica.",
      "Cita explicita por afirmacion sustantiva.",
      "Supuestos marcados cuando falten datos.",
      "Conclusion juridica propia y aplicable."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Delimitar conceptos y marco normativo.",
      "Contrastar evidencia y doctrina.",
      "Fijar postura razonada.",
      "Cerrar con implicacion juridica practica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Ejes editoriales de Filosofia del Derecho",
        "Normalizacion estructurada",
        "Validacion JSON estricta",
        "Integridad academica y verificabilidad",
        "Relacion problema-evidencia-conclusion"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta institucional exige citas verificables y rigor formal."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Relacion problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el flujo argumentativo completo."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "Sin estructura valida no hay propagacion confiable."
        },
        {
          "source": "Integridad academica y verificabilidad",
          "target": "Relacion problema-evidencia-conclusion",
          "kind": "supports",
          "justification": "La conclusion juridica requiere evidencia trazable."
        }
      ],
      "evidence": [
        "README define identidad UnADM, entrada canonica y pauta editorial.",
        "Programa analitico define proposito y cinco ejes de trabajo.",
        "Antecedentes de salidas no parseables justifican gate JSON estricto.",
        "Tokens Slug sin resolver en archivos base exigen verificacion previa."
      ]
    },
    "reinforcement_log": [
      "C14: deduplicacion de reglas repetidas con conservacion total de contenido util.",
      "C14: refuerzo lateral de patrones de estructura y calidad desde nodo hermano.",
      "C14: mantenimiento de regla critica de bloqueo por JSON no parseable.",
      "C14: se evita transferencia de conclusiones o bibliografia exclusiva de Actividad 1.",
      "C14: se mantienen supuestos explicitos donde falta consigna local."
    ]
  }
}