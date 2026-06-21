{
  "summary": [
    "Se consolida memoria lateral hacia Actividad 6 con union-dedupe sin perdida.",
    "Se preserva identidad UnADM y ubicacion curricular verificada.",
    "Se mantiene regla critica: normalizar antes de propagar.",
    "Se refuerzan ejes editoriales estables de la asignatura.",
    "Se evita transferir conclusiones o bibliografia exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener identidad institucional UnADM en tono y formato.",
    "Alinear actividad a Licenciatura en Derecho y asignatura Filosofia del Derecho.",
    "Contextualizar ubicacion curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local."
  ],
  "structure_rules": [
    "Entregar JSON valido y parseable en tareas de consolidacion.",
    "Usar exactamente el esquema requerido sin claves extra.",
    "Abrir con problema juridico o social delimitado.",
    "Separar en bloques: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto al formato solicitado por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a la practica."
  ],
  "activity_rules": [
    "Definir objetivo puntual de Actividad 6 antes del desarrollo.",
    "Sostener afirmaciones con fuentes verificables y cita explicita.",
    "Distinguir sintesis de fuentes y postura propia.",
    "Evitar entregas solo descriptivas.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Supuesto: si Actividad 6 aborda interpretacion juridica, articular hermeneutica, argumentacion y aplicacion normativa."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar.",
    "Confirmar trazabilidad de afirmaciones a fuente o supuesto marcado.",
    "Separar reglas confirmadas de supuestos.",
    "Validar consistencia entre citas en texto y .bib activo.",
    "No eliminar reglas utiles previas durante consolidacion."
  ],
  "latex_rules": [
    "Usar codificacion y acentos correctos en espanol en .tex y .bib.",
    "No cambiar claves BibTeX ya citadas en .tex.",
    "Comprobar que toda clave citada exista en el .bib usado.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos ni referencias rotas.",
    "Resolver tokens sin expandir tipo $(@{...}.Slug) en README y programa analitico.",
    "Supuesto: .bib canonico esperado es filosofia-del-derecho.bib por Slug del README."
  ],
  "bibliography_rules": [
    "No inventar referencias.",
    "Usar solo obras realmente consultables.",
    "Priorizar fuentes institucionales UnADM y juridicas verificables.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Registrar fuentes de actividad en el .bib de la asignatura.",
    "Conservar metadatos minimos: autor, titulo, ano, fuente editorial o URL.",
    "No asumir que clean.bib aplica a Actividad 6 sin confirmacion de consigna."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo despues de validar JSON y estructura.",
    "Transferir solo patrones reutilizables de identidad, estructura y calidad.",
    "No propagar redaccion literal ni conclusiones especificas entre hermanos.",
    "Conservar advertencias historicas de salidas no estructuradas.",
    "Aplicar union-dedupe lossless y evitar regresiones."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual de Actividad 6; confirmar producto exacto.",
    "Confirmar rubrica especifica de evaluacion de Actividad 6.",
    "Confirmar si se requiere reporte, presentacion u otro formato principal.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto.",
    "Confirmar si se reutiliza bibliografia existente o se exige corpus propio."
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
      "Conceptos, normas o doctrina pertinentes.",
      "Producto alineado a planeacion.",
      "Analisis propio con postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y evidencia.",
      "Mantener consistencia institucional y metodologica entre actividades hermanas."
    ],
    "style_markers": [
      "Inicio con encuadre breve del problema.",
      "Secciones explicitas y ordenadas.",
      "Citas verificables con trazabilidad.",
      "Diferenciacion clara entre fuente y postura propia.",
      "Cierre con utilidad profesional juridica."
    ],
    "argumentative_patterns": [
      "Delimitacion del problema.",
      "Marco conceptual y normativo.",
      "Analisis propio sustentado.",
      "Derivacion logica de conclusion.",
      "Transferencia a practica juridica."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Integridad academica",
        "Problema juridico o social",
        "Analisis propio",
        "Conclusion transferible",
        "Hermeneutica juridica",
        "Argumentacion juridica"
      ],
      "citations": [
        "malla-curricular-derecho-unadm.pdf",
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Problema juridico o social",
          "target": "Analisis propio",
          "kind": "depends_on",
          "justification": "El analisis requiere un problema delimitado."
        },
        {
          "source": "Analisis propio",
          "target": "Conclusion transferible",
          "kind": "develops",
          "justification": "La conclusion valida deriva del desarrollo argumentativo."
        },
        {
          "source": "Hermeneutica juridica",
          "target": "Argumentacion juridica",
          "kind": "supports",
          "justification": "Cuando hay interpretacion, la hermeneutica fundamenta la argumentacion."
        }
      ],
      "evidence": [
        "README confirma identidad, pauta editorial y ubicacion curricular.",
        "Programa analitico define cinco ejes de trabajo.",
        "Se detecta token Slug sin resolver en README y programa analitico.",
        "Existen dos .bib locales; su uso depende de consigna y trazabilidad de citas."
      ]
    },
    "reinforcement_log": [
      "Se deduplicaron reglas repetidas y se conservaron todas las utiles.",
      "Se reforzo la regla de normalizacion previa a propagacion.",
      "Se mantuvo separacion entre datos confirmados y supuestos.",
      "Se limitaron transferencias a patrones reutilizables entre nodos hermanos."
    ]
  }
}