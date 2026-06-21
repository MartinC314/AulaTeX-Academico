{
  "summary": [
    "Se consolida memoria lateral de Actividad 4 con deduplicacion lossless y sin recorte util.",
    "Se preserva identidad UnADM, marco curricular y ejes editoriales transferibles desde actividad hermana.",
    "Se refuerza validacion JSON estricta y normalizacion previa por antecedentes de salidas no parseables.",
    "Se mantiene regla de no transferir conclusiones especificas ni bibliografia exclusiva de la actividad hermana.",
    "Supuesto: la consigna textual de Actividad 4 no esta visible y debe confirmarse localmente."
  ],
  "identity_rules": [
    "Mantener tono formal academico y precision juridica alineada a UnADM.",
    "Vincular explicitamente la actividad con Licenciatura en Derecho y Filosofia del Derecho.",
    "Usar la carpeta de asignatura como entrada canonica documental.",
    "Marcar como supuesto todo dato no visible en la consigna local.",
    "Tratar fuentes heredadas no verificadas como provisionales hasta confirmacion local.",
    "Sostener integridad academica con citas verificables y trazables."
  ],
  "structure_rules": [
    "Iniciar con encuadre breve del problema juridico o social.",
    "Definir objetivo puntual antes del desarrollo.",
    "Separar secciones en conceptos clave, marco normativo o doctrinal, analisis propio y cierre.",
    "Alinear el producto final a la planeacion semanal y a la consigna local.",
    "Cerrar con conclusion juridica transferible a la practica profesional.",
    "Distinguir hechos, conceptos, argumentos y postura personal."
  ],
  "activity_rules": [
    "Adaptar Actividad 4 a los cinco ejes del programa analitico.",
    "Incluir problema, conceptos, evidencia y analisis propio en secuencia coherente.",
    "Evitar entregas solo descriptivas o de resumen.",
    "Verificar coherencia entre pregunta guia, desarrollo y conclusion.",
    "Sustentar cada afirmacion relevante con fuente verificable.",
    "No asumir que bibliografia de otra semana aplica automaticamente a Actividad 4."
  ],
  "quality_gates": [
    "Bloquear propagacion si la salida no es JSON parseable.",
    "Validar estructura minima completa antes de reutilizar aguas abajo.",
    "Revisar y normalizar cualquier respuesta no estructurada heredada.",
    "Confirmar que no existan afirmaciones sin respaldo o sin marca de supuesto.",
    "Validar consistencia entre citas en texto y archivo .bib.",
    "Verificar correspondencia entre producto entregable y consigna de Actividad 4."
  ],
  "latex_rules": [
    "Usar acentos y codificacion en espanol de forma consistente en .tex y .bib.",
    "Citar solo claves BibTeX existentes para evitar referencias rotas.",
    "Mantener claves estables y no renombrarlas sin necesidad editorial justificada.",
    "Compilar sin errores criticos ni referencias indefinidas.",
    "Verificar nombres reales de archivos cuando README tenga tokens sin resolver.",
    "Supuesto: el .bib canonico esperado es filosofia-del-derecho.bib por slug institucional."
  ],
  "bibliography_rules": [
    "Priorizar fuentes institucionales y juridicas verificables (UnADM, SCJN, UNAM-IIJ).",
    "Registrar fuentes especificas de Actividad 4 en el .bib de la asignatura.",
    "No inventar referencias ni metadatos faltantes.",
    "Conservar metadatos minimos: autor, titulo, anio, fuente editorial o URL.",
    "Distinguir bibliografia base de bibliografia especifica por actividad.",
    "Supuesto: filosofia-del-derecho-clean.bib pertenece a Semana 7 y requiere validacion de pertinencia para Actividad 4."
  ],
  "propagation_hints": [
    "Propagar recursivamente solo reglas generales y verificadas.",
    "Preservar reglas utiles previas sin regresion.",
    "Aplicar union-dedupe como compresion lossless en saltos laterales.",
    "No transferir redaccion literal ni conclusiones especificas entre hermanos.",
    "Si falta consigna local, propagar estructura base y preguntas abiertas.",
    "Mantener bandera de normalizacion manual para ciclos con salidas no estructuradas."
  ],
  "open_questions": [
    "Confirmar consigna textual completa de Actividad 4.",
    "Confirmar tipo de producto requerido (reporte, presentacion u otro).",
    "Confirmar rubrica de evaluacion especifica y criterios de profundidad argumentativa.",
    "Confirmar fuentes obligatorias de la semana de Actividad 4.",
    "Confirmar nombre canonico final del archivo .bib en uso real.",
    "Confirmar si la bibliografia limpia de Semana 7 aplica total, parcial o nada a Actividad 4."
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
        "Entrada canonica en carpeta de asignatura."
      ],
      "curricular": [
        "Licenciatura en Derecho.",
        "Semestre 1, bloque 2, obligatoria, 8 creditos.",
        "Asignatura: Filosofia del Derecho."
      ]
    },
    "essence": [
      "Problema juridico o social.",
      "Conceptos y marco normativo.",
      "Evidencia verificable.",
      "Analisis propio.",
      "Conclusion juridica transferible."
    ],
    "reason_for_being": [
      "Convertir planeacion semanal en productos academicos con fundamento juridico y trazabilidad.",
      "Asegurar coherencia entre estructura, evidencia y postura personal.",
      "Mantener estandar institucional reutilizable entre actividades hermanas."
    ],
    "style_markers": [
      "Objetivo explicito al inicio.",
      "Secciones funcionales claras.",
      "Cita explicita en afirmaciones clave.",
      "Marcado de supuestos cuando falte dato local.",
      "Cierre con criterio juridico propio."
    ],
    "argumentative_patterns": [
      "Plantear problema.",
      "Definir conceptos y marco normativo.",
      "Contrastar fuentes con analisis propio.",
      "Fijar postura argumentada.",
      "Concluir con aplicacion profesional."
    ],
    "knowledge_graph": {
      "concepts": [
        "Identidad institucional UnADM",
        "Normalizacion estructurada",
        "Validacion JSON",
        "Integridad academica",
        "Ejes editoriales de Filosofia del Derecho",
        "Coherencia problema-evidencia-conclusion"
      ],
      "citations": [
        "README.md de asignatura",
        "programa-analitico-filosofia-del-derecho.md",
        "malla-curricular-derecho-unadm.pdf"
      ],
      "relations": [
        {
          "source": "Identidad institucional UnADM",
          "target": "Tono formal y formato academico",
          "kind": "supports",
          "justification": "La pauta editorial exige alineacion institucional explicita."
        },
        {
          "source": "Normalizacion estructurada",
          "target": "Propagacion recursiva segura",
          "kind": "depends_on",
          "justification": "Sin estructura parseable no hay reutilizacion confiable."
        },
        {
          "source": "Ejes editoriales de Filosofia del Derecho",
          "target": "Coherencia problema-evidencia-conclusion",
          "kind": "develops",
          "justification": "Los ejes ordenan el desarrollo argumentativo completo."
        },
        {
          "source": "Integridad academica",
          "target": "Conclusion juridica propia",
          "kind": "supports",
          "justification": "La conclusion debe estar sustentada y no ser opinion aislada."
        }
      ],
      "evidence": [
        "Pauta editorial del README: identidad UnADM, citas verificables y conclusion juridica.",
        "Programa analitico: cinco ejes de trabajo reutilizables.",
        "Antecedentes de salidas no parseables: se justifica gate JSON estricto.",
        "Token slug sin resolver en README: requiere verificacion de nombres de archivo."
      ]
    },
    "reinforcement_log": [
      "Ciclo 56: deduplicacion semantica aplicada sin eliminar reglas utiles.",
      "Ciclo 56: se reforzo transferencia lateral solo de patrones reutilizables.",
      "Ciclo 56: se agregaron supuestos explicitos donde falta consigna local verificable."
    ]
  }
}