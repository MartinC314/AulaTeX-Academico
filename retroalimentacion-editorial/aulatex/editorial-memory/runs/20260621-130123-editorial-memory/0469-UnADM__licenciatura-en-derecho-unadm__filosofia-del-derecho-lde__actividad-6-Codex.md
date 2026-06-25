{
  "summary": [
    "Se consolida refuerzo lateral desde Actividad 1 hacia Actividad 6 con union y deduplicacion sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada: Licenciatura en Derecho, semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Se mantienen ejes editoriales estables: problema, conceptos o normas, producto, analisis propio y conclusion juridica transferible.",
    "Se mantiene regla critica: no propagar salida no estructurada; normalizar antes de reutilizar.",
    "Se refuerza control de supuestos por falta de consigna local completa de Actividad 6."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear contenido a Filosofia del Derecho de la Licenciatura en Derecho.",
    "Reconocer y citar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar la carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Conservar regla de no regresion en consolidaciones editoriales."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con encuadre breve del problema juridico o social.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Definir objetivo puntual antes del desarrollo.",
    "Alinear el producto al formato pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica profesional."
  ],
  "activity_rules": [
    "Adaptar redaccion al objetivo especifico de Actividad 6 sin romper ejes base.",
    "Sustentar afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No trasladar conclusiones especificas de actividad hermana.",
    "Supuesto: si la consigna aborda interpretacion juridica, vincular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de propagar.",
    "Revisar y normalizar respuestas no estructuradas antes de reutilizar.",
    "Confirmar que cada afirmacion relevante tenga fuente o marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "No eliminar reglas utiles previas durante consolidacion.",
    "Separar reglas confirmadas de supuestos editoriales."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "Mantener claves BibTeX estables; no renombrar claves ya citadas.",
    "Comprobar que toda clave citada exista en el .bib activo.",
    "Compilar sin errores criticos y sin referencias rotas.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico antes de fijar nombres canonicos.",
    "Corregir caracteres anomalos en rutas o nombres de archivo antes de compilar."
  ],
  "bibliography_rules": [
    "No inventar fuentes; usar solo obras consultables.",
    "Priorizar fuentes institucionales UnADM y fuentes juridicas verificables.",
    "Registrar fuentes especificas de la actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "No asumir que filosofia-del-derecho-clean.bib aplica automaticamente a Actividad 6.",
    "Marcar como supuesto cualquier dato bibliografico incompleto hasta verificarlo."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo tras validar JSON y estructura.",
    "Transferir solo patrones reutilizables; no copiar redaccion literal ni conclusiones puntuales.",
    "Mantener deduplicacion lossless por union de reglas equivalentes.",
    "Conservar advertencia historica sobre salidas no parseables en ciclos previos.",
    "Propagar identidad curricular y compuertas de calidad a nodos hermanos.",
    "Cuando falten datos locales, propagar plantilla base y preguntas abiertas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 6; confirmar producto exacto solicitado.",
    "Confirmar rubrica de evaluacion especifica de Actividad 6.",
    "Confirmar si Actividad 6 exige reporte, presentacion o ambos.",
    "Confirmar nombre canonico final del .bib por token Slug sin resolver y coexistencia de dos archivos .bib.",
    "Confirmar si las fuentes de interpretacion juridica de clean.bib son obligatorias o solo opcionales en Actividad 6.",
    "Confirmar si se exige formato adicional de citacion juridica ademas de BibTeX."
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
        "Asignatura: Filosofia del Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto segun planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos con fundamento juridico y utilidad profesional.",
      "Asegurar trazabilidad entre problema, fuentes, analisis y conclusion.",
      "Preservar consistencia editorial institucional entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Postura propia diferenciada de la sintesis.",
      "Cierre con criterio juridico aplicable.",
      "Marcado explicito de supuestos."
    ],
    "argumentative_patterns": [
      "Delimitar problema.",
      "Construir marco conceptual-normativo.",
      "Contrastar fuentes verificables.",
      "Sostener postura propia argumentada.",
      "Derivar conclusion desde el analisis."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Marco conceptual-normativo",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica [supuesto condicionado a consigna]",
        "Argumentacion juridica [supuesto condicionado a consigna]"
      ],
      "citations": [
        "UnADM/assets-unadm/malla-curricular-derecho-unadm.pdf",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/README.md",
        "UnADM/licenciatura-en-derecho-unadm/filosofia-del-derecho-lde/programa-analitico-filosofia-del-derecho.md"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial institucional exige citas verificables y formato consistente."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "Sin delimitacion del problema no hay argumentacion focalizada."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida debe derivar del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica [supuesto condicionado a consigna]",
          "target": "Argumentacion juridica [supuesto condicionado a consigna]",
          "kind": "supports",
          "justification": "Si la actividad trata interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README: identidad UnADM, ubicacion curricular y pauta editorial.",
        "Programa analitico: cinco ejes de trabajo.",
        "Historial de ciclos: necesidad de normalizacion por salidas no estructuradas."
      ]
    },
    "reinforcement_log": [
      "Ciclo 8: deduplicacion completa de reglas repetidas y variantes ortograficas.",
      "Ciclo 8: conservada regla de bloqueo por JSON no parseable.",
      "Ciclo 8: preservada identidad curricular verificada y entrada canonica de carpeta.",
      "Ciclo 8: agregado control explicito de transferencia hermana para evitar copia literal o bibliografia exclusiva.",
      "Ciclo 8: mantenidas preguntas abiertas donde faltan datos locales."
    ]
  }
}