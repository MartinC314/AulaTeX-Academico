{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con union y deduplicacion lossless.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales transferibles.",
    "Se refuerza validacion JSON estricta por antecedentes de salida no parseable.",
    "Se mantiene regla de marcar supuestos cuando falte consigna local.",
    "Se evita transferir conclusiones o bibliografia exclusiva de Actividad 1."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica de UnADM.",
    "Alinear toda entrega a Licenciatura en Derecho y Filosofia del Derecho.",
    "Conservar marco curricular: semestre 1, bloque 2, obligatoria, 8 creditos.",
    "Usar carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta validacion local."
  ],
  "structure_rules": [
    "Abrir con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones: conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear formato final al producto pedido por la planeacion semanal.",
    "Cerrar con conclusion juridica transferible a practica profesional.",
    "Separar hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, evidencia y postura propia de forma explicita.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Sustentar afirmaciones con citas verificables.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "No asumir fuentes de otras semanas sin confirmacion local."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Revisar estructura minima completa antes de reutilizar.",
    "Confirmar que no haya afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y .bib.",
    "Normalizar respuestas no estructuradas antes de aplicar aguas abajo.",
    "Confirmar correspondencia exacta con consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion correcta en .tex y .bib.",
    "Citar solo claves existentes en el .bib activo.",
    "No renombrar claves BibTeX usadas en documentos vigentes.",
    "Evitar comandos no estandar sin justificacion editorial.",
    "Compilar sin errores criticos, referencias rotas ni archivos inexistentes.",
    "Resolver tokens sin expandir en README y programa analitico antes de referenciar rutas."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables.",
    "Registrar fuentes especificas de Actividad 4 en el .bib de asignatura.",
    "No inventar referencias ni metadatos.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente o URL.",
    "Distinguir bibliografia base de bibliografia especifica de actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib esta orientado a Semana 7; verificar aplicabilidad en Actividad 4."
  ],
  "propagation_hints": [
    "Propagar solo patrones reutilizables: identidad, estructura, calidad y trazabilidad.",
    "No transferir redaccion literal ni conclusiones especificas entre hermanos.",
    "Mantener union-dedupe sin regresiones de reglas utiles previas.",
    "Si falta consigna local, propagar plantilla base y abrir preguntas.",
    "Aplicar refuerzo lateral progresivo con analogia controlada.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Supuesto: falta consigna textual completa de Actividad 4; confirmar producto exacto.",
    "Confirmar rubrica de evaluacion y extension requerida.",
    "Confirmar si Actividad 4 requiere reporte, presentacion u otro formato.",
    "Confirmar nombre canonico final del .bib por token Slug no resuelto en README.",
    "Confirmar si bibliografia de interpretacion juridica aplica o se crea set nuevo.",
    "Confirmar fuentes obligatorias de la semana correspondiente."
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
      "Problema juridico o social.",
      "Conceptos, normas, doctrina o datos pertinentes.",
      "Producto segun planeacion.",
      "Analisis propio y postura academica.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Transformar planeacion semanal en productos academicos verificables.",
      "Asegurar claridad argumentativa y fundamento juridico.",
      "Conectar evidencia con conclusion profesionalmente util."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales y trazables.",
      "Citas explicitas en afirmaciones sustantivas.",
      "Supuestos marcados cuando falten datos locales."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir marco conceptual y normativo.",
      "Contrastar fuentes con analisis propio.",
      "Emitir postura justificada.",
      "Cerrar con conclusion juridica aplicable."
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
        "README de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf",
        "filosofia-del-derecho.bib",
        "filosofia-del-derecho-clean.bib"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Integridad academica y verificabilidad",
          "kind": "supports",
          "justification": "La pauta editorial exige citas verificables y formato institucional."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Relacion problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo de la actividad."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Validacion JSON estricta",
          "kind": "depends_on",
          "justification": "La propagacion recursiva requiere estructura parseable."
        }
      ],
      "evidence": [
        "README fija identidad UnADM y punto de entrada canonico.",
        "Programa analitico define cinco ejes reutilizables.",
        "Historial reporta salidas no parseables; se activa gate JSON.",
        "Token Slug no resuelto en README obliga verificacion de nombres reales."
      ]
    },
    "reinforcement_log": [
      "Ciclo 13: refuerzo lateral desde hermano Actividad 1 sin copiar contenido especifico.",
      "Se deduplican reglas repetidas con preservacion total de patrones utiles.",
      "Se elevan a regla estable: supuestos explicitos y validacion JSON previa.",
      "Se mantiene separacion entre bibliografia base y bibliografia por actividad."
    ]
  }
}